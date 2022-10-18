import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="poke_tracker",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def insert_each_type(id, type):
    try:
        with connection.cursor() as cursor:
            query = f'INSERT IGNORE INTO pokemon_type VALUES ("{id}","{type}")'
            cursor.execute(query)
            connection.commit()
    except TypeError as e:
        print(e)


def get_pokemon_types_db(pokemon_id):
    try:
        with connection.cursor() as cursor:
            query = f'SELECT p_type FROM pokemon_type WHERE p_id = "{pokemon_id}";'
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except TypeError as e:
        print(e)


def get_pokemon_data_db(pokemon_name):
    try:
        with connection.cursor() as cursor:
            query = f'SELECT * FROM pokemon WHERE p_name = "{pokemon_name}";'
            cursor.execute(query)
            result = cursor.fetchone()
            return result
    except TypeError as e:
        print(e)

def get_pokemon_id(name):
    try:
        with connection.cursor() as cursor:
            query = f'SELECT id FROM pokemon WHERE p_name = "{name}";'
            cursor.execute(query)
            result = cursor.fetchone()
            return result
    except TypeError as e:
        print(e)

def find_pokemon_roster_db(trainer_name):
    try:
        with connection.cursor() as cursor:
            query = f'''SELECT p.p_name
                        FROM pokemon AS p 
                        JOIN pokemon_trainer AS pt
                        ON p.id = pt.p_id
                        WHERE pt.t_name = "{trainer_name}"'''
            cursor.execute(query)
            result = cursor.fetchall()
            return list(map(lambda p_name_dict: p_name_dict["p_name"], result))
    except TypeError as e:
        print(e)

def find_pokemons_by_type_db(type):
    try:
        with connection.cursor() as cursor:
            query = f'''SELECT p.p_name FROM pokemon AS p
             JOIN pokemon_type AS pt
             ON pt.p_id = p.id
             WHERE pt.p_type = "{type}"'''
            cursor.execute(query)
            result = cursor.fetchall()
            return list(map(lambda p_name_dict: p_name_dict["p_name"], result))
    except TypeError as e:
            print(e)


def delete_pokemon_of_trainer_from_db_query(pokemon_name, trainer_name):
    pokemon_id = get_pokemon_data_db(pokemon_name)["id"]
    try:
        with connection.cursor() as cursor:
            query = f'DELETE FROM pokemon_trainer WHERE (pokemon_trainer.p_id = {pokemon_id} AND pokemon_trainer.t_name = "{trainer_name}");'
            cursor.execute(query)
            connection.commit()
    except TypeError as e:
        print(e)

def insert_to_pokemon_trainer_db_query(p_id,t_name):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT IGNORE INTO pokemon_trainer VALUES ({int(p_id)},'{t_name}')"
            cursor.execute(query)
            connection.commit()
    except TypeError as e:
        print(e)