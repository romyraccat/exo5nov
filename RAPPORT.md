## 2.
3. Fonctions absentes du notebook (aidé par Vibe) : 
| supprimer les espaces aux extrémités | `s.str.strip()` |
| découper une chaîne | `s.str.split("+")` |
| éclater une liste en plusieurs lignes | `s.explode()` |
| tester le début / la fin d'une chaîne | `s.str.startswith("զ@")`, `s.str.endswith("@PRO+Dem")` |
| compter les effectifs par groupe | `df.groupby(["col1", "col2"]).size()` |
| remettre l'index en colonne | `s.reset_index()` |
| additionner / moyenner une colonne | `s.sum()`, `s.mean()` |
| repérer les valeurs absentes | `s.isna()` |
-- il y avait peut-etre plus ingénueux, dsl...


