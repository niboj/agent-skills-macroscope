---
name: macroscope-cartographier-livrables
description: Utiliser ce skill quand il faut construire une carte des liens entre livrables Macroscope, intrants, extrants, dépendances, variantes, domaines TOGAF et moments d’utilisation.
metadata:
  source-method: macroscope
  skill-type: transverse
  togaf-precedence: "true"
---

# Skill: Cartographier les livrables Macroscope

## But

Comprendre et documenter les dépendances entre livrables Macroscope.

## Quand utiliser

- Il faut planifier une chaîne de livrables.
- Les dépendances entre livrables sont ambiguës.
- Il faut visualiser les intrants et extrants.
- Il faut organiser une feuille de route de production documentaire.

## Entrées

- Demande utilisateur.
- Extraits, brouillons ou livrables existants, le cas échéant.
- `skills/INDEX.md` et `skills/variantes/INDEX.md` lorsque la sélection ou la comparaison de livrables est nécessaire.
- Références locales pertinentes dans les skills Macroscope.

## Procedure

1. Définir le périmètre de cartographie.
2. Recenser les livrables depuis `skills/INDEX.md`.
3. Identifier intrants, extrants, livrables liés et variantes.
4. Classer les livrables par domaine TOGAF et moment d’utilisation.
5. Produire une table ou un diagramme de dépendances.
6. Signaler les doublons, lacunes et points à confirmer.

## Validation

- La sortie répond au besoin utilisateur sans élargir inutilement le périmètre.
- Les liens avec TOGAF sont explicites lorsque l’architecture est concernée.
- Les hypothèses, limites et points à confirmer sont visibles.
- Les chemins cités existent.
- Les livrables ou variantes recommandés sont justifiés.

## Références internes

Consulter [le guide de la skill](references/GUIDE.md) pour les critères détaillés et les formats recommandés.
