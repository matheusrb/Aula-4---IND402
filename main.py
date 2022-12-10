from pymongo import MongoClient
import os
# Conectando com o mongo
mongo_client = MongoClient(os.environ.get("DB_STRING"))
# Criando base de dados 'escola'
mydb = mongo_client['escola']
# Criando colecao 'alunos'
mycol = mydb['alunos']
# Inserindo documento na colecao 'alunos'
mydict = {"nome":"Joaozinho","ano":"primeiro"}
x = mycol.insert_one(mydict)
# Mostrando colecao 'alunos'
cursor = mycol.find({})
for document in cursor:
    print(document)