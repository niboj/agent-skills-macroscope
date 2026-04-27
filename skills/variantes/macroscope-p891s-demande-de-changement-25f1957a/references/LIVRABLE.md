# Référence du livrable P891S Demande de changement

## Source analysée

- Fichier source : `../../../macroscope/livrables/25f1957a85b8.md`
- Méthode source : Macroscope
- Extraction du titre : premier lien codé du fichier

## Synthèse du livrable

L'conseiller en architecture de système, aidé du pilote, définit la ou les approches à utiliser pour la conception et la réalisation du changement, par exemple, l'approche par incréments, par sous-livraisons ou de prototypage évolutif et incrémentielle. Si l'importance du changement le justifie, les critères de répartition sont établis pour identifier les groupes d'intégration;) qui seront conçus, réalisés, assemblés et testés ensemble. Le responsable des essais identifie les groupes d'essai;) nécessaires à une bonne tenue des essais du changement. Dans un contexte de maintenance, on détermine les groupes d'essai en suivant la procédure suivante : 1. Dans le cas d'un changement fonctionnel, déterminer les exigences pour les essais et la séquence d'essai destinée à vérifier les composantes perceptibles par l'utilisateur (les unités de tâche, les chaînes de production, les processus de travail, les chaînes de soutien), nouvelles ou modifiées. Dans le cas d'un changement technique, les exigences pour les essais et la séquence d'essai sont déterminées d'après les composantes (nouvelles ou modifiées) de la technologie niveau réalisateur. 2. D'après les exigences pour les essais et la séquence d'essai déterminées à l'étape précédente, vérifier si on ne peut pas utiliser des groupes d'essai existants. Au besoin, ajuster les groupes d'essai existants qui sont convenables. Au besoin, créer de nouveaux groupes d'essai et les ajouter dans la liste des groupes d'essai de maintenance existants afin de les rendre permanents. 3. Identifier les groupes d'essai de non régression qui vont s'assurer que les parties non modifiées du système ou l'environnement technique ne sont pas touchées par le changement. Ajuster les groupes convenables d'essai de non régression au besoin. Au besoin, créer des groupes d'essai de non régression et les ajouter à la liste comprenant les groupes d'essais de maintenance existants afin de le rendre permanents. Note : Les essais d'acceptation seront préparés plus tard dans le processus, dans l'activité MNT.2.2 Préparer les essais d'acceptation. Le responsable des essais détermine alors l'environnement (incluant les outils et les mécanismes d'essai) nécessaire aux essais du changement et aux ajustements apportés à l'environnement actuel, au besoin. Il est à noter qu'il peut y avoir un environnement dédié aux essais unitaires et un autre aux essais d'intégration. On ajuste l'environnement d'essai d'intégration afin qu'il tienne compte des exigences des groupes d'essai d'intégration, des essais de non-régression et de la technologie niveau réalisateur. L'infrastructure de soutien aux essais est décrite, couvrant entre autres les bases de données d'essai, les procédures de régénération d'essai et les processus de chargement et de déchargement des bases de données d'essai. Si le système est réparti sur plusieurs sites, alors il est possible que des environnements distincts soient nécessaires pour la tenue des essais.

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

- * Déterminer la stratégie de réalisation et d'essai afin d'effectuer le changement de manière ordonnée.
- #### Modèle du processus
- **Architectures utilisateur et réalisateur ajustées** (voir le groupe de livrables Architecture du système) **Environnements d'essai de maintenance et groupes d'essai existants** P891S Demande de changement
- #### Description du processus
- L'conseiller en architecture de système, aidé du pilote, définit la ou les approches à utiliser pour la conception et la réalisation du changement, par exemple, l'approche par incréments, par sous-livraisons ou de prototypage évolutif et incrémentielle.
- Dans le cas d'un changement fonctionnel, déterminer les exigences pour les essais et la séquence d'essai destinée à vérifier les composantes perceptibles par l'utilisateur (les unités de tâche, les chaînes de production, les processus de travail, les chaînes d
- Dans le cas d'un changement technique, les exigences pour les essais et la séquence d'essai sont déterminées d'après les composantes (nouvelles ou modifiées) de la technologie niveau réalisateur.
- D'après les exigences pour les essais et la séquence d'essai déterminées à l'étape précédente, vérifier si on ne peut pas utiliser des groupes d'essai existants.
- Identifier les groupes d'essai de non régression qui vont s'assurer que les parties non modifiées du système ou l'environnement technique ne sont pas touchées par le changement.
- Note : Les essais d'acceptation seront préparés plus tard dans le processus, dans l'activité MNT.2.2 Préparer les essais d'acceptation.
- On ajuste l'environnement d'essai d'intégration afin qu'il tienne compte des exigences des groupes d'essai d'intégration, des essais de non-régression et de la technologie niveau réalisateur.
- L'infrastructure de soutien aux essais est décrite, couvrant entre autres les bases de données d'essai, les procédures de régénération d'essai et les processus de chargement et de déchargement des bases de données d'essai.

