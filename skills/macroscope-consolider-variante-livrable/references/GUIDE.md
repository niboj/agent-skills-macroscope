# Guide : Consolider une variante de livrable

## Intention

Réduire les variantes tout en conservant l’information utile.

## Détail méthodologique

Ne fusionner que les informations appuyées par les sources. Une variante peut rester archivée si son contexte diffère réellement.

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
