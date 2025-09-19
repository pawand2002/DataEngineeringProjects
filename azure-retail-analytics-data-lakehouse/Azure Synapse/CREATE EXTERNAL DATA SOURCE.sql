-- Create an External Data Source that uses the credential to point to your ADLS Gen2 root
CREATE EXTERNAL DATA SOURCE [pawandlgen2retail]
WITH (
    LOCATION = 'https://pawandlgen2retail.dfs.core.windows.net/salesdata/',
    CREDENTIAL = [pawandlgen2retail]
);