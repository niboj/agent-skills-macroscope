---
name: macroscope-aligner-togaf
description: Utiliser ce skill quand il faut positionner un livrable Macroscope dans TOGAF, identifier la phase ADM, le livrable TOGAF cible, les artefacts associés et les limites d’architecture.
metadata:
  source-method: macroscope
  skill-type: transverse
  togaf-precedence: "true"
---

# Skill: Aligner un livrable Macroscope sur TOGAF

## But

Établir une correspondance explicite entre un livrable Macroscope et TOGAF.

## Quand utiliser

- Le livrable doit être intégré à une architecture de service.
- La phase ADM ou le domaine TOGAF est incertain.
- Il faut éviter de confondre conception détaillée et architecture.
- Une matrice Macroscope-TOGAF est demandée.

## Entrées

- Demande utilisateur.
- Extraits, brouillons ou livrables existants, le cas échéant.
- `skills/INDEX.md` et `skills/variantes/INDEX.md` lorsque la sélection ou la comparaison de livrables est nécessaire.
- Références locales pertinentes dans les skills Macroscope.

## Procedure

1. Identifier le livrable Macroscope et son intention.
2. Classer le domaine : métier, données, applicatif, technologique, sécurité, migration, gouvernance ou exploitation.
3. Associer la phase ADM pertinente.
4. Associer les livrables et artefacts TOGAF.
5. Définir ce qui relève de l’architecture et ce qui relève d’une annexe détaillée.
6. Formuler les liens TOGAF à inclure dans la sortie.

## Validation

- La sortie répond au besoin utilisateur sans élargir inutilement le périmètre.
- Les liens avec TOGAF sont explicites lorsque l’architecture est concernée.
- Les hypothèses, limites et points à confirmer sont visibles.
- Les chemins cités existent.
- Les livrables ou variantes recommandés sont justifiés.

## Références internes

Consulter [le guide de la skill](references/GUIDE.md) pour les critères détaillés et les formats recommandés.
