# Référence du livrable P2867 Architecture du système

## Source analysée

- Fichier source : `../../../macroscope/livrables/162ea5d3d107.md`
- Méthode source : Macroscope
- Extraction du titre : code technique extrait de URL

## Synthèse du livrable

L'**architecture du système** regroupe les livrables qui identifient et définissent les composantes du système d'information ainsi que les relations entre ces composantes. Voir : À propos des diagrammes de groupes de livrables;) L'architecture du système d'information est définie selon les points de vue du propriétaire, de l'utilisateur et du réalisateur du système. Les descriptions détaillées des composantes faisant partie de l'architecture du système sont réservées pour les livrables de spécifications. Un système d'information englobe des ressources tant humaines que technologiques, ce qui explique l'existence des composantes utilisateur et réalisateur. L'architecture d'un système d'envergure ou complexe peut nécessiter de fragmenter le travail de conception afin d'en faciliter la gestion. Diverses catégories de composantes peuvent ainsi être confiées à plusieurs personnes : fonctions, facettes, interfaces utilisateur, etc. Chaque sujet peut être approfondi dans un livrable détaillé auquel on affectera un spécialiste des processus, des données ou des interfaces utilisateur. L'conseiller en architecture est le principal responsable de l'architecture du système. Ce rôle peut être spécialisé en conseiller en architecture de système et conseiller en architecture technique. L'conseiller en architecture de système est responsable de l'architecture dans la perspective propriétaire et utilisateur, tandis que l'conseiller en architecture technique est responsable de l'architecture dans la perspective réalisateur.

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

- L'**architecture du système** regroupe les livrables qui identifient et définissent les composantes du système d'information ainsi que les relations entre ces composantes.
- Voir : À propos des diagrammes de groupes de livrables;) L'architecture du système d'information est définie selon les points de vue du propriétaire, de l'utilisateur et du réalisateur du système.
- Les descriptions détaillées des composantes faisant partie de l'architecture du système sont réservées pour les livrables de spécifications.
- Un système d'information englobe des ressources tant humaines que technologiques, ce qui explique l'existence des composantes utilisateur et réalisateur.
- L'architecture d'un système d'envergure ou complexe peut nécessiter de fragmenter le travail de conception afin d'en faciliter la gestion.
- Diverses catégories de composantes peuvent ainsi être confiées à plusieurs personnes : fonctions, facettes, interfaces utilisateur, etc.
- Chaque sujet peut être approfondi dans un livrable détaillé auquel on affectera un spécialiste des processus, des données ou des interfaces utilisateur.
- L'conseiller en architecture est le principal responsable de l'architecture du système.
- Ce rôle peut être spécialisé en conseiller en architecture de système et conseiller en architecture technique.
- L'conseiller en architecture de système est responsable de l'architecture dans la perspective propriétaire et utilisateur, tandis que l'conseiller en architecture technique est responsable de l'architecture dans la perspective réalisateur.
- Ils sont utiles en ce qu'ils exigent seulement une fraction des coûts de mise en oeuvre du changement et parce qu'ils peuvent être utilisés pour trouver rapidement des réponses aux questions relatives aux systèmes à livrer.
- Comme il est difficile d'illustrer toutes les caractéristiques essentielles d'un système par une seule représentation simple, il est nécessaire de développer plusieurs modèles.

## Tableaux, modèles ou diagrammes recommandés

