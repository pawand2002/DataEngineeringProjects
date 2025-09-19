# 🛍️ Retail Sales Analytics on Azure

An end-to-end Retail Sales Analytics project built on Azure, showcasing modern data engineering practices using Python, Azure Data Factory (ADF), Azure Data Lake Storage Gen2, Azure Synapse Analytics, and Power BI. 

This project demonstrates how raw retail sales data can be ingested, transformed, analyzed, and visualized using a scalable cloud-based architecture.

---
#  🏗 Architecture Diagram

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/a6ae0b40-b918-491c-82f5-fa710b08482f" />


# 🚀 Project Architecture

```mermaid
graph TD
    A[Python Script] --> B[Azure Data Factory]
    B --> C[Azure Data Lake - Bronze/Silver/Gold]
    C --> D[Azure Synapse Analytics]
    D --> E[Power BI Reports]
```

# 🧰 Tech Stack
| Layer | Technology |
|-------|--------------|
| Data Source | Synthetic data via Python | 
| Storage | Azure Data Lake Storage Gen2 (ADLS) | 
| Orchestration | Azure Data Factory (ADF) | 
| Modeling | Azure Synapse Analytics | 
| Visualization | Power BI | 



# 🗂️ Dataset Overview
- Generator Script: generate_sales_data.py
- Format: CSV + optional Parquet
- Fields: TransactionID, CustomerID, ProductID, Quantity, Price, TransactionDate, Region
- Scope: ~6 months of synthetic retail activity across regions and products

# 🎯 Core Objectives
- Build reusable ETL flows using ADF pipelines
- Ingest and transform zone-based data in ADLS Gen2
- Apply Kimball-style dimensional modeling via Synapse Serverless SQL
- Create dynamic Power BI dashboards for sales insights
- Explore parameterized views, SCD types, and semantic layers

# 📈 Business Use Case
Objective: Analyze retail sales data to uncover trends, high-performing regions/products, and forecast revenue.

Data Source: Retail transactions CSV file (uploaded manually or automated).

Users: Business analysts, operations teams, and sales managers.

# Layers Explained:

* **Bronze Layer (Raw Data Lake):** Stores raw, immutable sales data as ingested from the source (CSV). This layer acts as a landing zone.
* **Silver Layer (Cleaned & Conformed Data Lake):** Data from the Bronze layer is cleaned, validated, and transformed into a structured, conformed format (Parquet). This layer is ready for further aggregation and feature engineering.
* **Gold Layer (Business-Ready Data Lake):** Aggregated and highly optimized data (Parquet) for direct consumption by business intelligence tools and analytical applications. This layer contains key business metrics like daily total sales, unique customers, and transaction counts.

## Azure Services Used

* **Azure Data Lake Storage Gen2 (ADLS Gen2):** Scalable and secure data lake for storing data in various formats across all layers (Bronze, Silver, Gold).
* **Azure Data Factory (ADF):** Cloud-based ETL/ELT service used for orchestrating the data movement and performing complex data transformations via Mapping Data Flows.
* **Azure Synapse Analytics (Serverless SQL Pool):** Provides a SQL interface over the data in ADLS Gen2, enabling ad-hoc querying and creating logical views (Gold Layer) without provisioning dedicated resources.
* **Power BI:** Business intelligence tool for creating interactive dashboards and reports, consuming data directly from the Synapse Serverless SQL Pool view (DirectQuery).

## Key Learnings & Demonstrated Skills

This project was a hands-on exercise in transitioning to modern cloud data platforms, specifically on Azure. It highlights my ability to:

* **Architect Cloud-Native Data Solutions:** Designed and implemented a robust Medallion Architecture, a best practice for data lakes.
* **Master Modern ETL/ELT:** Gained in-depth proficiency in Azure Data Factory's Data Flows for complex data transformations and pipeline orchestration.
* **Leverage Data Lakehouse Capabilities:** Successfully integrated ADLS Gen2 with Azure Synapse Analytics to provide a flexible and performant analytical layer directly on the data lake.
* **Ensure Data Quality & Integrity:** Implemented data cleaning and aggregation steps to deliver high-quality, business-ready data.
* **Integrate BI Tools:** Connected Power BI to a Synapse view using DirectQuery, showcasing real-time analytical capabilities.
* **Problem-Solving & Debugging:** Successfully navigated and resolved complex data type inference, authentication, and pathing challenges across different Azure services.
* **Multi-Cloud Versatility:** This project complements my existing expertise in GCP, demonstrating my adaptability and capability to design and implement robust data solutions across major cloud platforms. It showcases my commitment to continuous learning and expanding my cloud data engineering skillset.


## 🔄 Data Flow Pipeline
#  Ingestion: 
Python scripts upload raw .csv files to Azure Data Lake (Bronze layer).

# Orchestration via ADF triggers.

# Transformation:

ADF Mapping Data Flows process and clean data from Bronze → Silver → Gold layers.

Derived columns such as TotalSales,UniqueCustomersCounts, TotalTransactions.

# Modeling:

Data from Gold layer is loaded into Azure Synapse for analytics modeling.

