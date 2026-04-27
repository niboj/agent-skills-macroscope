# Cadre d architecture pour documenter et transmettre une solution

## Intention du cadre

Ce cadre explique comment organiser la documentation d architecture d une solution afin qu elle serve d intrant fiable aux phases suivantes : realisation, essais, implantation, exploitation et maintenance.

L objectif n est pas de produire des documents pour eux-memes. L objectif est de rendre les decisions, exigences, contraintes et impacts suffisamment clairs pour permettre aux equipes de realisation de construire la bonne solution, avec les bons criteres de verification et les bonnes conditions d exploitation.

Le cadre s appuie sur les livrables Macroscope du depot et les interprete comme des artefacts de travail, des vues specialisees et des intrants de passage entre phases.

## Pourquoi documenter l architecture

La documentation d architecture sert a :

1. expliquer pourquoi la solution est requise;
2. definir ce qui est inclus et exclu;
3. rendre les exigences verifiables;
4. expliciter les decisions qui orientent la solution;
5. montrer les impacts sur les processus, les donnees, les applications, la technologie, la securite et l exploitation;
6. fournir aux equipes de realisation des intrants prets a utiliser;
7. reduire les interpretations divergentes entre les parties prenantes;
8. soutenir les essais, l implantation et la maintenance;
9. conserver la trace des hypotheses, des risques et des points ouverts.

Une documentation d architecture est consideree utile lorsqu elle permet a une equipe de repondre clairement a ces questions :

- Que doit-on realiser?
- Pourquoi doit-on le realiser?
- Quelles exigences et decisions le justifient?
- Quels processus, donnees, composants, interfaces et operations sont touches?
- Quelles contraintes doivent etre respectees?
- Comment saura-t-on que le resultat est acceptable?
- Quelles questions restent ouvertes?

## Pour qui on documente

| Public cible | Besoin principal | Contenu utile |
| --- | --- | --- |
| Direction et responsables de portefeuille | Comprendre la valeur, la portee, les risques et les impacts majeurs. | Objectifs, portee, benefices, contraintes, risques, decisions majeures. |
| Responsable produit ou demandeur | Confirmer que la solution repond au besoin et aux priorites. | Exigences, scenarios, criteres d acceptation, impacts metier. |
| Conseiller en architecture | Maintenir la coherence des vues, decisions, contraintes et dependances. | Cadre d architecture, decisions, vues de solution, principes, points ouverts. |
| Analyste d affaires | Transformer le besoin en exigences, processus, regles et criteres verifiables. | Objectifs, portee, exigences, processus, regles, unites de tache. |
| Equipe de realisation | Construire la solution sans devoir reconstruire l intention initiale. | Paquet de transfert, specifications, composants, interfaces, contraintes, criteres d acceptation. |
| Responsable des essais | Preparer les cas d essai et les validations. | Exigences verifiables, criteres d acceptation, scenarios, dependances, environnements. |
| Responsable exploitation | Preparer l installation, l exploitation, le soutien et la maintenance. | Contraintes operationnelles, instructions d installation, niveaux de service, configuration. |
| Securite et conformite | Verifier que les controles et obligations sont pris en compte. | Exigences de securite, actifs sensibles, acces, controles, journaux, risques. |

## Principes de documentation

1. Documenter pour la prochaine decision ou la prochaine action.
2. Produire une documentation proportionnelle au risque et a la complexite.
3. Separer les faits sources, les hypotheses, les decisions et les points a confirmer.
4. Relier chaque exigence importante a un impact et a un critere de verification.
5. Eviter de melanger l architecture, la specification detaillee et le code.
6. Faire apparaitre les dependances entre metier, donnees, applications, technologie et exploitation.
7. Ne pas livrer un document volumineux sans synthese actionnable.
8. Garder une matrice de transfert entre architecture et realisation.

## Vue d ensemble de l approche

L approche comporte sept etapes :

1. cadrer la demande;
2. definir la vision et la portee;
3. documenter les exigences;
4. produire les vues d architecture;
5. prendre et tracer les decisions;
6. preparer le transfert vers la realisation;
7. soutenir la realisation, les essais, l implantation et l exploitation.

Chaque etape produit des intrants pour l etape suivante.

## Etape 1 - Cadrer la demande

### But

Comprendre le changement demande, son contexte, sa portee initiale, les parties prenantes et les contraintes connues.

### Questions a traiter

- Quel probleme ou quelle opportunite motive la solution?
- Quel service, processus, systeme ou domaine est vise?
- Qui demande le changement?
- Qui est touche par le changement?
- Quelles contraintes sont deja connues?
- Quels documents ou decisions existent deja?
- Quel niveau de documentation est attendu?

### Intrants possibles

