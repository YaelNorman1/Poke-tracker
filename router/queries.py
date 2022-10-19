import pymysql

try:
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="poke_tracker",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )
except TypeError as e:
    print(e)

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
    if not validate_pokemon_of_trainer_in_table_db(pokemon_id, trainer_name):
        raise Exception({"Error":"pokemon or trainer do not exist, sorry"})
    try:
        with connection.cursor() as cursor:
            query = f'DELETE FROM pokemon_trainer WHERE (pokemon_trainer.p_id = {pokemon_id} AND pokemon_trainer.t_name = "{trainer_name}");'
            cursor.execute(query)
            connection.commit()
    except Exception:
        raise Exception({"Error":"pokemon or trainer do not exist, sorry"})


def validate_pokemon_of_trainer_in_table_db(pokemon_id, trainer_name):
    try:
        with connection.cursor() as cursor:
            query = f'SELECT * FROM pokemon_trainer WHERE (pokemon_trainer.p_id = {pokemon_id} AND pokemon_trainer.t_name = "{trainer_name}");'
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except Exception:
        raise Exception({"Error":"pokemon or trainer do not exist, sorry"})



def insert_to_pokemon_trainer_db_query(p_id,t_name):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT IGNORE INTO pokemon_trainer VALUES ({int(p_id)},'{t_name}')"
            cursor.execute(query)
            connection.commit()
    except TypeError as e:
        print(e)


def find_pokemon_owners_db(pokemon_name):
    try:
        with connection.cursor() as cursor:
            query = f'''SELECT pt.t_name 
                        FROM pokemon_trainer AS pt
                        JOIN pokemon
                        ON (SELECT p.id FROM pokemon AS p WHERE p.p_name = "{pokemon_name}") = pt.p_id
                        WHERE pokemon.p_name = "{pokemon_name}"'''
            cursor.execute(query)
            result = cursor.fetchall()
            return list(map(lambda t_name_dict: t_name_dict["t_name"], result))
    except TypeError as e:
        print(e)


def get_heaviest_pokemon():
    try:
        with connection.cursor() as cursor:
            query = f'SELECT * FROM pokemon WHERE pokemon.weight = (SELECT MAX(pokemon.weight) FROM pokemon)'
            cursor.execute(query)
            result = cursor.fetchone()
            return result
    except TypeError as e:
        print(e)


def find_most_owned_pokemon():
    try:
        with connection.cursor() as cursor:
            query = f'''SELECT p_name,owners_number
                    FROM pokemon AS p
                    JOIN (
                    SELECT pokemon_trainer.p_id,
                        Count(pokemon_trainer.p_id) as owners_number
                    FROM pokemon_trainer
                    GROUP BY pokemon_trainer.p_id
                    ORDER BY owners_number DESC
                    ) AS new_table ON (
                    p.id = new_table.p_id
                    )'''
            cursor.execute(query)
            result = cursor.fetchall()
            max_number_of_owners = 0 if not result else result[0]["owners_number"]
            return list(map(lambda p_name_owners_number_dict: p_name_owners_number_dict["p_name"],filter(lambda p_name_owners_number_dict: p_name_owners_number_dict["owners_number"] == max_number_of_owners , result)))
    except TypeError as e:
        print(e)