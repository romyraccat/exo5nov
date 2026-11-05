import pandas as pd

# ---------- Chargement des données ----------
train = pd.read_csv("data/HYE_train.tsv", sep="\t")
test_in = pd.read_csv("data/HYE_test.tsv", sep="\t")
test_out = pd.read_csv("data/HYE_test (1).tsv", sep="\t")
tagset = pd.read_csv("data/HYE_tagset.txt", sep="\t", names=["tag", "def"])

# Nettoyage (espaces de fin de certaines étiquettes, fins de ligne)
train["pos"] = train["pos"].str.strip()
train["form"] = train["form"].str.strip()
train["lemma"] = train["lemma"].str.strip()
test_in["pos"] = test_in["pos"].str.strip()
test_in["form"] = test_in["form"].str.strip()
test_out["pos"] = test_out["pos"].str.strip()
test_out["form"] = test_out["form"].str.strip()

# ---------- Q1 : 5 catégories (pos) les plus fréquentes dans le train ----------
print("=== Q1 : 5 pos les plus fréquents dans le train ===")
vc_pos = train["pos"].value_counts()
print(vc_pos.head(5))
print("total mots train :", train.shape[0])

# ---------- Q2 : formes composées (@ dans pos) ----------
print("=== Q2 : formes composées (@ dans pos) ===")
est_compose = train["pos"].str.contains("@")
prop_compose = est_compose.mean()
print("proportion de formes composées :", round(prop_compose, 4), " soit ", int(est_compose.sum()), " mots sur ", train.shape[0])
composes = train[est_compose]
print("5 combinaisons pos les plus fréquentes parmi les formes composées :")
print(composes["pos"].value_counts().head(5))

# ---------- Q3 : article suffixé et préposition з ----------
print("=== Q3 : @PRO+Dem final et lemme en з@ ===")
n_dem = train["pos"].str.endswith("@PRO+Dem").sum()
n_z = train["lemma"].str.startswith("զ@").sum()
print("mots dont le pos finit par @PRO+Dem :", int(n_dem))
print("mots dont le lemma commence par з@ :", int(n_z))

# ---------- Q4 : étiquettes du train absentes du tagset ----------
print("=== Q4 : pos du train hors tagset ===")
valid_tags = tagset["tag"].str.strip().unique()
g = train.groupby("pos").size().reset_index(name="n")
# valide telle quelle si dans le tagset
g["whole_ok"] = g["pos"].isin(valid_tags)
# valide si chaque partie (séparée par @) est dans le tagset
parts_df = g["pos"].str.split("@").explode().reset_index()
parts_df = parts_df.rename(columns={"index": "orig", "pos": "part"})
parts_df["ok"] = parts_df["part"].isin(valid_tags)
s_ok = parts_df.groupby("orig")["ok"].sum()
s_n = parts_df.groupby("orig").size()
g["all_parts_ok"] = s_ok == s_n
g["valid"] = g["whole_ok"] | g["all_parts_ok"]
invalides = g[g["valid"] == False]
print("étiquettes du train absentes du tagset (et leurs effectifs) :")
print(invalides[["pos", "n"]])
print("nombre total de mots concernés :", int(invalides["n"].sum()))

# ---------- Q5 : dictionnaire form -> pos le plus fréquent, évaluation ----------
print("=== Q5 : dictionnaire du train, évaluation sur les deux tests ===")
counts = train.groupby(["form", "pos"]).size().reset_index(name="n")
counts = counts.sort_values("n", ascending=False)
dico = counts.drop_duplicates("form")[["form", "pos"]].rename(columns={"pos": "pos_pred"})
print("formes dans le dictionnaire :", dico.shape[0])


def evaluer(test, nom):
    merged = test.merge(dico, on="form", how="left")
    dans_dico = ~merged["pos_pred"].isna()
    sub = merged[dans_dico]
    acc = (sub["pos_pred"] == sub["pos"]).mean()
    couv = dans_dico.mean()
    print(nom, " : couverture =", round(couv, 4), "(", int(dans_dico.sum()), "/", merged.shape[0], " mots) ; proportion de pos corrects (formes connues) =", round(acc, 4))


evaluer(test_in, "test IN-DOMAIN (HYE_test.tsv)")
evaluer(test_out, "test OUT-OF-DOMAIN (HYE_test (1).tsv)")