## Tableaux, modèles ou diagrammes recommandés

- #### Modèle du processus

## Livrables et références liés

- P891S Demande de changement
- P405S - Stratégie de réalisation et d'essai
- P410S - Groupes d'essai
- P740S - Environnement d'essai
- P891S - Demande de changement
- P901S - Registre des demandes de changement

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase A - Vision d’architecture (Architecture Vision).
- Livrable TOGAF cible : Plan de validation et critères d’acceptation.
- Domaine d’architecture principal : essais.
- Artefacts associés : Critères d’acceptation, Cas de test, Registre des anomalies, Demande de travail d’architecture (Request for Architecture Work).

## Règles particulières de rédaction

- Présenter P891S Demande de changement comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
- Ne jamais faire primer Macroscope sur TOGAF.
- Documenter les hypothèses et les points à confirmer lorsque la source utilisateur est incomplète.
- Relier les éléments du livrable aux exigences, décisions, vues, composants et risques pertinents.
- Utiliser le terme conseiller en architecture pour désigner la contribution d’architecture.

## Exemples utiles ou indications extraites

- L'conseiller en architecture de système, aidé du pilote, définit la ou les approches à utiliser pour la conception et la réalisation du changement, par exemple, l'approche par incréments, par sous-livraisons ou de prototypage évolutif et incrémentielle.
- D'après les exigences pour les essais et la séquence d'essai déterminées à l'étape précédente, vérifier si on ne peut pas utiliser des groupes d'essai existants.

## Points de vigilance

- Vérifier que le livrable répond au besoin utilisateur plutôt qu’à une reproduction mécanique du gabarit.
- Éviter les doublons avec les autres livrables Macroscope liés.
- Ne pas transformer une annexe détaillée en décision d’architecture principale.
- Signaler les sections non applicables au lieu de les remplir artificiellement.
- Conserver la traçabilité entre sources, exigences, décisions et artefacts TOGAF.

## Extraits de contexte Macroscope

### Description

L'conseiller en architecture de système, aidé du pilote, définit la ou les approches à utiliser pour la conception et la réalisation du changement, par exemple, l'approche par incréments, par sous-livraisons ou de prototypage évolutif et incrémentielle. Si l'importance du changement le justifie, les critères de répartition sont établis pour identifier les groupes d'intégration;) qui seront conçus, réalisés, assemblés et testés ensemble. Le responsable des essais identifie les groupes d'essai;) nécessaires à une bonne tenue des essais du changement. Dans un contexte de maintenance, on détermine les groupes d'essai en suivant la procédure suivante : 1. Dans le cas d'un changement fonctionnel, déterminer les exigences pour les essais et la séquence d'essai destinée à vérifier les composantes perceptibles par l'utilisateur (les unités de tâche, les chaînes de production, les processus de travail, les chaînes de soutien), nouvelles ou modifiées. Dans le cas d'un changement technique, les exigences pour les essais et la séquence d'essai sont déterminées d'après les composantes (nouvelles ou modifiées) de la technologie niveau réalisateur. 2. D'après les exigences pour les essais et la séquence d'essai déterminées à l'étape précédente, vérifier si on ne peut pas utiliser des groupes d'essai existants. Au besoin, ajuster les groupes d'essai existants qui sont convenables. Au besoin, créer de nouveaux groupes d'essai et les ajouter dans la liste des groupes d'essai de maintenance existants afin de les rendre permanents. 3. Identifier les groupes d'essai de non régression qui vont s'assurer que les parties non modifiées du système ou l'environnement technique ne sont pas touchées par le changement. Ajuster les groupes convenables d'essai de non régression au besoin. Au besoin, créer des groupes d'essai de non régression et les ajouter à la liste comprenant les groupes d'essais de maintenance existants afin de le rendre permanents. Note : Les essais d'acceptation seront préparés plus tard dans le processus, dans l'activité MNT.2.2 Préparer les essais d'acceptation. Le responsable des essais détermine alors l'environnement (incluant les outils et les mécanismes d'essai) nécessaire aux essais du changement et aux ajustements apportés à l'environnement actuel, au besoin. Il est à noter qu'il peut y avoir un environnement dédié aux essais unitaires et un autre aux essais d'intégration. On ajuste l'environnement d'essai d'intégration afin qu'il tienne compte des exigences des groupes d'essai d'intégration, des essais de non-régression et de la technologie niveau réalisateur. L'infrastructure de soutien aux essais est décrite, couvrant entre autres les bases de données d'essai, les procédures de régénération d'essai et les processus de chargement et de déchargement des bases de données d'essai. Si le système est réparti sur plusieurs sites, alors il est possible que des environnements distincts soient nécessaires pour la tenue des essais.

### Intrants

**Architectures utilisateur et réalisateur ajustées** (voir le groupe de livrables Architecture du système) **Environnements d'essai de maintenance et groupes d'essai existants** P891S Demande de changement

### Extrants

Non disponible.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

* Pilote: Contribue * Conseiller en architecture de système: Produit * Responsable des essais: Produit
