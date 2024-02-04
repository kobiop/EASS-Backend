
from fastapi import HTTPException
from sqlalchemy import create_engine, text
from src.models.pydanticModels import ApartmentDetails,ApartmentSearchForm
def ConnectDB():
    DATABASE_URL = "mysql+mysqlconnector://root:root@localhost:3307/EASS_PROJECT"
    engine = create_engine(DATABASE_URL)
    return engine

def generate_dynamic_query(searchfrom):
    base_query="select * from EASS_PROJECT.apartments where 1=1"
    params={}
    if searchfrom['min_price']:
        base_query += " AND price >= :min_price"
        params['min_price'] = searchfrom['min_price']
    if searchfrom['max_price']:
        base_query += " AND price <= :max_price"
        params['max_price'] = searchfrom['max_price']
    if searchfrom['min_year_built']:
        base_query += " AND year_built >= :min_year_built"
        params['min_year_built'] = searchfrom['min_year_built']
    if searchfrom['min_sqft']:
        base_query += " AND sqft >= :min_sqft"
        params['min_sqft'] = searchfrom['min_sqft']
    if searchfrom['max_sqft']:
        base_query += " AND sqft <= :max_sqft"
        params['max_sqft'] = searchfrom['max_sqft']
    if searchfrom['min_beds']:
        base_query += " AND beds >= :min_beds"
        params['min_beds'] = searchfrom['min_beds']
    if searchfrom['max_beds']:
        base_query += " AND beds <= :max_beds"
        params['max_beds'] = searchfrom['max_beds']
    if searchfrom['min_bathrooms']:
        base_query += " AND bathrooms >= :min_bathrooms"
        params['min_bathrooms'] = searchfrom['min_bathrooms']
    if searchfrom['max_bathrooms']:
        base_query += " AND bathrooms <= :max_bathrooms"
        params['max_bathrooms'] = searchfrom['max_bathrooms']
    if searchfrom['min_price_per_sqft']:
        base_query += " AND price_per_sqft >= :min_price_per_sqft"
        params['min_price_per_sqft'] = searchfrom['min_price_per_sqft']
    if searchfrom['property_type']:
        property_types_values = [property_type.value for property_type in searchfrom['property_type']]
        if property_types_values:
            property_types_in_clause = ', '.join([':pt{}'.format(i) for i in range(len(property_types_values))])
            base_query += f" AND property_type IN ({property_types_in_clause})"
            params.update({f'pt{i}': val for i, val in enumerate(property_types_values)})
    if searchfrom['min_garage']:
        base_query += " AND garage >= :min_garage"
        params['min_garage'] = searchfrom['min_garage']
    if searchfrom['max_HOA_fees']:
        base_query += " AND HOA_fees <= :max_HOA_fees"
        params['max_HOA_fees'] = searchfrom['max_HOA_fees']
    if searchfrom['address'] and searchfrom['address'] != "No pref":
        base_query += " AND address LIKE :address"
        params['address'] = f"%{searchfrom['address']}%"
    if searchfrom['min_sqft_lot']:
        base_query += " AND sqft_lot >= :min_sqft_lot"
        params['min_sqft_lot'] = searchfrom['min_sqft_lot']

    return base_query, params

def userFilter(search_input):
        base_query,params=generate_dynamic_query(search_input)
        engine=ConnectDB()
        query = text(base_query)
        with engine.connect() as conn:
            result = conn.execute(query.bindparams(**params))
        apartments = [apartment._asdict() for apartment in result.all()]

        return apartments

def SelectAllApartments():
    engine = ConnectDB()
    query = text("select * from EASS_PROJECT.apartments")
    with engine.connect() as conn:
        result = conn.execute(query)
    apartments = result.fetchall()

    if not apartments:
        raise HTTPException(status_code=404, detail="No apartments found")

    apartment_details_list = []
    for apartment in apartments:
        apartment_details = ApartmentDetails(
            id = int(apartment[0]),
            price=float(apartment[1]) if apartment[1] is not None else 0,
            year_built=int(apartment[2]) if apartment[2] is not None else 0,
            sqft=int(apartment[3]) if apartment[3] is not None else 0,
            beds=int(apartment[4]) if apartment[4] is not None else 0,
            bathrooms=int(apartment[5]) if apartment[5] is not None else 0,
            price_per_sqft=float(apartment[6]) if apartment[6] is not None else 0,
            property_type=str(apartment[7]) if apartment[7] is not None else "No property type",
            garage=int(apartment[8]) if apartment[8] is not None else 0,
            HOA_fees=float(apartment[9]) if apartment[9] is not None else 0.0,
            address=str(apartment[10]) if apartment[10] is not None else "No Adress",
            sqft_lot=int(apartment[11]) if apartment[11] is not None else 0,
            img_link=str(apartment[12]) if apartment[12] is not None else "No Pic",
            created_at=str(apartment[13]) if apartment[13] is not None else "No Date",
        )
        apartment_details_list.append(apartment_details)
    return apartment_details_list
    
engine=ConnectDB()
apartmetns=SelectAllApartments()

def insertNewApartmentToDB(newApartments):
    engine = ConnectDB()
    query = text("INSERT INTO EASS_PROJECT.apartments (address, price, beds, garage, bathrooms, property_type, year_built, img_link, sqft, sqft_lot, HOA_fees) VALUES (:address, :price, :beds, :garage ,:bathrooms, :property_type, :year_built, :img_link, :sqft, :sqft_lot, :HOA_fees)")
    params={}
    params['address']=newApartments['address']
    params['price']=newApartments['price']
    params['beds']=newApartments['beds']
    params['bathrooms']=newApartments['bathrooms']
    params['property_type']=newApartments['property_type']
    params['year_built']=newApartments['year_built']
    params['img_link']=newApartments['img_link']
    params['sqft']=newApartments['sqft']
    params['sqft_lot']=newApartments['sqft_lot']
    params['HOA_fees']=newApartments['HOA_fees'] 
    params['garage']=newApartments['garage'] 
    with engine.connect() as conn: 
        try:
            conn.execute(query.bindparams(**params))
            conn.commit()
        except Exception as e:
            print(f"Error: {e}")
            conn.rollback()  
    return newApartments

