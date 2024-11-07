from tinydb import TinyDB, Query, table
#pip install tinydb


# Criar ou abrir um banco de dados nomeado
db = TinyDB('db.json')
# db = TinyDB('C:/Users/itarg/Downloads/db.json')
users_table = db.table('users')  # Nomeando a "tabela"

profissoes_table = db.table('profissoes')

# # Criar uma tabela
profissoes_table.insert({'id': 1, 'name': 'Engenheiro'})
profissoes_table.insert({'id': 2, 'name': 'Médico'})
profissoes_table.insert({'id': 3, 'name': 'Professor'})

# # Inserir registros no banco de dados
users_table.insert({'id': 1, 'name': 'Alice', 'age': 25, 'job': 'Engineer'})
users_table.insert({'id': 2, 'name': 'Bob', 'age': 30, 'job': 'Doctor'})
users_table.insert({'id': 3, 'name': 'Charlie', 'age': 35, 'job': 'Teacher'})

# Comentário:
# Em SQL, essas inserções seriam:
# INSERT INTO users (id, name, age, job) VALUES (1, 'Alice', 25, 'Engineer');
# INSERT INTO users (id, name, age, job) VALUES (2, 'Bob', 30, 'Doctor');
# INSERT INTO users (id, name, age, job) VALUES (3, 'Charlie', 35, 'Teacher');

# Ler todos os registros
print("Todos os registros:")
for item in users_table.all():
    print(item)

# Comentário:
# Em SQL, isso seria:
# SELECT * FROM users;

# Ler registros específicos usando uma consulta
User = Query()
print("\nBuscar registros onde o nome é 'Alice':")
result = users_table.search(User.name == 'Alice')
print(result)

# Comentário:
# Em SQL, isso seria:
# SELECT * FROM users WHERE name = 'Alice';

# Atualizar registros
print("\nAtualizar idade de Bob para 32:")
users_table.update({'age': 32}, User.name == 'Bob')

# Comentário:
# Em SQL, isso seria:
# UPDATE users SET age = 32 WHERE name = 'Bob';

# Verificar atualização
print("Registros após atualização:")
print(users_table.all())

# # Remover registros
print("\nRemover registro onde o nome é 'Charlie':")
users_table.remove(User.name == 'Charlie')

# Comentário:
# Em SQL, isso seria:
# DELETE FROM users WHERE name = 'Charlie';

# Deletar todos os registros da tabela
users_table.truncate()

# Comentário:
# Em SQL, isso seria:
# DELETE FROM users;

# Verificar após a remoção
print("Registros após remoção:")
print(users_table.all())


# Fechar o banco de dados
db.close()
