from datetime import date
from passlib.context import CryptContext


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Database initial data
INITIAL_DATA = {
    "users": [
        {
            "name": "admin",
            "lastname": "admin",
            "email": "admin@admin.com",
            "phone": "123456789",
            "role_id": 1,
            "code_id": 1,
            "password": bcrypt_context.hash("123456"),
        }
    ],
    "users_coders": [
        {
            "code_id": 1,
            "user_id": 1,
        }
    ],
    "codes": [
        {
            "code": "WZgeig",
            "owner": "Admin",
            "email": "admin@admin.com",
            "amount": 3000,
        }
    ],
    "roles": [
        {
            "role": "Owner",
        },
        {
            "role": "SuperAdmin",
        },
        {"role": "Accountant"},
    ],
    "companies": [
        {
           
            "name": "Empresa S.A.",
            "commercial_register": "357951",
            "registration_date": date.fromisoformat("1975-05-12"),
            "jurisdiction": "España",
            "code_id": 1,
            "coml": None,
            "number_patronal": "6598",
            "accountant_id": 1,
            "email": "empresa@gmail.com",
            "contact": "paco miendo",
            "contact_number": "555987321",
            "website": "https://www.google.com",
            "postal_address": "Street Avenue 9865",
            "zipcode_postal_address": "20011",
            "country_postal_address": "Puerto Rico",
            "state_postal_addess": "Gaseoso",
            "physical_address": "Street Avenue 9865",
            "zipcode_physical_address": "20011",
            "country_physical_address": "Puerto Rico",
            "state_physical_address": "Gaseoso",
            "phone_number": "9865322158 ",
            "fax_number": "8945221255",
            "industrial_code": "CNAE 65911",
            "payer": "ACME Inc.",
            "desem": "0.5",
            "employed_contribution": "0",
            "disabled_percent": "0.5",
            "unemployment_percentage": "10",
            "polize_number": "654285139",
            "driver_code": "A1",
            "driver_rate": "0.8",
            "is_deleted": False,
        },
        {
           
            "name": "ACME Company",
            "commercial_register": "453228",
            "registration_date": date.fromisoformat("1986-12-20"),
            "jurisdiction": "Puerto Rico",
            "code_id": 1,
            "coml": None,
            "number_patronal": "1850",
            "accountant_id": 1,
            "email": "acme@acme.com",
            "contact": "Coyote Correcaminos",
            "contact_number": "555987321",
            "website": "https://www.google.com",
            "postal_address": "Street Avenue 9865",
            "zipcode_postal_address": "20011",
            "country_postal_address": "Puerto Rico",
            "state_postal_addess": "Gaseoso",
            "physical_address": "Street Avenue 9865",
            "zipcode_physical_address": "20011",
            "country_physical_address": "Puerto Rico",
            "state_physical_address": "Gaseoso",
            "phone_number": "9865322158 ",
            "fax_number": "8945221255",
            "industrial_code": "CNAE 65911",
            "payer": "ACME Inc.",
            "desem": "0.5",
            "employed_contribution": "0",
            "disabled_percent": "0.5",
            "unemployment_percentage": "10",
            "polize_number": "654285139",
            "driver_code": "A1",
            "driver_rate": "0.8",
            "is_deleted": False,
        },
    ],
    "employers": [
        {
           
            "last_name": "Perez",
            "mother_last_name": "Sanchez",
            "first_name": "Juan",
            "middle_name": "Carlos",
            "company_id": 1,
            "employee_type": "",
            "social_security_number": "12-5456-511",
            "marital_status": 1,
            "address": "En algun lugar de la ciudad",
            "address_state": "Estado 1",
            "address_country": "En la calle real",
            "address_number": "5",
            "phone_number": "12345678",
            "smartphone_number": "123456789",
            "marbete": "",
            "type": 1,
            "date_marb": date.fromisoformat("2022-12-31"),
            "is_deleted": False,
            "clipboard": "",
            "exec_personal": 1,
            "choferil": "",
            "regular_time": 20.5,
            "period_norma": 24,
            "licence": "",
            "category_cfse": "",
            "gender": 1,
            "birthday": date.fromisoformat("1990-10-01"),
            "date_admission": date.fromisoformat("2023-02-15"),
            "date_egress": None,
            "overtime": 8,
            "mealtime": 6,
            "vacation_hours": 12,
            "vacation_date": date.fromisoformat("2023-02-15"),
            "sicks_hours": 28,
            "sicks_date": date.fromisoformat("2023-08-05"),
            "number_dependents": 5,
            "shared_custody": False,
            "number_concessions": 1,
            "veteran": False,
            "type_payroll": 1,
            "schedule_type": 1,
            "payment_percentage": "10%",
        },
        {
           
            "last_name": "Saavedra",
            "mother_last_name": "REbolledo",
            "first_name": "Dagoberto",
            "middle_name": "Ramon",
            "company_id": 1,
            "employee_type": "",
            "social_security_number": "45-6981-398",
            "marital_status": 1,
            "address": "Desde el corazon de la ciudad",
            "address_state": "Estado 2",
            "address_country": "La calle del medio",
            "address_number": "94",
            "phone_number": "887321564",
            "smartphone_number": "555666777",
            "marbete": "",
            "type": 1,
            "date_marb": date.fromisoformat("2021-05-14"),
            "is_deleted": False,
            "clipboard": "",
            "exec_personal": 1,
            "choferil": "",
            "regular_time": 17.25,
            "period_norma": 8,
            "licence": "",
            "category_cfse": "",
            "gender": 1,
            "birthday": date.fromisoformat("1985-06-12"),
            "date_admission": date.fromisoformat("2023-06-08"),
            "date_egress": None,
            "overtime": 8,
            "mealtime": 6,
            "vacation_hours": 12,
            "vacation_date": date.fromisoformat("2024-06-08"),
            "sicks_hours": 28,
            "sicks_date": date.fromisoformat("2023-08-05"),
            "number_dependents": 5,
            "shared_custody": False,
            "number_concessions": 1,
            "veteran": False,
            "type_payroll": 1,
            "schedule_type": 1,
            "payment_percentage": "10%",
        },
        {
          
            "last_name": "Vergara",
            "mother_last_name": "Restrepo",
            "first_name": "Sophia",
            "middle_name": "Magdalena",
            "company_id": 2,
            "employee_type": "",
            "social_security_number": "22-3898-111",
            "marital_status": 2,
            "address": "En el centro del getho",
            "address_state": "Estado 2",
            "address_country": "La calle del sabor",
            "address_number": "17",
            "phone_number": "1754571564",
            "smartphone_number": "66612154855",
            "marbete": "",
            "type": 1,
            "date_marb": date.fromisoformat("2021-05-14"),
            "is_deleted": False,
            "clipboard": "",
            "exec_personal": 1,
            "choferil": "",
            "regular_time": 17.25,
            "period_norma": 8,
            "licence": "",
            "category_cfse": "",
            "gender": 1,
            "birthday": date.fromisoformat("1985-06-12"),
            "date_admission": date.fromisoformat("2023-06-08"),
            "date_egress": None,
            "overtime": 8,
            "mealtime": 6,
            "vacation_hours": 12,
            "vacation_date": date.fromisoformat("2024-06-08"),
            "sicks_hours": 28,
            "sicks_date": date.fromisoformat("2023-08-05"),
            "number_dependents": 5,
            "shared_custody": False,
            "number_concessions": 1,
            "veteran": False,
            "type_payroll": 1,
            "schedule_type": 1,
            "payment_percentage": "10%",
        },
    ],
    "employers_time": [
        {
            
            "regular_hours": 30,
            "regular_min": 0,
            "over_hours": 0,
            "over_min": 0,
            "meal_hours": 0,
            "meal_min": 0,
            "sick_hours": 0,
            "sick_min": 0,
            "holiday_hours": 0,
            "holiday_min": 0,  #
            "vacations_hours": 0,
            "vacations_min": 0,
            "commissions": 0,
            "concessions": 0,
            "holyday_pay": 0,
            "sick_pay": 0,
            "tips": 0,
            "vacation_pay": 0,
            "meal_time_pay": 0,
            "overtime_pay": 0,
            "regular_pay": 300,
            "inability": 0.9,
            "medicare": 4.35,
            "secure_social": 18.65,
            "social_tips": 0,
            "tax_pr": 30,
            "employer_id": 1,
            "period_id": 1,
            "company_id": 1,
        },
        {
           
            "regular_hours": 16,
            "regular_min": 0,
            "over_hours": 1,
            "over_min": 0,
            "meal_hours": 1,
            "meal_min": 0,
            "sick_hours": 8,
            "sick_min": 0,
            "holiday_hours": 8,
            "holiday_min": 0,  #
            "vacations_hours": 8,
            "vacations_min": 0,
            "commissions": 100,
            "concessions": 100,
            "holyday_pay": 80,
            "sick_pay": 80,
            "tips": 100,
            "vacation_pay": 80,
            "meal_time_pay": 20,
            "overtime_pay": 15,
            "regular_pay": 160,
            "inability": 2.205,
            "medicare": 10.657499999999999,
            "secure_social": 45.57,
            "social_tips": 6.2,
            "tax_pr": 73.5,
            "employer_id": 2,
            "period_id": 1,
            "company_id": 1,
        },
        {
           
            "regular_hours": 40,
            "regular_min": 0,
            "over_hours": 1,
            "over_min": 0,
            "meal_hours": 1,
            "meal_min": 0,
            "sick_hours": 8,
            "sick_min": 0,
            "holiday_hours": 0,
            "holiday_min": 0,  #
            "vacations_hours": 8,
            "vacations_min": 0,
            "commissions": 100,
            "concessions": 100,
            "holyday_pay": 0,
            "sick_pay": 0,
            "tips": 100,
            "vacation_pay": 0,
            "meal_time_pay": 0,
            "overtime_pay": 0,
            "regular_pay": 400,
            "inability": 2.1,
            "medicare": 10.149999999999999,
            "secure_social": 43.4,
            "social_tips": 6.2,
            "tax_pr": 70.0,
            "employer_id": 2,
            "period_id": 2,
            "company_id": 1,
        },
        {
           
            "regular_hours": 0,
            "regular_min": 0,
            "over_hours": 0,
            "over_min": 0,
            "meal_hours": 0,
            "meal_min": 0,
            "sick_hours": 40,
            "sick_min": 0,
            "holiday_hours": 0,
            "holiday_min": 0,  #
            "vacations_hours": 0,
            "vacations_min": 0,
            "commissions": 0,
            "concessions": 0,
            "holyday_pay": 0,
            "sick_pay": 400,
            "tips": 100,
            "vacation_pay": 0,
            "meal_time_pay": 0,
            "overtime_pay": 0,
            "regular_pay": 0,
            "inability": 1.5,
            "medicare": 7.249999999999999,
            "secure_social": 31,
            "social_tips": 6.2,
            "tax_pr": 50.0,
            "employer_id": 2,
            "period_id": 3,
            "company_id": 1,
        },
        {
          
            "regular_hours": 0,
            "regular_min": 0,
            "over_hours": 0,
            "over_min": 0,
            "meal_hours": 0,
            "meal_min": 0,
            "sick_hours": 40,
            "sick_min": 0,
            "holiday_hours": 0,
            "holiday_min": 0,  #
            "vacations_hours": 40,
            "vacations_min": 0,
            "commissions": 0,
            "concessions": 0,
            "holyday_pay": 0,
            "sick_pay": 0,
            "tips": 100,
            "vacation_pay": 400,
            "meal_time_pay": 0,
            "overtime_pay": 0,
            "regular_pay": 0,
            "inability": 1.5,
            "medicare": 7.249999999999999,
            "secure_social": 31,
            "social_tips": 6.2,
            "tax_pr": 50.0,
            "employer_id": 2,
            "period_id": 4,
            "company_id": 1,
        },
    ],
    "periods": [
        {
           
            "year": 2024,
            "period_number": 1,
            "period_start": date.fromisoformat("2024-01-01"),
            "period_end": date.fromisoformat("2024-01-07"),
        },
        {
           
            "year": 2024,
            "period_number": 2,
            "period_start": date.fromisoformat("2024-01-08"),
            "period_end": date.fromisoformat("2024-01-14"),
        },
        {
           
            "year": 2024,
            "period_number": 3,
            "period_start": date.fromisoformat("2024-01-15"),
            "period_end": date.fromisoformat("2024-01-21"),
        },
        {
           
            "year": 2024,
            "period_number": 4,
            "period_start": date.fromisoformat("2024-01-22"),
            "period_end": date.fromisoformat("2024-01-28"),
        },
        {
           
            "year": 2024,
            "period_number": 5,
            "period_start": date.fromisoformat("2024-01-29"),
            "period_end": date.fromisoformat("2024-02-04"),
        },
    ],
}


# This method receives a table, a connection and inserts data to that table.
def initialize_table(target, connection, **kw):
    tablename = str(target)
    if tablename in INITIAL_DATA and len(INITIAL_DATA[tablename]) > 0:
        connection.execute(target.insert(), INITIAL_DATA[tablename])
