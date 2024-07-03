from flask import Flask, request, make_response, jsonify
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from src.orm_models.base import Base
from src.orm_models.employee import Employee
from src.orm_models.organization import Organization
from src.serializer.employee import EmployeeResponseSerializer, EmployeeSerializer
from src.serializer.organization import OrganizationSerializer
from logging import getLogger

logger = getLogger(__name__)

Session = sessionmaker()

engine = create_engine('postgres://fiddler_db_admin:fiddler_db_admin@localhost:5432/employee')
Session.configure(bind=engine)

session = Session()


app = Flask(__name__)
Base.metadata.create_all(engine)


@app.route('/employee', methods=['POST'])
def add_employee():
    employee = Employee(**EmployeeSerializer().dump(request.json))
    session.add(employee)
    session.commit()
    return make_response({})

@app.route('/organization', methods=['POST'])
def add_organization():
    organization = Organization(**OrganizationSerializer().dump(request.json))
    session.add(organization)
    session.commit()
    return make_response({})

@app.route('/employees', methods=['GET'])
def get_employees():
    organization_name = request.args.get('organization_name', None)
    organization_location = request.args.get('organization_location', None)
    organization_category = request.args.get('organization_category', None)
    employee_name = request.args.get('employee_name', None)
    employee_location = request.args.get('employee_location', None)
    query = session.query(Employee).join(Organization, Employee.organization_id == Organization.id)
    logger.info(organization_name)
    if organization_name:
        query.filter(Organization.name == organization_name)
    if organization_location:
        query.filter(Organization.location == organization_location)
    if organization_category:
        query.filter(Organization.category == organization_category)
    if employee_name:
        query.filter(Employee.name == employee_name)
    if employee_location:
        query.filter(Employee.location == employee_location)

    objects = query.all()
    emp_ser = EmployeeResponseSerializer()
    response = {}
    items = [emp_ser.dump(obj) for obj in objects]
    response['items'] = items

    return make_response(jsonify(response))
        
    

    
    
    