Views and aggregations created for Power BI consumption.

# Reporting:

Power BI dashboards built to display KPIs like Total Sales, Profit Margin, Regional Revenue, and Product Category Trends.

# 📊 Sample Dashboards

<img width="1411" height="773" alt="image" src="https://github.com/user-attachments/assets/297f241e-7777-4e83-b7b2-26944aa177d4" />

# 🧪 Key Features
Parameterized folder paths in ADF for dynamic pipeline execution

Derived column handling (e.g., Profit = Sales - Cost)

Incremental load pattern using metadata tracking (optional)

Power BI report with interactive slicers and drill-down

# 🧠 Learnings & Highlights
Practical experience working with Azure’s modern data stack

Designed a medallion architecture (Bronze/Silver/Gold) on Data Lake

Built reusable and scalable data pipelines in ADF

Integrated Power BI for actionable insights

# 📌 Prerequisites
Azure Subscription

Azure Data Factory instance

Azure Data Lake Gen2 and Synapse workspace

Power BI Desktop for dashboard creation

# 🧰 Tools Used
Visual Studio Code / Azure Portal

Azure Storage Explorer

Power BI Desktop

Python 3.x

# 🙌 Acknowledgements
This project is part of my learning journey to transition into modern cloud-based data architecture roles, building hands-on expertise with Microsoft Azure ecosystem.

📫 Let's Connect
If you found this useful, feel free to connect with me on LinkedIn or ⭐️ this repo!



## Getting Started: Deploying and Running the Project

Follow these steps to deploy and run the entire data pipeline in your Azure environment:

### **Phase 1: Azure Resource Deployment**

