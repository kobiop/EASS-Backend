from fastapi import APIRouter, HTTPException
from database.pydanticModels import SignUpForm ,SignInRequest,TokenResponse
from database.db import insert_new_user,get_user_by_email,create_access_token
from passlib.context import CryptContext 

auth_router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@auth_router.post("/signup", response_model=SignUpForm)
async def sign_up(new_user: SignUpForm):
    hashed_password = pwd_context.hash(new_user.password)

    user_data = {
        "first_name":new_user.first_name,
        "last_name":new_user.last_name,
        "email": new_user.email,
        "password": hashed_password
    }

    user_data_exist = get_user_by_email(new_user.email)
    if user_data_exist:
        raise HTTPException(status_code=401, detail="User does not exist")
    new_user_data=insert_new_user(user_data)
    return  new_user_data

@auth_router.post("/signin", response_model=TokenResponse)
async def sign_in(sign_in_request: SignInRequest):
    user_data = get_user_by_email(sign_in_request.email)
    if not user_data:
        raise HTTPException(status_code=401, detail="User does not exist")
    if not pwd_context.verify(sign_in_request.password, user_data["password"]):
        raise HTTPException(status_code=401, detail="Incorrect password")
    
    access_token = create_access_token({"sub": user_data["email"]})
 
    return TokenResponse(access_token=access_token, token_type="bearer")