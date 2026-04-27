# Référence du livrable P891S Demande de changement

## Source analysée

- Fichier source : `../../../macroscope/livrables/5bcb9c117004.md`
- Méthode source : Macroscope
- Extraction du titre : premier lien codé du fichier

## Synthèse du livrable

L'conseiller en architecture de système et l'conseiller en architecture technique, avec l'aide du pilote, des experts du domaine ou des utilisateurs, modifient le système, selon le changement à effectuer. Tout d'abord, les modèles (pris au sens large) d'architecture du système touchés par le changement sont identifiés. Ces modèles sont ceux qui comportent les composantes (ou y sont reliés) à modifier ou à ajouter. Ces composantes sont habituellement identifiées dans la solution à exécuter recommandée (dans le P891S Demande de changement). Ensuite, un ou plusieurs des ajustements suivants s'appliquent, au besoin : * Si le changement touche la structure de l'information, l'conseiller en architecture de système révise les **facettes**. Ces dernières sont documentées dans le P170S Structure de l'information. Au besoin, l'Administrateur de base de données met à jour le P510S Structure de l'information persistante afin de refléter les changements dans la structure de l'information. * Si le changement touche les **processus de travail** , la **clientèle** , les **environnements de travail** ou les **circonstances d'utilisation** du système, l'conseiller en architecture de système ajuste le P251S Processus de travail. Par exemple, la description des ressources de travail (dans le P251S) pourrait devoir être ajustée suite à une amélioration technique ou à un changement apporté aux environnements de travail ou aux circonstances d'utilisation. Le changement peut entraîner la nécessité d'augmenter ou de réduire le personnel, de confier des responsabilités additionnelles ou différentes aux utilisateurs (lesquelles sont reflétées dans les processus de travail). * Si l'architecture du système est complexe à un tel point que des **fonctions** sont définies et qu'elles ont, par la suite, besoin d'être révisées, le P250S Structure utilisateur du système est mis à jour par l'conseiller en architecture de système. Ce livrable fait aussi l'objet d'une révision si la structure de navigation est touchée par le changement. * Si le changement exige une amélioration technique ou que certains ajustements soient effectués à l'**architecture logicielle** ou à l'**infrastructure technologique** afin de supporter le système d'information modifié, le P219S Architecture logicielle et le P370S Infrastructure technologique sont alors mis à jour tel que demandé par l'conseiller en architecture technique. * Si les données et les processus du système sont répartis sur divers sites, et si le changement (technique ou fonctionnel) a un impact sur cette **répartition** , le P269S Technologie et répartition utilisateur et le P370S Infrastructure technologique sont ajustés tel que demandé par l'architecture technique. Habituellement, la technologie niveau réalisateur et les modèles de répartition sont ajustés simultanément. Les caractéristiques réalisateur du système peuvent varier en raison des différences que présentent les divers sites en matière de matériel, de systèmes d'exploitation, de communication et d'environnements réseaux. * Si de nouvelles **composantes de niveau réalisateur** , matérielles, ainsi que de nouveaux composants logiciels devaient être intégrés au système ou inclus dans l'infrastructure technologique, afin que le changement soit appliqué efficacement, l'conseiller en architecture technique remplit donc un P267S Choix de composantes réalisateur. Il faut garder en tête que ces composantes doivent être sélectionnées selon leur conformité aux principes et critères de qualité de niveau réalisateur et utilisateur. Au besoin, de nouvelles règles de niveau utilisateur ou réalisateur devraient être déterminées afin d'établir une correspondance avec l'utilisation de ces composantes spécifiques. * Selon les exigences de changement, il est possible que de nouvelles **solutions** doivent être étudiées et comparées en se basant sur les avantages et les inconvénients. Au besoin, le système actuel est étudié afin de déterminer ce qui motive la sélection de la ou des meilleures solutions pour appliquer le changement efficacement. Le P230S Orientations utilisateur et le P231S Orientations réalisateur sont mis à jour au besoin. Les principes techniques et de niveau utilisateur sont basés sur les solutions sélectionnées. * Les modèles améliorés d'architecture peuvent avoir introduit de nouveaux **principes** (à traduire en normes) ou critères de qualité, ou augmenté la portée de ceux déjà existants. Si c'est le cas, un ou plusieurs des livrables suivants doivent être mis à jour : P240S Principes utilisateur, P261S Principes réalisateur, P360S Règles utilisateur et P380S Règles réalisateur. Occasionné par les changements successifs au système, ce qui en découle c'est qu'un important groupe de règles peut être créé dans toute l'organisation et publié afin de guider la réalisation des changements actuels ou futurs. * Une fois le changement à effectuer défini et modélisé aux niveaux utilisateur et réalisateur, l'conseiller en architecture de système devra probablement effectuer des ajustements correspondant au **niveau propriétaire**. Les livrables qui seront peut-être touchés sont les suivants : P140S Exigences propriétaire, P200S Structure propriétaire du système et P201S Processus du système. L'conseiller en architecture de système, avec l'aide de l'conseiller en architecture technique, définit aussi les spécifications de conversion (stratégie et règles) à appliquer lors de la conversion des données afin d'être conforme à un changement fonctionnel (par exemple, ajout d'attributs à une classe du noyau) ou à un changement technique (par exemple, changer la technologie de base de données). Généralement, les spécifications de conversion sont définies selon les changements apportés à la structure (facettes et classes), la technologie, la répartition ou les règles concernant les données. Les procédures de chargement et de vidage des données, les formats et normes de transformation des données font partie de ces spécifications, au besoin. S'il y a des changements aux exigences du système et si un P900S Suivi des exigences existe pour le système, alors, une fois les composantes touchées conçues, l'conseiller en architecture de système, en collaboration avec l'conseiller en architecture technique, met à jour le livrable afin de refléter la nouvelle situation. L'historique des changements aux exigences est mis à jour et une description des impacts sur l'architecture du système est fournie.

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

