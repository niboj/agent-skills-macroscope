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

## Livrables pour l architecture d affaires

Pour documenter l architecture d affaires selon Macroscope, utiliser les livrables suivants comme noyau de travail. Le choix final depend de la portee, du niveau de detail attendu et des intrants disponibles.

| Besoin de documentation | Livrable Macroscope | Utilisation |
| --- | --- | --- |
| Objectifs d affaires et resultats attendus | `P130O Objectifs du systeme d'information` | Definir les resultats vises et les criteres mesurables d evaluation. |
| Portee metier | `P140O Portee du systeme d'information` | Delimiter le systeme, les frontieres, les sujets et le perimetre de changement. |
| Exigences d affaires | `P140S Exigences proprietaire` ou `P2863 Exigences` | Capturer les besoins, contraintes, orientations et exigences independantes d une solution. |
| Vue metier de haut niveau | `P201S Processus du systeme` | Decrire les processus de haut niveau, les dependances, les participants et la dynamique du systeme. |
| Dynamique metier | `P201O Dynamique du systeme d'information` | Decrire l enchainement des processus du systeme. |
| Fonctions metier et usage | `P250S Structure utilisateur du systeme` et `P250U Fonction` | Structurer les fonctions, responsabilites et unites de tache. |
| Processus de travail | `P251S Processus de travail` et `P251U Processus de travail utilisateur` | Decrire les processus de travail, les participants et les unites de tache manuelles ou automatisees. |
| Detail des unites de tache | `P490S Specifications de l'unite de tache` | Detailer les scenarios, interactions et comportements lorsque necessaire. |
| Regles metier | `P360S Regles utilisateur`, `P361U Regles administratives et d'organisation du travail`, `P363U Regles de fonctionnement du traitement automatise` | Documenter les regles qui gouvernent les processus, decisions et traitements. |
| Impacts organisationnels | `P280S Impacts`, avec `P280O` et `P280U` au besoin | Decrire les impacts sur l organisation, les roles, les facons de travailler et les systemes. |
| Tracabilite | `P900S Suivi des exigences` | Relier exigences, processus, fonctions, regles, decisions et composants de solution. |

Le minimum praticable pour une architecture d affaires complete mais raisonnable est :

1. `P130O Objectifs du systeme d'information`
2. `P140O Portee du systeme d'information`
3. `P2863 Exigences` ou `P140S Exigences proprietaire`
4. `P201S Processus du systeme`
5. `P251S Processus de travail`
6. `P250S Structure utilisateur du systeme`
7. `P360S Regles utilisateur`
8. `P280S Impacts`
9. `P900S Suivi des exigences`

## Livrables pour l architecture de solution

Pour documenter l architecture d une solution selon Macroscope, couvrir les vues d exigences, d affaires, de donnees, applicative, technologique, securite, implantation et exploitation. Le choix final depend de la nature de la solution, du niveau de detail attendu et des livraisons visees.

| Besoin de documentation | Livrable Macroscope | Utilisation |
| --- | --- | --- |
| Cadrage et exigences | `P2863 Exigences` | Regrouper les besoins, orientations, contraintes et exigences de base de la solution. |
| Cadre d architecture | `P200A Cadre d'architecture` | Documenter le cadre general, les exigences d affaires et techniques cles, les decisions et la portee. |
| Systeme actuel ou reference | `P120S` | Decrire le systeme actuel, les processus, ressources, informations, technologies, forces, faiblesses et constats de securite. |
| Architecture d affaires | `P201S Processus du systeme` et, au besoin, `P251S Processus de travail` | Decrire la dynamique du systeme, les processus, les fonctions et les usages. |
| Architecture des donnees | `P170S Structure de l'information`, `P150C Bases de donnees`, `P510S Structure de l'information persistante` | Documenter l information, les donnees persistantes et les bases de donnees. |
| Architecture applicative | `P219S Architecture logicielle` | Decrire le decoupage des logiciels applicatifs en sous-systemes et composants. |
| Detail applicatif | `P219C Sous-systeme, niveau realisateur`, `P229C Interfaces du sous-systeme, niveau realisateur`, `P555S Specifications de composant logiciel` | Detailer les sous-systemes, interfaces et composants lorsque le niveau de precision le justifie. |
| Architecture technologique | `P269S Technologie et repartition utilisateur`, complete par `P268U` et `P269U` | Decrire les composantes d infrastructure, la technologie et la repartition. |
| Securite | Sections securite de `P120S`, exigences de securite et vues de controle associees | Documenter la sensibilite des actifs, les menaces, les risques, les mesures de protection, les acces et les controles. |
| Tracabilite | `P900S Suivi des exigences` | Relier les exigences a l architecture, aux specifications et aux composants qui les realisent. |
| Implantation | `P270S Strategie d'implantation`, puis `P450S Plan d'implantation` | Preparer la transition, les contraintes, les lots de livraison et les activites d implantation. |
| Exploitation | `P705S Guide d'operation` | Documenter les mesures d installation, d exploitation et de soutien. |

Le minimum praticable pour une architecture de solution complete mais raisonnable est :

1. `P2863 Exigences`
2. `P200A Cadre d'architecture`
3. `P120S`
4. `P201S Processus du systeme`
5. `P170S Structure de l'information` ou `P510S Structure de l'information persistante`
6. `P219S Architecture logicielle`
7. `P269S Technologie et repartition utilisateur`
8. `P900S Suivi des exigences`
9. `P270S Strategie d'implantation` ou `P450S Plan d'implantation`

## Livrables pour la realisation d une solution

