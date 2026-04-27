# Référence du livrable P405S Stratégie de réalisation et d'essai

## Source analysée

- Fichier source : `../../../macroscope/livrables/9cce5ee192ae.md`
- Méthode source : Macroscope
- Extraction du titre : premier lien codé du fichier

## Synthèse du livrable

Le responsable des essais prépare les plans d'essai détaillés afin d'ordonner les activités d'essai. Les activités, les durées et les participants sont organisés d'après les interdépendances entre les groupes d'essai définis précédemment. L'analyste fonctionnel, en collaboration avec les experts du domaine et les utilisateurs du système, modifie les spécifications des composantes de niveau utilisateur existantes ou en crée de nouvelles, d'après l'architecture du système modifié. Au besoin, un ou plusieurs des ajustements suivants sont apportés aux spécifications utilisateur : * Le P490S Spécifications de l'unité de tâche et le P487S Spécifications de l'étape de tâche réutilisable : Généralement, les ajustements aux **unités de tâche** sont effectués d'après les changements apportés aux P251S Processus de travail, aux fonctions du système (P250S Structure utilisateur du système), ou aux facettes et classes d'information (P170S Structure de l'information). Il est à noter que si, on doit modifier les **interfaces utilisateur** , afin de, par exemple, respecter les nouvelles normes de présentation, ce sera représenté dans les unités de tâche (P490S Spécifications de l'unité de tâche) correspondantes. * Les modifications apportées aux unités de tâche ont un impact sur les **composantes réutilisables de l'interface utilisateur**. Si tel est le cas, un ou plusieurs P186S Spécifications de composante réutilisable d'interface peuvent devoir être mis à jour ou créés. * Si des facettes et classes d'information (P170S Structure de l'information) ont été modifiées, il est possible que leurs **services du noyau** doivent être révisés. Les services du noyau pourraient aussi devoir être ajustés afin de soutenir convenablement les unités de tâche modifiées. Dans ce cas, un ou plusieurs P180S Spécifications de composante du noyau peuvent devoir être mis à jour ou créés. * Si le changement résulte en des **traitements par lots** , nouveaux ou modifiés, le P580S Spécifications de processus automatisé doit alors évoluer. Au besoin, en se basant sur les spécifications utilisateur révisées, l'conseiller en architecture technique révise et complète l'architecture logicielle, et l'administrateur de base de données révise et complète la structure de l'information persistante. L'analyste-programmeur, en collaboration avec l'analyste fonctionnel, modifie les spécifications actuelles des composantes de réalisation ou en crée de nouvelles au besoin, d'après les modèles réalisateur ajustés, et les spécifications utilisateur nouvelles ou modifiées. Il identifie le nouveau code à écrire et le code existant à mettre à jour ou à supprimer : code fonctionnel (par exemple, créer une unité de tâche), code des bases de données ou code technique (par exemple, les composantes de l'infrastructure technologique). Ensuite, il code les composants logiciels en conséquence. Une fois la codification terminée, les composantes individuelles sont testées par l'analyste-programmeur pour faire en sorte que les spécifications utilisateur et réalisateur soient respectées. Il faut noter que, bien que l'analyste-programmeur ne doive pas codifier les composantes de réalisation sélectionnées (venant du commerce), celles-ci doivent cependant être testées comme le serait tout code maison. Si la solution recommandée le spécifie, les paramètres du système peuvent être modifiés et remplacés par de nouvelles valeurs. Dans ce cas, les essais unitaires ne sont généralement pas pertinents. Le testeur ajuste et complète les groupes d'essai d'intégration afin d'être prêt pour effectuer les essais appropriés pour le changement appliqué. Par exemple, il décide si le groupe d'essai d'intégration sera divisé tout de suite en cas d'essai ou bien en domaines d'essai pour ensuite être divisés en cas d'essai. Il ordonne les domaines d'essai, en tenant compte des dépendances ou préalables entre eux. En collaboration avec les experts du domaine et les utilisateurs, le testeur ajuste les cas d'essai de maintenance existants ou en crée de nouveaux. Selon la nature du changement, les cas d'essai sont basés sur les spécifications utilisateur, réalisateur ou sur la vue de la technologie. Le testeur détermine aussi les exigences liées aux données d'essai. Lorsque les composantes, nouvelles ou modifiées, sont prêtes, le testeur fait l'essai de chaque groupe d'intégration pour s'assurer que ce dernier fonctionne tel que prévu et qu'il n'a pas d'impact sur les parties non modifiées du système ou sur l'environnement technologique (essais de non-régression). S'il y a lieu, les essais d'intégration peuvent aussi être effectués dans le but de s'assurer une intégration appropriée des systèmes externes. Le testeur prépare un compte rendu d'essai pour chaque groupe d'essai d'intégration vérifié et consigne toute variation par rapport aux résultats attendus. Les problèmes ou anomalies identifiés ont la priorité. On identifie les problèmes qui peuvent attendre et on émet les demandes de changement appropriées. Les autres problèmes sont traités selon les priorités établies. S'il y a des changements apportés aux exigences du système et si un P900S Suivi des exigences existe pour le système, donc, une fois que les composantes touchées sont conçues, l'conseiller en architecture de système, en collaboration avec l'conseiller en architecture technique, met à jour le livrable afin de refléter la nouvelle situation. Une description de l'impact qu'ont les nouvelles exigences sur les spécifications et composantes du système est fournie. _Aller à la section_ _Lignes directrices pour changement urgent_ _pour voir comment adapter cette activité dans un contexte de changement urgent._

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

