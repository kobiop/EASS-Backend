from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.pydanticModels import Apartment
import logging

logger = logging.getLogger(__name__)

app = FastAPI()

def connect_db():
    DATABASE_URL = "mysql+mysqlconnector://root:root@localhost:3307/EASS_PROJECT"
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)
    return engine

def generate_dynamic_query(searchfrom, engine):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        base_query = session.query(Apartment).filter()
        
        if searchfrom['min_price']:
            base_query = base_query.filter(Apartment.price >= searchfrom['min_price'])
        if searchfrom['max_price']:
            base_query = base_query.filter(Apartment.price <= searchfrom['max_price'])
        if searchfrom['min_year_built']:
            base_query = base_query.filter(Apartment.year_built >= searchfrom['min_year_built'])
        if searchfrom['min_sqft']:
            base_query = base_query.filter(Apartment.sqft >= searchfrom['min_sqft'])
        if searchfrom['max_sqft']:
            base_query = base_query.filter(Apartment.sqft <= searchfrom['max_sqft'])
        if searchfrom['min_beds']:
            base_query = base_query.filter(Apartment.beds >= searchfrom['min_beds'])
        if searchfrom['max_beds']:
            base_query = base_query.filter(Apartment.beds <= searchfrom['max_beds'])
        if searchfrom['min_bathrooms']:
            base_query = base_query.filter(Apartment.bathrooms >= searchfrom['min_bathrooms'])
        if searchfrom['max_bathrooms']:
            base_query = base_query.filter(Apartment.bathrooms <= searchfrom['max_bathrooms'])
        if searchfrom['min_price_per_sqft']:
            base_query = base_query.filter(Apartment.price_per_sqft >= searchfrom['min_price_per_sqft'])
        if searchfrom['property_type']:
            base_query = base_query.filter(Apartment.property_type.in_(searchfrom['property_type']))
        if searchfrom['min_garage']:
            base_query = base_query.filter(Apartment.garage >= searchfrom['min_garage'])
        if searchfrom['max_HOA_fees']:
            base_query = base_query.filter(Apartment.HOA_fees <= searchfrom['max_HOA_fees'])
        if searchfrom['address']:
            base_query = base_query.filter(Apartment.address.like(f"%{searchfrom['address']}%"))
        if searchfrom['min_sqft_lot']:
            base_query = base_query.filter(Apartment.sqft_lot >= searchfrom['min_sqft_lot'])
        apartments = base_query.all()

    return apartments

def filter_apartments_by_user(search_input):
    engine = connect_db()
    try:
        apartments = generate_dynamic_query(search_input, engine)
        if not apartments:
            raise HTTPException(status_code=404, detail="No apartments found")
        return [apartment.__dict__ for apartment in apartments]
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

def get_all_apartments():
    engine = connect_db()
    try:
        Session = sessionmaker(bind=engine)
        with Session() as session:
            apartments = session.query(Apartment).all()
        if not apartments:
            raise HTTPException(status_code=404, detail="No apartments found")

        return [apartment.__dict__ for apartment in apartments]
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

def insert_new_apartment(new_apartments):
    try:
        engine = connect_db()
        Session = sessionmaker(bind=engine)
        with Session() as session:
            new_apartment_instance = Apartment(**new_apartments)
            session.add(new_apartment_instance)
            session.commit()
        return new_apartments
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Failed to insert new apartment")

def bring_last():
    engine = connect_db()
    try:
        Session = sessionmaker(bind=engine)
        with Session() as session:
            last_apartment = session.query(Apartment).order_by(Apartment.id.desc()).first()
        if not last_apartment:
            raise HTTPException(status_code=404, detail="No apartments found")
        return last_apartment
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
