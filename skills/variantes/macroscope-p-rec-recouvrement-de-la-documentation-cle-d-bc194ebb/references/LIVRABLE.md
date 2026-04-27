# Référence du livrable P-REC Recouvrement de la documentation clé de système

## Source analysée

- Fichier source : `../../../macroscope/livrables/bc194ebbe5cd.md`
- Méthode source : Macroscope
- Extraction du titre : lien inverse par URL

## Synthèse du livrable

On a recours à cette technique lorsqu'il y a peu ou pas de documentation sur le système à maintenir ou lorsque la documentation est trop vieille ou trop peu importante pour être utile. On peut aussi l'utiliser de façon préventive, en vue d'une éventuelle maintenance, lorsque le calendrier et le budget permettent un tel recouvrement. Les composantes clés du système sont récupérées et documentées avec assez de détails pour permettre une conception et une réalisation ultérieures du changement. Il ne faut surtout pas oublier que cette technique récupère les composantes du système dans leur état actuel. Ces dernières seront modifiées dans le contexte des phases Conception et réalisation et Architecture du processus Maintenance du système. Le recouvrement de la documentation clé du système commence par le haut avec l'architecture de base du système (composantes clés de l'architecture, principalement de la vue de l'utilisateur), ensuite va de bas en haut (recouvrement des modèles de niveau réalisateur touchés par le changement) et enfin s'arrête au milieu (recouvrement des modèles de haut niveau du système touchés) pour connecter le haut et le bas (raffiner l'architecture de base du système). S'il y a lieu, les composantes voisines sont aussi récupérées et documentées. Les composantes voisines ne sont pas touchées directement par le changement, mais sont liées aux composantes du système qui sont récupérées. Habituellement, la demande de changement précise si les composantes voisines doivent être récupérées ou non.

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

- * Récupérer la documentation du système touché par le changement de façon sélective avec assez de détails pour permettre une maintenance efficace.
- On a recours à cette technique lorsqu'il y a peu ou pas de documentation sur le système à maintenir ou lorsque la documentation est trop vieille ou trop peu importante pour être utile.
- Les composantes clés du système sont récupérées et documentées avec assez de détails pour permettre une conception et une réalisation ultérieures du changement.
- Il ne faut surtout pas oublier que cette technique récupère les composantes du système dans leur état actuel.
- Ces dernières seront modifiées dans le contexte des phases Conception et réalisation et Architecture du processus Maintenance du système.
- Le recouvrement de la documentation clé du système commence par le haut avec l'architecture de base du système (composantes clés de l'architecture, principalement de la vue de l'utilisateur), ensuite va de bas en haut (recouvrement des modèles de niveau réalis
- S'il y a lieu, les composantes voisines sont aussi récupérées et documentées.
- Les composantes voisines ne sont pas touchées directement par le changement, mais sont liées aux composantes du système qui sont récupérées.
- Habituellement, la demande de changement précise si les composantes voisines doivent être récupérées ou non.
- Cette technique est appliquée généralement dans le contexte d'améliorations fonctionnelles (mais pas limitée à ce contexte).
- #### Récupérer seulement les portions touchées du système
- Certaines parties de la documentation du système ne seront peut-être jamais récupérées, probablement parce qu'elles sont stables, ne se décomposent jamais, sont faciles à comprendre ou encore sont bien comprises par tout le monde.

## Tableaux, modèles ou diagrammes recommandés

- Le recouvrement de la documentation clé du système commence par le haut avec l'architecture de base du système (composantes clés de l'architecture, principalement de la vue de l'utilisateur), ensuite va de bas en haut (recouvrement des modèles de niveau réalis

## Livrables et références liés

- P-REC.1 - Décrire le cadre d'architecture du système
- P-REC.2 - Recouvrement des composantes de niveau réalisateur
- P-REC.3 - Recouvrement des composantes utilisateurs

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase G - Gouvernance de mise en œuvre (Implementation Governance).
- Livrable TOGAF cible : Annexe de conception détaillée référencée par l’architecture.
- Domaine d’architecture principal : conception détaillée.
- Artefacts associés : Bloc constitutif de solution (Solution Building Block), Spécification détaillée, Décision de conception.

## Règles particulières de rédaction

- Présenter P-REC Recouvrement de la documentation clé de système comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
- Ne jamais faire primer Macroscope sur TOGAF.
- Documenter les hypothèses et les points à confirmer lorsque la source utilisateur est incomplète.
- Relier les éléments du livrable aux exigences, décisions, vues, composants et risques pertinents.
- Utiliser le terme conseiller en architecture pour désigner la contribution d’architecture.

## Exemples utiles ou indications extraites

- On peut aussi l'utiliser de façon préventive, en vue d'une éventuelle maintenance, lorsque le calendrier et le budget permettent un tel recouvrement.
- #### Utiliser cette technique dans un contexte approprié
- * P-REC.1 - Décrire le cadre d'architecture du système

## Points de vigilance

- Vérifier que le livrable répond au besoin utilisateur plutôt qu’à une reproduction mécanique du gabarit.
- Éviter les doublons avec les autres livrables Macroscope liés.
- Ne pas transformer une annexe détaillée en décision d’architecture principale.
- Signaler les sections non applicables au lieu de les remplir artificiellement.
- Conserver la traçabilité entre sources, exigences, décisions et artefacts TOGAF.

## Extraits de contexte Macroscope

### Description

On a recours à cette technique lorsqu'il y a peu ou pas de documentation sur le système à maintenir ou lorsque la documentation est trop vieille ou trop peu importante pour être utile. On peut aussi l'utiliser de façon préventive, en vue d'une éventuelle maintenance, lorsque le calendrier et le budget permettent un tel recouvrement. Les composantes clés du système sont récupérées et documentées avec assez de détails pour permettre une conception et une réalisation ultérieures du changement. Il ne faut surtout pas oublier que cette technique récupère les composantes du système dans leur état actuel. Ces dernières seront modifiées dans le contexte des phases Conception et réalisation et Architecture du processus Maintenance du système. Le recouvrement de la documentation clé du système commence par le haut avec l'architecture de base du système (composantes clés de l'architecture, principalement de la vue de l'utilisateur), ensuite va de bas en haut (recouvrement des modèles de niveau réalisateur touchés par le changement) et enfin s'arrête au milieu (recouvrement des modèles de haut niveau du système touchés) pour connecter le haut et le bas (raffiner l'architecture de base du système). S'il y a lieu, les composantes voisines sont aussi récupérées et documentées. Les composantes voisines ne sont pas touchées directement par le changement, mais sont liées aux composantes du système qui sont récupérées. Habituellement, la demande de changement précise si les composantes voisines doivent être récupérées ou non.

### Intrants

Non disponible.

### Extrants

Non disponible.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

Non disponible.
