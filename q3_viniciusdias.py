import mysql.connector

# Conexão com o banco de dados
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="124272",
    database="sessao",
    auth_plugin='mysql_native_password'
)

meucursor = mydb.cursor()

# Função para executar comandos SQL
execsqlcmd = lambda cmd, meucursor: meucursor.execute(cmd)

# Função para criar tabelas
execcreatetable = lambda table, attrs, meucursor: execsqlcmd(f"CREATE TABLE {table} ({attrs});", meucursor)

# Função para inserir dados
exeinsertinfo = lambda table, attrs, values, meucursor: execsqlcmd(f"INSERT INTO {table} ({', '.join(attrs)}) VALUES ({', '.join([f'{value!r}' if isinstance(value, str) else str(value) for value in values])});", meucursor)

# Função para consultar dados
consultar_dados = lambda meucursor: [print(row) for row in meucursor]

# Função para remover dados
execsqlcmd_delete = lambda cmd, meucursor: [meucursor.execute(cmd)]

# Criar tabelas
execcreatetable("USERS", "id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), country VARCHAR(100), id_console INT", meucursor)
execcreatetable("VIDEOGAMES", "id_console INT, name VARCHAR(100), id_company INT, release_date DATE", meucursor)
execcreatetable("GAMES", "id_game INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(100), genre VARCHAR(100), release_date DATE, id_console INT", meucursor)
execcreatetable("COMPANY", "id_company INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), country VARCHAR(100)", meucursor)

# Inserir dados
exeinsertinfo("COMPANY", ["name", "country"], ["Nintendo", "Japan"], meucursor)
exeinsertinfo("VIDEOGAMES", ["id_console", "name", "id_company", "release_date"], [1, "Super Mario Bros.", 1, "1985-09-13"], meucursor)
exeinsertinfo("GAMES", ["title", "genre", "release_date", "id_console"], ["The Legend of Zelda", "Action/Adventure", "1986-02-21", 1], meucursor)
exeinsertinfo("USERS", ["name", "country", "id_console"], ["Alice", "USA", 1], meucursor)

# Consultar dados
consultar_dados(meucursor)

# Remover dados
execsqlcmd_delete("DELETE FROM USERS WHERE name = 'Alice';", meucursor)

# Commit e fechamento
mydb.commit()
meucursor.close()
mydb.close()
