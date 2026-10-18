**# Retail Sales Forecasting and Customer Analytics**



\*\*MSc Computer Science (Conversion) — Project Artefact\*\*



\## **1. Project Overview**



This project develops a retail analytics solution using the Brazilian E-Commerce Public Dataset by Olist. It combines data preparation, exploratory data analysis, customer segmentation, sales forecasting, relational database management and interactive business intelligence visualisation.



The main objective is to demonstrate how historical retail data can support business analysis and decision-making.



\## **2. Software Requirements**



\- Python 3 with Jupyter Notebook or Visual Studio Code

\- Python libraries: pandas, numpy, matplotlib, seaborn, scikit-learn, statsmodels and openpyxl

\- SQLite 3

\- Microsoft Power BI Desktop

\- Microsoft Word and PowerPoint for supporting documentation



Python libraries and their versions should be checked against the notebook imports before execution.



\## **3. Project Folder Structure**



\- \*\*01\_Raw\_Data:\*\* Nine original Olist CSV datasets.

\- \*\*02\_Cleaned\_Data:\*\* Prepared datasets, customer segmentation results and weekly sales forecasts.

\- \*\*03\_SQL:\*\* SQL scripts, Python database-loading and validation scripts, and the SQLite database.

\- \*\*04\_Python\_Analysis:\*\* Five Jupyter notebooks covering data inspection, cleaning, exploratory analysis, customer segmentation and sales forecasting.

\- \*\*05\_PowerBI:\*\* Interactive Power BI dashboard.

\- \*\*06\_Design:\*\* Dashboard design documentation and wireframes.

\- \*\*07\_Testing:\*\* Functional testing results and supporting screenshots.

\- \*\*08\_Report\_Evidence:\*\* Screenshots of SQL implementation, validation and customer segmentation results.

\- \*\*09\_Project\_Management:\*\* Project progress tracker.



\## **4. Opening the Artefact**



\*\*Power BI Dashboard\*\*



Open `05\_PowerBI/Retail\_Sales\_Analytics\_Dashboard.pbix` using Microsoft Power BI Desktop.



The dashboard contains four pages:



1\. Executive Overview

2\. Sales Analysis

3\. Customer Analytics

4\. Sales Forecasting



The dashboard uses prepared transaction, customer segmentation and forecasting data. Interactive filters allow users to explore the analytical results.



\*\*Python Analysis\*\*



Open the notebooks in `04\_Python\_Analysis` using Jupyter Notebook or Visual Studio Code.



The notebooks are numbered in the intended analytical order:



1\. `01\_Data\_Inspection.ipynb`

2\. `02\_Data\_Cleaning.ipynb`

3\. `03\_Exploratory\_Data\_Analysis.ipynb`

4\. `04\_Customer\_Segmentation.ipynb`

5\. `05\_Sales\_Forecasting.ipynb`



The required datasets are located in `01\_Raw\_Data` and `02\_Cleaned\_Data`. File paths may need adjustment if the project is extracted to a different directory.



\*\*SQLite Database\*\*



The `03\_SQL` folder contains `retail\_analytics.db`, together with SQL scripts for database setup, validation and analysis and Python scripts for data loading and validation.



The database can be examined using a SQLite-compatible application or Python's built-in sqlite3 library.



\## **5. Main Analytical Results**



The prepared transaction dataset contains 96,478 delivered orders and approximately R$13.22 million in product sales, excluding freight.



Customer segmentation identified four groups using purchasing recency, monetary value and purchased item count.



Five weekly sales forecasting methods were compared. Holt's linear trend achieved the lowest test error, with MAE of R$36,708.38 and MAPE of 19.77%. The selected method was used to produce a 12-week sales forecast.



\## **6. Testing and Evaluation**



Five functional Power BI tests were completed to validate selected calculations, filtering behaviour, customer segmentation results and forecasting visualisations.



Testing documentation and screenshots are available in `07\_Testing`.



The solution was developed as a local analytical prototype. Its limitations include historical data coverage, limited repeat-purchase behaviour and the absence of formal business-user testing.



\## **7. Data Source and Privacy**



The project uses the Brazilian E-Commerce Public Dataset by Olist, available through Kaggle.



The dataset contains historical, anonymised e-commerce information. No additional personal customer information was collected for this project.



\## **8. Project Scope**



The artefact demonstrates a complete retail analytics workflow, from raw data preparation to interactive visualisation.



It is intended for academic demonstration and has not been deployed as a live commercial system.

