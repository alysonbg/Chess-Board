# Chess-Board
![Python application](https://github.com/alysonbg/chessapi/workflows/Python%20application/badge.svg)
[![codecov](https://codecov.io/gh/alysonbg/chessapi/branch/main/graph/badge.svg?token=X88VO0WK32)](https://codecov.io/gh/alysonbg/chessapi)

How to install and run this project locally(Python 3.9 required):
```console
git clone https://github.com/alysonbg/chessapi.git
cd chessapi
cp contrib/env-sample .env
python -m pip install pipenv
pipenv sync
docker-compose up -d
pipenv shell
python manage.py migrate
python manage.py runserver
```

The purpose of this project is to find all the possible locations that a Knight can move in 2 turns.

To use it, there are two endpoints that expose the functionality:

POST api/pieces/

It receives a json with the type of the piece and its color. This endpoint returns the piece Id

GET api/moves/{piece_id}?coordinate={location}

It receives a piece Id and a coordinate(algebraic notation) as url arguments.
This endpoint returns a list of the possible moves for the next 2 turns.

#Improvements:
To solve this problem, first I created a function to find all the possible moves for a Knight. Then, I used this function again in all positions that were returned from the first call.

One thing that can be improved is the efficiency of the algorithm