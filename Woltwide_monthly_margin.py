



import sqlite3
import pandas as pd
conn = sqlite3.connect("Wolt_BI0.db")
cursor = conn.cursor()

try:
    query_1 = pd.read_sql_query('''
        SELECT MONTH_PROFIT/MONTH_REVENUE AS GROSS_MARGIN, *
        FROM (
        SELECT 
        SUM(PURCHASE_GROSS_PROFIT_EUR) MONTH_PROFIT, 
        SUM(PURCHASE_REVENUE_EUR) AS MONTH_REVENUE,
        strftime('%m', TIME_DELIVERED) AS MONTH
        FROM purchase_profit_data AS ppd JOIN purchase_data AS pd ON ppd.PURCHASE_ID = pd.PURCHASE_ID
        GROUP BY MONTH )
        ;
        ''', conn)
    conn.commit()
except: 
    None

finally:
    query_1.to_excel('Wolt_Global_Margin_2022.xlsx')
    conn.commit()
    conn.close()
                
    print("We're all done here, let's go home")

