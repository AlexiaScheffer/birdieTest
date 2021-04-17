# from flask import Flask, request, json, Response
# from pymongo import MongoClient
#
#
# class MongoAPI:
#
#     def __init__(self, data):
#         self.client = MongoClient("mongodb://localhost:27017/")
#
#         database = data['database']
#         collection = data['collection']
#         cursor = self.client[database]
#         self.collection = cursor[collection]
#         self.data = data
#
#     def read(self):
#         documents = self.collection.find()
#         output = [{item: data[item] for item in data if item != '_id'} for data in documents]
#         return output
#
#     def write(self, data):
#         log.info('Writing Data')
#         new_document = data['Document']
#         response = self.collection.insert_one(new_document)
#         output = {'Status': 'Successfully Inserted',
#                   'Document_ID': str(response.inserted_id)}
#         return output
#
#     def update(self):
#         filt = self.data['Filter']
#         updated_data = {"$set": self.data['DataToBeUpdated']}
#         response = self.collection.update_one(filt, updated_data)
#         output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
#         return output
#
#     def delete(self, data):
#         filt = data['Document']
#         response = self.collection.delete_one(filt)
#         output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
#         return output
#
#     if __name__ == '__main__':
#         data = {
#             "database": "IshmeetDB",
#             "collection": "people",
#         }
#         mongo_obj = MongoAPI(data)
#         print(json.dumps(mongo_obj.read(), indent=4))

# import pymysql
# import json
#
# mydb = pymysql.connect(host='localhost',
#                        user='root',
#                        password='Eu@momuitop@çoc@!1',
#                        db='TESTE_DB')
#
# cursor = mydb.cursor()
#
# f = open('output.json', )
# json_obj = json.load(f)
#
# for obj in json_obj:
#     print("product:", obj["product"])
#     print("price:", obj["price"])
#     print("store:", obj["store"])
#     print("link:", obj["link"])
#
#     print('---')
#     cursor.execute("INSERT INTO products (product, price, store, link) VALUES (%s,%s,%s,%s)",
#                    (obj["product"], obj["price"], obj["store"], obj["link"]))
#
# # close the connection to the database.
# mydb.commit()
# cursor.close()
