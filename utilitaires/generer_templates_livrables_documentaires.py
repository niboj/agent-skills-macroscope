#!/usr/bin/env python3
"""Genere des templates Markdown pour les livrables documentaires Macroscope."""

from __future__ import annotations

import argparse
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "skills" / "INDEX.md"

INCLUDE_KEYWORDS = (
    "plan",
    "cadre",
    "enonce",
    "compte rendu",
    "demande",
    "registre",
    "risque",
    "point en suspens",
    "notes de reunion",
    "lecons apprises",
    "strategie",
    "specification",
    "specifications",
    "architecture",
    "exigence",
    "exigences",
    "principes",
    "ressources",
    "structure",
    "processus de travail",
    "fonction",
    "choix",
    "criteres",
    "analyse des impacts",
    "impacts",
    "benefices",
    "couts",
    "liste",
    "modele du domaine",
    "matrice",
    "guide",
    "base de donnees",
    "rapport",
    "document",
    "dossier",
    "environnement",
    "materiel",
    "formation",
    "securite",
    "diagramme",
    "table de decision",
    "composantes du systeme",
    "gestion du changement organisationnel",
    "analyse preliminaire",
)

ACTIVITY_PREFIXES = (
    "ag.",
    "ccm.",
    "definir ",
    "identifier ",
    "etablir ",
    "decrire ",
    "effectuer ",
    "selectionner ",
    "former ",
    "preparer ",
    "evaluer ",
    "recommander ",
    "faire ",
    "revoir ",
    "creer ",
    "proposer ",
    "traduire ",
    "optimiser ",
    "ajuster ",
    "assurer ",
    "reduire ",
    "analyser ",
    "construire ",
    "ebaucher ",
    "attribuer ",
    "determiner ",
    "concevoir ",
    "proceder ",
    "realiser ",
    "tenir ",
    "controler ",
    "rendre compte",
)

EXCLUDED_CONCEPTS = (
    "adaptateur",
    "facade",
    "commande",
    "controleur",
    "fabrique abstraite",
    "fabrique concrete",
    "pont",
    "monteur",
    "decorateur",
    "chaine de responsabilite",
    "objet composite",
    "mapper de donnees",
    "mappers d heritage",
    "interpreteur",
    "iterateur",
    "couche supertype",
    "passerelle",
    "poids-mouche",
    "poids-plume",
    "verrou",
    "indirection",
    "expert en information",
    "createur",
    "eviteur",
    "acquisition",
    "correspondance",
    "table d",
    "etat de la session",
    "attribut identite",
    "enregistrement actif",
    "asynchrone",
    "valeur integree",
    "initialisation a la demande",
    "chargement a la demande",
    "jeu d'enregistrements",
    "patrons d",
    "patrons de",
    "gestionnaire de cycle de vie",
    "langage de definition",
    "harmonisation",
    "modelisation de",
    "classification et categorisation",
    "gestion de la complexite",
    "recouvrement",
)

ROLE_OR_ORG_KEYWORDS = (
    "administrateur",
    "analyste",
    "bureau",
    "chef",
    "comite",
    "conseiller",
    "coordonnateur",
    "equipe",
    "expert du domaine",
    "formateur",
    "groupe",
    "organisation de l'exploitation",
    "partie prenante",
    "pilote",
    "proprietaire",
    "redacteur",
    "responsable",
    "specialiste",
    "testeur",
    "utilisateur",
)

TEMPLATE_NOTE = (
    "Utiliser [le template du livrable](references/TEMPLATE.md) lorsque "
    "l'utilisateur demande un gabarit, un canevas ou une version vierge du livrable."
)


@dataclass(frozen=True)
class SkillRow:
    code: str
    name: str
    skill: str
    path: Path


def normalize(value: str) -> str:
    decomposed = unicodedata.normalize("NFD", value.lower())
    return "".join(
        char for char in decomposed if unicodedata.category(char) != "Mn"
    )


def contains_keyword(value: str, keyword: str) -> bool:
    return re.search(rf"(?<!\w){re.escape(keyword)}(?!\w)", value) is not None


def contains_any_keyword(value: str, keywords: tuple[str, ...]) -> bool:
    return any(contains_keyword(value, keyword) for keyword in keywords)


def parse_index() -> list[SkillRow]:
    rows: list[SkillRow] = []
    for line in INDEX.read_text(encoding="utf-8").splitlines():
        if (
            not line.startswith("| ")
            or line.startswith("| ---")
            or line.startswith("| Code")
        ):
            continue
        cells = [cell.strip().strip("`") for cell in line.strip("|").split("|")]
        if len(cells) < 6:
            continue
        rows.append(
            SkillRow(
                code=cells[0],
                name=cells[1],
                skill=cells[2],
                path=ROOT / cells[5],
            )
        )
    return rows


