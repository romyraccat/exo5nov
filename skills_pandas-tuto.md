---
name: pandas-tuto
description: Charger avant d'écrire scripts/analyser.py, liste des fonctions pandas autorisées pour l'analyse du corpus HYE.
---

Seules les fonctions pandas ci-dessous sont autorisées. On travaille sur des colonnes
entières : pas de boucle `for` sur les lignes d'un tableau.

| Je veux… | pandas |
|---|---|
| lire un TSV | `pd.read_csv(chemin, sep="\t")` |
| voir le début, la fin | `df.head()`, `df.tail()` |
| connaître la taille, les colonnes | `df.shape`, `df.columns`, `df.info()` |
| un résumé | `df.describe()` |
| une colonne, plusieurs colonnes | `df["col"]`, `df[["col1", "col2"]]` |
| compter les valeurs | `df["col"].value_counts()`, `.nunique()`, `.unique()` |
| filtrer des lignes | `df[df["col"] == valeur]`, `df[(condition1) & (condition2)]` |
| ajouter une colonne | `df["nouvelle"] = ...`, `.str.len()`, `.str.contains("@")` |
| trier | `df.sort_values("col", ascending=False)` |
| calculer par groupe | `df.groupby("col")["autre"].mean()` |
| réunir plusieurs tableaux | `pd.concat(liste_de_tableaux, ignore_index=True)` |
| tableau croisé | `pd.crosstab(df["col1"], df["col2"])` |
| tester l'appartenance | `df["col"].isin(autre_liste)` |
| associer deux tableaux | `df.merge(autre, on="col", how="left")` |
| renommer, dédoublonner | `df.rename(columns={"a": "b"})`, `df.drop_duplicates("col")` |
| enregistrer | `df.to_csv("fichier.csv", index=False)`  |
| supprimer les espaces aux extrémités | `s.str.strip()` |
| découper une chaîne | `s.str.split("+")`|
| éclater une liste en plusieurs lignes | `s.explode()` |
| tester le début / la fin d'une chaîne | `s.str.startswith("զ@")`, `s.str.endswith("@PRO+Dem")` |
| compter les effectifs par groupe | `df.groupby(["col1", "col2"]).size()` |
| remettre l'index en colonne | `s.reset_index()` |
| additionner / moyenner une colonne | `s.sum()`, `s.mean()` |
| repérer les valeurs absentes | `s.isna()` |
