import os

from dotenv import load_dotenv

load_dotenv()
ID = os.getenv('ID')

create_pet_data = {
    "id": ID,
    "category": {
        "id": ID,
        "name": "dog"
    },
    "name": "fluffy",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": ID,
            "name": "dog_fluffy"
        }
    ],
    "status": "available"
}

update_pet_data = {
    "id": ID,
    "category": {
        "id": ID,
        "name": "not_fluffy"
    },
    "name": "doggie",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": ID,
            "name": "dog_fluffy"
        }
    ],
    "status": "sold"
}