- demande initiale;
- orientation d affaires;
- exigences preliminaires;
- incidents ou problemes connus;
- contraintes legales, operationnelles ou technologiques;
- documentation existante du systeme actuel.

### Sorties attendues

- contexte synthetique;
- liste des parties prenantes;
- portee initiale;
- hypotheses;
- points a confirmer;
- decision sur les livrables a produire.

### Livrables Macroscope utiles

- `P2863 Exigences`
- `P130O Objectifs du systeme d'information`
- `P140O Portee du systeme d'information`
- `M002A Enonce du projet`
- `M045A Risque`
- `M046A Point en suspens`

## Etape 2 - Definir la vision et la portee

### But

Etablir pourquoi la solution existe, ce qu elle doit produire comme resultat, ce qui est inclus et ce qui est exclu.

### Questions a traiter

- Quels objectifs mesurables la solution doit-elle atteindre?
- Quelles capacites ou fonctions sont visees?
- Quelles clienteles ou utilisateurs sont concernes?
- Quels processus sont inclus?
- Quels sujets, donnees ou ressources sont inclus?
- Quelles limites doivent etre respectees?
- Quels elements sont explicitement hors portee?

### Prealables

Avant de produire une architecture plus detaillee, il faut disposer au minimum :

- d un objectif clair;
- d une portee explicite;
- d une liste initiale d exigences;
- d une liste des parties prenantes;
- d une premiere identification des risques et contraintes.

### Sorties attendues

- objectifs du systeme;
- portee du systeme;
- exigences initiales;
- criteres de succes;
- elements exclus;
- dependances majeures.

### Livrables Macroscope utiles

- `P130O Objectifs du systeme d'information`
- `P140O Portee du systeme d'information`
- `P140S Exigences proprietaire`
- `P2863 Exigences`

## Etape 3 - Documenter les exigences

### But

Transformer les besoins en exigences utilisables par l architecture, la realisation, les essais et l exploitation.

### Qualites attendues d une exigence

Une exigence devrait etre :

- claire;
- verifiable;
- priorisee;
- rattachee a une source;
- reliee a un objectif;
- associee a un impact;
- accompagnee d un critere d acceptation ou d une condition de verification.

### Types d exigences a distinguer

| Type | Description | Exemples d impacts |
| --- | --- | --- |
| Affaires | Besoin, regle ou resultat attendu. | Processus, roles, services, indicateurs. |
| Fonctionnelle | Fonction ou comportement attendu. | Unites de tache, cas d utilisation, traitements. |
| Donnees | Information a creer, lire, modifier, conserver ou proteger. | Entites, bases de donnees, conservation, qualite. |
| Applicative | Capacite ou composant logiciel attendu. | Sous-systemes, composants, interfaces, integrations. |
| Technologique | Infrastructure, plateforme ou repartition. | Environnements, reseau, stockage, postes, hebergement. |
| Securite | Protection, acces, journalisation, segregation, conformite. | Roles, controles, audit, chiffrement, traces. |
| Exploitation | Installation, surveillance, soutien, performance, disponibilite. | Guides, niveaux de service, configuration, maintenance. |

### Sorties attendues

- exigences classees et priorisees;
- exigences liees a des objectifs;
- exigences liees a des impacts;
- exigences liees a des criteres d acceptation;
- exigences non retenues ou reportees;
- points a confirmer.

### Livrables Macroscope utiles

- `P2863 Exigences`
- `P140S Exigences proprietaire`
- `P900S Suivi des exigences`
- `P360S Regles utilisateur`
- `P361U Regles administratives et d'organisation du travail`
- `P363U Regles de fonctionnement du traitement automatise`

## Etape 4 - Produire les vues d architecture

### But

Produire les vues necessaires pour comprendre la solution avant sa realisation.

Une vue d architecture doit repondre a une preoccupation precise. Elle ne doit pas tout documenter. Elle doit aider un public donne a comprendre une partie du changement.

### Vues recommandees

| Vue | Question traitee | Livrables Macroscope |
| --- | --- | --- |
| Vue de contexte | Quel est le contexte, la portee et les limites? | `P200A`, `P140O`, `P2863` |
| Vue metier | Quels processus, fonctions et roles sont touches? | `P201S`, `P251S`, `P250S` |
| Vue donnees | Quelles informations et donnees sont touchees? | `P170S`, `P150C`, `P510S` |
| Vue applicative | Quels sous-systemes, composants et interfaces sont requis? | `P219S`, `P219C`, `P229C`, `P555S` |
| Vue technologique | Quelle technologie, repartition et infrastructure sont requises? | `P269S`, `P268U`, `P269U` |
| Vue securite | Quels actifs, acces, controles et risques doivent etre geres? | `P120S`, exigences de securite, regles et controles |
| Vue exploitation | Comment installer, exploiter, soutenir et maintenir? | `P705S`, `P705U`, `P720C`, `P931G`, `P951S` |

