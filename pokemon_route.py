from fastapi import APIRouter, status
from pokemon_route_utils import *
import requests

router = APIRouter()


@router.get("/pokemons/{pokemon_name}", status_code=status.HTTP_200_OK)
def get_pokemon(pokemon_name):
    try:
        req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}") 
        req.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return  "Pokemon name doesn't exist"
    pokemon_data = get_pokemon_data(pokemon_name)
    pokemon_id= pokemon_data["id"]
    save_types_in_tabels(pokemon_id, req.json()["types"])
    pokemon_types_dict = get_pokemon_types(pokemon_id)
    pokemon_types_lst = list(map(lambda pokemon_type:pokemon_type["p_type"],pokemon_types_dict))
    pokemon_data["types"] = pokemon_types_lst
    return pokemon_data


@router.get("/pokemons", status_code=status.HTTP_200_OK)
def get_pokemons_by_trainer(trainer_name='', type_name=''):
    if trainer_name:
        return find_pokemon_roster(trainer_name)   
    elif type_name:
        return find_pokemons_by_type(type_name)    
    # TODO: add if not both


@router.delete("/pokemons", status_code=status.HTTP_200_OK)
def delete_pokemon_of_trainer(pokemon_name,trainer_name):
    delete_pokemon_of_trainer_from_db(pokemon_name, trainer_name)   


@router.put("/pokemons/evolve", status_code=status.HTTP_200_OK)
def evolve_pokemon_of_trainer(pokemon_name,trainer_name):          
    try:
        species_url = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}").json()["species"]["url"]
    except requests.exceptions.HTTPError as e:
        return  "Pokemon name doesn't exist"  
    try:
        evolution_chain_url = requests.get(f"{species_url}").json()["evolution_chain"]["url"]
    except requests.exceptions.HTTPError as e:
        return  "evolution url doesn't exists" 
    try:
        next_form = return_next_form(pokemon_name,requests.get(f"{evolution_chain_url}").json())
    except requests.exceptions.HTTPError as e:
        return  "Return next form doesn't exists"
    
    if next_form:
        update_db_evolve(pokemon_name,next_form,trainer_name)