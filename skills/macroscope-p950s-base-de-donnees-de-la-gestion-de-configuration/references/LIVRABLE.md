# Référence du livrable P950S Base de données de la gestion de configuration

## Source analysée

- Fichier source : `../../../macroscope/livrables/6e7b197cafbb.md`
- Méthode source : Macroscope
- Extraction du titre : lien inverse par URL

## Synthèse du livrable

Ce livrable présente les exigences minimales pour une base de données de la gestion de configuration (BDGC). La BDGC est un référentiel comprenant les données de configuration et l'information concernant les éléments de configuration;), ainsi que leurs relations et dépendances durant leur cycle de vie. La BDGC devrait être gérée exclusivement par la fonction de gestion de configuration;). La BDGC est au centre des activités d'exploitation informatique, et de mise en oeuvre et de maintenance, étant donné qu'elle contient, en plus des données de configuration et des éléments de configuration, de l'information utile telle que les profils d'utilisateurs, les configurations technologiques, les composantes de système et de service, les demandes de changement, les incidents, les problèmes et autres, et les relations entre toutes ces composantes. On consulte la BDGC pour, entre autres, avoir de l'information au sujet des ententes de niveau de service ou, lors des activités de soutien, pour évaluer l'impact d'un incident, ou rechercher des incidents ou problèmes connexes qui pourraient aider à le résoudre. Une organisation peut utiliser plus d'une BDGC pour la gestion de configuration. À tout le moins, la BDGC devrait contenir les informations suivantes (l'information doit être conforme au P951S Plan de gestion de configuration) : * Nom et identifiant uniques de l'élément de configuration (dans le cas d'un élément de configuration, il peut aussi y avoir les numéros de série et de modèles). * Version de l'élément de configuration. * État de l'élément de configuration (tel que «essai d'intégration» , «essai d'acceptation» , «production», «archive», etc.) et identifiant de la configuration de référence;) connexe. * Au besoin, la date planifiée (ou événement déclencheur) pour un changement d'état de l'élément de configuration (par exemple, dans le cas d'un élément de configuration que l'on prévoit mettre à jour, remplacer ou retirer). * Type de l'élément de configuration (par exemple, à un niveau plus général : matériel, logiciel, fournitures de bureau, documentation; à un niveau plus détaillé : exigences, spécifications, code, plans d'essai, matériel de formation, etc.). * Description de l'élément de configuration. * Propriétaire de l'élément de configuration (celui qui en a la responsabilité). * Emplacement de l'élément de configuration (bibliothèque ou lieu physique selon le type de l'élément). * Informations relatives à la création ou l'acquisition de l'élément de configuration, incluant son origine (développement à l'interne ou fournisseur tiers), sa date de création ou d'acquisition et, s'il y a lieu, sa date de renouvellement. * S'il y a lieu, information légale et contractuelle (ou sur la licence). * Registre de l'historique des changements apportés. * Relations parent/enfant : identifiant unique pour le parent et les enfants selon le cas. * Autres relations entre les éléments de configuration (par exemple, «est utilisé par», «est installé sur», etc.). * Relations des éléments de configuration avec les incidents, les problèmes et les demandes de changement connexes (par leur identifiant unique). * Relations entre les services et leurs éléments de configuration sous-jacents. * Enregistrement des incidents, des problèmes et des demandes de changement. La BDGC peut évidemment contenir beaucoup plus d'information, selon les besoins de l'organisation et la flexibilité des outils utilisés. Ce livrable ne propose pas de contenu détaillé étant donné que les organisations utilisent des outils différents selon leurs besoins spécifiques.

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

- * Saisir et structurer les données de configuration et l'information concernant les éléments de configuration;), y compris leurs relations et dépendances durant leur cycle de vie.
- * Permettre aux projets d'exploitation informatique, et de mise en oeuvre et de maintenance de mieux comprendre les interdépendances entre les composantes qu'ils ont à traiter.
- Ce livrable présente les exigences minimales pour une base de données de la gestion de configuration (BDGC).
- La BDGC est un référentiel comprenant les données de configuration et l'information concernant les éléments de configuration;), ainsi que leurs relations et dépendances durant leur cycle de vie.
- La BDGC devrait être gérée exclusivement par la fonction de gestion de configuration;).
- La BDGC est au centre des activités d'exploitation informatique, et de mise en oeuvre et de maintenance, étant donné qu'elle contient, en plus des données de configuration et des éléments de configuration, de l'information utile telle que les profils d'utilisa
- On consulte la BDGC pour, entre autres, avoir de l'information au sujet des ententes de niveau de service ou, lors des activités de soutien, pour évaluer l'impact d'un incident, ou rechercher des incidents ou problèmes connexes qui pourraient aider à le résoud
- * Type de l'élément de configuration (par exemple, à un niveau plus général : matériel, logiciel, fournitures de bureau, documentation; à un niveau plus détaillé : exigences, spécifications, code, plans d'essai, matériel de formation, etc.).
- * Relations entre les services et leurs éléments de configuration sous-jacents.

## Tableaux, modèles ou diagrammes recommandés

- * Nom et identifiant uniques de l'élément de configuration (dans le cas d'un élément de configuration, il peut aussi y avoir les numéros de série et de modèles).

