# AGENTS

## Portee

Ces instructions s appliquent a tout le depot.

## Objectif du depot

- Maintenir une bibliotheque de skills Markdown reutilisables pour la redaction de livrables selon la methodologie Macroscope.
- Appuyer les skills sur les references locales du depot, en particulier le corpus `macroscope/livrables/`.
- Conserver une structure simple par skill, avec un dossier dedie sous `skills/`.
- Produire des instructions claires, verifiables et portables vers Codex ou d autres runtimes compatibles Agent Skills.

## Regles de travail

- Avant de modifier une skill, lire au minimum son `SKILL.md` et les references directement liees a la demande.
- Pour une skill Macroscope, consulter d abord les references locales pertinentes dans `macroscope/livrables/` ou dans le sous-dossier `references/` de la skill.
- Preserver les conventions du depot : nommage stable, structure Markdown simple, responsabilite unique par skill.
- Limiter les changements au perimetre utile. Ne pas refactorer plusieurs skills sans besoin explicite.
- Distinguer les informations tirees des references, les hypotheses et les points a confirmer.
- Ne pas introduire de format proprietaire ou de generation complexe quand un fichier Markdown suffit.
- Si une regle locale est ajoutee plus bas dans l arborescence, elle prime sur ce fichier pour son sous-dossier.

## Serie d agents pour les skills Macroscope

Utiliser ces roles comme chaine de travail quand la demande porte sur la creation, la refonte ou l evaluation d une skill de livrable Macroscope.

### 1. Agent Analyse Source

- Mission: lire les pages Macroscope, documents sources et artefacts du depot.
- Declenchement: quand une skill ou un livrable doit etre base sur une notion, une phase, une technique, un modele ou un gabarit Macroscope.
- Livrable: une synthese des concepts stables, termes obligatoires, risques d interpretation et references a reutiliser.
- Regles: extraire uniquement ce qui influence le livrable ou la skill; signaler les zones ambigues; citer les chemins locaux consultes.

### 2. Agent Cadrage Livrable

- Mission: definir le type de livrable, son objectif, son audience, ses entrees et ses criteres de completude.
- Declenchement: quand le besoin utilisateur est large ou que le type de livrable Macroscope n est pas encore clair.
- Livrable: nom du livrable, contexte, contenu attendu, non-objectifs et references probables.
- Regles: eviter les livrables fourre-tout; borner le niveau de detail; expliciter les hypotheses.

### 3. Agent Redaction Skill

- Mission: transformer le cadrage en `SKILL.md` actionnable.
- Declenchement: quand le workflow de production ou de revision du livrable doit devenir reutilisable.
- Livrable: description orientee declenchement, procedure, controles qualite et sortie attendue.
- Regles: preferer des etapes observables; garder les details longs dans `references/`.

### 4. Agent Scripts et Automatisation

- Mission: decider si un script doit etre ajoute pour rechercher, verifier ou transformer des references.
- Declenchement: quand une verification mecanique devient repetee ou fragile.
- Livrable: decision "sans script" ou "avec script", prerequis, chemin relatif et mode d execution.
- Regles: n ajouter un script que s il apporte un gain reel de fiabilite ou de repetabilite; documenter les prerequis; utiliser des chemins relatifs depuis la racine de la skill.

### 5. Agent Evaluation

- Mission: evaluer le declenchement et la qualite des sorties d une skill.
- Declenchement: quand une skill nouvelle ou refondue doit etre verifiee.
- Livrable: cas de test, assertions, constats et recommandations de correction.
- Regles: tester des demandes explicites, des demandes ambigues et des demandes hors perimetre; exiger des preuves concretes pour chaque verdict.

## Regles specifiques aux livrables Macroscope

- Identifier le type de livrable avant de rediger.
- Rechercher les termes et conventions dans les references locales avant d inventer une structure.
- Citer les chemins locaux consultes quand ils influencent la sortie.
- Signaler explicitement les informations manquantes ou les arbitrages proposes.
- Produire une sortie exploitable, pas une explication generique de la methodologie.
- Verifier la coherence entre objectifs, activites, resultats, roles, evenements, biens livrables et controles de qualite lorsqu ils sont presents.

## Structure attendue d une skill

- Un dossier sous `skills/` avec un nom explicite et stable.
- Un fichier `SKILL.md` qui decrit le but, le contexte d usage, la procedure et la sortie attendue.
- Des fichiers de reference dans `references/` seulement s ils sont necessaires a l execution.
- Des evaluations dans `evals/` quand la skill porte un workflow reutilisable.

## Validation minimale

- Verifier que les chemins cites existent.
- Verifier que les liens entre `SKILL.md`, `references/` et `macroscope/livrables/` sont coherents.
- Relire le diff pour eviter les contradictions entre skills voisines.
- Verifier que la description d une skill indique clairement quand l utiliser.
- Verifier que la sortie attendue est observable et evaluable.
