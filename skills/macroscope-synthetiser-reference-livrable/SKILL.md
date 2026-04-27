---
name: macroscope-synthetiser-reference-livrable
description: Utiliser ce skill quand il faut améliorer un fichier references/LIVRABLE.md généré automatiquement pour en faire une synthèse fidèle, claire et plus utile à l’exécution d’une skill Macroscope.
metadata:
  source-method: macroscope
  skill-type: transverse
  togaf-precedence: "true"
---

# Skill: Synthétiser une référence de livrable

## But

Transformer une référence générée en guide d’exécution fiable.

## Quand utiliser

- La référence contient du contenu trop brut.
- Les sections attendues sont mal extraites.
- La synthèse du livrable est absente ou faible.
- Il faut préparer une référence pour usage récurrent.

## Entrées

- Demande utilisateur.
- Extraits, brouillons ou livrables existants, le cas échéant.
- `skills/INDEX.md` et `skills/variantes/INDEX.md` lorsque la sélection ou la comparaison de livrables est nécessaire.
- Références locales pertinentes dans les skills Macroscope.

## Procedure

1. Lire la source Macroscope citée et la référence générée.
2. Identifier la raison d’être, l’occurrence et la structure réelle.
3. Réécrire la synthèse sans ajouter de faits non sourcés.
4. Clarifier les sections, objets, tableaux et points de vigilance.
5. Renforcer le positionnement TOGAF.
6. Valider les chemins et la cohérence avec le SKILL.md.

## Validation

- La sortie répond au besoin utilisateur sans élargir inutilement le périmètre.
- Les liens avec TOGAF sont explicites lorsque l’architecture est concernée.
- Les hypothèses, limites et points à confirmer sont visibles.
- Les chemins cités existent.
- Les livrables ou variantes recommandés sont justifiés.

## Références internes

Consulter [le guide de la skill](references/GUIDE.md) pour les critères détaillés et les formats recommandés.
