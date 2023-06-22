validation_rules1 = {
    "validator": {
        "$jsonSchema": {
            "required": [
                "name",
                "age",
                "is_student",
                "interests",
                "address",
                "birth_date",
                "metadata",
                "favorite_things",
            ],
            "properties": {
                "name": {"bsonType": "string"},
                "age": {"bsonType": "int", "minimum": 0},
                "is_student": {"bsonType": "bool"},
                "interests": {"bsonType": ["string"]},
                "address": {
                    "bsonType": "object",
                    "required": ["street", "city", "country"],
                    "properties": {
                        "street": {"bsonType": "string"},
                        "city": {"bsonType": "string"},
                        "country": {
                            "bsonType": "object",
                            "required": ["name", "code"],
                            "properties": {
                                "name": {"bsonType": "string"},
                                "code": {"bsonType": "string"},
                            },
                        },
                    },
                },
                "birth_date": {"bsonType": "date"},
                "metadata": {
                    "bsonType": "object",
                    "required": ["category", "priority"],
                    "properties": {
                        "category": {"bsonType": "string"},
                        "priority": {"bsonType": "int"},
                    },
                },
                "favorite_things": {"bsonType": ["string", "int", "bool"]},
            },
        }
    }
}


validation_rules2 = {
    "validator": {
        "$jsonSchema": {
            "required": ["person", "products"],
            "properties": {
                "person": {
                    "bsonType": "object",
                    "required": [
                        "name",
                        "age",
                        "is_student",
                        "address",
                        "contacts",
                        "education",
                    ],
                    "properties": {
                        "name": {"bsonType": "string"},
                        "age": {"bsonType": "int", "minimum": 0},
                        "is_student": {"bsonType": "bool"},
                        "address": {
                            "bsonType": "object",
                            "required": ["street", "city", "country"],
                            "properties": {
                                "street": {"bsonType": "string"},
                                "city": {"bsonType": "string"},
                                "country": {
                                    "bsonType": "object",
                                    "required": ["name", "code"],
                                    "properties": {
                                        "name": {"bsonType": "string"},
                                        "code": {"bsonType": "string"},
                                    },
                                },
                            },
                        },
                        "contacts": [
                            {
                                "bsonType": "object",
                                "required": ["type", "value"],
                                "properties": {
                                    "type": {"bsonType": "string"},
                                    "value": {"bsonType": "string"},
                                },
                            }
                        ],
                        "education": [
                            {
                                "bsonType": "object",
                                "required": [
                                    "institution",
                                    "degree",
                                    "major",
                                    "completed",
                                ],
                                "properties": {
                                    "institution": {"bsonType": "string"},
                                    "degree": {"bsonType": "string"},
                                    "major": {"bsonType": "string"},
                                    "completed": {"bsonType": "bool"},
                                },
                            }
                        ],
                    },
                },
                "products": [
                    {
                        "bsonType": "object",
                        "required": ["id", "name", "price", "is_available"],
                        "properties": {
                            "id": {"bsonType": "int"},
                            "name": {"bsonType": "string"},
                            "price": {"bsonType": "double"},
                            "is_available": {"bsonType": "bool"},
                        },
                    }
                ],
            },
        }
    }
}


json_object = {
    "name": "John Doe",
    "age": 25,
    "is_student": True,
    "interests": ["reading", "traveling", "photography"],
    "address": {
        "street": "123 Main Street",
        "city": "New York",
        "country": {"name": "United States", "code": "US"},
    },
    "birth_date": "1998-05-10",
    "metadata": {"category": "A", "priority": 1},
    "favorite_things": ["apple", 5, False],
}
