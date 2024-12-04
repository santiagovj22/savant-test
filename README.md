# API Documentation
By Santiago Valle
## Introduction
Welcome to the API documentation for Savant proposal. This API provides a CRUD operation for users with authentication and authorization.
## Requirements ##
- docker
- python 3.12
- postman
## Getting Started
To get started with this API, follow the steps below:

1. Clone the repository: `git clone https://github.com/santiagovj22/savant-test`
2. Create environment:  `pip install pipenv`
3. Install the dependencies: `pipenv install`
4. Run setup folder docker-compose.postgres.yml
5. Add in the script of the schema.sql in the pgadmin
3. Start the server: `flask --app app run --debug`

## API Endpoints
The following endpoints are available in this API:

### Login
- Method: [POST]
- Path: [/api/auth/login]
- Description: [Create user and generate token to interact with the more endpoints]

### Get user by id
- Method: [GET]
- Path: [/api/users/:user_id]
- Description: [Return user by id]

### Get all users
- Method: [GET]
- Path: [Endpoint Path]
- Description: [Endpoint Description]

### Update user by id
- Method: [PUT]
- Path: [/api/users/:user_id]
- Description: [Update user by id]

### remove user by id
- Method: [DEL]
- Path: [/api/users/:user_id]
- Description: [remove user by id]

## Request and Response Examples
Here are some examples of how to make requests to the API and the corresponding responses:

Login - Input - Output:

    {
        "full_name": "santi",
        "cellphone": "+57 305 7349486",
        "email": "santi@gmail.com",
        "password": "test1234" 
    }

    {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNDA3NTM1NiwianRpIjoiZDQzNjRiYTQtYTM1OS00NWVjLT" 
    }

Get user by id - Input - Output:


    curl --location 'http://127.0.0.1:5000/api/users/10facdf8-4655-4f2e-96a4-4a6ba7cc39de' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNDA3NDI2NCwianRpIjoiMDg5YWQ1ZjAtNTUzMS00YTVhLWFmMTUtNzdkY2E5ZDVmNDA2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEwZmFjZGY4LTQ2NTUtNGYyZS05NmE0LTRhNmJhN2NjMzlkZSIsIm5iZiI6MTcxNDA3NDI2NCwiY3NyZiI6ImY0MjA2ZWZiLTMyNzYtNDY4Ny04YTE5LTRhN2E4YWViY2QwNCIsImV4cCI6MTcxNDA3NTE2NH0.ARgECBeX1S5wTQxJAIe0fi793kBtqJswg8ATmFc5nVk'


    

    "data": {
        "id": "10facdf8-4655-4f2e-96a4-4a6ba7cc39de",
        "full_name": "santi5",
        "email": "santi5@gmail.com",
        "cellphone": "+57 305 7349486"
    }

Get all users - input- output

    curl --location 'http://127.0.0.1:5000/api/users'

    {
        "data": [
            {
                "id": "3354cacb-6121-44d0-98ab-cc3d3f026d76",
                "full_name": "santi7",
                "email": "santi7@gmail.com",
                "cellphone": "+57 305 7349486"
            }
        ]
    }

Update user by id - input-output

        curl --location --request PATCH 'http://127.0.0.1:5000/api/users/10facdf8-4655-4f2e-96a4-4a6ba7cc39de' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNDA3NDI2NCwianRpIjoiMDg5YWQ1ZjAtNTUzMS00YTVhLWFmMTUtNzdkY2E5ZDVmNDA2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEwZmFjZGY4LTQ2NTUtNGYyZS05NmE0LTRhNmJhN2NjMzlkZSIsIm5iZiI6MTcxNDA3NDI2NCwiY3NyZiI6ImY0MjA2ZWZiLTMyNzYtNDY4Ny04YTE5LTRhN2E4YWViY2QwNCIsImV4cCI6MTcxNDA3NTE2NH0.ARgECBeX1S5wTQxJAIe0fi793kBtqJswg8ATmFc5nVk' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "full_name":"name updated 3",
        "email":"emailpdated3@gmail.com"
    }'

Remove user by id - input - output

    curl --location --request DELETE 'http://127.0.0.1:5000/api/users/10facdf8-4655-4f2e-96a4-4a6ba7cc39de' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNDA3NDI2NCwianRpIjoiMDg5YWQ1ZjAtNTUzMS00YTVhLWFmMTUtNzdkY2E5ZDVmNDA2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEwZmFjZGY4LTQ2NTUtNGYyZS05NmE0LTRhNmJhN2NjMzlkZSIsIm5iZiI6MTcxNDA3NDI2NCwiY3NyZiI6ImY0MjA2ZWZiLTMyNzYtNDY4Ny04YTE5LTRhN2E4YWViY2QwNCIsImV4cCI6MTcxNDA3NTE2NH0.ARgECBeX1S5wTQxJAIe0fi793kBtqJswg8ATmFc5nVk'


    {
        "message": "User with ID 10facdf8-4655-4f2e-96a4-4a6ba7cc39de deleted successfully"
    }
