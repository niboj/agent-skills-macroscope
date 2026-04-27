---
name: macroscope-generer-gabarit-livrable
description: Utiliser ce skill quand il faut produire un gabarit Markdown prêt à remplir pour un livrable Macroscope, avec sections, tableaux, contrôles qualité et emplacement des liens TOGAF.
metadata:
  source-method: macroscope
  skill-type: transverse
  togaf-precedence: "true"
---

# Skill: Générer un gabarit de livrable Macroscope

## But

Créer un squelette de livrable adapté au contexte et conforme à la référence.

## Quand utiliser

- L’utilisateur demande un modèle ou un canevas.
- Le contenu source n’est pas encore disponible.
- Il faut préparer un atelier de collecte.
- Il faut standardiser une structure de livrable.

## Entrées

- Demande utilisateur.
- Extraits, brouillons ou livrables existants, le cas échéant.
- `skills/INDEX.md` et `skills/variantes/INDEX.md` lorsque la sélection ou la comparaison de livrables est nécessaire.
- Références locales pertinentes dans les skills Macroscope.

## Procedure

1. Identifier le livrable cible.
2. Charger sa référence détaillée.
3. Sélectionner les sections applicables.
4. Ajouter les tableaux ou matrices attendus.
5. Inclure les champs d’hypothèses, décisions, points à confirmer et liens TOGAF.
6. Fournir le gabarit Markdown sans remplir les informations inconnues.

## Validation

- La sortie répond au besoin utilisateur sans élargir inutilement le périmètre.
- Les liens avec TOGAF sont explicites lorsque l’architecture est concernée.
- Les hypothèses, limites et points à confirmer sont visibles.
- Les chemins cités existent.
- Les livrables ou variantes recommandés sont justifiés.

## Références internes

Consulter [le guide de la skill](references/GUIDE.md) pour les critères détaillés et les formats recommandés.
