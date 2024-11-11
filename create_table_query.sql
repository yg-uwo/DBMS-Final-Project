CREATE DATABASE financial_data;

USE financial_data;

CREATE TABLE Stocks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL,
    company_name VARCHAR(100) NOT NULL
);

CREATE TABLE BalanceSheet (
    id INT AUTO_INCREMENT PRIMARY KEY,
    stock_id INT,
    date DATE,
    total_assets BIGINT,
    total_liabilities BIGINT,
    total_equity BIGINT,
    FOREIGN KEY (stock_id) REFERENCES Stocks(id)
);

CREATE TABLE CashFlow (
    id INT AUTO_INCREMENT PRIMARY KEY,
    stock_id INT,
    date DATE,
    net_cash_flow_operating BIGINT,
    net_cash_flow_investing BIGINT,
    net_cash_flow_financing BIGINT,
    FOREIGN KEY (stock_id) REFERENCES Stocks(id)
);

CREATE TABLE StockPrices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    stock_id INT,
    date DATE,
    open_price DECIMAL(10, 2),
    close_price DECIMAL(10, 2),
    high_price DECIMAL(10, 2),
    low_price DECIMAL(10, 2),
    volume BIGINT,
    FOREIGN KEY (stock_id) REFERENCES Stocks(id)
);

DESC BalanceSheet;
SHOW TABLES;