1.  **Azure Subscription:** Ensure you have an active Azure subscription. A [free trial](https://azure.microsoft.com/en-us/free/) is sufficient.
2.  **Resource Group Creation:**
    * Go to the Azure Portal.
    * Search for "Resource groups" and click **+ Create**.
    * Provide a name (e.g., `retail-analytics-rg`) and select your region. Click **Review + create**, then **Create**.
3.  **Azure Data Lake Storage Gen2 (ADLS Gen2) Deployment:**
    * In the Azure Portal, search for "Storage accounts" and click **+ Create**.
    * Select your Resource Group.
    * **Storage account name:** Choose a unique name (e.g., `pawandlgen2retail`).
    * **Region:** Select the same region as your Resource Group.
    * **Performance:** `Standard`.
    * **Redundancy:** `Locally-redundant storage (LRS)`.
    * Go to the **Advanced** tab, under "Data Lake Storage Gen2," enable **"Hierarchical namespace"**.
    * Review + create, then Create.
    * **Create Containers:** Once deployed, navigate to the storage account, go to **Containers**, and create the `salesdata` container. Inside the `salesdata` container, create folders named `bronze`, `silver`, and `gold`.
4.  **Azure Data Factory (ADF) Deployment:**
    * In the Azure Portal, search for "Data factories" and click **+ Create**.
    * Select your Resource Group.
    * **Name:** Choose a unique name (e.g., `pawan-retail-adf`).
    * **Region:** Select the same region.
    * **Version:** `V2`.
    * Review + create, then Create.
5.  **Azure Synapse Analytics Workspace Deployment:**
    * In the Azure Portal, search for "Azure Synapse Analytics workspaces" and click **+ Create**.
    * Select your Resource Group.
    * **Workspace name:** Choose a unique name (e.g., `pawan-retail-synapse-001`).
    * **Region:** Select the same region.
    * **Select Data Lake Storage Gen2:** Choose your `pawandlgen2retail` account.
    * **File system name:** Select your `salesdata` container.
    * **SQL Administrator credentials:** Set a strong username and password for the Synapse SQL Administrator. **Remember these credentials!**
    * Review + create, then Create.

### **Phase 2: Data Generation & Initial Ingestion (Bronze Layer)**

1.  **Generate Sample Data:**
    * Ensure you have Python installed locally.
    * Run the `generate_sales_data.py` script (provided in this repo) to create `sales_data.csv`.
2.  **Upload to Bronze Layer:**
    * Go to your `pawandlgen2retail` storage account in the Azure Portal.
    * Navigate to the `salesdata` container -> `bronze` folder.
    * Upload the `sales_data.csv` file into this folder.

### **Phase 3: Azure Data Factory Pipeline Setup**

1.  **Launch ADF Studio:** From your ADF resource in the Azure Portal, click "Launch studio."
2.  **Create Linked Services:**
    * In ADF Studio, go to the **Manage** hub (monitor icon).
    * Under "External connections," select **Linked services**.
    * Click **+ New**.
    * Search for `Azure Data Lake Storage Gen2`.
    * **Name:** `ls_adls_gen2_retail`.
    * **Authentication type:** `Managed Identity`.
    * **Storage account name:** Select your `pawandlgen2retail` account.
    * Test connection and Create.
3.  **Create Datasets:**
    * In ADF Studio, go to the **Author** hub (✍️ icon).
    * Under "Factory Resources," select **Datasets**.
    * **`ds_bronze_sales_csv`:**
        * Type: `Azure Data Lake Storage Gen2`, Format: `Delimited text`.
        * Linked service: `ls_adls_gen2_retail`.
        * File path: `salesdata/bronze/sales_data.csv`.
        * First row as header: Checked. Import schema: From connection/store.
    * **`ds_silver_sales_parquet`:**
        * Type: `Azure Data Lake Storage Gen2`, Format: `Parquet`.
        * Linked service: `ls_adls_gen2_retail`.
        * File path: `salesdata/silver/sales_cleaned/` (no specific file name).
        * Import schema: None.
    * **`ds_gold_daily_sales_parquet`:**
        * Type: `Azure Data Lake Storage Gen2`, Format: `Parquet`.
        * Linked service: `ls_adls_gen2_retail`.
        * File path: `salesdata/gold/daily_sales_summary/` (no specific file name).
        * Import schema: None.
4.  **Import Data Flows and Pipeline:**
    * Use the JSON files provided in this GitHub repository for `df_bronze_to_silver_sales.json`, `df_silver_to_gold_sales.json`, and `pl_bronze_to_silver_sales.json`.
    * In ADF Studio, go to the **Author** hub.
    * For Data Flows and Pipelines, click the three dots `...` next to their respective sections, then select **"Import"**. Upload the JSON files.
    * **Review and Adjust:** After import, open each Data Flow and Pipeline. Verify that all linked services and dataset paths are correctly mapped to your deployed resources. Pay close attention to the `toString(SalesDate, 'yyyy-MM-dd')` in `finalPrepareForSink` within `df_silver_to_gold_sales` and `count(distinct toString(CustomerID))` or `size(distinct(collect(CustomerID)))` expressions.
5.  **Publish All:** Click the **"Publish all"** button at the top of ADF Studio to save all changes.

### **Phase 4: Azure Synapse Analytics Setup**

1.  **Launch Synapse Studio:** From your Synapse Workspace in the Azure Portal, click "Open Synapse Studio."
2.  **Create Database:**
    * In Synapse Studio, go to the **Develop** hub (paper icon).
    * Click **+** > **SQL script**.
    * Ensure connected to `Built-in (serverless)`.
    * Run: `CREATE DATABASE retail_analytics_db;`
    * Publish the script.
3.  **Create Master Key, Credential, and External Data Source:**
    * In the same SQL script (or a new one), ensure connected to `retail_analytics_db`.
    * Run the SQL from `CREATE MASTER KEY.sql` (replace `'YourStrongPassword123!'` with a strong password).
    * Run the SQL from `CREATE DATABASE SCOPED CREDENTIAL and EXTERNAL DATA SOURCE.sql` (replace `youradlgen2` with your storage account name, ensure `LOCATION` is `https://youradlgen2.dfs.core.windows.net/salesdata/`).
    * Publish the script.
4.  **Create Gold Layer View:**
    * Open `CREATE OR ALTER VIEW gold_daily_sales_summary.sql` from this repo.
    * Ensure connected to `retail_analytics_db`.
    * Verify `BULK` path is `gold/daily_sales_summary/*.parquet` and `DATA_SOURCE = 'adls_gen2_source'`.
    * Verify `CAST(sales.SalesDate AS DATE) AS SalesDate` in the SELECT list.
    * Run the script.
    * Publish the script.

### **Phase 5: Execute Pipeline & Verify Data**

1.  **Trigger ADF Pipeline:**
    * In ADF Studio, go to the **Author** hub > **Pipelines**.
    * Open `pl_bronze_to_silver_sales`.
    * Click **"Add trigger"** > **"Trigger now"**.
    * Monitor the run in the **Monitor** hub. Ensure it succeeds.
2.  **Verify Gold Layer in Synapse:**
    * Once the pipeline is successful, go to Synapse Studio.
    * Open a new SQL script, connect to `retail_analytics_db`.
    * Run: `SELECT TOP 100 * FROM gold_daily_sales_summary ORDER BY SalesDate DESC, Region;`
    * Confirm data is present and `SalesDate` is not null.

### **Phase 6: Power BI Dashboard**

1.  **Open Power BI Desktop.**
2.  **Connect to Synapse Serverless SQL Pool View:**
    * Get Data > Azure Synapse Analytics SQL database.
    * Server: Your Synapse Serverless SQL endpoint (e.g., `pawan-retail-synapse-001-ondemand.sql.azuresynapse.net`).
    * Database: `retail_analytics_db`.
    * Data Connectivity mode: **DirectQuery**.
    * Authenticate.
    * Select `dbo.gold_daily_sales_summary` and Load.
3.  **Build Dashboard:** Create visuals as described in the Power BI Dashboard Creation Steps (e.g., Card for Total Sales, Line Chart for Sales Trend by Date, Bar Chart for Sales by Region, Slicer for Month).
4.  **Save and Publish:** Save your `.pbix` file and publish it to Power BI Service.

## Cost Management

**IMPORTANT:** To avoid incurring unnecessary costs, please remember to delete all Azure resources (especially the Resource Group containing your ADLS Gen2, ADF, and Synapse Workspace) once you are done exploring the project.
