---
name: macroscope-reviser-conformite-livrable
description: Utiliser ce skill quand il faut contrôler un livrable Macroscope existant selon sa structure attendue, sa complétude, sa traçabilité, son vocabulaire et son alignement TOGAF.
metadata:
  source-method: macroscope
  skill-type: transverse
  togaf-precedence: "true"
---

# Skill: Réviser la conformité d’un livrable Macroscope

## But

Évaluer un livrable et fournir des corrections concrètes.

## Quand utiliser

- Un brouillon de livrable doit être révisé.
- Il faut vérifier la conformité à une référence Macroscope.
- Il faut préparer une revue formelle.
- Il faut détecter les sections manquantes ou faibles.

## Entrées

- Demande utilisateur.
- Extraits, brouillons ou livrables existants, le cas échéant.
- `skills/INDEX.md` et `skills/variantes/INDEX.md` lorsque la sélection ou la comparaison de livrables est nécessaire.
- Références locales pertinentes dans les skills Macroscope.

## Procedure

1. Identifier le livrable et charger sa référence canonique.
2. Comparer le brouillon à la structure attendue.
3. Vérifier la portée, les exigences, décisions, risques et liens TOGAF.
4. Repérer les omissions, incohérences, doublons et affirmations non sourcées.
5. Classer les constats par gravité ou priorité.
6. Proposer des corrections directement exploitables.

## Validation

- La sortie répond au besoin utilisateur sans élargir inutilement le périmètre.
- Les liens avec TOGAF sont explicites lorsque l’architecture est concernée.
- Les hypothèses, limites et points à confirmer sont visibles.
- Les chemins cités existent.
- Les livrables ou variantes recommandés sont justifiés.

## Références internes

Consulter [le guide de la skill](references/GUIDE.md) pour les critères détaillés et les formats recommandés.
