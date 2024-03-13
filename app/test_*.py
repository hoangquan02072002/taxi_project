from app import informationdriver,authentication
from models import TaxiService,Order 
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

@pytest.fixture
def db_session():
    engine = create_engine('postgresql://postgres:linky1337@localhost:5432/taxi_project')
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_getall_information_driverTaxi(db_session):
    try:
        unique_number='м196oc55'
        driver = TaxiService(model='Kia Optima', driver='cuongcui', number=unique_number, online=False)
        db_session.add(driver)
        db_session.commit()
        result = informationdriver()
        assert driver in result
    except IntegrityError:
        db_session.rollback()

# def test_authenticate(db_session):
#     try:
#         order = Order(number_car='423742', driver='Driver 1', passenger='Passenger 1', address='Address 1', cmc_code='0207')
#         db_session.add(order)
#         db_session.commit()
#         client.post('/authentication', data={'code': '0207'})
#         result=authentication()
#         assert response.status_code == 200
#     except IntegrityError:
#         db_session.rollback()




