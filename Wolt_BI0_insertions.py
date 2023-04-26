






import sqlite3
import pandas as pd

conn = sqlite3.connect("Wolt_BI.db")
cursor = conn.cursor()
conn.execute("PRAGMA foreign_keys = 1")
conn.commit()

df = pd.read_csv('item_data.csv')
df.to_sql('item_data', conn, if_exists='append', index=False)

df = pd.read_csv('purchase_item_data_final.csv')
df.to_sql('purchase_item_data', conn, if_exists='append', index=False)

df = pd.read_csv('purchase_data_final.csv')
df.to_sql('purchase_data', conn, if_exists='append', index=False)

conn.commit()
conn.close()