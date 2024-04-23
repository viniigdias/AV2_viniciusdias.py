# Define as tabelas como expressões lambda
GAMES = lambda: ("GAMES", lambda: {"id_game": "int", "title": "varchar(100)", "genre": "varchar(100)", "release_date": "date", "id_console": "int"})
VIDEOGAMES = lambda: ("VIDEOGAMES", lambda: {"id_console": "int", "name": "varchar(100)", "id_company": "int", "release_date": "date"})
COMPANY = lambda: ("COMPANY", lambda: {"id_company": "int", "name": "varchar(100)", "country": "varchar(100)"})

# Função para gerar INNER JOIN entre as tabelas
gen_inner_join = lambda: \
    f"{GAMES()[0]} g INNER JOIN {VIDEOGAMES()[0]} v ON g.id_console = v.id_console " + \
    f"INNER JOIN {COMPANY()[0]} c ON v.id_company = c.id_company"

# Função para gerar o comando SELECT com os atributos envolvidos
gen_select_query = lambda attributes: f"SELECT {', '.join(attributes)}"

# Exemplo de uso:
join_code = gen_inner_join()
select_query = gen_select_query(["g.title", "v.name", "c.name AS company_name"])
print("Cláusula INNER JOIN:")
print(join_code)
print("\nComando SELECT:")
print(select_query)
