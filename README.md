# Insurance Dashboard App - Backend

This is the backend API for the Insurance Dashboard application, which displays data from a SQLite database.

## Frontend

This backend is used by the [Insurance Dashboard frontend application](https://github.com/fparejam/frontend-react), which is built with React and can be found deployed [here](https://www.bcginterview.fparejam.com/)

## Data

The data for this backend has been populated from a JSON file, and is stored in a SQLite database. The database schema consists of a single `policies` table with columns including policy ID, date of purchase, customer ID, fuel type, vehicle segment, premium, and more.

## Endpoints

### Policies

- `GET /api/policies`: Returns a list of all policies in the database.

## Setup

1. Clone the repository: `git clone https://github.com/fparejam/backend-flask.git`.
2. Install dependencies: `pip install -r requirements.txt`.
3. Start the development server: `python app.py`.
4. The API can be accessed at `http://localhost:5000`.

## Deployment

This backend is currently hosted on PythonAnywhere at `http://fparejam.pythonanywhere.com/`.
Feel free to make a request to it:

`curl http://fparejam.pythonanywhere.com/api/policies`


## Contact

For any questions or inquiries, please contact [fparejamayo@gmail.com](mailto:fparejamayo@gmail.com).
