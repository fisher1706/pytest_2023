POST_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "title": {"type": "string",
                  # "enum": ["POST"]
                  # indicate that type only "POST"
                  }
    },
    "required": ["id"]
}


data_of_validation = {
    'id': 1,
    'title': 'Post 1'
}
