from fastapi import APIRouter, status
from .trainer_utils import *
from DB.json_parser import insert_trainer_db

router = APIRouter()

@router.post("/trainers", status_code=status.HTTP_200_OK)
def add_trainer(name, city):
    insert_trainer_db(name, city)


@router.get("/trainers/pokemon", status_code=status.HTTP_200_OK)
def get_trainers_of_pokemon(pokemon_name):
    return find_pokemon_owners(pokemon_name)