import yfinance as yf
from db_connector import create_connection
from datetime import datetime
import pandas as pd

# Establish database connection
connection = create_connection()
cursor = connection.cursor()

def add_company_info(ticker, company_id):
    apple = yf.Ticker(ticker)
    info = apple.info

    company_info_data = (
        ticker,
        info.get("longName"),
        info.get("sector"),
        info.get("industry"),
        info.get("country"),
        info.get("website")
    )

    cursor.execute("""
        INSERT INTO company_info (ticker, long_name, sector, industry, country, website)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            long_name = VALUES(long_name),
            sector = VALUES(sector),
            industry = VALUES(industry),
            country = VALUES(country),
            website = VALUES(website)
    """, company_info_data)

    cursor.execute("SELECT company_id FROM company_info WHERE ticker = %s", (ticker,))
    company_id = cursor.fetchone()[0]
    return company_id

def add_income_statement(ticker, company_id):
    apple = yf.Ticker(ticker)
    income_statement = apple.financials.T  # Transposed for row-wise iteration

    for date_index, row in income_statement.iterrows():
        end_date = pd.to_datetime(date_index, errors='coerce')

        if pd.isna(end_date):
            print(f"Skipping invalid date: {date_index}")
            continue
        else:
            end_date = end_date.date() 

        fields = ['company_id', 'end_date']
        values = [company_id, end_date]
        
        for column_name, value in row.items():
            if pd.notnull(value):
                #Change column names to be matched with db_col names
                field_name = column_name.replace(" ", "_").replace(".", "").replace("-", "_")
                fields.append(field_name)
                values.append(value)

        sql_query = f"""
            INSERT INTO income_statement ({', '.join(fields)})
            VALUES ({', '.join(['%s'] * len(values))})
        """
        cursor.execute(sql_query, values)


def add_earnings_data(ticker, company_id):
    stock = yf.Ticker(ticker)
    earnings = stock.earnings_dates 
    # print("Raw Earnings Data:\n", earnings)
    for date, data in earnings.iterrows():
        earnings_date = date.date() 

        # print(earnings_date)

        eps_estimate = data.get('EPS Estimate')
        reported_eps = data.get('Reported EPS')
        surprise_percentage = data.get('Surprise(%)')

        # Replace NaN values with None (which will insert NULL in the database)
        eps_estimate = None if pd.isna(eps_estimate) else eps_estimate
        reported_eps = None if pd.isna(reported_eps) else reported_eps
        surprise_percentage = None if pd.isna(surprise_percentage) else surprise_percentage


        # Prepare the data for insertion into the database
        earnings_data = (
            company_id,
            earnings_date,
            eps_estimate,
            reported_eps,
            surprise_percentage
        )

        # print("VALUE TO BE INSERTED\n",earnings_data)

        cursor.execute("""
            INSERT INTO earnings_data (company_id, fiscal_period, eps_estimate, reported_eps, surprise_percentage)
            VALUES (%s, %s, %s, %s, %s)
        """, earnings_data)

def main():
    ticker = "AAPL" 
    
    company_id = add_company_info(ticker, None)

    # Add Income Statement
    add_income_statement(ticker, company_id)

    # Add Earnings Data
    add_earnings_data(ticker, company_id)

    connection.commit()
    cursor.close()
    connection.close()

main()
