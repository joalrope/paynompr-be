import bcrypt
from fastapi import APIRouter
from fastapi import APIRouter, Depends






from starlette.responses import FileResponse
from fastapi import  Response

from database.config import session
from routers.auth import user_dependency

from models.time import Time
from models.employers import Employers
from models.companies import Companies

from models.payments import Payments




from schemas.time import TimeIDShema, TimeShema
from passlib.context import CryptContext


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
time_router = APIRouter()


@time_router.post("/{employer_id}")
async def create_time(time_data: TimeShema, employer_id : int):    

    time_query = Time(        
        regular_hours = time_data.regular_hours,
        regular_min = time_data.regular_min,

        over_hours = time_data.over_hours,
        over_min = time_data.over_min,
        holyday_pay = time_data.holyday_pay,
        meal_hours = time_data.meal_hours,
        meal_min = time_data.meal_min,
        holiday_min = time_data.holiday_min,
        holiday_hours = time_data.holiday_hours,

        sick_hours = time_data.sick_hours,
        sick_min = time_data.sick_min,
        concessions = time_data.concessions,
        commissions = time_data.commissions,

        vacations_hours =  time_data.vacations_hours,  
        vacations_min =  time_data.vacations_min,     

        employer_id = employer_id,
        tips = time_data.tips,
        sick_pay= time_data.sick_pay,
        vacation_pay = time_data.vacation_pay,
        meal_time_pay = time_data.meal_time_pay,
        overtime_pay =   time_data.overtime_pay,
        regular_pay = time_data.regular_pay,
    )
    session.add(time_query)
    session.commit()
    session.refresh(time_query) 

    for item in time_data.payments:
        if (item.requiered == 2):
            payment_query = Payments(
                name = item.name,
                amount = item.amount,
                time_id = time_query.id,
                requiered = item.requiered,
                type_taxe = item.type_taxe,
                type_amount = item.type_amount
            );
            session.add(payment_query)
            session.commit() 
        if (item.requiered == 1 and item.is_active ):
            payment_query = Payments(
                name = item.name,
                amount = item.amount,
                time_id = time_query.id,
                requiered = item.requiered,
                type_taxe = item.type_taxe,
                type_amount = item.type_amount
            );
            session.add(payment_query)
            session.commit() 
        
  
      
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
        
    time_query.regular_hours = time.regular_hours
    time_query.regular_min = time.regular_min
    time_query.holyday_pay = time.holyday_pay
    time_query.over_hours = time.over_hours
    time_query.over_min = time.over_min
    time_query.concessions = time.concessions,
    time_query.commissions = time.commissions,
    time_query.meal_hourss = time.meal_hours
    time_query.meal_min = time.meal_min
    time_query.holiday_hours = time.holiday_hours
    time_query.holiday_min = time.holiday_min

    time_query.vacations_hours =  time.vacations_hours
    time_query.vacations_min =  time.vacations_min    

    time_query.sick_hours = time.sick_hours
    time_query.sick_min = time.sick_min


    time_query.sick_pay = time.sick_pay
    time_query.vacation_pay = time.vacation_pay
    time_query.meal_time_pay = time.meal_time_pay
    time_query.overtime_pay =   time.overtime_pay
    time_query.tips = time.tips

    session.add(time_query)
    session.commit()
    session.refresh(time_query)

    return {"ok": True, "msg": "user was successfully updated", "result": time_query}


