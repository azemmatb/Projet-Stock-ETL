# Système de Gestion de Stock & Valorisation (ETL Python)

## Contexte du Projet
Ce projet simule une problématique réelle de logistique (type Retail/Entrepôt).
L'objectif est d'automatiser le suivi des stocks et la valorisation financière des mouvements, tâches souvent effectuées manuellement sur Excel.

En tant que **Data Engineer**, j'ai construit un pipeline ETL (Extract, Transform, Load) capable de traiter des volumes de données pour produire des rapports financiers fiables.

## Fonctionnalités
Ce script Python automatise les étapes suivantes :
1. **Extraction (Extract) :** Chargement des données brutes (Mouvements de stock & Référentiel produits).
2. **Transformation (Transform) :**
    * Nettoyage et standardisation des données.
    * **Jointure (Merge) :** Réconciliation des mouvements avec les détails produits (prix, catégorie).
    * **Calculs Financiers :** Valorisation automatique des stocks (Quantité x Prix Unitaire).
    * **Agrégation (GroupBy) :** Génération de KPIs par type de produit.
3. **Chargement (Load) :** Export automatique d'un rapport de synthèse (`rapport_finance.csv`) prêt pour l'analyse décisionnelle.

## Stack Technique
* **Langage :** Python 3.x
* **Bibliothèque principale :** Pandas (Data Manipulation)
* **Format de données :** CSV

## Aperçu du Résultat
Le script génère automatiquement un tableau de bord consolidé :

| Produit | Quantité Totale | Valorisation (€) |
| :--- | :---: | :---: |
| Chaise | 8 | 360 € |
| Lampe | 50 | 750 € |
| Table | 5 | 600 € |
| Tapis | 20 | 1200 € |

## Pourquoi ce projet ?
Ce projet démontre ma capacité à :
* Remplacer des processus manuels (VLOOKUP Excel) par du code Python performant.
* Manipuler des DataFrames et réaliser des agrégations complexes.
* Structurer un code propre et maintenable pour l'industrie.
