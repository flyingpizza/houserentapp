from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.rest.schemas.calls import Call, HousePredictionPayload, HousePredictionResult
from typing import Dict, FrozenSet, List
from app.rest.dependencies import get_db
from app.rest.database import crud
from app.rest.dependencies.models import HousePriceModel
import json

router = APIRouter( prefix="/app" )


@router.get('/health')
async def root():
    return {'message': 'I am alive!'}

@router.get("/models/", response_model=List[Call], status_code=200, tags=["Model"])
async def get_model_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[Call]:
    """
    Return a list of model.
    """
    models = crud.get_models(db, skip=skip, limit=limit)
    for m in models:
        m.age = json.loads(m.age)
    return models

@router.post('/models/predictions', response_model=HousePredictionResult, status_code=201, tags=["Model"])
def make_predict(block_data: HousePredictionPayload = None) -> HousePredictionResult:
    model = HousePriceModel()
    prediction: HousePredictionResult = model.predict(block_data)
    return prediction
