# Référence du livrable PX000 Livrable a6bd030d17f8

## Source analysée

- Fichier source : `../../../macroscope/livrables/a6bd030d17f8.md`
- Méthode source : Macroscope
- Extraction du titre : fallback fichier

## Synthèse du livrable

Un participant est un type d'objets physiques ou abstraits. Le type est défini en fonction d'un ensemble de relations MDP, de règles MDP et d'attributs. Les participants représentent des types d'objets. En tant que type d'objets, un participant peut avoir un ensemble spécifique de types d'attributs (par exemple, le participant «Commande du client» peut présenter des types d'attributs tels que «date de la commande», «quantité commandée» et «instructions de livraison»). Un participant peut également se caractériser par un domaine d'états possibles du participant (par exemple, la «Commande du client» peut être dans un des états suivants à n'importe quel moment donné : «initiale», «saisie» ou «acceptée»). Un état du participant est une instance d'un participant et se définit par un ensemble de valeurs pour des attributs associés au participant. Par exemple, la «Commande du client» peut être dans un des états suivants à n'importe quel moment donné : «initiale», «saisie» ou «acceptée». Les états individuels sont déterminés par la valeur des attributs. Par exemple, «Commande du client - (saisie)» exige que l'attribut «date de commande» soit assigné et «Commande du client - (acceptée)» exige que l'attribut «instructions de livraison» soit assigné. Un «participant-en-état» est un sous-ensemble composé de toutes les instances de tous les états que l'objet peut présenter. Par exemple, la «Commande du client (passée)» est un sous-ensemble de l'ensemble des Commandes des clients (c'est-à-dire de toutes les commandes des clients peu importe leur état). Bien que les instances d'un participant puissent changer d'état, le type d'objets ne change pas. En d'autres termes, la Commande du client en tant que telle ne change pas; il s'agit toujours de la même commande, mais à laquelle des détails ont été ajoutés au cours de ses passages d'un état à un autre.

## Raison d’être

Aucune raison d’être explicite n’a été extraite. Déduire l’intention du livrable à partir de sa description, de son contenu et des livrables liés.

## Occurrence

Aucune occurrence explicite n’a été extraite du fichier source.

## Structure détaillée du livrable

1. Synthese
2. Portee
3. Contenu du livrable
4. Decisions et points ouverts
5. Tracabilite TOGAF

## Champs ou sections attendus

- Aucune information explicite extraite du fichier source.

## Objets documentés

- Le type est défini en fonction d'un ensemble de relations MDP, de règles MDP et d'attributs.

## Tableaux, modèles ou diagrammes recommandés

- Aucune information explicite extraite du fichier source.

## Livrables et références liés

- Aucune information explicite extraite du fichier source.

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase B - Architecture métier (Business Architecture).
- Livrable TOGAF cible : Document de définition d’architecture (Architecture Definition Document).
- Domaine d’architecture principal : architecture métier.
- Artefacts associés : Service d’affaires (Business Service), Processus métier, Acteur ou rôle métier.

## Règles particulières de rédaction

- Présenter PX000 Livrable a6bd030d17f8 comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
- Ne jamais faire primer Macroscope sur TOGAF.
- Documenter les hypothèses et les points à confirmer lorsque la source utilisateur est incomplète.
- Relier les éléments du livrable aux exigences, décisions, vues, composants et risques pertinents.
- Utiliser le terme conseiller en architecture pour désigner la contribution d’architecture.

## Exemples utiles ou indications extraites

- En tant que type d'objets, un participant peut avoir un ensemble spécifique de types d'attributs (par exemple, le participant «Commande du client» peut présenter des types d'attributs tels que «date de la commande», «quantité commandée» et «instructions de liv
- Un participant peut également se caractériser par un domaine d'états possibles du participant (par exemple, la «Commande du client» peut être dans un des états suivants à n'importe quel moment donné : «initiale», «saisie» ou «acceptée»).
- Par exemple, la «Commande du client» peut être dans un des états suivants à n'importe quel moment donné : «initiale», «saisie» ou «acceptée».
- Par exemple, «Commande du client - (saisie)» exige que l'attribut «date de commande» soit assigné et «Commande du client - (acceptée)» exige que l'attribut «instructions de livraison» soit assigné.
- Par exemple, la «Commande du client (passée)» est un sous-ensemble de l'ensemble des Commandes des clients (c'est-à-dire de toutes les commandes des clients peu importe leur état).
- Ainsi, dans l'exemple «Commande du client», les états de la «Commande du client» seront représentés par trois participants portant les descriptions suivantes : «Commande du client (initiale)», «Commande du client (saisie)» et «Commande du client (acceptée)».
- La description doit être un substantif au singulier, par exemple : personnel de distribution; commande du client; inventaire régional.

## Points de vigilance

- Vérifier que le livrable répond au besoin utilisateur plutôt qu’à une reproduction mécanique du gabarit.
- Éviter les doublons avec les autres livrables Macroscope liés.
- Ne pas transformer une annexe détaillée en décision d’architecture principale.
- Signaler les sections non applicables au lieu de les remplir artificiellement.
- Conserver la traçabilité entre sources, exigences, décisions et artefacts TOGAF.

## Extraits de contexte Macroscope

### Description

Un participant est un type d'objets physiques ou abstraits. Le type est défini en fonction d'un ensemble de relations MDP, de règles MDP et d'attributs. Les participants représentent des types d'objets. En tant que type d'objets, un participant peut avoir un ensemble spécifique de types d'attributs (par exemple, le participant «Commande du client» peut présenter des types d'attributs tels que «date de la commande», «quantité commandée» et «instructions de livraison»). Un participant peut également se caractériser par un domaine d'états possibles du participant (par exemple, la «Commande du client» peut être dans un des états suivants à n'importe quel moment donné : «initiale», «saisie» ou «acceptée»). Un état du participant est une instance d'un participant et se définit par un ensemble de valeurs pour des attributs associés au participant. Par exemple, la «Commande du client» peut être dans un des états suivants à n'importe quel moment donné : «initiale», «saisie» ou «acceptée». Les états individuels sont déterminés par la valeur des attributs. Par exemple, «Commande du client - (saisie)» exige que l'attribut «date de commande» soit assigné et «Commande du client - (acceptée)» exige que l'attribut «instructions de livraison» soit assigné. Un «participant-en-état» est un sous-ensemble composé de toutes les instances de tous les états que l'objet peut présenter. Par exemple, la «Commande du client (passée)» est un sous-ensemble de l'ensemble des Commandes des clients (c'est-à-dire de toutes les commandes des clients peu importe leur état). Bien que les instances d'un participant puissent changer d'état, le type d'objets ne change pas. En d'autres termes, la Commande du client en tant que telle ne change pas; il s'agit toujours de la même commande, mais à laquelle des détails ont été ajoutés au cours de ses passages d'un état à un autre.

### Intrants

Non disponible.

### Extrants

Non disponible.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

Non disponible.