def is_documentary(row: SkillRow) -> tuple[bool, str]:
    if "variantes" in row.path.parts:
        return False, "variante"
    if not (row.path / "references" / "LIVRABLE.md").exists():
        return False, "aucune reference LIVRABLE.md"

    normalized_name = normalize(row.name)
    code = row.code

    if code.startswith("P-"):
        return False, "activite ou capacite P-*"
    if normalized_name in {"code", "securite", "registre"} and re.fullmatch(
        r"P\d+", code
    ):
        return False, "concept sans suffixe documentaire"
    if re.fullmatch(r"P\d+", code) and any(
        keyword in normalized_name for keyword in ROLE_OR_ORG_KEYWORDS
    ):
        return False, "role ou organisation"
    if row.code == "PX000":
        return False, "livrable generique non classifie"
    if normalized_name == "code":
        return False, "code source"
    if contains_any_keyword(normalized_name, EXCLUDED_CONCEPTS):
        return False, "patron, element de code ou concept non documentaire"
    if any(normalized_name.startswith(prefix) for prefix in ACTIVITY_PREFIXES):
        return False, "activite ou procedure"
    if re.fullmatch(r"M\d+[A-Z]", code):
        return True, "code de document M"
    if re.fullmatch(r"P\d+[A-Z]", code):
        return True, "code de document P suffixe"
    if contains_any_keyword(normalized_name, INCLUDE_KEYWORDS):
        return True, "nom documentaire"
    return False, "a confirmer"


