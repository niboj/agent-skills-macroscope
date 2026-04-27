# http://intradoc-cadrenormatif.itp.extra/DMRPFr/Html/Fr_P_10364_99_DEL.html

|   
####  Raison d'être
  * Saisir et structurer les données de configuration et l'information concernant les [éléments de configuration](javascript:openPopUp\('/DMRHomeFr/Html/Fr_12707_100_748_CPP.html'\);), y compris leurs relations et dépendances durant leur cycle de vie.
  * Permettre aux projets d'exploitation informatique, et de mise en oeuvre et de maintenance de mieux comprendre les interdépendances entre les composantes qu'ils ont à traiter.


####  Description
Ce livrable présente les exigences minimales pour une base de données de la gestion de configuration (BDGC). La BDGC est un référentiel comprenant les données de configuration et l'information concernant les [éléments de configuration](javascript:openPopUp\('/DMRHomeFr/Html/Fr_12707_100_748_CPP.html'\);), ainsi que leurs relations et dépendances durant leur cycle de vie. La BDGC devrait être gérée exclusivement par la fonction de [gestion de configuration](javascript:openPopUp\('/DMRHomeFr/Html/Fr_4962_104_748_CPP.html'\);). La BDGC est au centre des activités d'exploitation informatique, et de mise en oeuvre et de maintenance, étant donné qu'elle contient, en plus des données de configuration et des éléments de configuration, de l'information utile telle que les profils d'utilisateurs, les configurations technologiques, les composantes de système et de service, les demandes de changement, les incidents, les problèmes et autres, et les relations entre toutes ces composantes. On consulte la BDGC pour, entre autres, avoir de l'information au sujet des ententes de niveau de service ou, lors des activités de soutien, pour évaluer l'impact d'un incident, ou rechercher des incidents ou problèmes connexes qui pourraient aider à le résoudre. Une organisation peut utiliser plus d'une BDGC pour la gestion de configuration. À tout le moins, la BDGC devrait contenir les informations suivantes (l'information doit être conforme au [P951S Plan de gestion de configuration](http://intradoc-cadrenormatif.itp.extra/DMRPFr/Html/Fr_P_1615_7_577_DEL.html)) :
  * Nom et identifiant uniques de l'élément de configuration (dans le cas d'un élément de configuration, il peut aussi y avoir les numéros de série et de modèles).
  * Version de l'élément de configuration.
  * État de l'élément de configuration (tel que «essai d'intégration» , «essai d'acceptation» , «production», «archive», etc.) et identifiant de la [configuration de référence](javascript:openPopUp\('/DMRHomeFr/Html/Fr_12909_100_CPP.html'\);) connexe.
  * Au besoin, la date planifiée (ou événement déclencheur) pour un changement d'état de l'élément de configuration (par exemple, dans le cas d'un élément de configuration que l'on prévoit mettre à jour, remplacer ou retirer).
  * Type de l'élément de configuration (par exemple, à un niveau plus général : matériel, logiciel, fournitures de bureau, documentation; à un niveau plus détaillé : exigences, spécifications, code, plans d'essai, matériel de formation, etc.).
  * Description de l'élément de configuration.
  * Propriétaire de l'élément de configuration (celui qui en a la responsabilité).
  * Emplacement de l'élément de configuration (bibliothèque ou lieu physique selon le type de l'élément).
  * Informations relatives à la création ou l'acquisition de l'élément de configuration, incluant son origine (développement à l'interne ou fournisseur tiers), sa date de création ou d'acquisition et, s'il y a lieu, sa date de renouvellement.
  * S'il y a lieu, information légale et contractuelle (ou sur la licence).
  * Registre de l'historique des changements apportés.
  * Relations parent/enfant : identifiant unique pour le parent et les enfants selon le cas.
  * Autres relations entre les éléments de configuration (par exemple, «est utilisé par», «est installé sur», etc.).
  * Relations des éléments de configuration avec les incidents, les problèmes et les demandes de changement connexes (par leur identifiant unique).
  * Relations entre les services et leurs éléments de configuration sous-jacents.
  * Enregistrement des incidents, des problèmes et des demandes de changement.

La BDGC peut évidemment contenir beaucoup plus d'information, selon les besoins de l'organisation et la flexibilité des outils utilisés. Ce livrable ne propose pas de contenu détaillé étant donné que les organisations utilisent des outils différents selon leurs besoins spécifiques.
#### Relations entre livrables
![](http://intradoc-cadrenormatif.itp.extra/DMRPFr/Images/Fr_P_Del_Dep_P950S.jpg)  |  
| --- |
