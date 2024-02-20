from fastapi import FastAPI,HTTPException

from database.db import get_all_apartments

app = FastAPI()

@app.get("/")
async def health_check():
    return {"server":"up"}

@app.get("/listings")
async def get_listings():
    try:
        apartments = get_all_apartments()
        return {"apartments": apartments}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    



