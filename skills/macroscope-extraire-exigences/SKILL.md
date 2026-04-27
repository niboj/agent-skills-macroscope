---
name: macroscope-extraire-exigences
description: Utiliser ce skill quand il faut extraire exigences, contraintes, règles, décisions, risques ou critères de conformité depuis un texte source et les rattacher aux livrables Macroscope et TOGAF pertinents.
metadata:
  source-method: macroscope
  skill-type: transverse
  togaf-precedence: "true"
---

# Skill: Extraire les exigences Macroscope

## But

Transformer un contenu brut en exigences et éléments de décision traçables.

## Quand utiliser

- Un texte source contient des besoins ou contraintes implicites.
- Il faut alimenter un livrable d’exigences.
- Il faut distinguer exigences, règles, risques et décisions.
- Une traçabilité vers TOGAF est attendue.

## Entrées

- Demande utilisateur.
- Extraits, brouillons ou livrables existants, le cas échéant.
- `skills/INDEX.md` et `skills/variantes/INDEX.md` lorsque la sélection ou la comparaison de livrables est nécessaire.
- Références locales pertinentes dans les skills Macroscope.

## Procedure

1. Lire la source et extraire les énoncés normatifs ou décisionnels.
2. Classer chaque élément : exigence, contrainte, règle, risque, hypothèse ou décision.
3. Reformuler les exigences pour les rendre vérifiables.
4. Associer chaque élément à un livrable Macroscope probable.
5. Associer les éléments aux artefacts TOGAF pertinents.
6. Produire une table de traçabilité.

## Validation

- La sortie répond au besoin utilisateur sans élargir inutilement le périmètre.
- Les liens avec TOGAF sont explicites lorsque l’architecture est concernée.
- Les hypothèses, limites et points à confirmer sont visibles.
- Les chemins cités existent.
- Les livrables ou variantes recommandés sont justifiés.

## Références internes

Consulter [le guide de la skill](references/GUIDE.md) pour les critères détaillés et les formats recommandés.
