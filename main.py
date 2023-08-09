from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from typing_extensions import Annotated
from src import schemas

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get('/items/')
def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}