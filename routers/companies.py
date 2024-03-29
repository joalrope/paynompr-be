import bcrypt
from datetime import  datetime

from sqlalchemy.orm import aliased

from fastapi import APIRouter
from database.config import session
from schemas.companies import CompaniesSchema , CompaniesWithEmployersSchema 

from models.companies import Companies
from models.employers import Employers
from models.time import Time

from routers.auth import user_dependency

companies_router = APIRouter()


@companies_router.post("/")
async def create_company(companie_data: CompaniesSchema,user: user_dependency):    
    
    companie_query = Companies(
        name= companie_data.name,
        commercial_register = companie_data.commercial_register,
        jurisdiction = companie_data.jurisdiction,
        accountant_id = companie_data.accountant_id,
        email= companie_data.email,
        contact= companie_data.contact,
        contact_number = companie_data.contact_number,
        website = companie_data.website,
        number_patronal= companie_data.number_patronal,
        coml = companie_data.coml,
        postal_address = companie_data.postal_address,
        zipcode_postal_address = companie_data.zipcode_postal_address,
        country_postal_address = companie_data.country_postal_address,
        state_postal_addess = companie_data.state_postal_addess,
        physical_address = companie_data.physical_address,
        zipcode_physical_address = companie_data.zipcode_physical_address,
        country_physical_address = companie_data.country_physical_address,
        state_physical_address = companie_data.state_physical_address,
        phone_number = companie_data.phone_number,
        fax_number = companie_data.fax_number,
        industrial_code = companie_data.industrial_code,
        payer = companie_data.payer,
        desem = companie_data.desem,
        disabled_percent = companie_data.disabled_percent,
        driver = companie_data.driver,
        code_id = user["code"],
        polize_number = companie_data.polize_number,
        driver_code = companie_data.driver_code,
        driver_rate = companie_data.driver_rate,   
    )
    

    
    session.add(companie_query)
   

    session.commit()
    
    session.refresh(companie_query)
    return {"ok": True, "msg": "user was successfully created", "result": companie_query}


@companies_router.get("/",response_model=list[CompaniesWithEmployersSchema])
async def get_all_companies(user: user_dependency):
    companies_query = session.query(Companies).filter(Companies.code_id == user["code"]).all()

    return companies_query




@companies_router.get("/{company_id}/{employers_id}")
async def get_all_company_and_employer(user: user_dependency,company_id: int,employers_id: int):    
    companies_query = session.query(Employers, Companies).join(Companies, onclause=Companies.id == company_id).filter(Companies.code_id == user["code"], Employers.id == employers_id).first()
    employer, company = companies_query # Desempaquetar la tupla  
    time_query = session.query(Time).filter(Time.employer_id == employers_id).all()


    return {"ok": True, "msg": "user was successfully created", "result": {"company": company, "employer": employer, "time": time_query}}

    

@companies_router.get("/employers/{companies_id}")
async def get_company(user: user_dependency,companies_id: int):
    companies_query = session.query(Companies).filter(Companies.code_id == user["code"], Companies.id == companies_id).one_or_none()

    return {
        "ok": True,
        "msg": "Companies were successfully retrieved",
        "result": companies_query,
    }


@companies_router.get("/{companies_id}")
async def get_companies_by_id(companies_id: int):
    company_query = session.query(Companies).filter_by(id=companies_id).first()

    if not company_query:
        return {"ok": False, "msg": "Companies not found", "result": None}

    return {"ok": True, "msg": "user was successfully retrieved", "result": company_query}


@companies_router.put("/{companies_id}")
async def update_company(companies_id: int, new_user_data: CompaniesSchema):
    company_query = session.query(Companies).filter_by(id=companies_id).one_or_none()
    
    if not company_query:
        return {"ok": False, "msg": "Companies not found", "result": new_user_data}
    company_query.name= new_user_data.name
    company_query.commercial_register = new_user_data.commercial_register
    company_query.jurisdiction = new_user_data.jurisdiction
    company_query.accountant_id = new_user_data.accountant_id
    company_query.email= new_user_data.email
    company_query.contact= new_user_data.contact
    company_query.contact_number = new_user_data.contact_number
    company_query.website = new_user_data.website
    company_query.postal_address = new_user_data.postal_address
    company_query.zipcode_postal_address = new_user_data.zipcode_postal_address
    company_query.country_postal_address = new_user_data.country_postal_address
    company_query.state_postal_addess = new_user_data.state_postal_addess
    company_query.number_patronal= new_user_data.number_patronal
    company_query.coml = new_user_data.coml
    company_query.physical_address = new_user_data.physical_address
    company_query.zipcode_physical_address = new_user_data.zipcode_physical_address
    company_query.country_physical_address = new_user_data.country_physical_address
    company_query.state_physical_address = new_user_data.state_physical_address
    company_query.phone_number = new_user_data.phone_number
    company_query.fax_number = new_user_data.fax_number
    company_query.industrial_code = new_user_data.industrial_code
    company_query.payer = new_user_data.payer
    company_query.desem = new_user_data.desem
    company_query.disabled_percent = new_user_data.disabled_percent
    company_query.driver = new_user_data.driver
  
    company_query.polize_number = new_user_data.polize_number
    company_query.driver_code = new_user_data.driver_code
    company_query.driver_rate = new_user_data.driver_rate

    session.add(company_query)
    session.commit()
    session.refresh(company_query)

    return {"ok": True, "msg": "Companies was successfully updated", "result": company_query}


@companies_router.delete("/{id}")
async def disable_company(id: int):
    companie_query = session.query(Companies).filter(Companies.id == id).first()
   
    
    
    companie_query.is_deleted = not companie_query.is_deleted    
    companie_query.deleted_at = datetime.utcnow()
    session.add(companie_query)   
    session.commit()  
    session.refresh(companie_query)   
    return {"ok": True, "msg": "user was successfully created", "result": companie_query}