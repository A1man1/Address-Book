import traceback
from typing import Optional
import requests

from fastapi import (APIRouter , HTTPException, 
                     status)                     

from src.core.config import log
from src.database.schema.opreation import UserAddressOperation 
from src.database.schema.schema import UserAddressCreate , UserAddressUpdate, UserAddressOut 
from src.endpoints.v1.helpers import create_data

# Declaring router for user resource.
router = APIRouter(prefix="/address", tags=["Location address"])

# Declare curd opreation
user_address:UserAddressOperation =  UserAddressOperation()


@router.post('/add-address',name='Add Address',response_model=UserAddressOut)
async def add_address(data:UserAddressCreate):
    try:
        return UserAddressOut(** await user_address.create(data))
			
    except Exception as err:
        log.error(err)
        log.error(traceback.format_exc())
        if hasattr(err, "status_code"):
            raise HTTPException(status_code=err.status_code, detail=err.detail)
        else:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error Msg: { err }")


@router.get('/get-address',name='Get Address')
async def get_address(distance,latidute,longitude):
    try:
        query = f"""SELECT id, address, ( 
        3959 * acos( cos( radians(37) ) * cos( radians( {latidute} ) ) * cos( radians( {longitude} ) - radians(-122) ) + 
        sin( radians(37) ) * sin( radians( {latidute} ) ) ) ) AS distance FROM markers HAVING 
        distance < {distance} ORDER BY distance LIMIT 0 , 20;"""
        return create_data(await UserAddressOperation._db.fetch_all(query=query))
    
    except Exception as err:
        log.error(err)
        log.error(traceback.format_exc())
        if hasattr(err, "status_code"):
            raise HTTPException(status_code=err.status_code, detail=err.detail)
        else:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error Msg: { err }")
    

@router.put('/update-address',name='Update Address',response_model=UserAddressOut)
async def update_address(data:UserAddressUpdate):
    try:
        return UserAddressOut(**user_address.update(data))
			
    except Exception as err:
        log.error(err)
        log.error(traceback.format_exc())
        if hasattr(err, "status_code"):
            raise HTTPException(status_code=err.status_code, detail=err.detail)
        else:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error Msg: { err }")
                
