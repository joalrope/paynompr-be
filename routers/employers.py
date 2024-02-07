import bcrypt
from fastapi import APIRouter
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from datetime import  datetime

from database.config import session
from routers.auth import user_dependency

from models.employers import Employers
from models.companies import Companies


from schemas.employee import EmployersSchema
from passlib.context import CryptContext


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
employers_router = APIRouter()


@employers_router.post("/{company_id}")
async def create_employer(employer_data: EmployersSchema, company_id : int):    

    employer_query = Employers(        
        last_name = employer_data.last_name,
        mother_last_name = employer_data.mother_last_name,
        first_name = employer_data.first_name,
        middle_name = employer_data.middle_name,
        company_id =  company_id,
        employee_type = employer_data.employee_type,
        social_security_number = employer_data.social_security_number,
        marital_status = employer_data.marital_status,
        address = employer_data.address,
        address_state = employer_data.address_state,
        address_country = employer_data.address_country,
        address_number = employer_data.address_number,
        phone_number = employer_data.phone_number,
        smartphone_number = employer_data.smartphone_number,
        marbete = employer_data.marbete,
        date_marb = employer_data.date_marb,
        type = employer_data.type,
        clipboard = employer_data.clipboard,
        exec_personal = employer_data.exec_personal,
        choferil = employer_data.choferil,
        regular_time = employer_data.regular_time,
        period_norma = employer_data.period_norma,
        licence = employer_data.licence,
        category_cfse = employer_data.category_cfse,
        gender = employer_data.gender,
        birthday = employer_data.birthday,
        date_admission = employer_data.date_admission,
        date_egress = employer_data.date_egress,
        about_time = employer_data.about_time,
        mealtime = employer_data.mealtime,
        vacation_hours = employer_data.vacation_hours,
        vacation_date = employer_data.vacation_date,
        number_dependents = employer_data.number_dependents,
        shared_custody = employer_data.shared_custody,
        number_concessions = employer_data.number_concessions,
        veteran = employer_data.veteran,
        type_payroll = employer_data.type_payroll,
        schedule_type = employer_data.schedule_type,
        payment_percentage = employer_data.payment_percentage,
    )   
    session.add(employer_query)
    session.commit()
    session.refresh(employer_query)   
    return {"ok": True, "msg": "user was successfully created", "result": employer_query}

def authenticate_user(username: str, password: str, db):
    employers = employer_query = session.query(Employers).join(Companies).filter(Employers.company_id == company_id, Companies.id == Employers.company_id,Companies.code_id == user["code"]).all()
       
    if not employers:
        return False    
    return employers
@employers_router.get("/{company_id}")
async def get_all_employers(company_id: int,user: user_dependency):
    employer_query = session.query(Employers).join(Companies).filter(Employers.company_id == company_id, Companies.id == Employers.company_id,Companies.code_id == user["code"]).all()

    return {
        "ok": True,
        "msg": "Employers were successfully retrieved",
        "result": employer_query,
    }


@employers_router.get("/{company_id}/{employers_id}")
async def get_employer_by_id(employers_id: int,company_id: int,user: user_dependency):
    employer_query = session.query(Employers).join(Companies).filter(Employers.id == employers_id,Employers.company_id == company_id, Companies.id == Employers.company_id,Companies.code_id == user["code"]).first()

    if not employer_query:
        return {"ok": False, "msg": "user not found", "result": None}

    return {"ok": True, "msg": "Employer was successfully retrieved", "result": employer_query}


@employers_router.put("/{employers_id}")
async def update_employer(employers_id: int, employer: EmployersSchema, user: user_dependency):
    employer_query = session.query(Employers).filter_by(id=employers_id).first()

        
    employer_query.last_name = employer.last_name,
    employer_query.mother_last_name = employer.mother_last_name,
    employer_query.first_name = employer.first_name,
    employer_query.middle_name = employer.middle_name,
    employer_query.employee_type = employer.employee_type,
    employer_query.social_security_number = employer.social_security_number,
    employer_query.marital_status = employer.marital_status,
    employer_query.address = employer.address,
    employer_query.address_state = employer.address_state,
    employer_query.address_country = employer.address_country,
    employer_query.address_number = employer.address_number,
    employer_query.phone_number = employer.phone_number,
    employer_query.smartphone_number = employer.smartphone_number,
    employer_query.marbete = employer.marbete,
    employer_query.date_marb = employer.date_marb,
    employer_query.type = employer.type,
    employer_query.clipboard = employer.clipboard,
    employer_query.exec_personal = employer.exec_personal,
    employer_query.choferil = employer.choferil,
    employer_query.regular_time = employer.regular_time,
    employer_query.period_norma = employer.period_norma,
    employer_query.licence = employer.licence,
    employer_query.category_cfse = employer.category_cfse,
    employer_query.gender = employer.gender,
    employer_query.birthday = employer.birthday,
    employer_query.date_admission = employer.date_admission,
    employer_query.date_egress = employer.date_egress,
    employer_query.about_time = employer.about_time,
    employer_query.mealtime = employer.mealtime,
    employer_query.vacation_hours = employer.vacation_hours,
    employer_query.vacation_date = employer.vacation_date,
    employer_query.number_dependents = employer.number_dependents,
    employer_query.shared_custody = employer.shared_custody,
    employer_query.number_concessions = employer.number_concessions,
    employer_query.veteran = employer.veteran,
    employer_query.type_payroll = employer.type_payroll,
    employer_query.schedule_type = employer.schedule_type,
    employer_query.payment_percentage = employer.payment_percentage,
    

    session.add(employer_query)
    session.commit()
    session.refresh(employer_query)

    return {"ok": True, "msg": "user was successfully updated", "result": employer_query}


@employers_router.delete("/{employers_id}")
async def employers(employers_id: int, user: user_dependency):
    employer_query = session.query(Employers).join(Companies).filter(Employers.id == employers_id, Companies.id == Employers.company_id,Companies.code_id == user["code"]).first()
   
    
    
    employer_query.is_deleted = not employer_query.is_deleted    
    employer_query.deleted_at = datetime.utcnow()
    session.add(employer_query)   
    session.commit()  
    session.refresh(employer_query)   
    return {"ok": True, "msg": "user was successfully created", "result": employer_query}
