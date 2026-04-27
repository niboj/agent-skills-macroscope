# agent-skills-macroscope

Depot de skills IA pour aider a produire, reviser et normaliser des livrables selon la methodologie Macroscope.

Ce depot est initialise a partir du gabarit `gabarit-agent-skills-depot-code`. Il conserve les conventions de structure Agent Skills du gabarit, puis les specialise pour un usage de redaction de livrables Macroscope.

## Objectif

Le depot sert a constituer une bibliotheque de skills reutilisables pour :

- cadrer une demande de livrable Macroscope ;
- retrouver les references pertinentes dans le corpus local ;
- produire un livrable coherent avec la terminologie et les conventions Macroscope ;
- reviser un livrable existant selon sa structure, sa tracabilite et sa completude ;
- faire evoluer progressivement les skills a partir d exemples reels.

## Structure du depot

```text
.
|-- AGENTS.MD
|-- README.md
|-- documentation/
|-- evaluations/
|-- exemples/
|-- gabarits/
|-- macroscope/
|   `-- livrables/
|-- references/
|-- skills/
`-- utilitaires/
```

## Role des repertoires

- `skills/` : bibliotheque de skills, un dossier par capacite.
- `macroscope/livrables/` : corpus local de pages et descriptions Macroscope utilise comme reference de travail.
- `references/` : conventions partagees pour la redaction, la structure et la compatibilite des skills.
- `gabarits/` : modeles de depart pour creer de nouvelles skills et evaluations.
- `utilitaires/` : scripts non interactifs pour initialiser, verifier et installer les skills.
- `evaluations/` : cas d evaluation au niveau du depot.
- `exemples/` : sources et sorties derivees pour guider la creation de nouvelles skills.
- `documentation/` : documentation humaine sur la redaction et la maintenance des skills.

## Skills de depart

Le gabarit fournit des skills d atelier pour concevoir, rediger, reviser et evaluer d autres skills. Ce depot ajoute aussi une premiere skill orientee Macroscope :

- `rediger-livrable-macroscope` : aide a produire ou reviser un livrable selon la methodologie Macroscope en s appuyant sur les references locales.

Les autres skills initiales restent utiles pour industrialiser la bibliotheque :

- `skill-definir-perimetre`
- `skill-rediger-instructions`
- `skill-optimiser-description`
- `skill-structurer-ressources`
- `skill-construire-gabarits`
- `skill-construire-evaluations`
- `skill-reviser`
- `skill-documenter-compatibilite`
- `skill-normaliser-style`
- `skill-depuis-artefact`

## Workflow recommande

1. Identifier le type de livrable, son audience et le niveau de detail attendu.
2. Rechercher dans `macroscope/livrables/` les notions, formats ou conventions applicables.
3. Utiliser ou creer une skill specialisee dans `skills/`.
4. Produire le livrable avec ses hypotheses, ses references et ses limites.
5. Verifier la coherence terminologique, la structure, la tracabilite et les sections manquantes.
6. Ajouter des cas d evaluation quand une skill devient reutilisable.

## Creer une nouvelle skill

```bash
python3 utilitaires/initialiser_skill.py \
  --root skills \
  --name rediger-modele-processus-macroscope \
  --description "Utiliser ce skill quand il faut produire ou reviser un livrable Macroscope de modelisation de processus a partir d exigences, d observations metier ou d un brouillon existant." \
  --with-references \
  --with-evals
```

Puis ajuster le `SKILL.md`, ajouter les references pertinentes et valider :

```bash
python3 utilitaires/verifier_skill.py skills/rediger-modele-processus-macroscope
python3 utilitaires/verifier_toutes_skills.py
```

## Validation

Avant publication ou installation :

- chaque skill doit contenir un `SKILL.md` avec `name` et `description` ;
- la description doit indiquer clairement quand utiliser la skill ;
- les chemins cites doivent exister ;
- les details volumineux doivent rester dans `references/`, `scripts/`, `assets/` ou `evals/` ;
- le livrable produit doit distinguer les faits sources, les hypotheses et les points a confirmer.
