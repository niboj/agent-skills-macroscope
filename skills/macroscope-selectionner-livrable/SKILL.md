---
name: macroscope-selectionner-livrable
description: Utiliser ce skill quand il faut choisir le bon livrable Macroscope à partir d’un besoin vague, d’un code incomplet, d’un objectif utilisateur, d’un domaine TOGAF ou d’un extrait de demande.
metadata:
  source-method: macroscope
  skill-type: transverse
  togaf-precedence: "true"
---

# Skill: Sélectionner un livrable Macroscope

## But

Identifier la skill Macroscope canonique la plus pertinente et expliquer le choix sans multiplier inutilement les livrables.

## Quand utiliser

- La demande ne nomme pas clairement le livrable.
- Le code du livrable est incomplet ou ambigu.
- Plusieurs livrables semblent possibles.
- Il faut orienter l’utilisateur vers une skill canonique ou une variante.

## Entrées

- Demande utilisateur.
- Extraits, brouillons ou livrables existants, le cas échéant.
- `skills/INDEX.md` et `skills/variantes/INDEX.md` lorsque la sélection ou la comparaison de livrables est nécessaire.
- Références locales pertinentes dans les skills Macroscope.

## Procedure

1. Extraire les mots-clés, codes, domaines et objectifs de la demande.
2. Consulter `skills/INDEX.md` pour repérer les livrables candidats.
3. Comparer les candidats selon l’objectif, les intrants et le domaine TOGAF.
4. Consulter `skills/variantes/INDEX.md` seulement si une variante peut changer l’interprétation.
5. Recommander un livrable principal et, au besoin, des livrables liés.
6. Expliquer les raisons du choix et les informations à confirmer.

## Validation

- La sortie répond au besoin utilisateur sans élargir inutilement le périmètre.
- Les liens avec TOGAF sont explicites lorsque l’architecture est concernée.
- Les hypothèses, limites et points à confirmer sont visibles.
- Les chemins cités existent.
- Les livrables ou variantes recommandés sont justifiés.

## Références internes

Consulter [le guide de la skill](references/GUIDE.md) pour les critères détaillés et les formats recommandés.