- Voir : À propos des diagrammes de groupes de livrables;) L'architecture du système d'information est définie selon les points de vue du propriétaire, de l'utilisateur et du réalisateur du système.
- #### Utilisation de modèles
- Les modèles sont une représentation simple d'une réalité complexe.
- Les modèles reflètent les caractéristiques jugées essentielles.
- Les modèles servent:
- * de base pour la validation du produit final (ce dernier étant accepté seulement s'il est conforme aux modèles).
- Comme il est difficile d'illustrer toutes les caractéristiques essentielles d'un système par une seule représentation simple, il est nécessaire de développer plusieurs modèles.
- Les modèles reflètent les points de vue du propriétaire, de l'utilisateur et du réalisateur; il existe deux catégories de modèles cohérents et interreliés:
- * des modèles **structuraux** , montrant comment, indépendamment du temps, les ressources d'un système sont organisées, structurées et découpées;
- * des modèles **dynamiques** , montrant comment, en fonction du temps, les différentes ressources d'un système interagissent ou collaborent pour produire les résultats.
- #### Hiérarchie de modèles
- La réalisation progressive de modèles est une façon d'apprivoiser la complexité.

## Livrables et références liés

- Aucune information explicite extraite du fichier source.

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase A - Vision d’architecture (Architecture Vision).
- Livrable TOGAF cible : Document de définition d’architecture (Architecture Definition Document).
- Domaine d’architecture principal : architecture métier.
- Artefacts associés : Service d’affaires (Business Service), Processus métier, Acteur ou rôle métier, Demande de travail d’architecture (Request for Architecture Work).

## Règles particulières de rédaction

- Présenter P2867 Architecture du système comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
- Ne jamais faire primer Macroscope sur TOGAF.
- Documenter les hypothèses et les points à confirmer lorsque la source utilisateur est incomplète.
- Relier les éléments du livrable aux exigences, décisions, vues, composants et risques pertinents.
- Utiliser le terme conseiller en architecture pour désigner la contribution d’architecture.

## Exemples utiles ou indications extraites

- **_ Exemple de processus _ ** Un processus se présente comme un enchaînement d'activités transformant des intrants en extrants.
- On retrouve selon ce point de vue une hiérarchie de processus formée des composantes utilisateur (par exemple, unités de tâche ou étapes de tâche) qui se décomposent en composantes réalisateur, qui elles-mêmes peuvent se décomposer en sous-composantes réalisat
- Un sous système réalisateur peut fournir des composantes des quatre couches, couvrant par exemple, la visualisation, le dépistage et le stockage d'images.

## Points de vigilance

- Vérifier que le livrable répond au besoin utilisateur plutôt qu’à une reproduction mécanique du gabarit.
- Éviter les doublons avec les autres livrables Macroscope liés.
- Ne pas transformer une annexe détaillée en décision d’architecture principale.
- Signaler les sections non applicables au lieu de les remplir artificiellement.
- Conserver la traçabilité entre sources, exigences, décisions et artefacts TOGAF.

## Extraits de contexte Macroscope

### Description

L'**architecture du système** regroupe les livrables qui identifient et définissent les composantes du système d'information ainsi que les relations entre ces composantes. Voir : À propos des diagrammes de groupes de livrables;) L'architecture du système d'information est définie selon les points de vue du propriétaire, de l'utilisateur et du réalisateur du système. Les descriptions détaillées des composantes faisant partie de l'architecture du système sont réservées pour les livrables de spécifications. Un système d'information englobe des ressources tant humaines que technologiques, ce qui explique l'existence des composantes utilisateur et réalisateur. L'architecture d'un système d'envergure ou complexe peut nécessiter de fragmenter le travail de conception afin d'en faciliter la gestion. Diverses catégories de composantes peuvent ainsi être confiées à plusieurs personnes : fonctions, facettes, interfaces utilisateur, etc. Chaque sujet peut être approfondi dans un livrable détaillé auquel on affectera un spécialiste des processus, des données ou des interfaces utilisateur. L'conseiller en architecture est le principal responsable de l'architecture du système. Ce rôle peut être spécialisé en conseiller en architecture de système et conseiller en architecture technique. L'conseiller en architecture de système est responsable de l'architecture dans la perspective propriétaire et utilisateur, tandis que l'conseiller en architecture technique est responsable de l'architecture dans la perspective réalisateur.

### Intrants

Non disponible.

### Extrants

Non disponible.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

Non disponible.
