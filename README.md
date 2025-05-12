# 📊 Financial Data Analysis — DBMS Final Project

This project demonstrates how to collect, store, and analyze financial data using Python, MySQL, and Tableau. We built an end-to-end data analytics pipeline that extracts financial metrics using the Yahoo Finance API, stores them in a normalized relational database, and visualizes insights using Tableau.

## 🚀 Project Overview

**Objective:**  
To automate financial data collection and build a structured pipeline that enables detailed analysis of companies’ financial health across stock prices, income statements, balance sheets, cash flows, and dividends.

**Key Deliverables:**
- Automated data ingestion from yFinance.
- Normalized MySQL schema for structured financial storage.
- Tableau dashboards for dynamic financial insights.

## 🛠️ Tech Stack

- **Python** — Data Extraction & Processing (`yfinance`, `pandas`, `mysql-connector-python`)
- **MySQL** — Relational Database Design & Management
- **Tableau** — Data Visualization and Dashboard Creation

## 🧱 Database Schema

We created a normalized schema with the following tables:

- `company_info`: Company metadata (sector, industry, country)
- `income_statement`: Revenue, net income, etc.
- `balance_sheet`: Assets, liabilities, equity
- `cashflow`: Operating, investing, and financing cash flows
- `stock_prices`: Daily historical prices
- `dividends`: Historical dividend data

Primary/foreign key relationships were enforced, and indexes were added for faster joins and query execution.

## 🔁 Data Pipeline

1. **Extract:**  
   Fetch real-time data from yFinance based on company tickers.

2. **Transform:**  
   Clean and standardize datasets for database compatibility.

3. **Load (ETL):**  
   Insert data into MySQL using parameterized queries to prevent SQL injection.

4. **Visualize:**  
   Connect MySQL to Tableau and generate dashboards by joining relevant tables via foreign keys.

## 📊 Sample Insights (2021–2024)

- 📉 Debt decreased steadily, while assets grew.
- 💸 Dividend payments surged since 1987.
- 📈 EBITDA increased despite plateauing net income due to higher operational costs.
- 🧾 Tax provision spiked, increasing post-EBIT burden.

## ⚠️ Challenges Faced

- Handling missing/incomplete data from APIs.
- Overcoming API rate limits.
- Designing a scalable schema for large datasets.

## 📎 Future Work

- Real-time data refresh and dashboard sync
- Expand metrics to include market cap, P/E ratio, and beta
- Deploy dashboards on web using Tableau Public / Power BI

## 👨‍💻 Authors

- Aekamjot Singh
- Yash Gupta

---