### Prealables entre vues

| Avant de produire | Il faut disposer de |
| --- | --- |
| Vue metier | Objectifs, portee, parties prenantes et processus cibles. |
| Vue donnees | Processus, informations manipulees et regles de gestion. |
| Vue applicative | Exigences fonctionnelles, processus, donnees et integrations connues. |
| Vue technologique | Vue applicative, besoins de repartition, contraintes d exploitation et securite. |
| Vue securite | Actifs, roles, donnees sensibles, risques et contraintes applicables. |
| Vue exploitation | Composants, environnements, contraintes de disponibilite, installation et soutien. |

## Etape 5 - Prendre et tracer les decisions

### But

Rendre les decisions explicites afin que la realisation ne doive pas les deduire.

### Une decision doit indiquer

- le sujet de la decision;
- le contexte;
- les options considerees;
- l option retenue;
- la justification;
- les impacts;
- les exigences concernees;
- les risques;
- les conditions ou limites;
- la date et le responsable de la decision.

### Sorties attendues

- registre de decisions;
- impacts sur les livrables;
- exigences mises a jour;
- points ouverts fermes ou assignes;
- contraintes de realisation clarifiees.

### Livrables Macroscope utiles

- `P200A Cadre d'architecture`
- `P900S Suivi des exigences`
- `M049S Notes de reunion`
- `M042A Demande de changement`
- `M046A Point en suspens`

## Etape 6 - Preparer le transfert vers la realisation

### But

Transformer la documentation d architecture en intrants directement utilisables par les equipes de realisation.

### Paquet de transfert

Le paquet de transfert doit synthetiser :

- les objectifs;
- la portee;
- les exigences retenues;
- les decisions applicables;
- les processus touches;
- les donnees touchees;
- les composants attendus;
- les interfaces attendues;
- les contraintes techniques, de securite et d exploitation;
- les criteres d acceptation;
- les dependances;
- les points ouverts.

### Matrice de transfert

| ID | Source | Exigence ou decision | Impact solution | Livrable de realisation | Critere d acceptation | Responsable | Statut |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TR-001 | `P2863-EX-001` | Exigence ou decision a transmettre. | Processus, donnee, composant, interface ou operation touche. | `P2871`, `P490S`, `P555S`, `P580S` ou autre. | Condition verifiable. | Equipe ou role. | Pret, a clarifier, bloque, realise. |

### Criteres de pret

Un element peut etre transmis a la realisation s il respecte les criteres suivants :

1. la portee est claire;
2. la source est connue;
3. la priorite est connue;
4. l impact solution est identifie;
5. le livrable de realisation cible est identifie;
6. le critere d acceptation est defini;
7. les dependances sont connues;
8. les points ouverts ne bloquent pas la realisation ou sont assignes.

### Livrables Macroscope utiles

- `P900S Suivi des exigences`
- `P2871 Specifications du systeme`
- `P405S Strategie de realisation et d'essai`
- `P490S Specifications de l'unite de tache`
- `P555S Specifications de composant logiciel`
- `P580S Specifications de processus automatise`

## Etape 7 - Soutenir la realisation, les essais et l exploitation

### But

S assurer que la realisation reste coherente avec les exigences et decisions, puis preparer les conditions d implantation et d exploitation.

### Activites attendues

- repondre aux questions de realisation;
- clarifier les exigences ambigues;
- traiter les demandes de changement;
- verifier les impacts des ajustements;
- maintenir la matrice de transfert;
- aligner les cas d essai avec les exigences;
- preparer les instructions d installation;
- confirmer les besoins d exploitation et de soutien.

### Livrables Macroscope utiles

- `P405S Strategie de realisation et d'essai`
- `P415G Plan d'integration et de verification`
- `P750S Cas d'essai`
- `P770S Resultats d'essai`
- `P070M Anomalie`
- `P072M Registre des anomalies`
- `P450S Plan d'implantation`
- `P705S Guide d'operation`
- `P720C Instructions d'installation, niveau realisateur`
- `P931G Entente de niveau de service`
- `P951S Plan de gestion de configuration`

## Ordre recommande des travaux

