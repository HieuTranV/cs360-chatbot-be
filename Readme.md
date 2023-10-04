## Setup Environment
```
pip install virtualenv
```
```
virtualenv venv
```
```
pip install -r requirements.txt
```

## Run
```
uvicorn chatbox.main:app --host 0.0.0.0 --port 8081
```