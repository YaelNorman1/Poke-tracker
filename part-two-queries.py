import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="Poke_tracker",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

#   EX1


def get_heaviest_pokemon():
    try:
        with connection.cursor() as cursor:
            query = f'SELECT * FROM pokemon WHERE pokemon.weight = (SELECT MAX(pokemon.weight) FROM pokemon)'
            cursor.execute(query)
            result = cursor.fetchone()
            return result
    except TypeError as e:
        return e

#   EX2


def find_pokemons_by_type(type):
    try:
        with connection.cursor() as cursor:
            query = f'SELECT pokemon.p_name FROM pokemon WHERE pokemon.type = "{type}"'
            cursor.execute(query)
            result = cursor.fetchall()
            return list(map(lambda p_name_dict: p_name_dict["p_name"], result))
    except TypeError as e:
        return e


#   EX3

def find_pokemon_owners(pokemon_name):
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
        return e


#   EX4

def find_pokemon_roster(trainer_name):
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
        return e


if __name__ == "__main__":
    # print(get_heaviest_pokemon())
    # print(find_pokemons_by_type("grass"))
    # print(find_pokemon_owners("gengar"))
    print(find_pokemon_roster("Loga"))
