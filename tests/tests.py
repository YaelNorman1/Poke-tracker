# from unittest import mock
from fastapi.testclient import TestClient
from router.pokemon_router.pokemon_utils import get_pokemon_types, find_pokemon_roster
from server import app

client = TestClient(app)

# class test_add_pokemon():
    # def test_validate_pokemon_type(self):
    #     response = client.get("/pokemons?type_name=normal")        
    #     response_message = response.json()
    #     assert response.status_code == 200
    #     assert "eevee" in response_message 


# def test_add_pokemon():
#     response = client.post("/pokemons/yanma")
#     response_message = response.json()
#     assert response.status_code == 201
#     assert "Success" in response_message

# def test_add_pokemon_already_exists():
#     response = client.post("/pokemons/yanma")
#     response_message = response.json()
#     assert response.status_code == 403
#     assert "Error" in response_message

# def test_validate_pokemon_type():
#     response = get_pokemon_types(193) #     
#     response_message = list(map(lambda pokemon_type: pokemon_type["p_type"],response))
#     assert "bug" in response_message 
#     assert "flying" in response_message


    
# def test_validate_pokemon_type():
#     response = client.get("/pokemons/venusaur")
#     venusaur_types =  get_pokemon_types(response.json()["id"])    
#     venusaur_types = list(map(lambda pokemon_type: pokemon_type["p_type"],venusaur_types))
#     assert "poison" in venusaur_types 
#     assert "grass" in venusaur_types


# def test_get_pokemon_roster():
#     response = client.get("/trainers/pokemon?pokemon_name=charmander")
#     assert response.status_code == 200
#     assert response.json() == ["Giovanni", "Jasmine", "Whitney"]


# def test_pokemon_by_trainer():
#     response= find_pokemon_roster("Drasna")
#     assert set(["wartortle", "caterpie", "beedrill", "arbok",
#                 "clefairy", "wigglytuff", "persian", 
#                 "growlithe", "machamp", "golem", "dodrio", 
#                 "hypno", "cubone", "eevee", "kabutops"]) == set(response)

def test_evolve_pinser():
    response= client.put("/pokemons/evolve?pokemon_name=pinsir&trainer_name=Whitney")
    response_message = response.json()
    assert "Error" in response_message 


# def test_evolve_pokemon_does_not_exist():
#     response= client.put("/pokemons/evolve?pokemon_name=spearow&trainer_name=Archie")
#     response_message = response.json()
#     #assert response.status_code == 403
#     assert "Error" in response_message


def test_delete_pokemon():
    before_delete_trainers_pokemon= client.get("/pokemons?trainer_name=Whitney")
    # if "venusaur" in before_delete_trainers_pokemon:
    delete_pokemon= client.delete("/pokemons?pokemon_name=venusaur&trainer_name=Whitney")
    after_delete_trainers_pokemon= client.get("/pokemons?trainer_name=Whitney")
    assert delete_pokemon.status_code == 200
    assert "venusaur" not in after_delete_trainers_pokemon
    assert before_delete_trainers_pokemon != after_delete_trainers_pokemon
    