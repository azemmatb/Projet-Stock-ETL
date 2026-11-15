# Stock Management & Valuation (Python ETL)

## Project context
This project simulates a real logistics problem (retail / warehouse).
The goal is to automate stock tracking and the financial valuation of stock movements, tasks that are often done by hand in Excel.

I built an ETL pipeline (Extract, Transform, Load) that processes the data and produces reliable financial reports.

## Features
The Python script automates the following steps:
1. **Extract:** loading the raw data (stock movements and product master data).
2. **Transform:**
    * data cleansing and standardisation;
    * **merge:** reconciling movements with product details (price, category);
    * **financial calculations:** automatic stock valuation (quantity × unit price);
    * **aggregation (`groupby`):** KPIs per product type.
3. **Load:** automatic export of a summary report (`rapport_finance.csv`) ready for analysis.

## Tech stack
* **Language:** Python 3.x
* **Main library:** pandas
* **Data format:** CSV

## Result
The script automatically generates a consolidated summary:

| Product | Total quantity | Valuation (€) |
| :--- | :---: | :---: |
| Chair | 8 | €360 |
| Lamp | 50 | €750 |
| Table | 5 | €600 |
| Rug | 20 | €1,200 |

## What this project shows
* Replacing manual processes (Excel VLOOKUP) with efficient Python code.
* Working with DataFrames and performing aggregations.
* Writing clean, maintainable code.
