# http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_908_99_72_TAC.html

|   
####  Raison d'être
    * Récupérer les composantes (modèles, spécifications) de niveau réalisateur touchées par le changement.
    * Récupérer les règles réalisateur qui vont guider la réalisation du changement.
    * Obtenir une documentation de base sur le système touché du point de vue du réalisateur.


####  Description
Dans le contexte de cette activité, les modèles et spécifications de niveau réalisateur touchés par le changement sont récupérés, et les règles réalisateur qui vont servir à la réalisation du changement sont déterminées. Au besoin, l'[Analyste-programmeur](http://intradoc-cadrenormatif.itp.extra/DMRPFr/Html/Fr_P_354_99_597_ROL.html), aidé des membres désignés de l'[Équipe de maintenance](http://intradoc-cadrenormatif.itp.extra/DMRPFr/Html/Fr_P_318_31_597_ROL.html), documente les composantes de niveau réalisateur touchées du système : modules ou programmes (leur code et la façon dont ils interagissent), bases de données ou fichiers physiques. Parallèlement, l'[Administrateur de base de données](http://intradoc-cadrenormatif.itp.extra/DMRPFr/Html/Fr_P_44_19_597_ROL.html) établit la structure de l'information persistante à partir de l'information obtenue suite au recouvrement des bases de données ou fichiers physiques. L'[Architecte technique](http://intradoc-cadrenormatif.itp.extra/DMRPFr/Html/Fr_P_355_99_597_ROL.html) ébauche l'architecture logicielle, l'infrastructure technologique (incluant les modèles réalisateur de la répartition) et les règles réalisateur, d'après l'information découverte. Les résultats de cette activité sont placés sous gestion de configuration (pour en savoir plus au sujet de la gestion de configuration, veuillez vous référer au processus [Contrôle de la gestion de configuration](http://intradoc-cadrenormatif.itp.extra/DMRPFr/Html/Fr_P_2650_99_PAC.html)). Ces composantes de niveau réalisateur sont maintenant prêtes à être modifiées pour refléter le changement, dans le contexte de la phase [Conception et réalisation](http://intradoc-cadrenormatif.itp.extra/DMRPFr/Html/Fr_P_2581_99_28_PAC.html). Elles servent aussi à déterminer quelles composantes de niveau utilisateur du système devront être récupérées dans la prochaine activité.
####  Intrants
On peut retrouver des renseignements précieux à même le [P891S Demande de changement](http://intradoc-cadrenormatif.itp.extra/DMRPFr/Html/Fr_P_9997_99_34_DEL.html) et dans des documents connexes tels que le [P280S Impacts](http://intradoc-cadrenormatif.itp.extra/DMRPFr/Html/Fr_P_2620_99_34_DEL.html) . De plus, les règles réalisateur existantes, les définitions de bases de données et d’autres éléments des bibliothèques existantes du système peuvent s’avérer utiles. Des règles réalisateur applicables venant d’autres systèmes peuvent servir de guide et assurer la cohérence. Les composantes de niveau utilisateur touchées, particulièrement les unités de tâche déjà identifiées dans la demande de changement, dans [P-REC.1 Décrire le cadre d'architecture du système](http://intradoc-cadrenormatif.itp.extra/DMRPFr/Html/Fr_P_907_99_72_TAC.html) ou dans la phase [Conception et réalisation](http://intradoc-cadrenormatif.itp.extra/DMRPFr/Html/Fr_P_2581_99_28_PAC.html) de maintenance, aident à identifier les composantes de niveau réalisateur à récupérer.
####  Extrants
Les livrables suivants peuvent servir à documenter les résultats de cette activité de technique. Les sections du livrable qui sont applicables sont montrées dans la liste sous chaque livrable.
####  [P219S - Architecture logicielle](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_1151_7_577_DEL.html)
####  [P370S - Infrastructure technologique](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_1255_7_577_DEL.html)
####  [P380S - Règles réalisateur](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_1258_7_577_DEL.html)
####  [P510S - Structure de l'information persistante](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_2660_99_34_DEL.html)
####  [P540S - Spécifications de la séquence réalisateur](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_2665_99_34_DEL.html)
####  [P555S - Spécifications de composant logiciel](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_2670_99_34_DEL.html)
####  Rôles
  * [Administrateur de base de données](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_44_19_597_ROL.html)
  * [Équipe de maintenance](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_318_31_597_ROL.html)
  * [Analyste-programmeur](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_354_99_597_ROL.html)
  * [Architecte technique](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_355_99_597_ROL.html)


####  Procédure
Bien que présentées dans un ordre séquentiel, les étapes suivantes devraient être effectuées parallèlement pour plus d'efficacité :
  1. Les modules de niveau réalisateur (ou programmes) touchés par le changement sont identifiés. La section Intrants de cette activité de technique suggère des sources précieuses d'information.
  2. Les spécifications réalisateur sont ébauchées pour chaque module de niveau réalisateur identifié dans le [P555S Spécifications de composant logiciel](http://intradoc-cadrenormatif.itp.extra/DMRPFr/Html/Fr_P_2670_99_34_DEL.html). Ces composants logiciels participent aux unités de tâche et aux chaînes de traitement en différé touchées.
  3. Les bases de données et données utilisées par les modules identifiés de niveau réalisateur sont identifiées et documentées (totalement ou seulement les portions utilisées) dans le [P510S Structure de l'information persistante](http://intradoc-cadrenormatif.itp.extra/DMRPFr/Html/Fr_P_2660_99_34_DEL.html).
  4. L'organisation et l'enchaînement des composantes de niveau réalisateur sont déterminés et décrits dans le [P540S Spécifications de la séquence réalisateur](http://intradoc-cadrenormatif.itp.extra/DMRPFr/Html/Fr_P_2665_99_34_DEL.html).
  5. Au besoin, dans le contexte du changement à appliquer, l'architecture logicielle est décrite comme une partition des sous-systèmes niveau réalisateur, et les interfaces qui donnent accès à ces sous-systèmes niveau réalisateur sont présentées. Tout est documenté dans le [P219S Architecture logicielle](http://intradoc-cadrenormatif.itp.extra/DMRPFr/Html/Fr_P_1151_7_577_DEL.html).
  6. Dans le contexte du changement à appliquer, l'infrastructure technologique nécessaire au support du système d'information est décrite dans le [P370S Infrastructure technologique](http://intradoc-cadrenormatif.itp.extra/DMRPFr/Html/Fr_P_1255_7_577_DEL.html), s'il y a lieu. Ce livrable documente aussi la répartition réalisateur, montrant celle des données et processus relatifs aux diverses configurations d'infrastructure technologique.
  7. Les règles réalisateur qui s'appliquent aux composantes de niveau réalisateur sont définies et documentées dans le [P380S Règles réalisateur](http://intradoc-cadrenormatif.itp.extra/DMRPFr/Html/Fr_P_1258_7_577_DEL.html).
  8. Les composantes du système récupérées de niveau réalisateur sont placées sous gestion de configuration. Pour en savoir plus au sujet de la gestion de configuration, veuillez vous référer au processus [Contrôle de la gestion de configuration](http://intradoc-cadrenormatif.itp.extra/DMRPFr/Html/Fr_P_2650_99_PAC.html).

 |  
| --- |
