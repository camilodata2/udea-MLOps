from fastapi import FastAPI

from router.model_predi import predicion_de_modelo
from fastapi import APIRouter


app = FastAPI(docs_url='/')

app.include_router(predicion_de_modelo)