Pour documenter la realisation d une solution selon Macroscope, couvrir la planification de la realisation, les specifications detaillees, les composants produits, les essais, l implantation et l exploitation. Le choix final depend du type de solution, du mode de livraison et du niveau de preuve attendu.

| Besoin de documentation | Livrable Macroscope | Utilisation |
| --- | --- | --- |
| Vue d ensemble de la realisation | `P2397 AG.2 Conception et realisation d'une livraison` ou `P3358 Conception et realisation d'une livraison` | Decrire la phase de conception et realisation, les iterations, les composants produits et la validation progressive. |
| Strategie de realisation et d essai | `P405S Strategie de realisation et d'essai` | Definir l approche de conception, de realisation, d essai et de gestion des essais. |
| Specifications du systeme | `P2871 Specifications du systeme` | Regrouper les specifications qui guident la construction de la solution. |
| Specifications des unites de tache | `P490S Specifications de l'unite de tache` | Decrire les scenarios, interactions, comportements et unites de travail a realiser. |
| Specifications des processus automatises | `P580S Specifications de processus automatise` | Decrire les chaines, traitements automatises, taches et cheminements. |
| Specifications des composants logiciels | `P555S Specifications de composant logiciel` | Definir les composants, classes, modules et interfaces a produire. |
| Interfaces de realisation | `P560C Interface, niveau realisateur` ou `P229C Interfaces du sous-systeme, niveau realisateur` | Decrire les interfaces techniques ou applicatives necessaires a la realisation. |
| Code et composants produits | `P650C Code` et `P600A Composants logiciels` | Documenter ou referencer les composants logiciels realises. |
| Environnements d essai | `P730C Environnement d'essai unitaire`, `P740C Environnement d'essai d'integration`, `P740S Environnement d'essai` | Decrire les environnements requis pour verifier la solution. |
| Plan d integration et de verification | `P415G Plan d'integration et de verification` | Organiser l integration, les sous-livraisons et les verifications. |
| Cas et resultats d essai | `P750S Cas d'essai`, `P750A Cas d'essai et resultats`, `P770S Resultats d'essai` | Decrire les cas d essai, executions, resultats et ecarts. |
| Anomalies | `P070M Anomalie`, `P072M Registre des anomalies` | Documenter les anomalies, leur suivi et leur resolution. |
| Implantation | `P450S Plan d'implantation`, `P720C Instructions d'installation, niveau realisateur` | Preparer l installation, la transition et les contraintes d implantation. |
| Exploitation | `P705S Guide d'operation` | Decrire les mesures d installation, d exploitation et de soutien. |

Le minimum praticable pour documenter la realisation d une solution est :

1. `P405S Strategie de realisation et d'essai`
2. `P2871 Specifications du systeme`
3. `P490S Specifications de l'unite de tache`
4. `P580S Specifications de processus automatise`, si la solution inclut des traitements automatises
5. `P555S Specifications de composant logiciel`
6. `P415G Plan d'integration et de verification`
7. `P750S Cas d'essai`
8. `P770S Resultats d'essai`
9. `P450S Plan d'implantation`
10. `P705S Guide d'operation`

## Livrables pour les operations et l exploitation d une solution

Pour documenter les operations et l exploitation d une solution selon Macroscope, couvrir l installation, les procedures d exploitation, le soutien, les niveaux de service, la maintenance, la gestion des changements, les anomalies et la configuration.

| Besoin de documentation | Livrable Macroscope | Utilisation |
| --- | --- | --- |
| Guide d exploitation | `P705S Guide d'operation` | Decrire les mesures a prendre par le personnel de soutien et d exploitation pour installer, utiliser et soutenir le systeme. |
| Procedures operateur | `P705U Guide de l'operateur` | Detailer les actions a executer pour le fonctionnement technique du systeme dans des circonstances precises. |
| Instructions d installation techniques | `P720C Instructions d'installation, niveau realisateur` | Specifier la configuration des composants logiciels a installer pour le fonctionnement du systeme. |
| Instructions d installation utilisateur | `P720U Instructions d'installation, niveau utilisateur` | Decrire l installation ou la configuration cote utilisateur. |
| Entente de niveau de service | `P931G Entente de niveau de service` | Definir les priorites, responsabilites, cibles de performance, metriques, procedures de gestion et escalades. |
| Plan de maintenance | `P895S Plan global de maintenance` | Organiser la maintenance, les responsabilites, les activites recurrentes et le suivi. |
| Demande de changement | `P891S Demande de changement` | Documenter les demandes de correction, amelioration ou modification en exploitation. |
| Registre des changements | `P901S Registre des demandes de changement` | Suivre l etat, la priorite, l historique et le traitement des changements. |
| Anomalies | `P070M Anomalie` | Decrire une anomalie, son contexte, son impact et sa resolution attendue. |
| Registre des anomalies | `P072M Registre des anomalies` | Centraliser le suivi des anomalies. |
| Gestion de configuration | `P951S Plan de gestion de configuration` | Definir l approche de controle des elements de configuration. |
| Referentiel de configuration | `P950S Base de donnees de la gestion de configuration` | Structurer les donnees de configuration, versions, etats, dependances, relations avec incidents, problemes et changements. |

Le minimum praticable pour documenter les operations et l exploitation d une solution est :

1. `P705S Guide d'operation`
2. `P705U Guide de l'operateur`
3. `P720C Instructions d'installation, niveau realisateur`
4. `P931G Entente de niveau de service`
5. `P895S Plan global de maintenance`
6. `P891S Demande de changement`
7. `P901S Registre des demandes de changement`
8. `P070M Anomalie`
9. `P072M Registre des anomalies`
10. `P951S Plan de gestion de configuration`
11. `P950S Base de donnees de la gestion de configuration`

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
