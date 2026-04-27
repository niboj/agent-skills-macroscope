---
name: macroscope-reviser-vocabulaire
description: Utiliser ce skill quand il faut normaliser le vocabulaire d’un livrable ou d’une skill Macroscope, notamment les termes TOGAF français/anglais, les rôles, les exigences et les termes interdits localement.
metadata:
  source-method: macroscope
  skill-type: transverse
  togaf-precedence: "true"
---

# Skill: Réviser le vocabulaire Macroscope et TOGAF

## But

Rendre le vocabulaire cohérent, formel et conforme aux conventions du dépôt.

## Quand utiliser

- Un livrable mélange plusieurs vocabulaires.
- Les termes TOGAF doivent être ajoutés ou clarifiés.
- Les rôles ou responsabilités sont mal nommés.
- Il faut vérifier les termes interdits localement.

## Entrées

- Demande utilisateur.
- Extraits, brouillons ou livrables existants, le cas échéant.
- `skills/INDEX.md` et `skills/variantes/INDEX.md` lorsque la sélection ou la comparaison de livrables est nécessaire.
- Références locales pertinentes dans les skills Macroscope.

## Procedure

1. Lire le texte à réviser.
2. Repérer les termes Macroscope, TOGAF et locaux.
3. Remplacer les termes interdits par les termes recommandés.
4. Ajouter le terme anglais TOGAF entre parenthèses lorsque pertinent.
5. Uniformiser les exigences, décisions, risques et contrôles.
6. Fournir la version révisée ou une liste de corrections.

## Validation

- La sortie répond au besoin utilisateur sans élargir inutilement le périmètre.
- Les liens avec TOGAF sont explicites lorsque l’architecture est concernée.
- Les hypothèses, limites et points à confirmer sont visibles.
- Les chemins cités existent.
- Les livrables ou variantes recommandés sont justifiés.

## Références internes

Consulter [le guide de la skill](references/GUIDE.md) pour les critères détaillés et les formats recommandés.
