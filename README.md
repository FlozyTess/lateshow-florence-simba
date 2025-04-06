# Late Show API - Florence Simba
### This project implements a Flask API for a fictional Late Show TV program. The API allows the management of episodes, guests, and their appearances on the show. The system models the relationships between episodes, guests, and their appearances, with validations and necessary CRUD functionality.

# Table of Contents
1. Installation

2. Usage

3. Endpoints

4. Testing with Postman

5. License

# Installation
1. Clone this repository:
  `git clone https://github.com/yourusername/lateshow-florence-simba.git`
2. Install dependencies:

- Navigate into the project directory and install the required Python packages.
    `cd lateshow-florence-simba`  
    `pip install -r requirements.txt`

3. Set up the database:

- Run the following commands to create and set up the database:
    `flask db init`
    `flask db migrate`
    `flask db upgrade`
4. Seed the database (optional):

- If you have seed data available, you can load it into the database. If you are using the provided CSV file:
    `flask seed_db`

# Usage
- To start the Flask server locally, use the following command:
`flask run`
- This will start the server on `http://127.0.0.1:5000`. You can now test the API endpoints.

# Endpoints
1. GET /episodes
- Returns a list of all episodes.
2. GET /episodes/:id
- Returns the details of a specific episode, including the associated guests through their appearances.
3. GET /guests
- Returns a list of all guests.
4. POST /appearances
- Creates a new appearance for a guest on a specific episode.

# Testing with Postman
#### Import Postman Collection:

#### Download the Postman collection file from the repository.

- Open Postman and click on Import.

- Choose the challenge-4-lateshow.postman_collection.json file and click Import.

- Test all the endpoints using the provided collection.

- Testing Locally:

- Ensure that your Flask application is running on `http://127.0.0.1:5000` and test the endpoints in the Postman collection.

# License
#### This project is licensed under the MIT License

