import requests
import uvicorn
from fastapi import FastAPI, Request, HTTPException, status
import pymysql

app = FastAPI()

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="poke_tracker",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)



@app.get("/pokemon", status_code=status.HTTP_200_OK)
def get_pokemon(pokemon_name):
    req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    pokemon_data = get_pokemon_data(pokemon_name)
    pokemon_id= pokemon_data["id"]
    save_types_in_tabels(pokemon_id, req.json()["types"])
    pokemon_types_dict = get_pokemon_types(pokemon_id)
    pokemon_types_lst = list(map(lambda pokemon_type:pokemon_type["p_type"],pokemon_types_dict))
    pokemon_data["types"] = pokemon_types_lst
    return pokemon_data

def get_pokemon_data(pokemon_name):
    try:
        with connection.cursor() as cursor:
            query = f'SELECT * FROM pokemon WHERE p_name = "{pokemon_name}";'
            cursor.execute(query)
            result = cursor.fetchone()
            return result
    except TypeError as e:
        return e

def get_pokemon_id(name):
    try:
        with connection.cursor() as cursor:
            query = f'SELECT id FROM pokemon WHERE p_name = "{name}";'
            cursor.execute(query)
            result = cursor.fetchone()
            return result
    except TypeError as e:
        return e


def get_pokemon_types(pokemon_id):
    try:
        with connection.cursor() as cursor:
            query = f'SELECT p_type FROM pokemon_type WHERE p_id = "{pokemon_id}";'
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except TypeError as e:
        return e

def save_types_in_tabels(pokemon_id, pokemon_types):
    for type in pokemon_types:
        insert_each_type(pokemon_id, type["type"]["name"])


def insert_each_type(id, type):
    try:
        with connection.cursor() as cursor:
            query = f'INSERT IGNORE INTO pokemon_type VALUES ("{id}","{type}")'
            cursor.execute(query)
            connection.commit()
    except TypeError as e:
        print(e)

if __name__ == "__main__":
    uvicorn.run("part-three-server:app", host="0.0.0.0", port=8000, reload=True)

