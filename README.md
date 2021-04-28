## Starting the application

docker-compose up

Check --> [http://localhost:8888](http://localhost:8888)

## Use venv during dev-phase
  - docker doesnt work currently
### Install the dependencies and start the Python Backend server
```sh
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 -m uvicorn serverFast:app --reload --port=5555 
```

### Open another terminal and start the server for the UI
```sh
cd ui
yarn install
yarn serve
```
