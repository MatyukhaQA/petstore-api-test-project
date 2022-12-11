from voluptuous import Schema

pet_schema = Schema(
    {
        "id": int,
        "category": {
            "id": int,
            "name": str
        },
        "name": str,
        "photoUrls": [
            str
        ],
        "tags": [
            {
                "id": int,
                "name": str
            }
        ],
        "status": str
    }
)

pet_status_schema = Schema(
[
  {
    "id": int,
    "category": {
      "id": int,
      "name": str
    },
    "name": str,
    "photoUrls": [
      str
    ],
    "tags": [
      {
        "id": int,
        "name": str
      }
    ],
    "status": str
  }
]
)
delete_pet_schema = Schema(
    {
      "code": int,
      "type": str,
      "message": str
    }
)