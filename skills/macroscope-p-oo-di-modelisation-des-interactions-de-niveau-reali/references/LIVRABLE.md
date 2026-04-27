# Référence du livrable P-OO DI Modélisation des interactions de niveau réalisateur

## Source analysée

- Fichier source : `../../../macroscope/livrables/4f1f0593953c.md`
- Méthode source : Macroscope
- Extraction du titre : lien inverse par URL

## Synthèse du livrable

À partir des unités de tâche produites par la technique P-OO-UA Modélisation d'analyse utilisateur détaillée, et des modèles de classe réalisateur produits par la technique P-OO-DO Modélisation des objets de niveau réalisateur, cette technique permet de déterminer les interactions entre les objets ainsi que les opérations nécessaires pour donner le comportement perceptible par l'utilisateur d'une unité de tâche ou d'une étape de tâche réutilisable. Vue d'ensemble des activités des techniques de modélisation des interactions réalisateur La technique P-OO-DI Modélisation réalisateur des interactions produit le séquencement de niveau réalisateur, les règles d'appel d'opération, et les spécifications de réalisation d'opération. Ces éléments d'information sont dérivés des extrants des techniques P-OO-UA de modélisation d'analyse utilisateur détaillée (soit Définition utilisateur d'un service du noyau, Définition utilisateur d'un service d'interface utilisateur, Spécifications utilisateur d'une étape de tâche, Spécifications utilisateur d'une unité de tâche) et réutilisent les spécifications de classe réalisateur existantes. Les classes et diagrammes réalisateur requis par cette technique sont produits par la technique P-OO-DO Modélisation des objets de niveau réalisateur. La technique P-OO-DI Modélisation des interactions de niveau réalisateur utilise les modèles produits par la technique P-OO-UA Modélisation d'analyse utilisateur détaillée, effectue une certaine analyse des cas d'utilisation de niveau utilisateur et élabore les modèles d'interaction réalisateur de l'application. Ces modèles d'interaction constituent une partie des spécifications de niveau réalisateur qui permettent de réaliser la vue utilisateur de l'application. L'autre partie est composée des modèles de classe réalisateur élaborés par la technique P-OO-DO Modélisation des objets de niveau réalisateur. On élabore un modèle d'interaction à partir du séquencement des services dans l'unité de tâche en cours d'analyse. Pour contrôler la complexité, on analyse les détails supplémentaires à part et on effectue des itérations subséquentes (par exemple, «design patterns», exigences de performances, besoins de réutilisation) pour permettre l'ajout de toute amélioration ou optimisation nécessaire. La technique P-OO-DI Modélisation des interactions de niveau réalisateur, influence également les modèles de classe réalisateur en suggérant de nouvelles classes, de nouvelles opérations et des attributs possibles. À l'aide des spécifications utilisateur du service, on esquisse la dynamique des opérations, c'est-à-dire qu'on spécifie leurs règles d'appel et qu'on esquisse leur algorithme. Celles qui sont jugées complexes sont approfondies par de nouvelles interactions (nouvelles opérations et règles d'appel). Les plus simples de ces interactions sont codées immédiatement. En résumé, cette technique détaille le comportement des cas d'utilisation et services utilisateur, ainsi que de toutes les opérations qui les appuient. Une technique complémentaire, P-OO-DO Modélisation des objets de niveau réalisateur, assure l'affectation des opérations aux classes.

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

