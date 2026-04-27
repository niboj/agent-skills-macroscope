# Référence du livrable P-OO DM Modélisation de l'architecture et de la conception de niveau réalisateur

## Source analysée

- Fichier source : `../../../macroscope/livrables/3324adfab2b3.md`
- Méthode source : Macroscope
- Extraction du titre : lien inverse par URL

## Synthèse du livrable

Les techniques P-OO-DM Modélisation de l'architecture et de la conception de niveau réalisateur visent à traduire les unités de tâche et les modèles utilisateur de classe en modèles de classe réalisateur, modèles de l'information persistante, spécifications de classe réalisateur, et modèles d'interaction. Les quatre techniques suivantes fonctionnent de concert pour optimiser ce travail. * P-OO-DA Modélisation de l'architecture de niveau réalisateur - Cette technique est réservée à la conception d'architecture de sous-systèmes réalisateur. Elle regroupe les composants logiciels et les classes réalisateur qui leur sont associés en sous-systèmes réalisateur modulaires. Elle établit l'architecture par couches (divisions horizontales) et sections (divisions verticales). Les couches horizontales isolent l'information de présentation, de dialogue, du noyau et de stockage. De leur côté, les sections verticales isolent l'infrastructure technologique, le logiciel de base et le logiciel spécifique de l'application. Il en résulte une plus grande facilité de maintenance, une meilleure portabilité et une rentabilité accrue. * P-OO-DO Modélisation des objets de niveau réalisateur - Cette technique traduit les modèles de classe utilisateur en modèles de classe réalisateur. Elle affecte les opérations aux classes appropriées. * P-OO-DI Modélisation des interactions de niveau réalisateur - Cette technique permet de définir la dynamique et la séquence des opérations. Elle sert à élaborer les modèles d'interaction pour les opérations clés et leur séquencement. * P-OO-DH Harmonisation des modèles de niveau réalisateur - Cette technique assure la cohérence entre l'architecture de sous-systèmes réalisateur, les modèles d'interaction, les modèles de classe réalisateur et les modèles de l'information persistante, ainsi que la conformité des opérations aux «design patterns» et autres normes réalisateur. Elle permet de réduire la redondance, de maximiser la réutilisation et d'optimiser la répartition des responsabilités entre les classes réalisateur. Les modèles de classe réalisateur et les modèles d'interaction constituent le point de départ des activités de codage. La figure qui suit présente la technique comme étant une boîte noire, avec ses intrants et ses extrants. Vue d'ensemble des techniques de modélisation d'analyse réalisateur

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

- * Assurer la conformité des modèles de classe réalisateur, des modèles de l'information persistante, des modèles d'interaction et de l'architecture de sous-systèmes réalisateur aux «design patterns» et aux normes réalisateur.
- * Regrouper les composants logiciels et les classes réalisateur qui leur sont associées en sous-systèmes réalisateur afin de faciliter l'analyse, la conception et la réalisation du système d'information.
- * Assurer la cohérence entre l'architecture de sous-systèmes, les modèles de classe réalisateur, les modèles de l'information persistante, et les modèles d'interaction de sorte que la réalisation des composants logiciels puisse reposer sur une base stable.
- Les quatre techniques suivantes fonctionnent de concert pour optimiser ce travail.
- * P-OO-DA Modélisation de l'architecture de niveau réalisateur - Cette technique est réservée à la conception d'architecture de sous-systèmes réalisateur.
- Elle regroupe les composants logiciels et les classes réalisateur qui leur sont associés en sous-systèmes réalisateur modulaires.
- * P-OO-DH Harmonisation des modèles de niveau réalisateur - Cette technique assure la cohérence entre l'architecture de sous-systèmes réalisateur, les modèles d'interaction, les modèles de classe réalisateur et les modèles de l'information persistante, ainsi q
- Perspective statique de l'architecture et de la conception réalisateur Ces techniques fonctionnent en simultanéité pour traduire les besoins utilisateur en modèles réalisateur.
- La technique P-OO-DA Modélisation de l'architecture de niveau réalisateur, sert à définir l'architecture réalisateur en identifiant les sous-systèmes réalisateur.
- Elle découpe le système en sous-systèmes d'après les normes relatives à une architecture en couches et les critères de partition des sous-systèmes réalisateur.
- Elle décrit en détail les spécifications de chacun des sous-systèmes réalisateur identifiés dans l'architecture de sous-systèmes réalisateur, détermine les liens de dépendance entre les sous-systèmes et définit l'interface requise.
- La technique P-OO-DI Modélisation des interactions de niveau réalisateur, permet d'établir les spécifications de séquencement réalisateur à partir des spécifications détaillées d'une unité de tâche et de ses étapes de tâche, ou des spécifications détaillées d'

## Tableaux, modèles ou diagrammes recommandés

