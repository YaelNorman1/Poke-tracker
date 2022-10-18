import requests
import uvicorn
from fastapi import FastAPI, Request, HTTPException, status
# import pymysql
from part_two_queries import find_pokemon_roster ,find_pokemon_owners,find_pokemons_by_type
from main import insert_trainer_db, insert_pokemon_trainer_db


# app = FastAPI()

# connection = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     db="poke_tracker",
#     charset="utf8",
#     cursorclass=pymysql.cursors.DictCursor
# )

# @app.get("/pokemons/{pokemon_name}", status_code=status.HTTP_200_OK)
# def get_pokemon(pokemon_name):
#     try:
#         req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
#         req.raise_for_status()
#     except requests.exceptions.HTTPError as e:
#         return  "Pokemon name doesn't exist"
#     pokemon_data = get_pokemon_data(pokemon_name)
#     pokemon_id= pokemon_data["id"]
#     save_types_in_tabels(pokemon_id, req.json()["types"])
#     pokemon_types_dict = get_pokemon_types(pokemon_id)
#     pokemon_types_lst = list(map(lambda pokemon_type:pokemon_type["p_type"],pokemon_types_dict))
#     pokemon_data["types"] = pokemon_types_lst
#     return pokemon_data

# def get_pokemon_data(pokemon_name):
#     try:
#         with connection.cursor() as cursor:
#             query = f'SELECT * FROM pokemon WHERE p_name = "{pokemon_name}";'
#             cursor.execute(query)
#             result = cursor.fetchone()
#             return result
#     except TypeError as e:
#         print(e)

# def get_pokemon_id(name):
#     try:
#         with connection.cursor() as cursor:
#             query = f'SELECT id FROM pokemon WHERE p_name = "{name}";'
#             cursor.execute(query)
#             result = cursor.fetchone()
#             return result
#     except TypeError as e:
#         print(e)


# def get_pokemon_types(pokemon_id):
#     try:
#         with connection.cursor() as cursor:
#             query = f'SELECT p_type FROM pokemon_type WHERE p_id = "{pokemon_id}";'
#             cursor.execute(query)
#             result = cursor.fetchall()
#             return result
#     except TypeError as e:
#         print(e)

# def save_types_in_tabels(pokemon_id, pokemon_types):
#     for type in pokemon_types:
#         insert_each_type(pokemon_id, type["type"]["name"])


# def insert_each_type(id, type):
#     try:
#         with connection.cursor() as cursor:
#             query = f'INSERT IGNORE INTO pokemon_type VALUES ("{id}","{type}")'
#             cursor.execute(query)
#             connection.commit()
#     except TypeError as e:
#         print(e)
        

# @app.get("/pokemons", status_code=status.HTTP_200_OK)
# def get_pokemons_by_trainer(trainer_name='', type_name=''):
#     if trainer_name:
#         return find_pokemon_roster(trainer_name)
#     elif type_name:
#         return find_pokemons_by_type(type_name)

    

# @app.get("/trainers/pokemon", status_code=status.HTTP_200_OK)
# def get_trainers_of_pokemon(pokemon_name):
#     return find_pokemon_owners(pokemon_name)

 
# @app.post("/trainers", status_code=status.HTTP_200_OK)
# def add_trainer(name, city):
#     insert_trainer_db(name, city)
  

# @app.get("/pokemons", status_code=status.HTTP_200_OK)
# def get_pokemon_by_type(type_name):
#     return find_pokemons_by_type(type_name)

# @app.delete("/pokemons", status_code=status.HTTP_200_OK)
# def delete_pokemon_of_trainer(pokemon_name,trainer_name):
# def delete_pokemon_of_trainer_from_db(pokemon_name, trainer_name):
#     pokemon_id = get_pokemon_data(pokemon_name)["id"]
#     try:
#         with connection.cursor() as cursor:
#             query = f'DELETE FROM pokemon_trainer WHERE (pokemon_trainer.p_id = {pokemon_id} AND pokemon_trainer.t_name = "{trainer_name}");'
#             cursor.execute(query)
#             connection.commit()
#     except TypeError as e:
#         print(e)


# @app.put("/pokemons/evolve", status_code=status.HTTP_200_OK)
# def evolve_pokemon_of_trainer(pokemon_name,trainer_name):
#     try:
#         species_url = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}").json()["species"]["url"]
#     except requests.exceptions.HTTPError as e:
#         return  "Pokemon name doesn't exist"  
#     try:
#         evolution_chain_url = requests.get(f"{species_url}").json()["evolution_chain"]["url"]
#     except requests.exceptions.HTTPError as e:
#         return  "evolution url doesn't exists" 
#     try:
#         next_form = return_next_form(pokemon_name,requests.get(f"{evolution_chain_url}").json())
#     except requests.exceptions.HTTPError as e:
#         return  "Return next form doesn't exists"
    
#     if next_form:
#         update_db_evolve(pokemon_name,next_form,trainer_name)
   
    

# def return_next_form(pokemon_name,evolution_chain):
#     chain = evolution_chain["chain"]
#     for _ in range(2):
#         if chain["species"]["name"] == pokemon_name :
#             if chain["evolves_to"]:
#                 return chain["evolves_to"][0]["species"]["name"]
#         else:
#             chain = chain["evolves_to"][0]




# def update_db_evolve(old_pokemon_name, new_pokemon_name, trainer_name):
#     delete_pokemon_of_trainer_from_db(old_pokemon_name, trainer_name)
#     pokemon_id = get_pokemon_data(new_pokemon_name)["id"]
#     insert_pokemon_trainer_db(pokemon_id, trainer_name)

    

# if __name__ == "__main__":
#     uvicorn.run("part_three_server:app", host="0.0.0.0", port=8000, reload=True)

