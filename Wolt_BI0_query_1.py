


import sqlite3
import pandas as pd
conn = sqlite3.connect("Wolt_BI0.db")

cursor = conn.cursor()

try:
    query_1 = pd.read_sql_query('''
        SELECT *, (VENUE_REVENUE-VENUE_COGS)/VENUE_REVENUE AS VENUE_GROSS_MARGIN
        FROM(
        ELECT VENUE_ID, SUM(PURCHASE_REVENUE_EUR) AS VENUE_REVENUE, SUM(PURCHASE_COGS_EUR) AS VENUE_COGS, AVG(ORDER_SIZE)
        FROM purchase_profit_data as ppd
        GROUP BY VENUE_ID
        )
        ORDER BY VENUE_GROSS_MARGIN DESC;
        ''', conn)
    conn.commit()
except: 
    None

finally:
    query_1.to_excel('venue_profit.xlsx')
    conn.commit()
    conn.close()
                
    print("We're all done here, let's go home")




#SELECT Abs_profit/Cost AS Profit_Margin, VENUE_ID, COUNTRY, TIME_RECEIVED
#        FROM (
#            SELECT SUM((BASEPRICE/(1+VAT_PERCENTAGE/100)-COST_PER_UNIT)*(COST_PER_UNIT_EUR/COST_PER_UNIT)*COUNT) as Abs_Profit, 
#            SUM(COST_PER_UNIT_EUR*COUNT) AS Cost, purchase_item_data.PURCHASE_ID AS PURCHASE_ID
#            
#            FROM item_data JOIN purchase_item_data ON item_data.PRODUCT_ID = purchase_item_data.PRODUCT_ID
#            GROUP BY purchase_item_data.PURCHASE_ID ) as profit_data
#            JOIN purchase_data
