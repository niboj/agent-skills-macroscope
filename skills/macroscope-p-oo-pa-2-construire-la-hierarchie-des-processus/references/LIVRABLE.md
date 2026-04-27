# Référence du livrable P-OO PA.2 Construire la hiérarchie des processus

## Source analysée

- Fichier source : `../../../macroscope/livrables/71d041d23481.md`
- Méthode source : Macroscope
- Extraction du titre : lien inverse par URL

## Synthèse du livrable

Une combinaison d'analyse de haut en bas et de bas en haut est utilisée pour transformer la liste de processus identifiés à l'activité précédente en une hiérarchie complète. Des critères sont suggérés pour la décomposition des processus de système et de travail. Ils reposent sur la découverte des principaux événements survenant dans un processus et des transitions clés dans les classes concernées. Les principaux événements résultent d'un transfert de responsabilité, d'autorité, de compétence ou d'emplacement, d'un délai ou d'autres types de discontinuité. La décomposition est poursuivie jusqu'à ce que l'on atteigne la granularité d'unités de tâche. Inversement, et en parallèle, les processus de niveau unités de tâche sont positionnés dans des processus de travail et les processus de travail positionnés dans les processus de système. La hiérarchie des processus est construite de manière itérative. Structuration des processus Au cours de cette activité, deux aspects complémentaires sont pris en considération : * l'aspect dynamique est rendu concret par les événements correspondant aux discontinuités (rupture de raison d'être, de temps ou de responsabilité); * l'aspect structural est rendu concret en déterminant le niveau d'un processus, les sous-processus qui le composent et les processus de plus haut niveau auxquels il contribue. L'information recueillie à l'aide de cette technique peut entraîner la révision de la définition de la portée. Il est à prévoir que l'alignement processus-facettes effectué par la technique de gestion de la complexité aura un impact sur la hiérarchie des processus.

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

- Une combinaison d'analyse de haut en bas et de bas en haut est utilisée pour transformer la liste de processus identifiés à l'activité précédente en une hiérarchie complète.
- Des critères sont suggérés pour la décomposition des processus de système et de travail.
- Ils reposent sur la découverte des principaux événements survenant dans un processus et des transitions clés dans les classes concernées.
- Inversement, et en parallèle, les processus de niveau unités de tâche sont positionnés dans des processus de travail et les processus de travail positionnés dans les processus de système.
- La hiérarchie des processus est construite de manière itérative.
- Structuration des processus Au cours de cette activité, deux aspects complémentaires sont pris en considération :
- * l'aspect structural est rendu concret en déterminant le niveau d'un processus, les sous-processus qui le composent et les processus de plus haut niveau auxquels il contribue.
- Il est à prévoir que l'alignement processus-facettes effectué par la technique de gestion de la complexité aura un impact sur la hiérarchie des processus.
- * Voir aussi l'activité de technique P-OO-CM.1 Définir les fonctions et les sous-systèmes d'information
- * L'activité de technique P-UIAP.2 Analyse des circonstances d'utilisation du système actuel et du système cible fournit les circonstances d'utilisation qui sont considérées dans le découpage des processus en unités de tâche.
- * Modèle dynamique de processus (Macroscope), ou
- #### P201S - Processus du système

## Tableaux, modèles ou diagrammes recommandés

- #### Notations
- * Modèle dynamique de processus (Macroscope), ou
- * Diagramme d'activité.

## Livrables et références liés

- P-OO-OC.2 Identifier et catégoriser les classes et les associations
- P-OO-CM.1 Définir les fonctions et les sous-systèmes d'information
- P201S - Processus du système
- P201O - Dynamique du système d'information
- P251S - Processus de travail
- P251U - Processus de travail utilisateur

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase A - Vision d’architecture (Architecture Vision).
- Livrable TOGAF cible : Document de définition d’architecture (Architecture Definition Document).
- Domaine d’architecture principal : architecture métier.
- Artefacts associés : Service d’affaires (Business Service), Processus métier, Acteur ou rôle métier, Demande de travail d’architecture (Request for Architecture Work).

## Règles particulières de rédaction

- Présenter P-OO PA.2 Construire la hiérarchie des processus comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
- Ne jamais faire primer Macroscope sur TOGAF.
- Documenter les hypothèses et les points à confirmer lorsque la source utilisateur est incomplète.
- Relier les éléments du livrable aux exigences, décisions, vues, composants et risques pertinents.
- Utiliser le terme conseiller en architecture pour désigner la contribution d’architecture.

## Exemples utiles ou indications extraites

- Les livrables suivants peuvent être utilisés pour documenter les résultats de cette activité de technique.

## Points de vigilance

- Vérifier que le livrable répond au besoin utilisateur plutôt qu’à une reproduction mécanique du gabarit.
- Éviter les doublons avec les autres livrables Macroscope liés.
- Ne pas transformer une annexe détaillée en décision d’architecture principale.
- Signaler les sections non applicables au lieu de les remplir artificiellement.
- Conserver la traçabilité entre sources, exigences, décisions et artefacts TOGAF.

## Extraits de contexte Macroscope

### Description

Une combinaison d'analyse de haut en bas et de bas en haut est utilisée pour transformer la liste de processus identifiés à l'activité précédente en une hiérarchie complète. Des critères sont suggérés pour la décomposition des processus de système et de travail. Ils reposent sur la découverte des principaux événements survenant dans un processus et des transitions clés dans les classes concernées. Les principaux événements résultent d'un transfert de responsabilité, d'autorité, de compétence ou d'emplacement, d'un délai ou d'autres types de discontinuité. La décomposition est poursuivie jusqu'à ce que l'on atteigne la granularité d'unités de tâche. Inversement, et en parallèle, les processus de niveau unités de tâche sont positionnés dans des processus de travail et les processus de travail positionnés dans les processus de système. La hiérarchie des processus est construite de manière itérative. Structuration des processus Au cours de cette activité, deux aspects complémentaires sont pris en considération : * l'aspect dynamique est rendu concret par les événements correspondant aux discontinuités (rupture de raison d'être, de temps ou de responsabilité); * l'aspect structural est rendu concret en déterminant le niveau d'un processus, les sous-processus qui le composent et les processus de plus haut niveau auxquels il contribue. L'information recueillie à l'aide de cette technique peut entraîner la révision de la définition de la portée. Il est à prévoir que l'alignement processus-facettes effectué par la technique de gestion de la complexité aura un impact sur la hiérarchie des processus.

### Intrants

Non disponible.

### Extrants

Les livrables suivants peuvent être utilisés pour documenter les résultats de cette activité de technique. Les sections des livrables qui sont applicables sont montrées sous chaque livrable. Les livrables détaillés qui peuvent être utilisés au lieu des livrables succincts, ou en complément à ceux-ci, sont listés directement sous les livrables succincts concernés.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

Non disponible.
