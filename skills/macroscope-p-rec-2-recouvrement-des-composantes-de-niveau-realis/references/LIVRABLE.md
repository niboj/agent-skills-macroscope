# Référence du livrable P-REC.2 Recouvrement des composantes de niveau réalisateur

## Source analysée

- Fichier source : `../../../macroscope/livrables/b1ab8dae74e7.md`
- Méthode source : Macroscope
- Extraction du titre : lien inverse par URL

## Synthèse du livrable

Dans le contexte de cette activité, les modèles et spécifications de niveau réalisateur touchés par le changement sont récupérés, et les règles réalisateur qui vont servir à la réalisation du changement sont déterminées. Au besoin, l'Analyste-programmeur, aidé des membres désignés de l'Équipe de maintenance, documente les composantes de niveau réalisateur touchées du système : modules ou programmes (leur code et la façon dont ils interagissent), bases de données ou fichiers physiques. Parallèlement, l'Administrateur de base de données établit la structure de l'information persistante à partir de l'information obtenue suite au recouvrement des bases de données ou fichiers physiques. L'Conseiller en architecture technique ébauche l'architecture logicielle, l'infrastructure technologique (incluant les modèles réalisateur de la répartition) et les règles réalisateur, d'après l'information découverte. Les résultats de cette activité sont placés sous gestion de configuration (pour en savoir plus au sujet de la gestion de configuration, veuillez vous référer au processus Contrôle de la gestion de configuration). Ces composantes de niveau réalisateur sont maintenant prêtes à être modifiées pour refléter le changement, dans le contexte de la phase Conception et réalisation. Elles servent aussi à déterminer quelles composantes de niveau utilisateur du système devront être récupérées dans la prochaine activité.

## Raison d’être

Aucune raison d’être explicite n’a été extraite. Déduire l’intention du livrable à partir de sa description, de son contenu et des livrables liés.

## Occurrence

Aucune occurrence explicite n’a été extraite du fichier source.

## Structure détaillée du livrable

1. Synthese
2. Portee
3. Contenu du livrable
4. Decisions et points ouverts
5. Tracabilite TOGAF

## Champs ou sections attendus

- Aucune information explicite extraite du fichier source.

## Objets documentés

- * Récupérer les composantes (modèles, spécifications) de niveau réalisateur touchées par le changement.
- * Récupérer les règles réalisateur qui vont guider la réalisation du changement.
- * Obtenir une documentation de base sur le système touché du point de vue du réalisateur.
- Dans le contexte de cette activité, les modèles et spécifications de niveau réalisateur touchés par le changement sont récupérés, et les règles réalisateur qui vont servir à la réalisation du changement sont déterminées.
- Au besoin, l'Analyste-programmeur, aidé des membres désignés de l'Équipe de maintenance, documente les composantes de niveau réalisateur touchées du système : modules ou programmes (leur code et la façon dont ils interagissent), bases de données ou fichiers ph
- Parallèlement, l'Administrateur de base de données établit la structure de l'information persistante à partir de l'information obtenue suite au recouvrement des bases de données ou fichiers physiques.
- L'Conseiller en architecture technique ébauche l'architecture logicielle, l'infrastructure technologique (incluant les modèles réalisateur de la répartition) et les règles réalisateur, d'après l'information découverte.
- Les résultats de cette activité sont placés sous gestion de configuration (pour en savoir plus au sujet de la gestion de configuration, veuillez vous référer au processus Contrôle de la gestion de configuration).
- Ces composantes de niveau réalisateur sont maintenant prêtes à être modifiées pour refléter le changement, dans le contexte de la phase Conception et réalisation.
- Elles servent aussi à déterminer quelles composantes de niveau utilisateur du système devront être récupérées dans la prochaine activité.
- De plus, les règles réalisateur existantes, les définitions de bases de données et d’autres éléments des bibliothèques existantes du système peuvent s’avérer utiles.
- Des règles réalisateur applicables venant d’autres systèmes peuvent servir de guide et assurer la cohérence.

## Tableaux, modèles ou diagrammes recommandés

- * Récupérer les composantes (modèles, spécifications) de niveau réalisateur touchées par le changement.
- Dans le contexte de cette activité, les modèles et spécifications de niveau réalisateur touchés par le changement sont récupérés, et les règles réalisateur qui vont servir à la réalisation du changement sont déterminées.
- L'Conseiller en architecture technique ébauche l'architecture logicielle, l'infrastructure technologique (incluant les modèles réalisateur de la répartition) et les règles réalisateur, d'après l'information découverte.

## Livrables et références liés

- P891S Demande de changement
- P280S Impacts
- P-REC.1 Décrire le cadre d'architecture du système
- P219S - Architecture logicielle
- P370S - Infrastructure technologique
- P380S - Règles réalisateur
- P510S - Structure de l'information persistante
- P540S - Spécifications de la séquence réalisateur
- P555S - Spécifications de composant logiciel
- P555S Spécifications de composant logiciel
- P510S Structure de l'information persistante
- P540S Spécifications de la séquence réalisateur
- P219S Architecture logicielle
- P370S Infrastructure technologique
- P380S Règles réalisateur

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase C - Architecture des données (Data Architecture).
- Livrable TOGAF cible : Document de définition d’architecture (Architecture Definition Document).
- Domaine d’architecture principal : architecture des données.
- Artefacts associés : Entité de données, Modèle conceptuel de données, Matrice données-fonctions.

