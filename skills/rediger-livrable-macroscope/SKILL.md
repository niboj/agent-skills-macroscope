---
name: rediger-livrable-macroscope
description: Utiliser ce skill quand il faut produire, completer ou reviser un livrable selon la methodologie Macroscope a partir d une demande, d un brouillon, d exigences, d observations metier ou de references locales du depot.
---

# Skill: rediger-livrable-macroscope

## But

Produire ou reviser un livrable Macroscope exploitable, structure et trace aux references disponibles.

## Quand utiliser

- Quand l utilisateur demande un livrable Macroscope sans nommer une skill plus specialisee.
- Quand un brouillon doit etre aligne sur la terminologie, les objets ou les conventions Macroscope.
- Quand la demande mentionne une activite, un processus, un evenement, un bien livrable, un modele ou une notation Macroscope.
- Quand il faut transformer des notes de travail en contenu de livrable.

## Entrees

- Demande utilisateur
- Brouillon ou contenu source, le cas echeant
- References locales dans `macroscope/livrables/`
- References propres a la skill, le cas echeant

## Procedure

1. Identifier le type de livrable vise, son audience, son objectif et son niveau de detail attendu.
2. Relever les informations sources disponibles et les informations manquantes.
3. Rechercher dans `macroscope/livrables/` les notions ou conventions applicables. Charger seulement les fichiers utiles au cas courant.
4. Distinguer les faits tires des sources, les hypotheses raisonnables et les points a confirmer.
5. Rediger le livrable avec une structure explicite adaptee au type de sortie demande.
6. Integrer la terminologie Macroscope pertinente sans ajouter de sections decoratives.
7. Verifier la coherence entre objectifs, activites, resultats, roles, evenements, biens livrables et controles de qualite lorsqu ils sont presents.
8. Conclure avec les references locales consultees et les limites si elles influencent l usage du livrable.

## Validation

- Le type de livrable est identifiable.
- La sortie est directement reutilisable par le demandeur.
- Les termes Macroscope importants sont coherents avec les references consultees.
- Les hypotheses et points a confirmer sont explicites.
- Les chemins locaux cites existent.
- Le livrable ne remplit pas les blancs avec des affirmations non sourcees quand l information manque.

## Sortie attendue

Fournir le livrable ou la revision demandee. Ajouter une courte section de tracabilite seulement si des references locales ont ete consultees ou si des hypotheses importantes doivent etre signalees.
