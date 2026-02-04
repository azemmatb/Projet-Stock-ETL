import pandas as pd

print("\n-Démarrage du job")

df_produits = pd.read_csv('produits.csv')
df_mouvements = pd.read_csv('mouvements.csv')

print("Aperçu Produits")
print(df_produits.head())

print("Aperçu Mouvements")
print(df_mouvements.head())

print("\n-ÉTAPE 4 : LA FUSION")

df_complet = pd.merge(df_mouvements, df_produits, on='id_prod', how='left')

print(df_complet.head())

print("\n-ÉTAPE 5: CALCULS FINANCIERS")

df_complet['Montant_Total'] = df_complet['quantite'] * df_complet['prix']

print(df_complet[['nom', 'quantite', 'prix', 'Montant_Total']].head())

print("\n-ÉTAPE 6: LE RAPPORT FINAL (GROUPBY)")

df_synthese = df_complet.groupby('nom')[['quantite', 'Montant_Total']].sum()

print("Rapport consolidé par produit:")
print(df_synthese)

print("\n-ÉTAPE 7 : EXPORT (SAUVEGARDE)")

df_synthese.to_csv('rapport_finance.csv')

print("Succès! Le fichier 'rapport_finance.csv' a été créé.")