# agent-skills-macroscope

Dépôt de skills IA pour aider à produire, réviser et normaliser des livrables selon la méthodologie Macroscope.

Ce dépôt est initialisé à partir du gabarit `gabarit-agent-skills-depot-code`. Il conserve les conventions de structure Agent Skills du gabarit, puis les spécialise pour un usage de rédaction de livrables Macroscope.

## Objectif

Le dépôt sert à constituer une bibliothèque de skills réutilisables pour :

- cadrer une demande de livrable Macroscope ;
- retrouver les références pertinentes dans le corpus local ;
- produire un livrable cohérent avec la terminologie et les conventions Macroscope ;
- réviser un livrable existant selon sa structure, sa traçabilité et sa complétude ;
- faire évoluer progressivement les skills à partir d'exemples réels.

## Documents connexes

Les documents suivants complètent ce README et précisent comment utiliser les livrables comme intrants entre les phases de travail :

| Document | Rôle |
| --- | --- |
| [`cadre-architecutre.md`](cadre-architecutre.md) | Explique le cadre d'architecture, les étapes, les préalables, les publics cibles, les responsabilités et les contrôles de qualité. |
| [`approche-documentation.md`](approche-documentation.md) | Définit l'approche de documentation orientée transfert vers la réalisation, incluant le paquet de transfert, la matrice de transfert et les critères de prêt. |
| [`macroscope/README.md`](macroscope/README.md) | Décrit le corpus local de références Macroscope et les règles d'utilisation des sources. |
| [`skills/README.md`](skills/README.md) | Décrit l'organisation des skills, les skills transversales et les conventions communes du répertoire `skills/`. |

## Livrables pour l'architecture d'affaires

Pour documenter l'architecture d'affaires selon Macroscope, utiliser les livrables suivants comme noyau de travail. Le choix final dépend de la portée, du niveau de détail attendu et des intrants disponibles.

| Besoin de documentation | Livrable Macroscope | Utilisation |
| --- | --- | --- |
| Objectifs d'affaires et résultats attendus | `P130O Objectifs du système d'information` | Définir les résultats visés et les critères mesurables d'évaluation. |
| Portée métier | `P140O Portée du système d'information` | Délimiter le système, les frontières, les sujets et le périmètre de changement. |
| Exigences d'affaires | `P140S Exigences propriétaire` ou `P2863 Exigences` | Capturer les besoins, contraintes, orientations et exigences indépendantes d'une solution. |
| Vue métier de haut niveau | `P201S Processus du système` | Décrire les processus de haut niveau, les dépendances, les participants et la dynamique du système. |
| Dynamique métier | `P201O Dynamique du système d'information` | Décrire l'enchaînement des processus du système. |
| Fonctions métier et usage | `P250S Structure utilisateur du système` et `P250U Fonction` | Structurer les fonctions, responsabilités et unités de tâche. |
| Processus de travail | `P251S Processus de travail` et `P251U Processus de travail utilisateur` | Décrire les processus de travail, les participants et les unités de tâche manuelles ou automatisées. |
| Détail des unités de tâche | `P490S Spécifications de l'unité de tâche` | Détailler les scénarios, interactions et comportements lorsque nécessaire. |
| Règles métier | `P360S Règles utilisateur`, `P361U Règles administratives et d'organisation du travail`, `P363U Règles de fonctionnement du traitement automatisé` | Documenter les règles qui gouvernent les processus, décisions et traitements. |
| Impacts organisationnels | `P280S Impacts`, avec `P280O` et `P280U` au besoin | Décrire les impacts sur l'organisation, les rôles, les façons de travailler et les systèmes. |
| Traçabilité | `P900S Suivi des exigences` | Relier exigences, processus, fonctions, règles, décisions et composants de solution. |

Le minimum praticable pour une architecture d'affaires complète mais raisonnable est :

