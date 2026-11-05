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

**Les questions :**

1. Quelles sont les 5 catégories (`pos`) les plus fréquentes dans le train ?
2. Quelle proportion des mots du train sont des formes composées (`@` dans `pos`) ? Quelles sont les 5 combinaisons les plus fréquentes ?
3. Combien de mots du train se terminent par l'article suffixé (`pos` qui finit par `@PRO+Dem`) ? Combien commencent par la préposition `զ` (`lemma` qui commence par `զ@`) ?
4. Quelles étiquettes du train **ne figurent pas** dans `HYE_tagset.txt`, et combien de fois chacune apparaît-elle ? Attention à deux pièges :
   - certains noms d'étiquettes du tagset se terminent par une espace ;
   - une étiquette composée est valide si chacune de ses parties l'est.
5. Refaites le **dictionnaire** de la partie 12 du notebook, avec le train arménien. Quel score obtient-il sur le test `in-domain`, puis sur le test `out-of-domain` ? Le score baisse-t-il autant qu'en grec (0,73 contre 0,51) ?
