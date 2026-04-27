# AGENTS

## Portée

Ces instructions s’appliquent à tout le dépôt.

## Mission du dépôt

Ce dépôt maintient une bibliothèque de skills IA pour produire, compléter, réviser et contrôler des livrables selon la méthode Macroscope, dans une démarche d’architecture de service alignée sur TOGAF.

TOGAF a préséance sur Macroscope. Les livrables Macroscope doivent être interprétés comme des artefacts, vues spécialisées, gabarits ou annexes détaillées qui alimentent les livrables TOGAF, notamment le Document de définition d’architecture (Architecture Definition Document), la Spécification des exigences d’architecture (Architecture Requirements Specification), les vues d’architecture et les plans de migration ou d’implantation.

## Règles générales

- Répondre en français, avec un style clair, formel et opérationnel.
- Produire un livrable exploitable, pas une explication générique de la méthode.
- Utiliser les références locales avant d’inventer une structure ou une terminologie.
- Distinguer explicitement les faits tirés des sources, les hypothèses et les points à confirmer.
- Ne jamais présenter Macroscope comme ayant préséance sur TOGAF.
- Ne pas utiliser le mot « Architecte » pour désigner un rôle professionnel. Utiliser « Conseiller en architecture ».
- Ne pas utiliser le terme « structurant ».
- Garder les changements de fichiers limités au périmètre demandé.
- Ne pas modifier les sources brutes dans `macroscope/livrables/` sauf demande explicite.

## Répertoires de référence

- `skills/` : skills actives, une skill canonique par livrable ou capacité.
- `skills/INDEX.md` : index des skills Macroscope actives.
- `skills/variantes/` : variantes de contenu non actives par défaut, conservées pour consolidation.
- `skills/variantes/INDEX.md` : correspondance entre variantes et skills canoniques.
- `macroscope/livrables/` : corpus source Macroscope converti en Markdown.
- `references/` : conventions transversales de rédaction, nommage et compatibilité Agent Skills.
- `gabarits/` : modèles de départ pour créer ou réviser des skills.
- `utilitaires/` : scripts de validation et d’installation.

## Sélection d’une skill Macroscope

Quand une demande vise un livrable Macroscope :

1. Identifier le code du livrable si l’utilisateur le donne, par exemple `P140S`, `P580S` ou `P700U`.
2. Sinon, identifier le livrable par mots-clés, domaine, phase ou type de sortie.
3. Consulter `skills/INDEX.md` pour choisir la skill canonique.
4. Lire le `SKILL.md` de la skill sélectionnée.
5. Lire `references/LIVRABLE.md` dans cette skill.
6. Si une variante semble pertinente, consulter `skills/variantes/INDEX.md`, puis la référence de la variante.
7. Ne pas activer plusieurs livrables si un livrable canonique suffit. Mentionner les livrables liés seulement s’ils changent la sortie.

## Application de Macroscope

Pour appliquer Macroscope à une demande :

1. Cadrer la demande : livrable, objectif, portée, audience, niveau de détail et état attendu.
2. Identifier les intrants disponibles : besoin, exigences, processus, données, règles, contraintes, décisions, risques, technologies, exploitation ou formation.
3. Relever les informations manquantes qui empêchent de produire une version fiable.
4. Produire une structure Markdown adaptée au livrable.
5. Rédiger les sections utiles en respectant la référence du livrable.
6. Relier les éléments aux concepts TOGAF pertinents.
7. Documenter les hypothèses et les points à confirmer.
8. Vérifier la cohérence, la traçabilité et la complétude.

## Positionnement TOGAF

Chaque livrable Macroscope doit être positionné dans TOGAF.

Utiliser les correspondances suivantes comme point de départ :

- Opportunité, objectifs, portée, exigences : Vision d’architecture (Architecture Vision), Demande de travail d’architecture (Request for Architecture Work), Énoncé de travail d’architecture (Statement of Architecture Work), Spécification des exigences d’architecture (Architecture Requirements Specification).
- Évaluation du système actuel : architecture de référence, architecture actuelle, analyse des écarts.
- Structure du système d’information : Architecture métier (Business Architecture) et Architecture applicative (Application Architecture).
- Dynamique du système d’information : Architecture métier, processus, services, événements.
- Sujet, facette, composante du noyau : Architecture des données (Data Architecture).
- Processus de travail, fonction, unité de tâche : Architecture métier et vue des usages.
- Architecture logicielle, interface niveau réalisateur : Architecture applicative.
- Infrastructure technologique, répartition : Architecture technologique (Technology Architecture).
- Sécurité du système : vue sécurité, exigences de sécurité, contrôles, accès, journalisation, séparation des tâches.
- Règles d’affaires : exigences, règles métier, critères de conformité.
- Cadre de conception et spécifications détaillées : conception détaillée référencée par l’architecture.
- Plan d’essai et environnement d’essai : gouvernance de mise en œuvre et validation.
- Plan d’implantation : plan d’implantation et de migration.
- Guide d’utilisation, guide d’opération, matériel de formation : transition, exploitation, adoption et transfert.

## Contrôles de qualité d’un livrable

Avant de remettre un livrable ou une révision :

- Le code et le nom du livrable sont clairs.
- La portée est explicite.
- Les objectifs, exigences, décisions et contraintes sont traçables.
- Les termes Macroscope et TOGAF sont utilisés de manière cohérente.
- Les sections non applicables sont omises ou indiquées comme non applicables.
- Les tableaux, matrices ou diagrammes recommandés sont produits ou signalés comme manquants.
- Les décisions sont justifiées.
- Les exigences sont vérifiables.
- Les liens avec TOGAF sont explicites.
- Les informations de conception détaillée ne remplacent pas l’architecture.
- Les hypothèses et les points à confirmer sont visibles.

## Création ou révision de skills

Quand il faut créer ou modifier une skill :

1. Lire les références existantes du livrable.
2. Vérifier si une skill canonique existe déjà dans `skills/INDEX.md`.
3. Ne pas créer de doublon actif pour le même code et le même nom de livrable.
4. Placer les variantes non canoniques dans `skills/variantes/`.
5. Garder `SKILL.md` concis et opérationnel.
6. Placer le détail long dans `references/LIVRABLE.md`.
7. Utiliser un nom conforme Agent Skills : lettres minuscules, chiffres et traits d’union seulement, maximum 64 caractères.
8. Le champ `name` doit être identique au nom du répertoire.
9. La `description` doit indiquer quand utiliser la skill.

## Validation des skills

Après modification de skills, exécuter :

```bash
python3 utilitaires/verifier_toutes_skills.py
```

Pour valider les variantes :

```bash
python3 utilitaires/verifier_toutes_skills.py --skills-root skills/variantes
```

Vérifier aussi :

- les chemins relatifs vers `references/LIVRABLE.md`;
- l’absence de doublon actif dans `skills/INDEX.md`;
- la cohérence entre `skills/INDEX.md` et les répertoires sous `skills/`;
- la cohérence entre `skills/variantes/INDEX.md` et les répertoires sous `skills/variantes/`.

## Sortie attendue d’un agent

Quand l’agent applique une skill Macroscope, la réponse doit généralement contenir :

1. Le livrable ou la section demandée.
2. Les hypothèses retenues.
3. Les points à confirmer.
4. Les références internes consultées, lorsque leur contenu influence la sortie.
5. Les liens TOGAF pertinents.

Éviter les longues explications méthodologiques si l’utilisateur demande directement un livrable.
