import yfinance as yf
from db_connector import create_connection
import pandas as pd 
connection = create_connection()
cursor = connection.cursor()

def insert_stock_data(symbol, company_name):
    cursor.execute("INSERT INTO Stocks (symbol, company_name) VALUES (%s, %s)", (symbol, company_name))
    stock_id = cursor.lastrowid
    connection.commit()
    return stock_id

def insert_stock_price(stock_id, stock_data):
    for date, row in stock_data.iterrows():
        date = date.to_pydatetime()
        cursor.execute("""
        INSERT INTO StockPrices (stock_id, date, open_price, close_price, high_price, low_price, volume)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            stock_id,
            date,
            float(row['Open'].iloc[0]),
            float(row['Close'].iloc[0]),
            float(row['High'].iloc[0]),
            float(row['Low'].iloc[0]),
            float(row['Volume'].iloc[0])
        ))
    connection.commit()

def insert_balance_sheet(stock_id, balance_sheet_data):
    for date, data in balance_sheet_data.items():
        total_assets = data.get('Total Assets', None)
        total_liabilities = data.get('Total Liabilities', None)
        total_equity = data.get('Total Stockholder Equity', None)
          # Handle missing values
        total_assets = None if pd.isna(total_assets) else total_assets
        total_liabilities = None if pd.isna(total_liabilities) else total_liabilities
        total_equity = None if pd.isna(total_equity) else total_equity

        
        cursor.execute("""
        INSERT INTO BalanceSheet (stock_id, date, total_assets, total_liabilities, total_equity)
        VALUES (%s, %s, %s, %s, %s)
        """, (stock_id, date, total_assets, total_liabilities, total_equity))
    connection.commit()

def insert_cash_flow(stock_id, cash_flow_data):
    for date, data in cash_flow_data.items():
        net_cash_flow_operating = data.get('Total Cash From Operating Activities')
        net_cash_flow_investing = data.get('Total Cashflows From Investing Activities')
        net_cash_flow_financing = data.get('Total Cash From Financing Activities')
        cursor.execute("""
        INSERT INTO CashFlow (stock_id, date, net_cash_flow_operating, net_cash_flow_investing, net_cash_flow_financing)
        VALUES (%s, %s, %s, %s, %s)
        """, (stock_id, date, net_cash_flow_operating, net_cash_flow_investing, net_cash_flow_financing))
    connection.commit()

def main():
    symbol = "AAPL" # Company Name 
    ticker = yf.Ticker(symbol)

    stock_data = ticker.history(start="2020-01-01", end="2023-01-01")

    balance_sheet_data = ticker.balance_sheet.T
    balance_sheet_data = balance_sheet_data.to_dict(orient="index")

    cash_flow_data = ticker.cash_flow.T
    cash_flow_data = cash_flow_data.to_dict(orient="index")

    stock_id = insert_stock_data(symbol, "Apple Inc.")
    #insert_stock_price(stock_id, stock_data)
    #insert_balance_sheet(stock_id, balance_sheet_data)
    insert_cash_flow(stock_id, cash_flow_data)

    print(f"Data for {symbol} inserted successfully into the databases.")

if __name__ == "__main__":
    main()

cursor.close()
connection.close()
