# NSNCO Tasks - Backend Structure and Rest API

This project implements a backend structure using Django models and Rest API. The project consists of three models: Client, Artist, and Work. A Client object is created automatically after each User registration using signals. The Work model has a ManyToManyField relationship with the Artist model and contains a link and work_type. The work_type field is a choice field with three options: Youtube, Instagram, and Other.

## API Endpoints

### Register User

This endpoint allows the user to register using a username and password. The request body should contain the following parameters:

- username (string): The username of the user
- password (string): The password of the user

**Endpoint**: `/api/register`

**Method**: POST

**Example**: 

POST http://127.0.0.1:8000/api/register

{
"username": "testuser",
"password": "password123"
}


### Get List of Works

This endpoint allows the user to retrieve a list of works with the option to filter by work_type and search by artist name. The response will contain the link, work_type, and artists associated with each work.

**Endpoint**: `/api/works`

**Method**: GET

**Parameters**:

- work_type (string): Filter by work_type. Possible values are "Youtube", "Instagram", and "Other".
- artist (string): Search by artist name.

**Example**: 

GET http://127.0.0.1:8000/api/works?work_type=Youtube


### Get List of Artists

This endpoint allows the user to retrieve a list of artists with their associated works. The response will contain the name of the artist and the works associated with each artist.

**Endpoint**: `/api/artists`

**Method**: GET

**Parameters**:

- search (string): Search by artist name.

**Example**: 

GET http://127.0.0.1:8000/api/artists?search=John


## Dummy Data

The project contains some dummy data for testing purposes. You can log in to the admin panel using the following credentials:

- Username: admin
- Password: admin

After logging in, you can add, modify, or delete objects of the Client, Artist, and Work models. The dummy data contains two clients, three artists, and six works.

## Conclusion

This project provides a backend structure using Django models and Rest API. The API endpoints allow the user to register, retrieve a list of works, and retrieve a list of artists. The project also contains some dummy data for testing purposes.
