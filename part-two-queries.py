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
            return list(map(lambda p_name_dict:p_name_dict["p_name"],result))
    except TypeError as e:
        return e
    pass

if __name__ == "__main__":
    # print(get_heaviest_pokemon())
    print(find_pokemons_by_type("grass"))
