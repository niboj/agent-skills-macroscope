---
name: macroscope-generer-diagrammes
description: Utiliser ce skill quand il faut recommander ou produire les diagrammes utiles à un livrable Macroscope : processus, données, composants, déploiement, séquence, états, matrices ou vues TOGAF.
metadata:
  source-method: macroscope
  skill-type: transverse
  togaf-precedence: "true"
---

# Skill: Générer les diagrammes pertinents

## But

Choisir et produire des représentations visuelles adaptées au livrable et à la décision à soutenir.

## Quand utiliser

- Un livrable demande un diagramme ou modèle.
- La structure textuelle ne suffit pas.
- Il faut choisir entre plusieurs notations.
- Une vue TOGAF doit être illustrée.

## Entrées

- Demande utilisateur.
- Extraits, brouillons ou livrables existants, le cas échéant.
- `skills/INDEX.md` et `skills/variantes/INDEX.md` lorsque la sélection ou la comparaison de livrables est nécessaire.
- Références locales pertinentes dans les skills Macroscope.

## Procedure

1. Identifier le livrable et le type d’information à représenter.
2. Choisir la notation pertinente : processus, données, composants, déploiement, séquence ou états.
3. Définir les éléments, relations et limites du diagramme.
4. Produire le diagramme en Markdown, Mermaid ou description textuelle selon le contexte.
5. Ajouter les hypothèses et points à confirmer.
6. Vérifier la cohérence avec la référence du livrable.

## Validation

- La sortie répond au besoin utilisateur sans élargir inutilement le périmètre.
- Les liens avec TOGAF sont explicites lorsque l’architecture est concernée.
- Les hypothèses, limites et points à confirmer sont visibles.
- Les chemins cités existent.
- Les livrables ou variantes recommandés sont justifiés.

## Références internes

Consulter [le guide de la skill](references/GUIDE.md) pour les critères détaillés et les formats recommandés.
