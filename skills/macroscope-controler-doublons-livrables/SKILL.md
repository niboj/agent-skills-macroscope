---
name: macroscope-controler-doublons-livrables
description: Utiliser ce skill quand il faut détecter, analyser et recommander une action sur les doublons entre skills, variantes, références ou livrables Macroscope.
metadata:
  source-method: macroscope
  skill-type: transverse
  togaf-precedence: "true"
---

# Skill: Contrôler les doublons de livrables

## But

Décider si des livrables ou skills doivent être fusionnés, déplacés en variante ou conservés séparément.

## Quand utiliser

- Plusieurs skills portent le même code et nom.
- Des références semblent identiques.
- Une variante doit être évaluée.
- Il faut nettoyer l’index des skills.

## Entrées

- Demande utilisateur.
- Extraits, brouillons ou livrables existants, le cas échéant.
- `skills/INDEX.md` et `skills/variantes/INDEX.md` lorsque la sélection ou la comparaison de livrables est nécessaire.
- Références locales pertinentes dans les skills Macroscope.

## Procedure

1. Comparer les couples code et nom dans `skills/INDEX.md`.
2. Comparer les références en neutralisant les lignes de source.
3. Classer les cas : doublon exact, variante utile ou collision de nom.
4. Recommander fusion, déplacement en variante ou conservation.
5. Mettre à jour les index si une action est appliquée.
6. Valider les skills actives et les variantes.

## Validation

- La sortie répond au besoin utilisateur sans élargir inutilement le périmètre.
- Les liens avec TOGAF sont explicites lorsque l’architecture est concernée.
- Les hypothèses, limites et points à confirmer sont visibles.
- Les chemins cités existent.
- Les livrables ou variantes recommandés sont justifiés.

## Références internes

Consulter [le guide de la skill](references/GUIDE.md) pour les critères détaillés et les formats recommandés.
