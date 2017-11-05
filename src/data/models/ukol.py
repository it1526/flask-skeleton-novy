from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime

from ..database import db
from ..mixins import CRUDModel

class Lide(CRUDModel):
    __tablename__ = 'lide'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True,index = True)
    jmeno = Column(String, nullable=False, index=False)
    prijmeni = Column(String, nullable=False,index = False)
    pokuty = relationship('Pokuty', backref='lide', lazy=True)
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

class Pokuty(CRUDModel):
    __tablename__ = 'pokuty'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True )
    idPokutovaneho =  Column(Integer, ForeignKey('lide.id'),nullable=False)
    duvod = Column(String, nullable=False,index = False)
    castka = Column(Integer)
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)