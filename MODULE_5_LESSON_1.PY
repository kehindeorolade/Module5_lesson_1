import sqlite3

con = sqlite3.connect('sale.db')


cur = con.cursor()

#Create table
# cur.execute('''CREATE TABLE inventory1
#               (Item_ID integer, Item_name text, price integer, quantity_lest_in_stock integer)''')


print("successful")

inventory_data1 = [
                (1, 'diary', 20, 12),
                (2, 'blade', 50, 7),
                (3, 'paper tape', 150, 2),
                (4, 'pen', 60, 20),
                (5, 'stapler', 300, 5),
                (6, 'calculator', 1500, 4),
                (7, 'glue', 70, 15),
                (8, 'files', 100, 50),
                (9, 'Envelope', 50, 100),
                (10, 'notebook', 250, 49)
]


cur.executemany('INSERT INTO inventory1 VALUES(?, ?, ?, ?)', inventory_data1)

print("execution successful")





for row in cur.execute('SELECT * FROM inventory1'):
    print(row)




#print(cur.fetchall())

cur.execute('''select * from inventory1
where quantity_lest_in_stock < 2
order by price desc;
'''
)
#item = cur.fetchall()
#print(item)