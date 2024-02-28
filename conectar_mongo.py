from pymongo import MongoClient

client = MongoClient("mongodb://root:senac123@127.0.0.1:37452")


# selecionando o banco de dados loja_db
db = client.loja_db

# Estamos obtendo os dados que estão cadastrado na tabela(coleção) usuario, usamos db [""].find().
# O comando find localiza os dados e retorna com todos eles para a variável us. Depois fizemos a leitura de todas linha com o for e exibimos na tela.
for us in db["usuario"].find():
     print(us)

# Abaixo a consulta realiza o cadastro de um novo usuário e retorna o id do usuário cadastrado
# usuario_id = db["usuario"].insert_one({"nomeusuario":"amelie","senha":"123","nivel":"usuario"}).inserted_id
# print(usuario_id)

# Localizar apenas um usuário no banco de dados
# rs = db["usuario"].find_one({"nivel":"usuario"})
# print(rs)

# Localizar todos os dados com nivel de acesso usuario
# for rs in db["usuario"].find({"nivel":"usuario"}):
   # print(rs)