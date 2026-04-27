# http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_590_60_72_TAC.html

|   
####  Description
La perspective locale d'un service illustre les collaborations de classe nécessaires pour un comportement de service donné. Ces collaborations de classes peuvent comprendre des services privés de la classe et des services d'autres classes. Les sources possibles de collaborations de classe sont décrites dans les activités suivantes de la technique [P-OO-UO Analyse d'objet détaillée](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_179_60_39_TEC.html):
  * [P-OO-UO.1 Attribuer un service à une classe utilisateur](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_587_60_72_TAC.html);
  * [P-OO-UO.2 Établir les spécifications détaillées d'un service utilisateur](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_588_60_72_TAC.html);
  * [P-OO-UO.3 Déterminer les attributs d'une classe utilisateur](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_589_60_72_TAC.html).

Cette activité de technique peut être utilisée pour décrire la perspective locale de services du noyau et de services d'interface. Toutefois, en général il n'est pas nécessaire de spécifier une perspective locale pour les services d'interface.
####  Notations
  * La perspective locale d'un service peut être illustrée à l'aide soit :
    * de [Diagramme de collaboration](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_5155_99_33_NOT.html),
    * d'objets composites UML (voir le [Diagramme d'objet](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_12712_99_60_NOT.html)).


####  Extrants
Les livrables suivants peuvent être utilisés pour documenter les résultats de cette activité de technique. Les sections des livrables qui sont applicables sont montrées sous chaque livrable. Les livrables détaillés qui peuvent être utilisés au lieu des livrables succincts, ou en complément à ceux-ci, sont listés directement sous les livrables succincts concernés.
####  [P180S - Spécifications de composante du noyau](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_2580_99_34_DEL.html)
  * 1.1.3 - Perspective locale du service


####  [P186S - Spécifications de composante réutilisable d'interface](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_2590_99_34_DEL.html)
  * 2.3 - Service d'interface utilisateur


####  [P487S - Spécifications de l'étape de tâche réutilisable](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_8496_99_34_DEL.html)
  * 1.2.2 - Service d'interface utilisateur


####  [P490S - Spécifications de l'unité de tâche](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_2655_99_34_DEL.html)
  * 4.1.2 - Service d'interface utilisateur


####  Techniques utilisées
  * [Analyse détaillée de cas d'utilisation](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_181_60_39_TEC.html)
  * [Classification et catégorisation des objets](http://intradoc-cadrenormatif.itp.extra/DMRPFr/html/Fr_P_173_60_39_TEC.html)


####  Exemples
#### Exemple de collaboration
Exemple de collaboration utilisant un diagramme de collaboration (UML). ![](http://intradoc-cadrenormatif.itp.extra/DMRPFr/Images/FP31OO-UO02.gif)Diagramme de collaboration UML Un utilisateur déclenche une recherche pour obtenir une liste de livres correspondant aux critères de recherche. La classe de la fenêtre Recherche de livre collabore avec la classe Recherche inf. sur livres pour fournir le service. Le résultat de la recherche est affiché par la classe Afficher inf. liste de livres.  |  
| --- |
