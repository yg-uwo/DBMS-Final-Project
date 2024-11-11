import yfinance as yf
from db_connector import create_connection 
connection = create_connection()
cursor = connection.cursor()



def add_company_info():
    print("G6TFGYSU")

def insert_stock_data(symbol, company_name):
    cursor.execute("INSERT INTO Stocks (symbol, company_name) VALUES (%s, %s)", (symbol, company_name))
    stock_id = cursor.lastrowid
    return stock_id

def insert_stock_price(stock_id, stock_data):
    for date, row in stock_data.iterrows():
        date = date.to_pydatetime()
        cursor.execute("""
        INSERT INTO StockPrices (stock_id, date, open_price, close_price, high_price, low_price, volume)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (stock_id, date, float(row['Open']), float(row['Close']), float(row['High']), float(row['Low']), float(row['Volume'])))

def insert_balance_sheet(stock_id, balance_sheet_data):
    connection = create_connection()
    cursor = connection.cursor()

    for date, data in balance_sheet_data.items():
        cursor.execute("""
        INSERT INTO BalanceSheet (stock_id, date, total_assets, total_liabilities, total_equity)
        VALUES (%s, %s, %s, %s, %s)
        """, (stock_id, date, data['total_assets'], data['total_liabilities'], data['total_equity']))

def insert_cash_flow(stock_id, cash_flow_data):
    connection = create_connection()
    cursor = connection.cursor()

    for date, data in cash_flow_data.items():
        cursor.execute("""
        INSERT INTO CashFlow (stock_id, date, net_cash_flow_operating, net_cash_flow_investing, net_cash_flow_financing)
        VALUES (%s, %s, %s, %s, %s)
        """, (stock_id, date, data['net_cash_flow_operating'], data['net_cash_flow_investing'], data['net_cash_flow_financing']))

def main():
    symbol = "AAPL" # Company Name 
    stock_data = yf.download(symbol, start="2020-01-01", end="2023-01-01")
    balance_sheet_data = {
        "2020-12-31": {"total_assets": 100000000, "total_liabilities": 50000000, "total_equity": 50000000},
        "2023-12-31": {"total_assets": 120000000, "total_liabilities": 60000000, "total_equity": 60000000}
    }
    cash_flow_data =  {
        "2020-12-31": {"net_cash_flow_operating": 100000000, "net_cash_flow_investing": -2000000, "net_cash_flow_financing": 50000000},
        "2023-12-31": {"net_cash_flow_operating": 120000000, "net_cash_flow_investing": -3000000, "net_cash_flow_financing": 60000000}
    }

    stock_id = insert_stock_data(symbol, "Apple Inc.")
    print(stock_data)

    insert_stock_price(stock_id, stock_data)
    insert_balance_sheet(stock_id, balance_sheet_data)
    insert_cash_flow(stock_id, cash_flow_data)

    print(f"Data for {symbol} inserted successfully into the databases.")

if __name__ == "__main__":
    main()


connection.commit()
cursor.close()
connection.close()