1. `P130O Objectifs du système d'information`
2. `P140O Portée du système d'information`
3. `P2863 Exigences` ou `P140S Exigences propriétaire`
4. `P201S Processus du système`
5. `P251S Processus de travail`
6. `P250S Structure utilisateur du système`
7. `P360S Règles utilisateur`
8. `P280S Impacts`
9. `P900S Suivi des exigences`

## Livrables pour l'architecture de solution

Pour documenter l'architecture d'une solution selon Macroscope, couvrir les vues d'exigences, d'affaires, de données, applicative, technologique, sécurité, implantation et exploitation. Le choix final dépend de la nature de la solution, du niveau de détail attendu et des livraisons visées.

| Besoin de documentation | Livrable Macroscope | Utilisation |
| --- | --- | --- |
| Cadrage et exigences | `P2863 Exigences` | Regrouper les besoins, orientations, contraintes et exigences de base de la solution. |
| Cadre d'architecture | `P200A Cadre d'architecture` | Documenter le cadre général, les exigences d'affaires et techniques clés, les décisions et la portée. |
| Système actuel ou référence | `P120S` | Décrire le système actuel, les processus, ressources, informations, technologies, forces, faiblesses et constats de sécurité. |
| Architecture d'affaires | `P201S Processus du système` et, au besoin, `P251S Processus de travail` | Décrire la dynamique du système, les processus, les fonctions et les usages. |
| Architecture des données | `P170S Structure de l'information`, `P150C Bases de données`, `P510S Structure de l'information persistante` | Documenter l'information, les données persistantes et les bases de données. |
| Architecture applicative | `P219S Architecture logicielle` | Décrire le découpage des logiciels applicatifs en sous-systèmes et composants. |
| Détail applicatif | `P219C Sous-système, niveau réalisateur`, `P229C Interfaces du sous-système, niveau réalisateur`, `P555S Spécifications de composant logiciel` | Détailler les sous-systèmes, interfaces et composants lorsque le niveau de précision le justifie. |
| Architecture technologique | `P269S Technologie et répartition utilisateur`, complété par `P268U` et `P269U` | Décrire les composantes d'infrastructure, la technologie et la répartition. |
| Sécurité | Sections sécurité de `P120S`, exigences de sécurité et vues de contrôle associées | Documenter la sensibilité des actifs, les menaces, les risques, les mesures de protection, les accès et les contrôles. |
| Traçabilité | `P900S Suivi des exigences` | Relier les exigences à l'architecture, aux spécifications et aux composants qui les réalisent. |
| Implantation | `P270S Stratégie d'implantation`, puis `P450S Plan d'implantation` | Préparer la transition, les contraintes, les lots de livraison et les activités d'implantation. |
| Exploitation | `P705S Guide d'opération` | Documenter les mesures d'installation, d'exploitation et de soutien. |

Le minimum praticable pour une architecture de solution complète mais raisonnable est :

1. `P2863 Exigences`
2. `P200A Cadre d'architecture`
3. `P120S`
4. `P201S Processus du système`
5. `P170S Structure de l'information` ou `P510S Structure de l'information persistante`
6. `P219S Architecture logicielle`
7. `P269S Technologie et répartition utilisateur`
8. `P900S Suivi des exigences`
9. `P270S Stratégie d'implantation` ou `P450S Plan d'implantation`

## Livrables pour la réalisation d'une solution

Pour documenter la réalisation d'une solution selon Macroscope, couvrir la planification de la réalisation, les spécifications détaillées, les composants produits, les essais, l'implantation et l'exploitation. Le choix final dépend du type de solution, du mode de livraison et du niveau de preuve attendu.

