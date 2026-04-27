# Approche de documentation orientee transfert vers la realisation

## Objectif

Cette approche definit comment utiliser les livrables Macroscope comme intrants successifs entre la vision, l architecture, la realisation et l exploitation d une solution.

Le principe directeur est le suivant : un livrable n est utile que s il permet a la phase suivante de prendre une decision, de produire un element concret, de verifier une exigence ou de reduire une incertitude.

Cette approche vise particulierement le passage entre la vision ou l architecture et les equipes de realisation.

## Principes

1. Chaque livrable doit avoir un destinataire explicite.
2. Chaque section produite doit servir d intrant a une activite ulterieure.
3. Les exigences, decisions, processus, donnees, composants et contraintes doivent etre tracables.
4. Les points ouverts doivent etre visibles et assignables.
5. La documentation doit soutenir la realisation, les essais, l implantation et l exploitation.
6. Les livrables volumineux doivent etre resumes dans un paquet de transfert exploitable.

## Chaine de passage entre phases

| Phase | Livrables intrants | Sortie attendue pour la phase suivante |
| --- | --- | --- |
| Vision | `P130O Objectifs du systeme d'information`, `P140O Portee du systeme d'information`, `P2863 Exigences` | Objectifs, portee, besoins, contraintes et resultats attendus. |
| Architecture | `P200A Cadre d'architecture`, `P201S Processus du systeme`, `P170S Structure de l'information`, `P219S Architecture logicielle`, `P269S Technologie et repartition utilisateur` | Decisions, vues de solution, composants attendus, contraintes et impacts. |
| Transfert vers la realisation | `P900S Suivi des exigences`, synthese des decisions, matrice de transfert | Elements prets a realiser, criteres d acceptation, dependances et points a confirmer. |
| Realisation | `P2871 Specifications du systeme`, `P490S Specifications de l'unite de tache`, `P555S Specifications de composant logiciel`, `P580S Specifications de processus automatise`, `P405S Strategie de realisation et d'essai` | Specifications detaillees, composants, traitements, interfaces et strategie d essai. |
| Implantation et exploitation | `P450S Plan d'implantation`, `P705S Guide d'operation`, `P720C Instructions d'installation, niveau realisateur`, `P931G Entente de niveau de service`, `P951S Plan de gestion de configuration` | Instructions d installation, procedures d exploitation, niveaux de service, maintenance et configuration. |

## Paquet de transfert vers la realisation

Le paquet de transfert est le livrable de synthese qui rend l architecture consommable par les equipes de realisation.

Il ne remplace pas les livrables sources. Il les relie, les resume et transforme leurs conclusions en intrants actionnables.

### Contenu minimal

| Section | Contenu attendu | Source principale |
| --- | --- | --- |
| Contexte et objectif | Raison du changement, objectifs, resultats attendus. | `P130O`, `P2863` |
| Portee | Inclus, exclus, limites, dependances. | `P140O`, `P200A` |
| Exigences retenues | Exigences priorisees et verifiables. | `P2863`, `P900S` |
| Processus touches | Processus, fonctions, unites de tache et acteurs concernes. | `P201S`, `P251S`, `P490S` |
| Donnees touchees | Informations, donnees persistantes, bases de donnees, responsabilites. | `P170S`, `P510S`, `P150C` |
| Composants attendus | Sous-systemes, composants logiciels, interfaces et traitements. | `P219S`, `P555S`, `P580S` |
| Contraintes techniques | Technologie, repartition, securite, exploitation, performance. | `P269S`, `P705S`, `P931G` |
| Decisions | Decisions applicables a la realisation et justification. | `P200A`, comptes rendus, registre de decisions |
| Criteres d acceptation | Conditions de verification et resultats attendus. | `P405S`, `P750S` |
| Points ouverts | Questions, hypotheses, risques et responsables. | Tous les livrables sources |

## Matrice de transfert

La matrice de transfert est le mecanisme central de passage entre architecture et realisation.

Elle doit permettre a une equipe de realisation de comprendre :

- pourquoi un element doit etre realise;
- quel besoin ou decision le justifie;
- quel livrable source le supporte;
- quel composant, processus, donnee ou interface est touche;
- comment l element sera verifie;
- ce qui reste a confirmer.

### Modele de matrice

| ID | Source | Exigence ou decision | Impact solution | Livrable de realisation | Critere d acceptation | Responsable | Statut |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TR-001 | `P2863-EX-001` | Exigence priorisee et verifiable. | Processus, composant, donnee ou interface touche. | `P490S`, `P555S`, `P580S` ou autre. | Condition mesurable de verification. | Equipe ou role responsable. | Pret, a clarifier, bloque, realise. |

### Statuts recommandes

| Statut | Signification |
| --- | --- |
| A cadrer | L element existe, mais la portee ou l objectif n est pas assez clair. |
| A analyser | L impact sur la solution n est pas encore determine. |
| A clarifier | Une question empeche le passage vers la realisation. |
| Pret | L equipe de realisation peut utiliser l element comme intrant. |
| En realisation | L element est pris en charge par l equipe de realisation. |
| Realise | L element a ete produit ou integre. |
| Verifie | L element a ete valide par essai, revue ou acceptation. |

## Criteres de pret pour la realisation

Un element est pret pour la realisation seulement si les criteres suivants sont satisfaits :

