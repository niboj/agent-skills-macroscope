---
name: macroscope-consolider-variante-livrable
description: Utiliser ce skill quand il faut analyser une variante dans skills/variantes, décider si elle enrichit la skill canonique, puis fusionner les informations utiles sans créer de doublon actif.
metadata:
  source-method: macroscope
  skill-type: transverse
  togaf-precedence: "true"
---

# Skill: Consolider une variante de livrable

## But

Réduire les variantes tout en conservant l’information utile.

## Quand utiliser

- Une variante semble plus riche que la référence canonique.
- Il faut fusionner des sources multiples.
- Une variante doit être retirée de `skills/variantes/`.
- La référence canonique doit être enrichie.

## Entrées

- Demande utilisateur.
- Extraits, brouillons ou livrables existants, le cas échéant.
- `skills/INDEX.md` et `skills/variantes/INDEX.md` lorsque la sélection ou la comparaison de livrables est nécessaire.
- Références locales pertinentes dans les skills Macroscope.

## Procedure

1. Identifier la skill canonique dans `skills/variantes/INDEX.md`.
2. Comparer la référence canonique et la variante.
3. Extraire uniquement les différences utiles.
4. Ajouter les compléments dans la référence canonique avec traçabilité des sources.
5. Supprimer ou conserver la variante selon la valeur résiduelle.
6. Mettre à jour les index et valider.

## Validation

- La sortie répond au besoin utilisateur sans élargir inutilement le périmètre.
- Les liens avec TOGAF sont explicites lorsque l’architecture est concernée.
- Les hypothèses, limites et points à confirmer sont visibles.
- Les chemins cités existent.
- Les livrables ou variantes recommandés sont justifiés.

## Références internes

Consulter [le guide de la skill](references/GUIDE.md) pour les critères détaillés et les formats recommandés.
