






import sqlite3
import pandas as pd
conn = sqlite3.connect("Wolt_BI0.db")

cursor = conn.cursor()

try:
    query_1 = pd.read_sql_query('''
        SELECT COUNTRY, AVG(PURCHASE_REVENUE_EUR) AS AVG_VALUE
        FROM purchase_profit_data as ppd JOIN purchase_data as p ON p.PURCHASE_ID = ppd.PURCHASE_ID
        GROUP BY COUNTRY
        ORDER BY AVG_VALUE DESC
        LIMIT 5
        ;
        ''', conn)
    conn.commit()
except: 
    None

finally:
    query_1.to_excel('Country_OrderValue_copy.xlsx')
    conn.commit()
    conn.close()
                
    print("We're all done here, let's go home")
