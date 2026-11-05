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

**Consigne Vibe :**

Tu doit créer et écrire, dans le fichier "scripts/analyser.py" les réponses aux 5 questions, que tu trouves dans le fichier RAPPORT.md, ne modifie pas le fichier RAPPORT.md, utilise le sous-agent analyste et le skill pandas-tuto.

**Résultats :**

 Réponses aux 5 questions (sortie de uv run python scripts/analyser.py, train = 4 712 mots) :
                                                                                                                                                                             ┌────────────────────────────────────────────────────────────┬──────────────────────────────────────────────────────────────────────────────────────────────────────────────
  │ Question                                                   │ Réponse ├────────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────
  │ Q1 — 5 pos les plus fréquents du train                     │ V = 1008, N+Com = 786, I+Conj = 745, I+Prep = 310, A = 295 ├────────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────
  │ Q2 — formes composées (@ dans pos)                         │ 669/4712 = 0,142 ; top 5 : N+Com@PRO+Dem = 166, I+Prep@N+Com = 164, I+Prep@N+Com@PRO+Dem = 76, A@PRO+Dem =
  │                                                            │ 41, I+Prep@PRO+Dem = 37   ├────────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────
  │ Q3 — pos finissant par @PRO+Dem / lemma commençant par զ@  │ 383 mots / 339 mots                                                                                       ├────────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────
  │ Q4 — étiquettes du train absentes du tagset                │ une seule : PRO+Pos3, 10 occurrences (10 mots)  ├────────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────
  │ Q5 — dictionnaire form→pos le plus fréquent (2 014 formes) │ in-domain (HYE_test.tsv) : couverture 0,5767 (173/300), pos corrects 0,9827 ; out-of-domain (HYE_test
  │                                                            │ (1).tsv) : couverture 0,535 (168/314), pos corrects 0,9702 └────────────────────────────────────────────────────────────┴────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
  Pour Q5, la baisse est minime (0,98 → 0,97), très loin de la chute observée en grec (0,73 → 0,51) : le score ne baisse pas autant. Le mapping retenu pour les deux fichiers de test — HYE_test.tsv = in-domain, HYE_test (1).tsv = out-of-domain — est cohérent avec la couverture légèrement supérieure du premier (0,577 contre 0,535).
  
  
 **erreur de l'agent :**
 
 aucune, tout est #parfait (c'était un peu long, je ne sais pas a quel point c'est efficace / il y a sans doute une erreur que je n'ai su voir)
 
 **ce qu'apporte l'agent :**
 
L'agent permet de déléguer l'écriture d'un long script avec l'utilisation de chaque fonction a la main. Il est également reproductible (avec d'autres questions si nécessaire). Il coute : du temps (le fait de mettre en place la structure agentique), de l'argent (le cout des 61.4K tokens utilisés), j'imagine donc aussi un bilan carbone non-négligeable / cout écologique ?


