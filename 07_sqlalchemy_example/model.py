from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Corresp(Base):
    __tablename__ = 'Corresp'
    id = Column(Integer, primary_key=True)
    number = Column(String)
    subject = Column(String)
    date = Column(Date)
    direction = Column(Boolean) # True = in, False = out
    type_id = Column(Integer, ForeignKey('Type.id'))
    type = relationship('Type', back_populates='corresp')
    internal_id = Column(Integer, ForeignKey('Department.id'))
    internal = relationship('Department', back_populates='corresp')
    external_id = Column(Integer, ForeignKey('External.id'))
    external = relationship('External', back_populates='corresp')

    def __repr__(self):
        return f'<n={self.number}, s={self.subject}, date={self.date}, dir={"in" if self.direction else "out"}>'

class Type(Base):
    __tablename__ = 'Type'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    corresp = relationship('Corresp', back_populates='type')

    def __repr__(self):
        return self.name

class Department(Base):
    __tablename__ = 'Department'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    corresp = relationship('Corresp', back_populates='internal')

    def __repr__(self):
        return self.name

class External(Base):
    __tablename__ = 'External'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    corresp = relationship('Corresp', back_populates='external')

    def __repr__(self):
        return f'{self.name}: {self.address}'