## Règles particulières de rédaction

- Présenter P-REC.2 Recouvrement des composantes de niveau réalisateur comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
- Ne jamais faire primer Macroscope sur TOGAF.
- Documenter les hypothèses et les points à confirmer lorsque la source utilisateur est incomplète.
- Relier les éléments du livrable aux exigences, décisions, vues, composants et risques pertinents.
- Utiliser le terme conseiller en architecture pour désigner la contribution d’architecture.

## Exemples utiles ou indications extraites

- Les composantes de niveau utilisateur touchées, particulièrement les unités de tâche déjà identifiées dans la demande de changement, dans P-REC.1 Décrire le cadre d'architecture du système ou dans la phase Conception et réalisation de maintenance, aident à ide
- Les livrables suivants peuvent servir à documenter les résultats de cette activité de technique.

## Points de vigilance

- Vérifier que le livrable répond au besoin utilisateur plutôt qu’à une reproduction mécanique du gabarit.
- Éviter les doublons avec les autres livrables Macroscope liés.
- Ne pas transformer une annexe détaillée en décision d’architecture principale.
- Signaler les sections non applicables au lieu de les remplir artificiellement.
- Conserver la traçabilité entre sources, exigences, décisions et artefacts TOGAF.

## Extraits de contexte Macroscope

### Description

Dans le contexte de cette activité, les modèles et spécifications de niveau réalisateur touchés par le changement sont récupérés, et les règles réalisateur qui vont servir à la réalisation du changement sont déterminées. Au besoin, l'Analyste-programmeur, aidé des membres désignés de l'Équipe de maintenance, documente les composantes de niveau réalisateur touchées du système : modules ou programmes (leur code et la façon dont ils interagissent), bases de données ou fichiers physiques. Parallèlement, l'Administrateur de base de données établit la structure de l'information persistante à partir de l'information obtenue suite au recouvrement des bases de données ou fichiers physiques. L'Conseiller en architecture technique ébauche l'architecture logicielle, l'infrastructure technologique (incluant les modèles réalisateur de la répartition) et les règles réalisateur, d'après l'information découverte. Les résultats de cette activité sont placés sous gestion de configuration (pour en savoir plus au sujet de la gestion de configuration, veuillez vous référer au processus Contrôle de la gestion de configuration). Ces composantes de niveau réalisateur sont maintenant prêtes à être modifiées pour refléter le changement, dans le contexte de la phase Conception et réalisation. Elles servent aussi à déterminer quelles composantes de niveau utilisateur du système devront être récupérées dans la prochaine activité.

### Intrants

On peut retrouver des renseignements précieux à même le P891S Demande de changement et dans des documents connexes tels que le P280S Impacts . De plus, les règles réalisateur existantes, les définitions de bases de données et d’autres éléments des bibliothèques existantes du système peuvent s’avérer utiles. Des règles réalisateur applicables venant d’autres systèmes peuvent servir de guide et assurer la cohérence. Les composantes de niveau utilisateur touchées, particulièrement les unités de tâche déjà identifiées dans la demande de changement, dans P-REC.1 Décrire le cadre d'architecture du système ou dans la phase Conception et réalisation de maintenance, aident à identifier les composantes de niveau réalisateur à récupérer.

### Extrants

Les livrables suivants peuvent servir à documenter les résultats de cette activité de technique. Les sections du livrable qui sont applicables sont montrées dans la liste sous chaque livrable.

### Procédure ou indications de production

Bien que présentées dans un ordre séquentiel, les étapes suivantes devraient être effectuées parallèlement pour plus d'efficacité : 1. Les modules de niveau réalisateur (ou programmes) touchés par le changement sont identifiés. La section Intrants de cette activité de technique suggère des sources précieuses d'information. 2. Les spécifications réalisateur sont ébauchées pour chaque module de niveau réalisateur identifié dans le P555S Spécifications de composant logiciel. Ces composants logiciels participent aux unités de tâche et aux chaînes de traitement en différé touchées. 3. Les bases de données et données utilisées par les modules identifiés de niveau réalisateur sont identifiées et documentées (totalement ou seulement les portions utilisées) dans le P510S Structure de l'information persistante. 4. L'organisation et l'enchaînement des composantes de niveau réalisateur sont déterminés et décrits dans le P540S Spécifications de la séquence réalisateur. 5. Au besoin, dans le contexte du changement à appliquer, l'architecture logicielle est décrite comme une partition des sous-systèmes niveau réalisateur, et les interfaces qui donnent accès à ces sous-systèmes niveau réalisateur sont présentées. Tout est documenté dans le P219S Architecture logicielle. 6. Dans le contexte du changement à appliquer, l'infrastructure technologique nécessaire au support du système d'information est décrite dans le P370S Infrastructure technologique, s'il y a lieu. Ce livrable documente aussi la répartition réalisateur, montrant celle des données et processus relatifs aux diverses configurations d'infrastructure technologique. 7. Les règles réalisateur qui s'appliquent aux composantes de niveau réalisateur sont définies et documentées dans le P380S Règles réalisateur. 8. Les composantes du système récupérées de niveau réalisateur sont placées sous gestion de configuration. Pour en savoir plus au sujet de la gestion de configuration, veuillez vous référer au processus Contrôle de la gestion de configuration.

### Rôles mentionnés dans la source

* Administrateur de base de données * Équipe de maintenance * Analyste-programmeur * Conseiller en architecture technique
