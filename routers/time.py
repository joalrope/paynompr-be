import bcrypt
from fastapi import APIRouter
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from datetime import  datetime

from database.config import session
from routers.auth import user_dependency

from models.time import Time



from schemas.time import TimeIDShema, TimeShema
from passlib.context import CryptContext


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
time_router = APIRouter()


@time_router.post("/{employer_id}")
async def create_time(time_data: TimeShema, employer_id : int):    

    time_query = Time(        
        regular_time = time_data.regular_time,
        overtime = time_data.overtime,
        meal_time = time_data.meal_time,
        sick_hours = time_data.sick_hours,
        vacations_hours =  time_data.vacations_hours,     
        employer_id = employer_id,
        disability = time_data.disability,
        medicare = time_data.medicare,
        regular_pay = time_data.regular_pay,
    )
     
  
    session.add(time_query)
    session.commit()
    session.refresh(time_query)   
    return {"ok": True, "msg": "Time was successfully created", "result": time_query}



@time_router.get("/{employer_id}")
async def get_time_by_employer_id(employer_id: int):
    time_query = session.query(Time).filter(Time.employer_id == employer_id).all()

    return {
        "ok": True,
        "msg": "Employers were successfully retrieved",
        "result": time_query,
    }

@time_router.put("/{employers_id}")
async def update_employer(employers_id: int, time: TimeIDShema):
    time_query = session.query(Time).filter_by(Time.employer_id==employers_id).first()
        
    regular_time = time.regular_time,
    overtime = time.overtime,
    meal_time = time.meal_time,
    sick_hours = time.sick_hours,
    vacations_hours =  time.sick_vacations,     
    employer_id = employer_id    
    

    session.add(time_query)
    session.commit()
    session.refresh(time_query)

    return {"ok": True, "msg": "user was successfully updated", "result": time_query}