| Besoin de documentation | Livrable Macroscope | Utilisation |
| --- | --- | --- |
| Vue d'ensemble de la réalisation | `P2397 AG.2 Conception et réalisation d'une livraison` ou `P3358 Conception et réalisation d'une livraison` | Décrire la phase de conception et réalisation, les itérations, les composants produits et la validation progressive. |
| Stratégie de réalisation et d'essai | `P405S Stratégie de réalisation et d'essai` | Définir l'approche de conception, de réalisation, d'essai et de gestion des essais. |
| Spécifications du système | `P2871 Spécifications du système` | Regrouper les spécifications qui guident la construction de la solution. |
| Spécifications des unités de tâche | `P490S Spécifications de l'unité de tâche` | Décrire les scénarios, interactions, comportements et unités de travail à réaliser. |
| Spécifications des processus automatisés | `P580S Spécifications de processus automatisé` | Décrire les chaînes, traitements automatisés, tâches et cheminements. |
| Spécifications des composants logiciels | `P555S Spécifications de composant logiciel` | Définir les composants, classes, modules et interfaces à produire. |
| Interfaces de réalisation | `P560C Interface, niveau réalisateur` ou `P229C Interfaces du sous-système, niveau réalisateur` | Décrire les interfaces techniques ou applicatives nécessaires à la réalisation. |
| Code et composants produits | `P650C Code` et `P600A Composants logiciels` | Documenter ou référencer les composants logiciels réalisés. |
| Environnements d'essai | `P730C Environnement d'essai unitaire`, `P740C Environnement d'essai d'intégration`, `P740S Environnement d'essai` | Décrire les environnements requis pour vérifier la solution. |
| Plan d'intégration et de vérification | `P415G Plan d'intégration et de vérification` | Organiser l'intégration, les sous-livraisons et les vérifications. |
| Cas et résultats d'essai | `P750S Cas d'essai`, `P750A Cas d'essai et résultats`, `P770S Résultats d'essai` | Décrire les cas d'essai, exécutions, résultats et écarts. |
| Anomalies | `P070M Anomalie`, `P072M Registre des anomalies` | Documenter les anomalies, leur suivi et leur résolution. |
| Implantation | `P450S Plan d'implantation`, `P720C Instructions d'installation, niveau réalisateur` | Préparer l'installation, la transition et les contraintes d'implantation. |
| Exploitation | `P705S Guide d'opération` | Décrire les mesures d'installation, d'exploitation et de soutien. |

Le minimum praticable pour documenter la réalisation d'une solution est :

1. `P405S Stratégie de réalisation et d'essai`
2. `P2871 Spécifications du système`
3. `P490S Spécifications de l'unité de tâche`
4. `P580S Spécifications de processus automatisé`, si la solution inclut des traitements automatisés
5. `P555S Spécifications de composant logiciel`
6. `P415G Plan d'intégration et de vérification`
7. `P750S Cas d'essai`
8. `P770S Résultats d'essai`
9. `P450S Plan d'implantation`
10. `P705S Guide d'opération`

## Livrables pour les opérations et l'exploitation d'une solution

Pour documenter les opérations et l'exploitation d'une solution selon Macroscope, couvrir l'installation, les procédures d'exploitation, le soutien, les niveaux de service, la maintenance, la gestion des changements, les anomalies et la configuration.

| Besoin de documentation | Livrable Macroscope | Utilisation |
| --- | --- | --- |
| Guide d'exploitation | `P705S Guide d'opération` | Décrire les mesures à prendre par le personnel de soutien et d'exploitation pour installer, utiliser et soutenir le système. |
| Procédures opérateur | `P705U Guide de l'opérateur` | Détailler les actions à exécuter pour le fonctionnement technique du système dans des circonstances précises. |
| Instructions d'installation techniques | `P720C Instructions d'installation, niveau réalisateur` | Spécifier la configuration des composants logiciels à installer pour le fonctionnement du système. |
| Instructions d'installation utilisateur | `P720U Instructions d'installation, niveau utilisateur` | Décrire l'installation ou la configuration côté utilisateur. |
| Entente de niveau de service | `P931G Entente de niveau de service` | Définir les priorités, responsabilités, cibles de performance, métriques, procédures de gestion et escalades. |
| Plan de maintenance | `P895S Plan global de maintenance` | Organiser la maintenance, les responsabilités, les activités récurrentes et le suivi. |
| Demande de changement | `P891S Demande de changement` | Documenter les demandes de correction, amélioration ou modification en exploitation. |
| Registre des changements | `P901S Registre des demandes de changement` | Suivre l'état, la priorité, l'historique et le traitement des changements. |
| Anomalies | `P070M Anomalie` | Décrire une anomalie, son contexte, son impact et sa résolution attendue. |
| Registre des anomalies | `P072M Registre des anomalies` | Centraliser le suivi des anomalies. |
| Gestion de configuration | `P951S Plan de gestion de configuration` | Définir l'approche de contrôle des éléments de configuration. |
| Référentiel de configuration | `P950S Base de données de la gestion de configuration` | Structurer les données de configuration, versions, états, dépendances, relations avec incidents, problèmes et changements. |

