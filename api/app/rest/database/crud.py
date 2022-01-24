import json
from app.rest.database import models
from app.rest.schemas import calls
from sqlalchemy.orm import Session


def get_models(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Heart).offset(skip).limit(limit).all()