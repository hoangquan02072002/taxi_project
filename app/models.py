import os
import sqlalchemy as sa
from app import db

class TaxiService(db.Model):
    __tablename__ = 'taxi_service'

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    driver = db.Column(db.String(100), nullable=False)
    number = db.Column(db.String(20), unique=True, nullable=False)
    online = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"TaxiService(id={self.id}, model='{self.model}', driver='{self.driver}', number='{self.number}', online={self.online})"


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    number_car = db.Column(db.String(20), unique=True, nullable=False)
    driver = db.Column(db.String(100), nullable=False)
    passenger = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    cmc_code = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"Order(id={self.id}, number_car='{self.number_car}', driver='{self.driver}', passenger='{self.passenger}', address='{self.address}', cmc_code='{self.cmc_code}')"