Le minimum praticable pour documenter les opérations et l'exploitation d'une solution est :

1. `P705S Guide d'opération`
2. `P705U Guide de l'opérateur`
3. `P720C Instructions d'installation, niveau réalisateur`
4. `P931G Entente de niveau de service`
5. `P895S Plan global de maintenance`
6. `P891S Demande de changement`
7. `P901S Registre des demandes de changement`
8. `P070M Anomalie`
9. `P072M Registre des anomalies`
10. `P951S Plan de gestion de configuration`
11. `P950S Base de données de la gestion de configuration`

## Structure du dépôt

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

## Rôle des répertoires

- `skills/` : bibliothèque de skills, un dossier par capacité.
- `macroscope/livrables/` : corpus local de pages et descriptions Macroscope utilisé comme référence de travail.
- `references/` : conventions partagées pour la rédaction, la structure et la compatibilité des skills.
- `gabarits/` : modèles de départ pour créer de nouvelles skills et évaluations.
- `utilitaires/` : scripts non interactifs pour initialiser, vérifier et installer les skills.
- `evaluations/` : cas d'évaluation au niveau du dépôt.
- `exemples/` : sources et sorties dérivées pour guider la création de nouvelles skills.
- `documentation/` : documentation humaine sur la rédaction et la maintenance des skills.

## Skills de départ

Le gabarit fournit des skills d'atelier pour concevoir, rédiger, réviser et évaluer d'autres skills. Ce dépôt ajoute aussi une première skill orientée Macroscope :

- `rediger-livrable-macroscope` : aide à produire ou réviser un livrable selon la méthodologie Macroscope en s'appuyant sur les références locales.

Les autres skills initiales restent utiles pour industrialiser la bibliothèque :

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

## Workflow recommandé

1. Identifier le type de livrable, son audience et le niveau de détail attendu.
2. Rechercher dans `macroscope/livrables/` les notions, formats ou conventions applicables.
3. Utiliser ou créer une skill spécialisée dans `skills/`.
4. Produire le livrable avec ses hypothèses, ses références et ses limites.
5. Vérifier la cohérence terminologique, la structure, la traçabilité et les sections manquantes.
6. Ajouter des cas d'évaluation quand une skill devient réutilisable.

## Créer une nouvelle skill

```bash
python3 utilitaires/initialiser_skill.py \
  --root skills \
  --name rediger-modele-processus-macroscope \
  --description "Utiliser ce skill quand il faut produire ou réviser un livrable Macroscope de modélisation de processus à partir d'exigences, d'observations métier ou d'un brouillon existant." \
  --with-references \
  --with-evals
```

Puis ajuster le `SKILL.md`, ajouter les références pertinentes et valider :

```bash
python3 utilitaires/verifier_skill.py skills/rediger-modele-processus-macroscope
python3 utilitaires/verifier_toutes_skills.py
```

## Validation

Avant publication ou installation :

- chaque skill doit contenir un `SKILL.md` avec `name` et `description` ;
- la description doit indiquer clairement quand utiliser la skill ;
- les chemins cités doivent exister ;
- les détails volumineux doivent rester dans `references/`, `scripts/`, `assets/` ou `evals/` ;
- le livrable produit doit distinguer les faits sources, les hypothèses et les points à confirmer.