- * Au besoin, modifier l'architecture du système existant (modèles utilisateur et réalisateur) et les exigences du système (principes et normes), afin de refléter le changement.
- * Déterminer les spécifications de conversion selon lesquelles les données concernées seront converties pour qu'elles soient compatibles au changement à effectuer.
- * Mettre à jour les exigences de suivi du système existant, le cas échéant.
- #### Modèle du processus
- Il est possible que les modèles d'architecture de systèmes voisins soient pris en compte lors de la conception du changement.
- * **Conseiller en architecture du système existant** (voir le groupe de livrables Architecture du système)
- * **Exigences du système existant** (voir le groupe de livrables Exigences)
- #### Description du processus
- L'conseiller en architecture de système et l'conseiller en architecture technique, avec l'aide du pilote, des experts du domaine ou des utilisateurs, modifient le système, selon le changement à effectuer.
- Tout d'abord, les modèles (pris au sens large) d'architecture du système touchés par le changement sont identifiés.
- Ces modèles sont ceux qui comportent les composantes (ou y sont reliés) à modifier ou à ajouter.
- Ces composantes sont habituellement identifiées dans la solution à exécuter recommandée (dans le P891S Demande de changement).

## Tableaux, modèles ou diagrammes recommandés

- * Au besoin, modifier l'architecture du système existant (modèles utilisateur et réalisateur) et les exigences du système (principes et normes), afin de refléter le changement.
- #### Modèle du processus
- Il est possible que les modèles d'architecture de systèmes voisins soient pris en compte lors de la conception du changement.
- Tout d'abord, les modèles (pris au sens large) d'architecture du système touchés par le changement sont identifiés.
- Ces modèles sont ceux qui comportent les composantes (ou y sont reliés) à modifier ou à ajouter.
- Habituellement, la technologie niveau réalisateur et les modèles de répartition sont ajustés simultanément.
- * Les modèles améliorés d'architecture peuvent avoir introduit de nouveaux **principes** (à traduire en normes) ou critères de qualité, ou augmenté la portée de ceux déjà existants.

## Livrables et références liés

