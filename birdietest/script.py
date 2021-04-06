import pymysql
import json

mydb = pymysql.connect(host='localhost',
                       user='root',
                       password='Eu@momuitop@çoc@!1',
                       db='TESTE_DB')

cursor = mydb.cursor()

f = open('output.json', )
json_obj = json.load(f)

for obj in json_obj:
    print("product:", obj["product"])
    print("price:", obj["price"])
    print("store:", obj["store"])
    print("link:", obj["link"])

    print('---')
    cursor.execute("INSERT INTO products (product, price, store, link) VALUES (%s,%s,%s,%s)",
                   (obj["product"], obj["price"], obj["store"], obj["link"]))

# close the connection to the database.
mydb.commit()
cursor.close()
