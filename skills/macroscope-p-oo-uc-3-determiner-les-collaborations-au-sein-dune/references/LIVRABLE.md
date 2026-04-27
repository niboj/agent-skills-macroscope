# Référence du livrable P-OO UC.3 Déterminer les collaborations au sein d'une unité de tâche

## Source analysée

- Fichier source : `../../../macroscope/livrables/52badcbf3945.md`
- Méthode source : Macroscope
- Extraction du titre : lien inverse par URL

## Synthèse du livrable

À partir de la liste des services utilisés dans une unité de tâche et du modèle d'objet qui montre les classes offrant ces services, cette activité de technique permet de déterminer les collaborations de classes nécessaires au support des services. La perspective locale d'une unité de tâche liste les services d'interface utilisateur et les services du noyau, et décrit les collaborations de classes. Cette activité peut aussi être exécutée chaque fois qu'une perspective locale d'une étape de tâche est nécessaire. Composantes d'une perspective locale La perspective locale d'une unité de tâche contient au moins une liste des services utilisés (et des classes qui les fournissent). La collaboration entre les classes participant à l'unité de tâche est également illustrée pour les cas non triviaux. À cette étape, les services doivent avoir été assignés aux classes utilisateur qui leur sont associées (voir la technique P-OO-UO Analyse d'objet détaillée). La perspective locale d'une unité de tâche est définie en : * énumérant les services connexes de l'unité de tâche; * résumant la façon dont les classes collaborent. Les perspectives locales d'une unité de tâche servent à : * présenter à l'utilisateur une vue des collaborations de classes nécessaires pour que la tâche puisse fournir ses services; * s'assurer que les modèles d'objet utilisateur contiennent toutes les classes requises par la tâche; * évaluer la complexité de la tâche.

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

- À partir de la liste des services utilisés dans une unité de tâche et du modèle d'objet qui montre les classes offrant ces services, cette activité de technique permet de déterminer les collaborations de classes nécessaires au support des services.
- La perspective locale d'une unité de tâche liste les services d'interface utilisateur et les services du noyau, et décrit les collaborations de classes.
- Composantes d'une perspective locale La perspective locale d'une unité de tâche contient au moins une liste des services utilisés (et des classes qui les fournissent).
- À cette étape, les services doivent avoir été assignés aux classes utilisateur qui leur sont associées (voir la technique P-OO-UO Analyse d'objet détaillée).
- * énumérant les services connexes de l'unité de tâche;
- * présenter à l'utilisateur une vue des collaborations de classes nécessaires pour que la tâche puisse fournir ses services;
- * Les services participant à une unité de tâche sont consignés sous forme de liste à la section Perspective locale de l'unité de tâche du P490S Spécifications de l'unité de tâche.
- * Les services participant à une étape de tâche sont consignés sous forme de liste dans la Perspective locale de l'étape de tâche.
- * Conception des composantes de l'interface utilisateur
- * Conception des règles de fonctionnement de l'interface utilisateur
- sur livres pour fournir le service.

## Tableaux, modèles ou diagrammes recommandés

- À partir de la liste des services utilisés dans une unité de tâche et du modèle d'objet qui montre les classes offrant ces services, cette activité de technique permet de déterminer les collaborations de classes nécessaires au support des services.
- * s'assurer que les modèles d'objet utilisateur contiennent toutes les classes requises par la tâche;
- #### Notations
- * Les collaborations de la section Perspective locale de l'unité de tâche, peuvent être illustrées à l'aide d'un Diagramme de collaboration UML ou d'un objet composite dans un Diagramme d'objet UML.
- * Les collaborations de la section Perspective locale de l'étape de tâche peuvent être illustrées à l'aide d'un Diagramme de collaboration UML ou d'un objet composite dans un Diagramme d'objet UML.
- * Harmonisation détaillée des modèles de niveau utilisateur
- Diagramme de collaboration UML Un utilisateur déclenche une recherche pour obtenir une liste de livres correspondant aux critères de recherche.

## Livrables et références liés

- P-OO-UO Analyse d'objet détaillée
- P490S Spécifications de l'unité de tâche
- P487S - Spécifications de l'étape de tâche réutilisable
- P490S - Spécifications de l'unité de tâche

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase G/H - Gouvernance de mise en œuvre et gestion du changement.
- Livrable TOGAF cible : Plan de transition, exploitation et adoption.
- Domaine d’architecture principal : utilisation.
- Artefacts associés : Procédure d’exploitation, Guide utilisateur, Matériel de transfert.

## Règles particulières de rédaction

- Présenter P-OO UC.3 Déterminer les collaborations au sein d'une unité de tâche comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
- Ne jamais faire primer Macroscope sur TOGAF.
- Documenter les hypothèses et les points à confirmer lorsque la source utilisateur est incomplète.
- Relier les éléments du livrable aux exigences, décisions, vues, composants et risques pertinents.
- Utiliser le terme conseiller en architecture pour désigner la contribution d’architecture.

## Exemples utiles ou indications extraites

- Les livrables suivants peuvent être utilisés pour documenter les résultats de cette activité de technique.
- #### Exemples

## Points de vigilance

- Vérifier que le livrable répond au besoin utilisateur plutôt qu’à une reproduction mécanique du gabarit.
- Éviter les doublons avec les autres livrables Macroscope liés.
- Ne pas transformer une annexe détaillée en décision d’architecture principale.
- Signaler les sections non applicables au lieu de les remplir artificiellement.
- Conserver la traçabilité entre sources, exigences, décisions et artefacts TOGAF.

## Extraits de contexte Macroscope

### Description

À partir de la liste des services utilisés dans une unité de tâche et du modèle d'objet qui montre les classes offrant ces services, cette activité de technique permet de déterminer les collaborations de classes nécessaires au support des services. La perspective locale d'une unité de tâche liste les services d'interface utilisateur et les services du noyau, et décrit les collaborations de classes. Cette activité peut aussi être exécutée chaque fois qu'une perspective locale d'une étape de tâche est nécessaire. Composantes d'une perspective locale La perspective locale d'une unité de tâche contient au moins une liste des services utilisés (et des classes qui les fournissent). La collaboration entre les classes participant à l'unité de tâche est également illustrée pour les cas non triviaux. À cette étape, les services doivent avoir été assignés aux classes utilisateur qui leur sont associées (voir la technique P-OO-UO Analyse d'objet détaillée). La perspective locale d'une unité de tâche est définie en : * énumérant les services connexes de l'unité de tâche; * résumant la façon dont les classes collaborent. Les perspectives locales d'une unité de tâche servent à : * présenter à l'utilisateur une vue des collaborations de classes nécessaires pour que la tâche puisse fournir ses services; * s'assurer que les modèles d'objet utilisateur contiennent toutes les classes requises par la tâche; * évaluer la complexité de la tâche.

### Intrants

Non disponible.

### Extrants

Les livrables suivants peuvent être utilisés pour documenter les résultats de cette activité de technique. Les sections des livrables qui sont applicables sont montrées sous chaque livrable. Les livrables détaillés qui peuvent être utilisés au lieu des livrables succincts, ou en complément à ceux-ci, sont listés directement sous les livrables succincts concernés.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

Non disponible.
