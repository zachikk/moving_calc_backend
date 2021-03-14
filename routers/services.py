from typing import List
from fastapi import Depends, APIRouter, status
from data_base.database import get_db
from schemas import services as services_schema
from crud import services as services_crud
from sqlalchemy.orm import Session

router = APIRouter(tags=["Services"])


@router.post("/service/", status_code=status.HTTP_201_CREATED)
def create_services(services: services_schema.ServicesCreate, db: Session = Depends(get_db)):
    services_crud.create(db, services)


@router.get("/service/{services_id}", response_model=services_schema.ServicesGet, status_code=status.HTTP_200_OK)
def get_services(services_id: int, q: str = None, db: Session = Depends(get_db)):
    return services_crud.read(db, services_id, q)


@router.get("/service/", response_model=List[services_schema.ServicesGet], status_code=status.HTTP_200_OK)
def get_all_services(db: Session = Depends(get_db)):
    return services_crud.read_all(db)
