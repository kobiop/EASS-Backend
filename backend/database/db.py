from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from .pydanticModels import Apartment,User,convert_to_apartment_response
import logging
from dotenv import load_dotenv
import os
import jwt
from datetime import datetime, timedelta, timezone

logger = logging.getLogger(__name__)
  
load_dotenv()

def connect_db():
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
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
        return [convert_to_apartment_response(apartment) for apartment in apartments]
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

def get_all_apartments():
    engine = connect_db()
    Session = sessionmaker(bind=engine)
    try:
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

def insert_new_user(new_user_data):
    try:
        engine = connect_db()
        Session = sessionmaker(bind=engine)
        with Session() as session:
            existing_user = session.query(User).filter(User.email == new_user_data["email"]).first()
            if existing_user:
                raise HTTPException(status_code=400, detail="Email already exists")
            new_user_instance = User(**new_user_data)
            session.add(new_user_instance)
            session.commit()
        return new_user_data
    except IntegrityError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Failed to insert new user")
    
def get_user_by_email(email: str):
    try:
        engine = connect_db()
        Session = sessionmaker(bind=engine)
        with Session() as session:
            user = session.query(User).filter(User.email == email).first()
            if user:
                return {
                    "email": user.email,
                    "password": user.password
                }
            return None
    except Exception as e:
        return None
    

SECRET_KEY = "MySecret"

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt