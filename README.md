# Late Show API - Florence Simba
## This project implements a Flask API for a fictional Late Show TV program. The API allows the management of episodes, guests, and their appearances on the show. The system models the relationships between episodes, guests, and their appearances, with validations and necessary CRUD functionality.

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

Navigate into the project directory and install the required Python packages.
    `cd lateshow-florence-simba
pip install -r requirements.txt
`
3. Set up the database:

Run the following commands to create and set up the database:
    `flask db init
flask db migrate
flask db upgrade`
4. Seed the database (optional):

If you have seed data available, you can load it into the database. If you are using the provided CSV file:
    `flask seed_db`
