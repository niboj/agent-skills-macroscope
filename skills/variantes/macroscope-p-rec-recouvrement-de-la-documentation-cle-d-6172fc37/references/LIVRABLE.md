# Référence du livrable P-REC Recouvrement de la documentation clé de système

## Source analysée

- Fichier source : `../../../macroscope/livrables/6172fc375ece.md`
- Méthode source : Macroscope
- Extraction du titre : premier lien codé du fichier

## Synthèse du livrable

Le fichier source ne contient pas de synthèse explicite. Utiliser le contexte, le contenu et les liens de livrables pour cadrer la production.

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

- #### Récupérer la documentation du système au besoin
- Si la documentation du système n'existe pas ou très peu, les spécifications réalisateur et utilisateur à modifier doivent d'abord être récupérées à l'aide de la technique P-REC Recouvrement de la documentation clé de système.
- Au besoin, utiliser des prototypes pour valider les spécifications, nouvelles ou modifiées (par exemple, une nouvelle manière d'exécuter une tâche ou d'afficher l'information sur l'interface graphique utilisateur).
- Lorsqu'un prototypage évolutif est utilisé, on a moins besoin de spécifications détaillées étant donné que l'analyste-programmeur travaille directement avec les utilisateurs et l'analyste fonctionnel.
- Si le prototypage n'est pas possible, les utilisateurs valident fréquemment les spécifications de composante.
- #### Utiliser des outils de cheminement des processus
- Les outils de cheminement des processus devraient servir à corriger les processus de travail administratif automatisés.
- Lorsque l'on code et teste le changement, il faut tenir compte du fait que les caractéristiques réalisateur du système peuvent varier en raison des différences que présentent les divers sites de déploiement en matière de matériel, de systèmes d'exploitation, d
- Selon la technologie et la répartition du système, les essais peuvent devoir être répétés dans des environnements d'essai multiples ou effectués dans des environnements spécifiques.
- Il est important que les composantes sur lesquelles le reste de la livraison est basé soient stabilisées le plus rapidement possible.
- Par exemple, il faut prévoir la conception et l'assemblage des composantes techniques de base au tout début de la livraison.
- Les vérifications devraient être effectuées pour faire en sorte que les spécifications utilisateur résultantes soient appropriées (qu'elles correspondent vraiment à la solution recommandée pour le changement), conformes à l'architecture modifiée du système et

## Tableaux, modèles ou diagrammes recommandés

- Il est préférable d'utiliser les commentaires et annotations dans le code du module plutôt que dans des documents distincts, parce que toute documentation se trouvant séparée du code devient rapidement périmée.

## Livrables et références liés

- P-REC Recouvrement de la documentation clé de système
- M009S Plan détaillé
- P-JWT Technique d'ateliers conjoints de développement
- P951S Plan de gestion de configuration
- P891S Demande de changement
- P931G Entente de niveau de service
- P901S Registre des demandes de changement
- P902S Compte rendu de l'information

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase A - Vision d’architecture (Architecture Vision).
- Livrable TOGAF cible : Plan de validation et critères d’acceptation.
- Domaine d’architecture principal : essais.
- Artefacts associés : Critères d’acceptation, Cas de test, Registre des anomalies, Demande de travail d’architecture (Request for Architecture Work).

## Règles particulières de rédaction

- Présenter P-REC Recouvrement de la documentation clé de système comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
- Ne jamais faire primer Macroscope sur TOGAF.
- Documenter les hypothèses et les points à confirmer lorsque la source utilisateur est incomplète.
- Relier les éléments du livrable aux exigences, décisions, vues, composants et risques pertinents.
- Utiliser le terme conseiller en architecture pour désigner la contribution d’architecture.

## Exemples utiles ou indications extraites

- #### Utiliser des prototypes
- Au besoin, utiliser des prototypes pour valider les spécifications, nouvelles ou modifiées (par exemple, une nouvelle manière d'exécuter une tâche ou d'afficher l'information sur l'interface graphique utilisateur).
- #### Utiliser des outils de cheminement des processus
- #### Documenter les modifications apportées au code
- Si des corrections et des améliorations sont apportées au code existant, elles devraient être documentées afin d'expliquer le changement (par exemple, citer le numéro de la demande de changement).
- Il est préférable d'utiliser les commentaires et annotations dans le code du module plutôt que dans des documents distincts, parce que toute documentation se trouvant séparée du code devient rapidement périmée.
- Par exemple, il faut prévoir la conception et l'assemblage des composantes techniques de base au tout début de la livraison.
- Par exemple, les classes, nouvelles ou modifiées, leurs services, leurs attributs (valeurs allouées et règles d'intégrité) et leur niveau de sécurité devraient faire l'objet d'une vérification afin de s'assurer qu'ils soutiennent correctement les unités de tâc

## Points de vigilance

- Vérifier que le livrable répond au besoin utilisateur plutôt qu’à une reproduction mécanique du gabarit.
- Éviter les doublons avec les autres livrables Macroscope liés.
- Ne pas transformer une annexe détaillée en décision d’architecture principale.
- Signaler les sections non applicables au lieu de les remplir artificiellement.
- Conserver la traçabilité entre sources, exigences, décisions et artefacts TOGAF.

## Extraits de contexte Macroscope

### Description

Non disponible.

### Intrants

Non disponible.

### Extrants

Non disponible.

### Procédure ou indications de production

On ne devrait pas éviter les procédures générales de gestion lors d'une situation urgente. Même, dans un tel cas, un processus d'approbation minimum doit s'appliquer et le P931G Entente de niveau de service devrait identifier les autorités responsables impliquées. On devrait aussi y trouver des instructions et règles à suivre dans ce contexte particulier.

### Rôles mentionnés dans la source

Non disponible.
