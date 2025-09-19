-- Corrected view definition for gold_daily_sales_summary using External Data Source
CREATE OR ALTER VIEW gold_daily_sales_summary AS
SELECT
    CAST(SalesDate AS DATE) AS SalesDate,
    Region,
    SUM(TotalDailySales) AS TotalDailySales,
    SUM(UniqueCustomers) AS UniqueCustomers,
    SUM(TotalTransactions) AS TotalTransactions
FROM
    OPENROWSET(
        BULK 'gold/daily_sales_summary/*.parquet', -- RELATIVE PATH
        DATA_SOURCE = 'pawandlgen2retail',         -- Use the new data source
        FORMAT = 'PARQUET'
    ) WITH (
        SalesDate VARCHAR(50),
        Region VARCHAR(50),
        TotalDailySales DECIMAL(18, 2),
        UniqueCustomers INT,
        TotalTransactions INT
    ) AS sales
GROUP BY
    CAST(SalesDate AS DATE),
    Region;