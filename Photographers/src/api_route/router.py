from typing import List

from fastapi import FastAPI, HTTPException

from src.models.photographer_respnse import PhotographerResponse
from src.services.data_loader import DataLoader
from src.services.photographerRepository import PhotographerRepository
from src.services.photographer_service import PhotographerService
import logging


app = FastAPI()

def get_photographer_service():
    photographers = DataLoader.load_photographers()
    repository = PhotographerRepository(photographers)
    service = PhotographerService(repository)
    return service


@app.get('/api/photographers', response_model=List[PhotographerResponse])
async def get_all_photographers():
    service = get_photographer_service()
    photographers = service.get_all_photographers()
    if not photographers:
        raise HTTPException(status_code=404, detail="photographers not found")
    return photographers


@app.get('/api/photographers/{photographer_id}', response_model=PhotographerResponse)
async def get_photographer_by_id(photographer_id: int):
    service = get_photographer_service()
    photographer = service.get_photographer_by_id(photographer_id)  # Removed `await`
    if not photographer:
        raise HTTPException(status_code=404, detail="Photographer not found")
    return photographer


@app.get('/api/photographers/event/{photographer_event_type}', response_model=List[PhotographerResponse])
async def get_photographer_by_event_type(photographer_event_type: str):
    service = get_photographer_service()
    photographers = service.get_photographer_by_event_type(photographer_event_type)
    if not photographers:
        raise HTTPException(status_code=404, detail=f"Photographers not found for {photographer_event_type}")
    return photographers


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