- * Identifier les unités de tâche clés afin d'élaborer les modèles d'interaction pour ces tâches.
- * Traduire les modèles de classe utilisateur en modèles de classe réalisateur.
- * Terminer les modèles de classe réalisateur et les modèles de l'information persistante, ainsi que les spécifications de classe réalisateur, en vue de l'étape de codage.
- * Assurer la conformité des modèles de classe réalisateur, des modèles de l'information persistante, des modèles d'interaction et de l'architecture de sous-systèmes réalisateur aux «design patterns» et aux normes réalisateur.
- * Assurer la cohérence entre l'architecture de sous-systèmes, les modèles de classe réalisateur, les modèles de l'information persistante, et les modèles d'interaction de sorte que la réalisation des composants logiciels puisse reposer sur une base stable.
- Les techniques P-OO-DM Modélisation de l'architecture et de la conception de niveau réalisateur visent à traduire les unités de tâche et les modèles utilisateur de classe en modèles de classe réalisateur, modèles de l'information persistante, spécifications de
- * P-OO-DO Modélisation des objets de niveau réalisateur - Cette technique traduit les modèles de classe utilisateur en modèles de classe réalisateur.
- Elle sert à élaborer les modèles d'interaction pour les opérations clés et leur séquencement.
- * P-OO-DH Harmonisation des modèles de niveau réalisateur - Cette technique assure la cohérence entre l'architecture de sous-systèmes réalisateur, les modèles d'interaction, les modèles de classe réalisateur et les modèles de l'information persistante, ainsi q
- Les modèles de classe réalisateur et les modèles d'interaction constituent le point de départ des activités de codage.
- * P-OO-DH Harmonisation des modèles de niveau réalisateur.
- Le diagramme qui suit présente une vue statique des quatre techniques P-OO-DM Modélisation de l'architecture et de la conception de niveau réalisateur, et leur position par rapport aux techniques P-OO-UA Modélisation d'analyse utilisateur détaillée.

## Livrables et références liés

- P-OO-DM Modélisation de l'architecture et de la conception de niveau réalisateur
- P-OO-DA Modélisation de l'architecture de niveau réalisateur
- P-OO-DO Modélisation des objets de niveau réalisateur
- P-OO-DI Modélisation des interactions de niveau réalisateur
- P-OO-DH Harmonisation des modèles de niveau réalisateur
- P-OO-UA Modélisation d'analyse utilisateur détaillée
- P-OO-CM Gestion de la complexité
- P-OO-UO Analyse d'objet détaillée
- P-OO-OC Classification et catégorisation des objets
- P-OO-UC Analyse détaillée de cas d'utilisation
- P-OO-UH Harmonisation détaillée des modèles de niveau utilisateur
- P-UID Conception de l'interface utilisateur
- P-OO-DA - Modélisation de l'architecture de niveau réalisateur
- P-OO-DO - Modélisation des objets de niveau réalisateur
- P-OO-DI - Modélisation des interactions de niveau réalisateur
- P-OO-DH - Harmonisation des modèles de niveau réalisateur

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase C - Architecture des données (Data Architecture).
- Livrable TOGAF cible : Document de définition d’architecture (Architecture Definition Document).
- Domaine d’architecture principal : architecture des données.
- Artefacts associés : Entité de données, Modèle conceptuel de données, Matrice données-fonctions.

## Règles particulières de rédaction

- Présenter P-OO DM Modélisation de l'architecture et de la conception de niveau réalisateur comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
- Ne jamais faire primer Macroscope sur TOGAF.
- Documenter les hypothèses et les points à confirmer lorsque la source utilisateur est incomplète.
- Relier les éléments du livrable aux exigences, décisions, vues, composants et risques pertinents.
- Utiliser le terme conseiller en architecture pour désigner la contribution d’architecture.

## Exemples utiles ou indications extraites

- Aucune information explicite extraite du fichier source.

## Points de vigilance

- Vérifier que le livrable répond au besoin utilisateur plutôt qu’à une reproduction mécanique du gabarit.
- Éviter les doublons avec les autres livrables Macroscope liés.
- Ne pas transformer une annexe détaillée en décision d’architecture principale.
- Signaler les sections non applicables au lieu de les remplir artificiellement.
- Conserver la traçabilité entre sources, exigences, décisions et artefacts TOGAF.

## Extraits de contexte Macroscope

### Description

Les techniques P-OO-DM Modélisation de l'architecture et de la conception de niveau réalisateur visent à traduire les unités de tâche et les modèles utilisateur de classe en modèles de classe réalisateur, modèles de l'information persistante, spécifications de classe réalisateur, et modèles d'interaction. Les quatre techniques suivantes fonctionnent de concert pour optimiser ce travail. * P-OO-DA Modélisation de l'architecture de niveau réalisateur - Cette technique est réservée à la conception d'architecture de sous-systèmes réalisateur. Elle regroupe les composants logiciels et les classes réalisateur qui leur sont associés en sous-systèmes réalisateur modulaires. Elle établit l'architecture par couches (divisions horizontales) et sections (divisions verticales). Les couches horizontales isolent l'information de présentation, de dialogue, du noyau et de stockage. De leur côté, les sections verticales isolent l'infrastructure technologique, le logiciel de base et le logiciel spécifique de l'application. Il en résulte une plus grande facilité de maintenance, une meilleure portabilité et une rentabilité accrue. * P-OO-DO Modélisation des objets de niveau réalisateur - Cette technique traduit les modèles de classe utilisateur en modèles de classe réalisateur. Elle affecte les opérations aux classes appropriées. * P-OO-DI Modélisation des interactions de niveau réalisateur - Cette technique permet de définir la dynamique et la séquence des opérations. Elle sert à élaborer les modèles d'interaction pour les opérations clés et leur séquencement. * P-OO-DH Harmonisation des modèles de niveau réalisateur - Cette technique assure la cohérence entre l'architecture de sous-systèmes réalisateur, les modèles d'interaction, les modèles de classe réalisateur et les modèles de l'information persistante, ainsi que la conformité des opérations aux «design patterns» et autres normes réalisateur. Elle permet de réduire la redondance, de maximiser la réutilisation et d'optimiser la répartition des responsabilités entre les classes réalisateur. Les modèles de classe réalisateur et les modèles d'interaction constituent le point de départ des activités de codage. La figure qui suit présente la technique comme étant une boîte noire, avec ses intrants et ses extrants. Vue d'ensemble des techniques de modélisation d'analyse réalisateur

### Intrants

Non disponible.

### Extrants

Non disponible.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

Non disponible.
