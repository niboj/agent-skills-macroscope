# Guide : Cartographier les livrables Macroscope

## Intention

Comprendre et documenter les dépendances entre livrables Macroscope.

## Détail méthodologique

La cartographie doit faciliter la planification et la gouvernance documentaire. Elle doit indiquer les dépendances utiles, pas toutes les références possibles.

## Format de sortie recommandé

```markdown
# Résultat

## Synthèse
## Analyse
## Recommandation ou contenu produit
## Liens TOGAF
## Hypothèses et points à confirmer
## Références consultées
```

Adapter le format à la demande. Pour une sortie courte, conserver seulement les sections utiles.

## Contrôles spécifiques

- Vérifier la cohérence avec `AGENTS.MD`.
- Vérifier si une skill canonique existe déjà avant de créer ou recommander une nouvelle skill.
- Utiliser `skills/variantes/` pour les variantes de contenu non canoniques.
- Ne pas modifier `macroscope/livrables/` sauf demande explicite.
- Préserver la préséance TOGAF sur Macroscope.

## Sources utiles

- `AGENTS.MD`
- `skills/INDEX.md`
- `skills/variantes/INDEX.md`
- `macroscope/livrables/`