| Ordre | Travail | Raison |
| --- | --- | --- |
| 1 | Cadrer la demande et les parties prenantes. | Eviter de documenter un mauvais perimetre. |
| 2 | Definir objectifs, portee et exigences initiales. | Donner une base commune aux vues d architecture. |
| 3 | Produire la vue metier. | Comprendre les processus et usages avant les composants. |
| 4 | Produire la vue donnees. | Identifier les informations touchees par les processus. |
| 5 | Produire la vue applicative. | Definir les sous-systemes, composants et interfaces. |
| 6 | Produire la vue technologique. | Aligner l infrastructure sur l applicatif et l exploitation. |
| 7 | Documenter securite et exploitation. | Integrer les contraintes avant la realisation. |
| 8 | Tracer les decisions et exigences. | Eviter les pertes d information. |
| 9 | Prepararer le paquet de transfert. | Rendre l architecture exploitable par la realisation. |
| 10 | Tenir la revue de transfert. | Confirmer que les intrants sont prets. |

## Qui devrait faire quoi

| Role | Responsabilites principales |
| --- | --- |
| Responsable produit ou demandeur | Confirmer les objectifs, priorites, valeur attendue et criteres d acceptation metier. |
| Conseiller en architecture | Diriger la coherence des vues, decisions, contraintes, impacts et dependances. |
| Analyste d affaires | Formaliser exigences, processus, regles, scenarios et impacts metier. |
| Specialiste donnees | Documenter les informations, donnees persistantes, qualite, responsabilites et contraintes de conservation. |
| Specialiste applicatif | Preciser sous-systemes, composants, interfaces et integrations. |
| Specialiste technologique | Preciser infrastructure, environnements, repartition, performance et contraintes techniques. |
| Specialiste securite | Identifier actifs sensibles, risques, controles, acces, journalisation et obligations. |
| Responsable de realisation | Confirmer que les intrants sont utilisables et planifiables par les equipes de realisation. |
| Responsable des essais | Transformer exigences et decisions en scenarios, cas d essai et resultats attendus. |
| Responsable exploitation | Confirmer les conditions d installation, operation, soutien, maintenance et niveaux de service. |

## Gouvernance minimale

### Points de controle

| Moment | Controle |
| --- | --- |
| Fin du cadrage | Les objectifs, la portee, les parties prenantes et les contraintes majeures sont connus. |
| Fin des exigences | Les exigences prioritaires sont verifiables et liees a des objectifs. |
| Fin de l architecture | Les vues necessaires sont produites et les decisions importantes sont tracees. |
| Avant realisation | Le paquet de transfert est accepte par les equipes de realisation, essais et exploitation. |
| Pendant realisation | Les changements et questions sont evalues selon leurs impacts. |
| Avant implantation | Les instructions, controles, essais et conditions d exploitation sont prets. |

### Revue de transfert vers la realisation

La revue doit confirmer :

- ce qui est pret a realiser;
- ce qui doit etre clarifie;
- ce qui est hors portee;
- les decisions qui doivent etre respectees;
- les exigences qui seront verifiees;
- les risques acceptes ou a suivre;
- les dependances de livraison;
- les responsabilites.

## Gabarit de cadre d architecture

```markdown
# Cadre d architecture de la solution

## 1. Contexte et objectifs

## 2. Portee

### Inclus

### Exclus

### Dependances

## 3. Parties prenantes et publics cibles

## 4. Exigences retenues

| ID | Exigence | Source | Priorite | Critere d acceptation |
| --- | --- | --- | --- | --- |

## 5. Vues d architecture

### 5.1 Vue metier

### 5.2 Vue donnees

### 5.3 Vue applicative

### 5.4 Vue technologique

### 5.5 Vue securite

### 5.6 Vue exploitation

## 6. Decisions

| ID | Decision | Justification | Impact | Source |
| --- | --- | --- | --- | --- |

## 7. Contraintes et risques

## 8. Matrice de transfert vers la realisation

| ID | Source | Exigence ou decision | Impact solution | Livrable de realisation | Critere d acceptation | Responsable | Statut |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 9. Points ouverts

| ID | Point ouvert | Impact | Responsable | Date cible | Statut |
| --- | --- | --- | --- | --- | --- |

## 10. Decision de passage vers la realisation
```

## Controles de qualite

Avant de transmettre l architecture a la realisation, verifier que :

- la portee est explicite;
- les objectifs sont relies aux exigences;
- les exigences importantes sont verifiables;
- les vues necessaires sont presentes;
- les decisions importantes sont tracees;
- les impacts sur processus, donnees, composants, interfaces et exploitation sont identifies;
- les contraintes de securite et d exploitation sont connues;
- les criteres d acceptation sont disponibles;
- les points ouverts sont assignes;
- la matrice de transfert est utilisable par les equipes de realisation;
- le responsable de realisation confirme que les intrants sont suffisamment clairs pour planifier et executer le travail.

## Lien avec l approche de documentation

Le fichier `approche-documentation.md` complete ce cadre en precisant le mecanisme de transfert entre architecture et realisation. Le present fichier definit l approche globale d architecture; `approche-documentation.md` detaille la documentation de passage et la matrice de transfert.