- P891S Demande de changement
- P170S Structure de l'information
- P510S Structure de l'information persistante
- P251S Processus de travail
- P250S Structure utilisateur du système
- P219S Architecture logicielle
- P370S Infrastructure technologique
- P269S Technologie et répartition utilisateur
- P267S Choix de composantes réalisateur
- P230S Orientations utilisateur
- P231S Orientations réalisateur
- P240S Principes utilisateur
- P261S Principes réalisateur
- P360S Règles utilisateur
- P380S Règles réalisateur
- P140S Exigences propriétaire
- P200S Structure propriétaire du système
- P201S Processus du système
- P900S Suivi des exigences
- P140S - Exigences propriétaire
- P170S - Structure de l'information
- P200S - Structure propriétaire du système
- P201S - Processus du système
- P219S - Architecture logicielle
- P230S - Orientations utilisateur
- P231S - Orientations réalisateur
- P240S - Principes utilisateur
- P250S - Structure utilisateur du système
- P251S - Processus de travail
- P261S - Principes réalisateur

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase A - Vision d’architecture (Architecture Vision).
- Livrable TOGAF cible : Plan de transition, exploitation et adoption.
- Domaine d’architecture principal : utilisation.
- Artefacts associés : Procédure d’exploitation, Guide utilisateur, Matériel de transfert, Demande de travail d’architecture (Request for Architecture Work).

## Règles particulières de rédaction

- Présenter P891S Demande de changement comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
- Ne jamais faire primer Macroscope sur TOGAF.
- Documenter les hypothèses et les points à confirmer lorsque la source utilisateur est incomplète.
- Relier les éléments du livrable aux exigences, décisions, vues, composants et risques pertinents.
- Utiliser le terme conseiller en architecture pour désigner la contribution d’architecture.

## Exemples utiles ou indications extraites

- Par exemple, la description des ressources de travail (dans le P251S) pourrait devoir être ajustée suite à une amélioration technique ou à un changement apporté aux environnements de travail ou aux circonstances d'utilisation.
- L'conseiller en architecture de système, avec l'aide de l'conseiller en architecture technique, définit aussi les spécifications de conversion (stratégie et règles) à appliquer lors de la conversion des données afin d'être conforme à un changement fonctionnel

## Points de vigilance

- Vérifier que le livrable répond au besoin utilisateur plutôt qu’à une reproduction mécanique du gabarit.
- Éviter les doublons avec les autres livrables Macroscope liés.
- Ne pas transformer une annexe détaillée en décision d’architecture principale.
- Signaler les sections non applicables au lieu de les remplir artificiellement.
- Conserver la traçabilité entre sources, exigences, décisions et artefacts TOGAF.

## Extraits de contexte Macroscope

### Description

