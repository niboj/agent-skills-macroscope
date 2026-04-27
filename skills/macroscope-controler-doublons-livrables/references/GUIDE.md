# Guide : Contrôler les doublons de livrables

## Intention

Décider si des livrables ou skills doivent être fusionnés, déplacés en variante ou conservés séparément.

## Détail méthodologique

Un doublon exact peut être fusionné. Une variante de contenu doit être conservée dans `skills/variantes/` tant que son apport n’a pas été intégré.

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
