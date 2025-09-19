-- Create a Database Scoped Credential to authenticate to ADLS Gen2 using Managed Identity
CREATE DATABASE SCOPED CREDENTIAL [pawandlgen2retail]
WITH IDENTITY = 'Managed Identity';