# Guide : Générer un gabarit de livrable Macroscope

## Intention

Créer un squelette de livrable adapté au contexte et conforme à la référence.

## Détail méthodologique

Le gabarit doit aider la collecte et la rédaction. Les sections non applicables doivent être clairement indiquées plutôt que remplies artificiellement.

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