- * Décrire comment les objets interagissent les uns avec les autres afin d'assurer le comportement attendu d'un cas d'utilisation ou d'un service de niveau utilisateur.
- Vue d'ensemble des activités des techniques de modélisation des interactions réalisateur La technique P-OO-DI Modélisation réalisateur des interactions produit le séquencement de niveau réalisateur, les règles d'appel d'opération, et les spécifications de réal
- Ces éléments d'information sont dérivés des extrants des techniques P-OO-UA de modélisation d'analyse utilisateur détaillée (soit Définition utilisateur d'un service du noyau, Définition utilisateur d'un service d'interface utilisateur, Spécifications utilisat
- On élabore un modèle d'interaction à partir du séquencement des services dans l'unité de tâche en cours d'analyse.
- Pour contrôler la complexité, on analyse les détails supplémentaires à part et on effectue des itérations subséquentes (par exemple, «design patterns», exigences de performances, besoins de réutilisation) pour permettre l'ajout de toute amélioration ou optimis
- À l'aide des spécifications utilisateur du service, on esquisse la dynamique des opérations, c'est-à-dire qu'on spécifie leurs règles d'appel et qu'on esquisse leur algorithme.
- Celles qui sont jugées complexes sont approfondies par de nouvelles interactions (nouvelles opérations et règles d'appel).
- En résumé, cette technique détaille le comportement des cas d'utilisation et services utilisateur, ainsi que de toutes les opérations qui les appuient.
- En règle générale, si l'information obtenue par la technique P-OO-UA Modélisation d'analyse utilisateur détaillée n'est pas de nature très complexe, les interactions sont déterminées lors du codage.

## Tableaux, modèles ou diagrammes recommandés

- À partir des unités de tâche produites par la technique P-OO-UA Modélisation d'analyse utilisateur détaillée, et des modèles de classe réalisateur produits par la technique P-OO-DO Modélisation des objets de niveau réalisateur, cette technique permet de déterm
- Les classes et diagrammes réalisateur requis par cette technique sont produits par la technique P-OO-DO Modélisation des objets de niveau réalisateur.
- La technique P-OO-DI Modélisation des interactions de niveau réalisateur utilise les modèles produits par la technique P-OO-UA Modélisation d'analyse utilisateur détaillée, effectue une certaine analyse des cas d'utilisation de niveau utilisateur et élabore le
- Ces modèles d'interaction constituent une partie des spécifications de niveau réalisateur qui permettent de réaliser la vue utilisateur de l'application.
- L'autre partie est composée des modèles de classe réalisateur élaborés par la technique P-OO-DO Modélisation des objets de niveau réalisateur.
- On élabore un modèle d'interaction à partir du séquencement des services dans l'unité de tâche en cours d'analyse.
- La technique P-OO-DI Modélisation des interactions de niveau réalisateur, influence également les modèles de classe réalisateur en suggérant de nouvelles classes, de nouvelles opérations et des attributs possibles.
- #### Utilisation des modèles de conception (Design Pattern)
- Les modèles de conception servent à documenter les interactions entre les objets.
- Les modèles de conception servent à :
- Les modèles de conception sont contextuels et, dans certaines situations, la solution offerte n'est peut-être pas appropriée.
- Dans de tels cas, il peut être utile d'adapter le modèle de conception existant.

## Livrables et références liés

- P-OO-UA Modélisation d'analyse utilisateur détaillée
- P-OO-DO Modélisation des objets de niveau réalisateur
- P-OO-DI Modélisation des interactions de niveau réalisateur
- P-OO-DI.1 - Déterminer les spécifications d'enchaînement
- P-OO-DI.2 - Proposer des définitions d'opération
- P-OO-DI.3 - Définir la dynamique détaillée de l'opération

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase A - Vision d’architecture (Architecture Vision).
- Livrable TOGAF cible : Plan de transition, exploitation et adoption.
- Domaine d’architecture principal : utilisation.
- Artefacts associés : Procédure d’exploitation, Guide utilisateur, Matériel de transfert, Demande de travail d’architecture (Request for Architecture Work).

## Règles particulières de rédaction

- Présenter P-OO DI Modélisation des interactions de niveau réalisateur comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
- Ne jamais faire primer Macroscope sur TOGAF.
- Documenter les hypothèses et les points à confirmer lorsque la source utilisateur est incomplète.
- Relier les éléments du livrable aux exigences, décisions, vues, composants et risques pertinents.
- Utiliser le terme conseiller en architecture pour désigner la contribution d’architecture.

## Exemples utiles ou indications extraites

- * Décrire comment les objets interagissent les uns avec les autres afin d'assurer le comportement attendu d'un cas d'utilisation ou d'un service de niveau utilisateur.
- Pour contrôler la complexité, on analyse les détails supplémentaires à part et on effectue des itérations subséquentes (par exemple, «design patterns», exigences de performances, besoins de réutilisation) pour permettre l'ajout de toute amélioration ou optimis
- Les modèles de conception servent à documenter les interactions entre les objets.
- La technique est particulièrement utile pour documenter les cas clés et pour donner de bons exemples par l'analyse des cas représentatifs.

## Points de vigilance

- Vérifier que le livrable répond au besoin utilisateur plutôt qu’à une reproduction mécanique du gabarit.
- Éviter les doublons avec les autres livrables Macroscope liés.
- Ne pas transformer une annexe détaillée en décision d’architecture principale.
- Signaler les sections non applicables au lieu de les remplir artificiellement.
- Conserver la traçabilité entre sources, exigences, décisions et artefacts TOGAF.

## Extraits de contexte Macroscope

### Description

À partir des unités de tâche produites par la technique P-OO-UA Modélisation d'analyse utilisateur détaillée, et des modèles de classe réalisateur produits par la technique P-OO-DO Modélisation des objets de niveau réalisateur, cette technique permet de déterminer les interactions entre les objets ainsi que les opérations nécessaires pour donner le comportement perceptible par l'utilisateur d'une unité de tâche ou d'une étape de tâche réutilisable. Vue d'ensemble des activités des techniques de modélisation des interactions réalisateur La technique P-OO-DI Modélisation réalisateur des interactions produit le séquencement de niveau réalisateur, les règles d'appel d'opération, et les spécifications de réalisation d'opération. Ces éléments d'information sont dérivés des extrants des techniques P-OO-UA de modélisation d'analyse utilisateur détaillée (soit Définition utilisateur d'un service du noyau, Définition utilisateur d'un service d'interface utilisateur, Spécifications utilisateur d'une étape de tâche, Spécifications utilisateur d'une unité de tâche) et réutilisent les spécifications de classe réalisateur existantes. Les classes et diagrammes réalisateur requis par cette technique sont produits par la technique P-OO-DO Modélisation des objets de niveau réalisateur. La technique P-OO-DI Modélisation des interactions de niveau réalisateur utilise les modèles produits par la technique P-OO-UA Modélisation d'analyse utilisateur détaillée, effectue une certaine analyse des cas d'utilisation de niveau utilisateur et élabore les modèles d'interaction réalisateur de l'application. Ces modèles d'interaction constituent une partie des spécifications de niveau réalisateur qui permettent de réaliser la vue utilisateur de l'application. L'autre partie est composée des modèles de classe réalisateur élaborés par la technique P-OO-DO Modélisation des objets de niveau réalisateur. On élabore un modèle d'interaction à partir du séquencement des services dans l'unité de tâche en cours d'analyse. Pour contrôler la complexité, on analyse les détails supplémentaires à part et on effectue des itérations subséquentes (par exemple, «design patterns», exigences de performances, besoins de réutilisation) pour permettre l'ajout de toute amélioration ou optimisation nécessaire. La technique P-OO-DI Modélisation des interactions de niveau réalisateur, influence également les modèles de classe réalisateur en suggérant de nouvelles classes, de nouvelles opérations et des attributs possibles. À l'aide des spécifications utilisateur du service, on esquisse la dynamique des opérations, c'est-à-dire qu'on spécifie leurs règles d'appel et qu'on esquisse leur algorithme. Celles qui sont jugées complexes sont approfondies par de nouvelles interactions (nouvelles opérations et règles d'appel). Les plus simples de ces interactions sont codées immédiatement. En résumé, cette technique détaille le comportement des cas d'utilisation et services utilisateur, ainsi que de toutes les opérations qui les appuient. Une technique complémentaire, P-OO-DO Modélisation des objets de niveau réalisateur, assure l'affectation des opérations aux classes.

### Intrants

Non disponible.

### Extrants

Non disponible.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

Non disponible.
