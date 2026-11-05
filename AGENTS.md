# Mini-analyste pandas : arménien classique (HYE)

<!-- TODO : en une phrase, l'objectif du projet. -->

Répondre aux questions sur le corpus arménien HYE, uniquement en écrivant puis en lançant scripts/analyser.py avec pandas.


## Règles
<!-- TODO : 3 ou 4 règles, une par ligne. Pensez à :
     - comment lancer Python ;
     - d'où doivent venir les chiffres ;
     - ce que l'agent n'a pas le droit de lire. -->
     
- Python se lance uniquement par `uv run python scripts/analyser.py`.
- Tout chiffre rapporté provient de la sortie du script sur les fichiers de `data/`, jamais d'une autre source.
- Interdit de lire : `consignes.md`, `RAPPORT.md`, `.env` et tout fichier hors de `data/` et `scripts/`.
- Pas de boucle `for` sur les lignes : uniquement des opérations pandas sur des colonnes entières, limitées aux fonctions de la skill `pandas-tuto`.

## Rôles
<!-- TODO : quel agent fait quoi. -->

- - `analyste` : écrit `scripts/analyser.py`, le lance avec `uv run python scripts/analyser.py`, rapporte sa sortie. Rien d'autre.

## Repères
- Données : `data/HYE_train.tsv`, `data/HYE_test_in-domain.tsv`, `data/HYE_test_out-of-domain.tsv`, colonnes `text_form form lemma pos`.
- Tagset : `data/HYE_tagset.txt` (étiquette, tabulation, définition).