L'conseiller en architecture de système et l'conseiller en architecture technique, avec l'aide du pilote, des experts du domaine ou des utilisateurs, modifient le système, selon le changement à effectuer. Tout d'abord, les modèles (pris au sens large) d'architecture du système touchés par le changement sont identifiés. Ces modèles sont ceux qui comportent les composantes (ou y sont reliés) à modifier ou à ajouter. Ces composantes sont habituellement identifiées dans la solution à exécuter recommandée (dans le P891S Demande de changement). Ensuite, un ou plusieurs des ajustements suivants s'appliquent, au besoin : * Si le changement touche la structure de l'information, l'conseiller en architecture de système révise les **facettes**. Ces dernières sont documentées dans le P170S Structure de l'information. Au besoin, l'Administrateur de base de données met à jour le P510S Structure de l'information persistante afin de refléter les changements dans la structure de l'information. * Si le changement touche les **processus de travail** , la **clientèle** , les **environnements de travail** ou les **circonstances d'utilisation** du système, l'conseiller en architecture de système ajuste le P251S Processus de travail. Par exemple, la description des ressources de travail (dans le P251S) pourrait devoir être ajustée suite à une amélioration technique ou à un changement apporté aux environnements de travail ou aux circonstances d'utilisation. Le changement peut entraîner la nécessité d'augmenter ou de réduire le personnel, de confier des responsabilités additionnelles ou différentes aux utilisateurs (lesquelles sont reflétées dans les processus de travail). * Si l'architecture du système est complexe à un tel point que des **fonctions** sont définies et qu'elles ont, par la suite, besoin d'être révisées, le P250S Structure utilisateur du système est mis à jour par l'conseiller en architecture de système. Ce livrable fait aussi l'objet d'une révision si la structure de navigation est touchée par le changement. * Si le changement exige une amélioration technique ou que certains ajustements soient effectués à l'**architecture logicielle** ou à l'**infrastructure technologique** afin de supporter le système d'information modifié, le P219S Architecture logicielle et le P370S Infrastructure technologique sont alors mis à jour tel que demandé par l'conseiller en architecture technique. * Si les données et les processus du système sont répartis sur divers sites, et si le changement (technique ou fonctionnel) a un impact sur cette **répartition** , le P269S Technologie et répartition utilisateur et le P370S Infrastructure technologique sont ajustés tel que demandé par l'architecture technique. Habituellement, la technologie niveau réalisateur et les modèles de répartition sont ajustés simultanément. Les caractéristiques réalisateur du système peuvent varier en raison des différences que présentent les divers sites en matière de matériel, de systèmes d'exploitation, de communication et d'environnements réseaux. * Si de nouvelles **composantes de niveau réalisateur** , matérielles, ainsi que de nouveaux composants logiciels devaient être intégrés au système ou inclus dans l'infrastructure technologique, afin que le changement soit appliqué efficacement, l'conseiller en architecture technique remplit donc un P267S Choix de composantes réalisateur. Il faut garder en tête que ces composantes doivent être sélectionnées selon leur conformité aux principes et critères de qualité de niveau réalisateur et utilisateur. Au besoin, de nouvelles règles de niveau utilisateur ou réalisateur devraient être déterminées afin d'établir une correspondance avec l'utilisation de ces composantes spécifiques. * Selon les exigences de changement, il est possible que de nouvelles **solutions** doivent être étudiées et comparées en se basant sur les avantages et les inconvénients. Au besoin, le système actuel est étudié afin de déterminer ce qui motive la sélection de la ou des meilleures solutions pour appliquer le changement efficacement. Le P230S Orientations utilisateur et le P231S Orientations réalisateur sont mis à jour au besoin. Les principes techniques et de niveau utilisateur sont basés sur les solutions sélectionnées. * Les modèles améliorés d'architecture peuvent avoir introduit de nouveaux **principes** (à traduire en normes) ou critères de qualité, ou augmenté la portée de ceux déjà existants. Si c'est le cas, un ou plusieurs des livrables suivants doivent être mis à jour : P240S Principes utilisateur, P261S Principes réalisateur, P360S Règles utilisateur et P380S Règles réalisateur. Occasionné par les changements successifs au système, ce qui en découle c'est qu'un important groupe de règles peut être créé dans toute l'organisation et publié afin de guider la réalisation des changements actuels ou futurs. * Une fois le changement à effectuer défini et modélisé aux niveaux utilisateur et réalisateur, l'conseiller en architecture de système devra probablement effectuer des ajustements correspondant au **niveau propriétaire**. Les livrables qui seront peut-être touchés sont les suivants : P140S Exigences propriétaire, P200S Structure propriétaire du système et P201S Processus du système. L'conseiller en architecture de système, avec l'aide de l'conseiller en architecture technique, définit aussi les spécifications de conversion (stratégie et règles) à appliquer lors de la conversion des données afin d'être conforme à un changement fonctionnel (par exemple, ajout d'attributs à une classe du noyau) ou à un changement technique (par exemple, changer la technologie de base de données). Généralement, les spécifications de conversion sont définies selon les changements apportés à la structure (facettes et classes), la technologie, la répartition ou les règles concernant les données. Les procédures de chargement et de vidage des données, les formats et normes de transformation des données font partie de ces spécifications, au besoin. S'il y a des changements aux exigences du système et si un P900S Suivi des exigences existe pour le système, alors, une fois les composantes touchées conçues, l'conseiller en architecture de système, en collaboration avec l'conseiller en architecture technique, met à jour le livrable afin de refléter la nouvelle situation. L'historique des changements aux exigences est mis à jour et une description des impacts sur l'architecture du système est fournie.

### Intrants

Il est possible que les modèles d'architecture de systèmes voisins soient pris en compte lors de la conception du changement. La ou les solutions documentées dans la ou les demandes de changement peuvent être une source d'information utile. * **Conseiller en architecture du système existant** (voir le groupe de livrables Architecture du système) * **Exigences du système existant** (voir le groupe de livrables Exigences) * P891S Demande de changement

### Extrants

Non disponible.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

* Pilote: Contribue * Administrateur de base de données: Produit * Conseiller en architecture de système: Produit * Conseiller en architecture technique: Produit * Utilisateur: Contribue * Expert du domaine: Contribue
