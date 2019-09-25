user_mutation_query = '''
mutation {
  createUser(fullname: "Victory Akaniru", username: "vic3king") {
    user {
      username
      email
      instagramFollowing
      instagramFollowers
    }
  }
}
'''
user_mutation_query_invalid_email = '''
mutation {
  createUser(fullname: "Victory Akaniru", username: "vic3king", email: "test.com") { # noqa
    user {
      username
      email
      instagramFollowing
      instagramFollowers
    }
  }
}
'''

user_mutation_response = {
    "data": {
        "createUser": {
            "user": {
                "username": "vic3king",
                "email": None,
                "instagramFollowing": None,
                "instagramFollowers": None
            }
        }
    }
}

user_mutation_response_invalid_email = {
    "errors": [
        {
            "message": "This email is not allowed",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "createUser"
            ]
        }
    ],
    "data": {
        "createUser": None
    }
}

user_duplication_mutation_response = {
    "errors": [
        {
            "message": "vic3king username already exists",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "createUser"
            ]
        }
    ],
    "data": {
        "createUser": None
    }
}