## Livrables et références liés

- P951S Plan de gestion de configuration

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase A - Vision d’architecture (Architecture Vision).
- Livrable TOGAF cible : Plan de transition, exploitation et adoption.
- Domaine d’architecture principal : formation.
- Artefacts associés : Procédure d’exploitation, Guide utilisateur, Matériel de transfert, Demande de travail d’architecture (Request for Architecture Work).

## Règles particulières de rédaction

- Présenter P950S Base de données de la gestion de configuration comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
- Ne jamais faire primer Macroscope sur TOGAF.
- Documenter les hypothèses et les points à confirmer lorsque la source utilisateur est incomplète.
- Relier les éléments du livrable aux exigences, décisions, vues, composants et risques pertinents.
- Utiliser le terme conseiller en architecture pour désigner la contribution d’architecture.

## Exemples utiles ou indications extraites

- Une organisation peut utiliser plus d'une BDGC pour la gestion de configuration.
- * Au besoin, la date planifiée (ou événement déclencheur) pour un changement d'état de l'élément de configuration (par exemple, dans le cas d'un élément de configuration que l'on prévoit mettre à jour, remplacer ou retirer).
- * Type de l'élément de configuration (par exemple, à un niveau plus général : matériel, logiciel, fournitures de bureau, documentation; à un niveau plus détaillé : exigences, spécifications, code, plans d'essai, matériel de formation, etc.).
- * Autres relations entre les éléments de configuration (par exemple, «est utilisé par», «est installé sur», etc.).

## Points de vigilance

- Vérifier que le livrable répond au besoin utilisateur plutôt qu’à une reproduction mécanique du gabarit.
- Éviter les doublons avec les autres livrables Macroscope liés.
- Ne pas transformer une annexe détaillée en décision d’architecture principale.
- Signaler les sections non applicables au lieu de les remplir artificiellement.
- Conserver la traçabilité entre sources, exigences, décisions et artefacts TOGAF.

## Extraits de contexte Macroscope

### Description

Ce livrable présente les exigences minimales pour une base de données de la gestion de configuration (BDGC). La BDGC est un référentiel comprenant les données de configuration et l'information concernant les éléments de configuration;), ainsi que leurs relations et dépendances durant leur cycle de vie. La BDGC devrait être gérée exclusivement par la fonction de gestion de configuration;). La BDGC est au centre des activités d'exploitation informatique, et de mise en oeuvre et de maintenance, étant donné qu'elle contient, en plus des données de configuration et des éléments de configuration, de l'information utile telle que les profils d'utilisateurs, les configurations technologiques, les composantes de système et de service, les demandes de changement, les incidents, les problèmes et autres, et les relations entre toutes ces composantes. On consulte la BDGC pour, entre autres, avoir de l'information au sujet des ententes de niveau de service ou, lors des activités de soutien, pour évaluer l'impact d'un incident, ou rechercher des incidents ou problèmes connexes qui pourraient aider à le résoudre. Une organisation peut utiliser plus d'une BDGC pour la gestion de configuration. À tout le moins, la BDGC devrait contenir les informations suivantes (l'information doit être conforme au P951S Plan de gestion de configuration) : * Nom et identifiant uniques de l'élément de configuration (dans le cas d'un élément de configuration, il peut aussi y avoir les numéros de série et de modèles). * Version de l'élément de configuration. * État de l'élément de configuration (tel que «essai d'intégration» , «essai d'acceptation» , «production», «archive», etc.) et identifiant de la configuration de référence;) connexe. * Au besoin, la date planifiée (ou événement déclencheur) pour un changement d'état de l'élément de configuration (par exemple, dans le cas d'un élément de configuration que l'on prévoit mettre à jour, remplacer ou retirer). * Type de l'élément de configuration (par exemple, à un niveau plus général : matériel, logiciel, fournitures de bureau, documentation; à un niveau plus détaillé : exigences, spécifications, code, plans d'essai, matériel de formation, etc.). * Description de l'élément de configuration. * Propriétaire de l'élément de configuration (celui qui en a la responsabilité). * Emplacement de l'élément de configuration (bibliothèque ou lieu physique selon le type de l'élément). * Informations relatives à la création ou l'acquisition de l'élément de configuration, incluant son origine (développement à l'interne ou fournisseur tiers), sa date de création ou d'acquisition et, s'il y a lieu, sa date de renouvellement. * S'il y a lieu, information légale et contractuelle (ou sur la licence). * Registre de l'historique des changements apportés. * Relations parent/enfant : identifiant unique pour le parent et les enfants selon le cas. * Autres relations entre les éléments de configuration (par exemple, «est utilisé par», «est installé sur», etc.). * Relations des éléments de configuration avec les incidents, les problèmes et les demandes de changement connexes (par leur identifiant unique). * Relations entre les services et leurs éléments de configuration sous-jacents. * Enregistrement des incidents, des problèmes et des demandes de changement. La BDGC peut évidemment contenir beaucoup plus d'information, selon les besoins de l'organisation et la flexibilité des outils utilisés. Ce livrable ne propose pas de contenu détaillé étant donné que les organisations utilisent des outils différents selon leurs besoins spécifiques.

### Intrants

Non disponible.

### Extrants

Non disponible.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

Non disponible.