- * Concevoir et réaliser les composantes liées au changement.
- * Mettre à jour les exigences de suivi existantes du système, s'il y a lieu.
- #### Modèle du processus
- * **Architectures utilisateur et réalisateur ajustées** (voir le groupe de livrables Architecture du système)
- * **Spécifications utilisateur et réalisateur existantes** (voir le groupe de livrables Spécifications du système)
- * **Composantes réalisateur existantes** (voir le groupe de livrables Composantes du système)
- #### Description du processus
- L'analyste fonctionnel, en collaboration avec les experts du domaine et les utilisateurs du système, modifie les spécifications des composantes de niveau utilisateur existantes ou en crée de nouvelles, d'après l'architecture du système modifié.
- * Le P490S Spécifications de l'unité de tâche et le P487S Spécifications de l'étape de tâche réutilisable : Généralement, les ajustements aux **unités de tâche** sont effectués d'après les changements apportés aux P251S Processus de travail, aux fonctions du s
- Il est à noter que si, on doit modifier les **interfaces utilisateur** , afin de, par exemple, respecter les nouvelles normes de présentation, ce sera représenté dans les unités de tâche (P490S Spécifications de l'unité de tâche) correspondantes.
- * Les modifications apportées aux unités de tâche ont un impact sur les **composantes réutilisables de l'interface utilisateur**.
- Si tel est le cas, un ou plusieurs P186S Spécifications de composante réutilisable d'interface peuvent devoir être mis à jour ou créés.

## Tableaux, modèles ou diagrammes recommandés

- #### Modèle du processus
- L'analyste-programmeur, en collaboration avec l'analyste fonctionnel, modifie les spécifications actuelles des composantes de réalisation ou en crée de nouvelles au besoin, d'après les modèles réalisateur ajustés, et les spécifications utilisateur nouvelles ou

## Livrables et références liés

- P405S - Stratégie de réalisation et d'essai
- P410S - Groupes d'essai
- P740S - Environnement d'essai
- P891S - Demande de changement
- P490S Spécifications de l'unité de tâche
- P487S Spécifications de l'étape de tâche réutilisable
- P251S Processus de travail
- P250S Structure utilisateur du système
- P170S Structure de l'information
- P186S Spécifications de composante réutilisable d'interface
- P180S Spécifications de composante du noyau
- P580S Spécifications de processus automatisé
- P900S Suivi des exigences
- P180S - Spécifications de composante du noyau
- P186S - Spécifications de composante réutilisable d'interface
- P219S - Architecture logicielle
- P415S - Plan d'essai
- P487S - Spécifications de l'étape de tâche réutilisable
- P490S - Spécifications de l'unité de tâche
- P510S - Structure de l'information persistante
- P540S - Spécifications de la séquence réalisateur
- P555S - Spécifications de composant logiciel
- P580S - Spécifications de processus automatisé
- P600S - Composant logiciel
- P750S - Cas d'essai
- P770S - Résultats d'essai
- P900S - Suivi des exigences
- P901S - Registre des demandes de changement
- P902S - Compte rendu de l'information
- P891S Demande de changement

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase A - Vision d’architecture (Architecture Vision).
- Livrable TOGAF cible : Plan de validation et critères d’acceptation.
- Domaine d’architecture principal : essais.
- Artefacts associés : Critères d’acceptation, Cas de test, Registre des anomalies, Demande de travail d’architecture (Request for Architecture Work).

## Règles particulières de rédaction

- Présenter P405S Stratégie de réalisation et d'essai comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
- Ne jamais faire primer Macroscope sur TOGAF.
- Documenter les hypothèses et les points à confirmer lorsque la source utilisateur est incomplète.
- Relier les éléments du livrable aux exigences, décisions, vues, composants et risques pertinents.
- Utiliser le terme conseiller en architecture pour désigner la contribution d’architecture.

## Exemples utiles ou indications extraites

- Il est à noter que si, on doit modifier les **interfaces utilisateur** , afin de, par exemple, respecter les nouvelles normes de présentation, ce sera représenté dans les unités de tâche (P490S Spécifications de l'unité de tâche) correspondantes.
- Il identifie le nouveau code à écrire et le code existant à mettre à jour ou à supprimer : code fonctionnel (par exemple, créer une unité de tâche), code des bases de données ou code technique (par exemple, les composantes de l'infrastructure technologique).
- Par exemple, il décide si le groupe d'essai d'intégration sera divisé tout de suite en cas d'essai ou bien en domaines d'essai pour ensuite être divisés en cas d'essai.

## Points de vigilance

- Vérifier que le livrable répond au besoin utilisateur plutôt qu’à une reproduction mécanique du gabarit.
- Éviter les doublons avec les autres livrables Macroscope liés.
- Ne pas transformer une annexe détaillée en décision d’architecture principale.
- Signaler les sections non applicables au lieu de les remplir artificiellement.
- Conserver la traçabilité entre sources, exigences, décisions et artefacts TOGAF.

## Extraits de contexte Macroscope

### Description

Le responsable des essais prépare les plans d'essai détaillés afin d'ordonner les activités d'essai. Les activités, les durées et les participants sont organisés d'après les interdépendances entre les groupes d'essai définis précédemment. L'analyste fonctionnel, en collaboration avec les experts du domaine et les utilisateurs du système, modifie les spécifications des composantes de niveau utilisateur existantes ou en crée de nouvelles, d'après l'architecture du système modifié. Au besoin, un ou plusieurs des ajustements suivants sont apportés aux spécifications utilisateur : * Le P490S Spécifications de l'unité de tâche et le P487S Spécifications de l'étape de tâche réutilisable : Généralement, les ajustements aux **unités de tâche** sont effectués d'après les changements apportés aux P251S Processus de travail, aux fonctions du système (P250S Structure utilisateur du système), ou aux facettes et classes d'information (P170S Structure de l'information). Il est à noter que si, on doit modifier les **interfaces utilisateur** , afin de, par exemple, respecter les nouvelles normes de présentation, ce sera représenté dans les unités de tâche (P490S Spécifications de l'unité de tâche) correspondantes. * Les modifications apportées aux unités de tâche ont un impact sur les **composantes réutilisables de l'interface utilisateur**. Si tel est le cas, un ou plusieurs P186S Spécifications de composante réutilisable d'interface peuvent devoir être mis à jour ou créés. * Si des facettes et classes d'information (P170S Structure de l'information) ont été modifiées, il est possible que leurs **services du noyau** doivent être révisés. Les services du noyau pourraient aussi devoir être ajustés afin de soutenir convenablement les unités de tâche modifiées. Dans ce cas, un ou plusieurs P180S Spécifications de composante du noyau peuvent devoir être mis à jour ou créés. * Si le changement résulte en des **traitements par lots** , nouveaux ou modifiés, le P580S Spécifications de processus automatisé doit alors évoluer. Au besoin, en se basant sur les spécifications utilisateur révisées, l'conseiller en architecture technique révise et complète l'architecture logicielle, et l'administrateur de base de données révise et complète la structure de l'information persistante. L'analyste-programmeur, en collaboration avec l'analyste fonctionnel, modifie les spécifications actuelles des composantes de réalisation ou en crée de nouvelles au besoin, d'après les modèles réalisateur ajustés, et les spécifications utilisateur nouvelles ou modifiées. Il identifie le nouveau code à écrire et le code existant à mettre à jour ou à supprimer : code fonctionnel (par exemple, créer une unité de tâche), code des bases de données ou code technique (par exemple, les composantes de l'infrastructure technologique). Ensuite, il code les composants logiciels en conséquence. Une fois la codification terminée, les composantes individuelles sont testées par l'analyste-programmeur pour faire en sorte que les spécifications utilisateur et réalisateur soient respectées. Il faut noter que, bien que l'analyste-programmeur ne doive pas codifier les composantes de réalisation sélectionnées (venant du commerce), celles-ci doivent cependant être testées comme le serait tout code maison. Si la solution recommandée le spécifie, les paramètres du système peuvent être modifiés et remplacés par de nouvelles valeurs. Dans ce cas, les essais unitaires ne sont généralement pas pertinents. Le testeur ajuste et complète les groupes d'essai d'intégration afin d'être prêt pour effectuer les essais appropriés pour le changement appliqué. Par exemple, il décide si le groupe d'essai d'intégration sera divisé tout de suite en cas d'essai ou bien en domaines d'essai pour ensuite être divisés en cas d'essai. Il ordonne les domaines d'essai, en tenant compte des dépendances ou préalables entre eux. En collaboration avec les experts du domaine et les utilisateurs, le testeur ajuste les cas d'essai de maintenance existants ou en crée de nouveaux. Selon la nature du changement, les cas d'essai sont basés sur les spécifications utilisateur, réalisateur ou sur la vue de la technologie. Le testeur détermine aussi les exigences liées aux données d'essai. Lorsque les composantes, nouvelles ou modifiées, sont prêtes, le testeur fait l'essai de chaque groupe d'intégration pour s'assurer que ce dernier fonctionne tel que prévu et qu'il n'a pas d'impact sur les parties non modifiées du système ou sur l'environnement technologique (essais de non-régression). S'il y a lieu, les essais d'intégration peuvent aussi être effectués dans le but de s'assurer une intégration appropriée des systèmes externes. Le testeur prépare un compte rendu d'essai pour chaque groupe d'essai d'intégration vérifié et consigne toute variation par rapport aux résultats attendus. Les problèmes ou anomalies identifiés ont la priorité. On identifie les problèmes qui peuvent attendre et on émet les demandes de changement appropriées. Les autres problèmes sont traités selon les priorités établies. S'il y a des changements apportés aux exigences du système et si un P900S Suivi des exigences existe pour le système, donc, une fois que les composantes touchées sont conçues, l'conseiller en architecture de système, en collaboration avec l'conseiller en architecture technique, met à jour le livrable afin de refléter la nouvelle situation. Une description de l'impact qu'ont les nouvelles exigences sur les spécifications et composantes du système est fournie. _Aller à la section_ _Lignes directrices pour changement urgent_ _pour voir comment adapter cette activité dans un contexte de changement urgent._

### Intrants

* **Architectures utilisateur et réalisateur ajustées** (voir le groupe de livrables Architecture du système) * **Spécifications utilisateur et réalisateur existantes** (voir le groupe de livrables Spécifications du système) * **Composantes réalisateur existantes** (voir le groupe de livrables Composantes du système) P405S - Stratégie de réalisation et d'essai P410S - Groupes d'essai P740S - Environnement d'essai P891S - Demande de changement

### Extrants

Non disponible.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

Des rôles (ils peuvent changer d'une livraison à l'autre) désignés effectuent la mise à jour des P891S Demande de changement, P901S Registre des demandes de changement et P902S Compte rendu de l'information. * Administrateur de base de données: Produit * Expert du domaine: Contribue * Analyste fonctionnel: Produit * Analyste-programmeur: Produit * Conseiller en architecture technique: Produit * Testeur: Produit * Utilisateur: Contribue * Responsable des essais: Produit * Conseiller en architecture de système: Produit
