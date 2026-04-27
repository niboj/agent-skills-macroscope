# http://intradoc-cadrenormatif.itp.extra/DMRPFr/Html/Fr_P_6156_99_39_TEC.html

|   
####  Raison d'être
  * Récupérer la documentation du système touché par le changement de façon sélective avec assez de détails pour permettre une maintenance efficace.  



####  Description
On a recours à cette technique lorsqu'il y a peu ou pas de documentation sur le système à maintenir ou lorsque la documentation est trop vieille ou trop peu importante pour être utile. On peut aussi l'utiliser de façon préventive, en vue d'une éventuelle maintenance, lorsque le calendrier et le budget permettent un tel recouvrement. Les composantes clés du système sont récupérées et documentées avec assez de détails pour permettre une conception et une réalisation ultérieures du changement. Il ne faut surtout pas oublier que cette technique récupère les composantes du système dans leur état actuel. Ces dernières seront modifiées dans le contexte des phases [Conception et réalisation](http://intradoc-cadrenormatif.itp.extra/DMRPFr/Html/Fr_P_2581_99_28_PAC.html) et [Architecture](http://intradoc-cadrenormatif.itp.extra/DMRPFr/Html/Fr_P_2488_99_28_PAC.html) du processus [Maintenance du système](http://intradoc-cadrenormatif.itp.extra/DMRPFr/Html/Fr_P_182_99_PTH.html). Le recouvrement de la documentation clé du système commence par le haut avec l'architecture de base du système (composantes clés de l'architecture, principalement de la vue de l'utilisateur), ensuite va de bas en haut (recouvrement des modèles de niveau réalisateur touchés par le changement) et enfin s'arrête au milieu (recouvrement des modèles de haut niveau du système touchés) pour connecter le haut et le bas (raffiner l'architecture de base du système). S'il y a lieu, les composantes voisines sont aussi récupérées et documentées. Les composantes voisines ne sont pas touchées directement par le changement, mais sont liées aux composantes du système qui sont récupérées. Habituellement, la demande de changement précise si les composantes voisines doivent être récupérées ou non.
####  Principes
#### Utiliser cette technique dans un contexte approprié
Étant donné que cette technique demande du temps et du travail, elle devrait être exécutée lorsque le travail de maintenance à faire est assez important et que le calendrier et le budget permettent un tel recouvrement. Cette technique est appliquée généralement dans le contexte d'améliorations fonctionnelles (mais pas limitée à ce contexte). Le besoin de récupérer la conception est généralement spécifié et évalué en même temps que l'est la demande de changement.
#### Récupérer seulement les portions touchées du système
Certaines parties de la documentation du système ne seront peut-être jamais récupérées, probablement parce qu'elles sont stables, ne se décomposent jamais, sont faciles à comprendre ou encore sont bien comprises par tout le monde.
####  Composition
  * [P-REC.1 - Décrire le cadre d'architecture du système](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_907_99_72_TAC.html)
  * [P-REC.2 - Recouvrement des composantes de niveau réalisateur](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_908_99_72_TAC.html)
  * [P-REC.3 - Recouvrement des composantes utilisateurs](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_909_99_72_TAC.html)

 |  
| --- |