def extract_list_section(text: str, title: str) -> list[str]:
    pattern = re.compile(
        rf"^## {re.escape(title)}\n(?P<body>.*?)(?=^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        return []
    items: list[str] = []
    for line in match.group("body").splitlines():
        stripped = line.strip()
        if stripped.startswith("- ") and "Aucune information explicite" not in stripped:
            items.append(stripped[2:].strip())
    return items[:8]


def extract_togaf(text: str) -> list[str]:
    items = extract_list_section(text, "Correspondances TOGAF")
    return [item for item in items if not item.startswith("Préséance")]


def markdown_comment_lines(items: list[str], empty: str) -> str:
    if not items:
        return f"<!-- {empty} -->\n"
    return "\n".join(f"<!-- - {item} -->" for item in items) + "\n"


def build_template(row: SkillRow) -> str:
    reference = (row.path / "references" / "LIVRABLE.md").read_text(encoding="utf-8")
    diagrams = extract_list_section(reference, "Tableaux, modèles ou diagrammes recommandés")
    linked = extract_list_section(reference, "Livrables et références liés")
    togaf = extract_togaf(reference)

    return f"""# {row.code} - {row.name}

## 1. Identification du livrable

| Élément | Valeur |
| --- | --- |
| Code | {row.code} |
| Nom | {row.name} |
| Service ou système d'information | À compléter |
| Version | À compléter |
| Date | À compléter |
| Responsable de la production | À compléter |
| Conseiller en architecture | À compléter |

## 2. Contexte et portée

### Contexte

À compléter.

### Portée incluse

- À compléter.

### Hors portée

- À compléter.

## 3. Objectifs du livrable

- À compléter.

## 4. Intrants utilisés

| Intrant | Source | Statut | Commentaire |
| --- | --- | --- | --- |
| À compléter | À compléter | À confirmer | À compléter |

## 5. Contenu du livrable

À compléter selon la référence `references/LIVRABLE.md`.

## 6. Tableaux, modèles ou diagrammes à produire

{markdown_comment_lines(diagrams, "Aucun tableau, modèle ou diagramme spécifique n'a été extrait.")}
| Élément | Objectif | Statut | Référence |
| --- | --- | --- | --- |
| À compléter | À compléter | À produire | À compléter |

## 7. Exigences, décisions et contraintes

| Type | Identifiant | Description | Source | Traçabilité TOGAF |
| --- | --- | --- | --- | --- |
| Exigence | À compléter | À compléter | À compléter | À compléter |
| Décision | À compléter | À compléter | À compléter | À compléter |
| Contrainte | À compléter | À compléter | À compléter | À compléter |

## 8. Correspondance TOGAF

{markdown_comment_lines(togaf, "Compléter la correspondance TOGAF à partir de la référence du livrable.")}
| Élément du livrable | Artefact ou concept TOGAF lié | Justification |
| --- | --- | --- |
| À compléter | À compléter | À compléter |

## 9. Livrables et références liés

{markdown_comment_lines(linked, "Aucun livrable lié spécifique n'a été extrait.")}
| Livrable ou référence | Relation | Utilisation prévue |
| --- | --- | --- |
| À compléter | À compléter | À compléter |

## 10. Hypothèses

| Hypothèse | Impact | Validation attendue |
| --- | --- | --- |
| À compléter | À compléter | À compléter |

## 11. Points à confirmer

| Point | Responsable | Échéance | Impact si non confirmé |
| --- | --- | --- | --- |
| À compléter | À compléter | À compléter | À compléter |

## 12. Contrôles de qualité

- [ ] Le code et le nom du livrable sont exacts.
- [ ] La portée est explicite.
- [ ] Les faits, hypothèses et points à confirmer sont distingués.
- [ ] Les exigences, décisions et contraintes sont traçables.
- [ ] Les liens avec TOGAF sont explicites.
- [ ] Les sections non applicables sont indiquées comme telles.
- [ ] Les tableaux, matrices ou diagrammes attendus sont produits ou signalés.
"""


def update_skill(skill_path: Path) -> bool:
    text = skill_path.read_text(encoding="utf-8")
    if "references/TEMPLATE.md" in text:
        return False
    marker = "3. Consulter [la référence du livrable](references/LIVRABLE.md) pour sélectionner les sections pertinentes.\n"
    replacement = marker + f"4. {TEMPLATE_NOTE}\n"
    if marker not in text:
        return False
    text = text.replace(marker, replacement, 1)
    for old, new in (
        ("4. Produire le contenu demandé", "5. Produire le contenu demandé"),
        ("5. Relier les éléments", "6. Relier les éléments"),
        ("6. Formuler les constats", "7. Formuler les constats"),
        ("7. Produire les tableaux", "8. Produire les tableaux"),
        ("8. Vérifier la cohérence", "9. Vérifier la cohérence"),
    ):
        text = text.replace(old, new, 1)
    ref_marker = "Consulter [la référence du livrable](references/LIVRABLE.md) pour la structure détaillée et les consignes spécifiques.\n"
    if ref_marker in text:
        text = text.replace(
            ref_marker,
            ref_marker
            + "\n"
            + "Utiliser [le template du livrable](references/TEMPLATE.md) pour générer un canevas prêt à remplir.\n",
            1,
        )
    skill_path.write_text(text, encoding="utf-8")
    return True


def remove_skill_note(skill_path: Path) -> bool:
    text = skill_path.read_text(encoding="utf-8")
    if "references/TEMPLATE.md" not in text:
        return False
    text = text.replace(
        f"4. {TEMPLATE_NOTE}\n",
        "",
        1,
    )
    for old, new in (
        ("5. Produire le contenu demandé", "4. Produire le contenu demandé"),
        ("6. Relier les éléments", "5. Relier les éléments"),
        ("7. Formuler les constats", "6. Formuler les constats"),
        ("8. Produire les tableaux", "7. Produire les tableaux"),
        ("9. Vérifier la cohérence", "8. Vérifier la cohérence"),
    ):
        text = text.replace(old, new, 1)
    text = text.replace(
        "\nUtiliser [le template du livrable](references/TEMPLATE.md) pour générer un canevas prêt à remplir.\n",
        "",
        1,
    )
    skill_path.write_text(text, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--prune",
        action="store_true",
        help="Supprime les TEMPLATE.md des skills qui ne sont plus retenues.",
    )
    args = parser.parse_args()

    selected: list[tuple[SkillRow, str]] = []
    excluded: list[tuple[SkillRow, str]] = []
    for row in parse_index():
        keep, reason = is_documentary(row)
        if keep:
            selected.append((row, reason))
        else:
            excluded.append((row, reason))

    selected_paths = {row.path for row, _reason in selected}
    created = 0
    updated = 0
    pruned = 0
    reverted = 0
    if args.prune and not args.dry_run:
        for template_path in (ROOT / "skills").glob("*/references/TEMPLATE.md"):
            skill_dir = template_path.parents[1]
            if skill_dir not in selected_paths:
                template_path.unlink()
                pruned += 1
                if remove_skill_note(skill_dir / "SKILL.md"):
                    reverted += 1

    for row, _reason in selected:
        template_path = row.path / "references" / "TEMPLATE.md"
        skill_path = row.path / "SKILL.md"
        if not args.dry_run:
            if not template_path.exists():
                template_path.write_text(build_template(row), encoding="utf-8")
                created += 1
            if update_skill(skill_path):
                updated += 1

    print(f"Livrables documentaires retenus: {len(selected)}")
    print(f"Livrables exclus: {len(excluded)}")
    if args.dry_run:
        print("Mode simulation: aucun fichier modifie.")
    else:
        print(f"TEMPLATE.md crees: {created}")
        print(f"SKILL.md mis a jour: {updated}")
        if args.prune:
            print(f"TEMPLATE.md supprimes: {pruned}")
            print(f"SKILL.md retablis: {reverted}")
    print("\nExclusions a confirmer:")
    for row, reason in excluded:
        if reason == "a confirmer":
            print(f"- {row.code} | {row.name} | {row.path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
