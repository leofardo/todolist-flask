import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='admin'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `todolist`;")

cursor.execute("CREATE DATABASE `todolist`;")

cursor.execute("USE `todolist`;")

# criando tabelas
TABLES = {}
TABLES['Tarefas'] = ('''
      CREATE TABLE `tarefas` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `descricao` varchar(100) NOT NULL,
        `status` varchar(30) NOT NULL,
        `data_cadastro` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')

# inserindo jogos
tarefas_sql = 'INSERT INTO tarefas (descricao, status) VALUES (%s, %s)'
tarefas = [
    ('Finalizar relatório financeiro', 'Pendente'),
    ('Enviar e-mail de atualização para a equipe', 'Pendente'),
    ('Organizar reunião de equipe', 'Pendente'),
    ('Revisar proposta de projeto', 'Pendente'),
    ('Atualizar documento de requisitos', 'Pendente'),
    ('Preparar apresentação para cliente', 'Pendente'),
    ('Verificar backups do sistema', 'Pendente'),
    ('Agendar avaliações de desempenho', 'Pendente')
]
cursor.executemany(tarefas_sql, tarefas)

cursor.execute('select * from todolist.tarefas')
print(' -------------  Tarefas:  -------------')
for tarefa in cursor.fetchall():
    print(tarefa[1])

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()