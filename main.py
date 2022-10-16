import requests
import pymysql 
import json

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="Poke_tracker",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def insert_to_tables():
    json_file = open('poke_data.json')
    poke_data_dict = json.load(json_file)
    
    for pokemon_data in poke_data_dict:
        insert_pokemon_db(pokemon_data["id"],pokemon_data["name"],pokemon_data["height"],pokemon_data["weight"])
        for trainer in pokemon_data["ownedBy"]:
            insert_trainer_db(trainer["name"],trainer["town"])
            insert_pokemon_trainer_db(pokemon_data["id"],trainer["name"])

def insert_pokemon_db(id, name, height, weight):
    try:
        with connection.cursor() as cursor:
            query = f'INSERT INTO pokemon VALUES ({id}, "{name}", {height}, {weight})'
            cursor.execute(query)
            connection.commit()
    except TypeError as e:
        print(e)



def insert_trainer_db(name,city):
    try:
        with connection.cursor() as cursor:
            query = f'INSERT IGNORE INTO trainer VALUES ("{name}","{city}")'
            cursor.execute(query)
            connection.commit()
    except TypeError as e:
        print(e)



def insert_pokemon_trainer_db(p_id,t_name):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT IGNORE INTO pokemon_trainer VALUES ({int(p_id)},'{t_name}')"
            cursor.execute(query)
            connection.commit()
    except TypeError as e:
        print(e)

def insert_types_db():
    try:
        base_url = "https://pokeapi.co/api/v2/type/"
        result=requests.get("https://pokeapi.co/api/v2/type/")
        parsed = result.json()
        types =parsed["results"]
        types = list(map(lambda type: (int(type["url"].replace(base_url,'')[0:-1]),type["name"]),types))
        with connection.cursor() as cursor:
            query = "INSERT INTO types(id, t_name) VALUES (%s,%s)"
            cursor.executemany(query,types)
            connection.commit()
    except TypeError as e:
        print(e)
   

if __name__ == "__main__":
    insert_to_tables()