| Critere | Verification attendue |
| --- | --- |
| Portee claire | L element precise ce qui est inclus et exclu. |
| Source connue | L element renvoie a une exigence, une decision, un processus ou une contrainte source. |
| Priorite et valeur | L importance de l element est connue. |
| Impact identifie | Les processus, donnees, composants, interfaces ou operations touches sont identifies. |
| Critere d acceptation | Le resultat attendu est verifiable. |
| Dependances connues | Les dependances avec d autres livrables, composants ou equipes sont visibles. |
| Points ouverts geres | Les questions restantes sont assignees et ne bloquent pas la realisation. |
| Responsable identifie | Une equipe ou un role responsable est indique. |

## Definition des responsabilites

| Role | Responsabilite dans le transfert |
| --- | --- |
| Conseiller en architecture | Maintenir la coherence des decisions, vues, contraintes et impacts. |
| Analyste d affaires | Assurer la clarte des exigences, processus, regles et criteres d acceptation metier. |
| Responsable de realisation | Confirmer que les intrants sont utilisables par l equipe de realisation. |
| Responsable des essais | Traduire les exigences et decisions en criteres et cas d essai. |
| Responsable exploitation | Confirmer les contraintes d installation, de soutien, d exploitation et de maintenance. |
| Responsable produit ou demandeur | Confirmer la priorite, la valeur et l acceptabilite du resultat. |

## Revue de transfert

La revue de transfert est une activite courte qui confirme que les intrants sont prets pour la realisation.

### Intrants de la revue

- paquet de transfert;
- matrice de transfert;
- liste des exigences retenues;
- decisions applicables;
- points ouverts;
- risques;
- criteres d acceptation;
- dependances de livraison.

### Sorties de la revue

- elements acceptes pour realisation;
- elements retournes pour clarification;
- decisions a confirmer;
- risques a suivre;
- assignations;
- mise a jour de la matrice de transfert.

## Implementation dans le depot de skills

### 1. Ajouter une reference transversale

Creer une reference commune dans `references/`, par exemple :

```text
references/approche-transfert-realisation.md
```

Cette reference devrait contenir :

- le modele de paquet de transfert;
- le modele de matrice de transfert;
- les criteres de pret;
- les statuts;
- les controles de qualite.

### 2. Ajouter ou adapter une skill de transfert

Creer une skill dediee, par exemple :

```text
skills/macroscope-transfert-architecture-realisation/
```

Cette skill servirait lorsque l utilisateur demande :

- une synthese pour une equipe de realisation;
- une matrice de transfert;
- une revue de passage architecture vers realisation;
- une verification de la maturite des intrants;
- une transformation de livrables sources en backlog ou en lot de realisation.

### 3. Relier les skills existantes

Les skills suivantes devraient mentionner la matrice de transfert dans leur reference ou leur procedure :

- `macroscope-p2863-exigences`
- `macroscope-p200a-cadre-darchitecture`
- `macroscope-p201s-processus-du-systeme`
- `macroscope-p170s-structure-de-linformation`
- `macroscope-p219s-architecture-logicielle`
- `macroscope-p269s-technologie-et-repartition-utilisateur`
- `macroscope-p900s-suivi-des-exigences`
- `macroscope-p2871-specifications-du-systeme`
- `macroscope-p405s-strategie-de-realisation-et-dessai`

### 4. Ajouter un controle de qualite

Tout livrable destine a alimenter la realisation devrait etre verifie avec les questions suivantes :

1. Qui utilisera ce livrable dans la phase suivante?
2. Quelle decision ou action ce livrable permet-il?
3. Quels elements sont directement realisables?
4. Quels elements restent ambigus?
5. Quels criteres permettront de verifier la realisation?
6. Quelles dependances doivent etre suivies?
7. Quels points ouverts bloquent la realisation?

### 5. Valider les skills modifiees

Apres modification des skills ou references, executer :

```bash
python3 utilitaires/verifier_toutes_skills.py
```

Si des variantes sont modifiees :

```bash
python3 utilitaires/verifier_toutes_skills.py --skills-root skills/variantes
```

## Gabarit de paquet de transfert

```markdown
# Paquet de transfert vers la realisation

## 1. Contexte

## 2. Objectifs et resultats attendus

## 3. Portee

### Inclus

### Exclus

### Dependances

## 4. Exigences retenues

| ID | Exigence | Priorite | Source | Critere d acceptation |
| --- | --- | --- | --- | --- |

## 5. Decisions applicables

| ID | Decision | Justification | Impact | Source |
| --- | --- | --- | --- | --- |

## 6. Impacts de solution

| Element | Type | Impact | Livrable de realisation |
| --- | --- | --- | --- |

## 7. Contraintes

## 8. Matrice de transfert

| ID | Source | Exigence ou decision | Impact solution | Livrable de realisation | Critere d acceptation | Responsable | Statut |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 9. Points ouverts

| ID | Point ouvert | Impact | Responsable | Date cible | Statut |
| --- | --- | --- | --- | --- | --- |

## 10. Decision de passage

| Element | Decision | Conditions |
| --- | --- | --- |
```

## Controles de qualite

Avant de remettre un paquet de transfert :

- chaque exigence importante est reliee a une source;
- chaque decision applicable a un impact de realisation;
- chaque impact de realisation a un livrable cible;
- chaque element pret a realiser a un critere d acceptation;
- les points ouverts sont visibles et assignes;
- les dependances sont explicites;
- les contraintes d exploitation sont considerees avant la realisation;
- le contenu est exploitable par une equipe de realisation sans relire tous les livrables sources.
