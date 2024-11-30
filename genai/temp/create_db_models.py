# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py

from sqlalchemy.dialects.sqlite import *


class Bakery(Base):
    """description: Store information about different bakeries"""
    __tablename__ = 'bakery'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    location = Column(String)
    established_date = Column(DateTime)


class Product(Base):
    """description: Represent baked products available in various bakeries"""
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    bakery_id = Column(Integer, ForeignKey('bakery.id'))
    name = Column(String)
    type = Column(String)
    price = Column(Integer)


class Customer(Base):
    """description: Customer information including names and preferred bakery"""
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    preferred_bakery_id = Column(Integer, ForeignKey('bakery.id'))


class Order(Base):
    """description: Orders placed by customers in bakeries"""
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    bakery_id = Column(Integer, ForeignKey('bakery.id'))
    order_date = Column(DateTime)


class OrderDetail(Base):
    """description: Details of each order placed, including product and quantity"""
    __tablename__ = 'order_detail'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer)


class Supplier(Base):
    """description: Information about suppliers for the bakeries"""
    __tablename__ = 'supplier'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    contact_number = Column(String)


class Supply(Base):
    """description: Supplies provided by suppliers to bakeries"""
    __tablename__ = 'supply'

    id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_id = Column(Integer, ForeignKey('supplier.id'))
    bakery_id = Column(Integer, ForeignKey('bakery.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    supply_date = Column(DateTime)
    quantity = Column(Integer)


class Inventory(Base):
    """description: Inventory details for each bakery for stock keeping"""
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True, autoincrement=True)
    bakery_id = Column(Integer, ForeignKey('bakery.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    stock_quantity = Column(Integer)


class Employee(Base):
    """description: Details about bakery employees, including their role and contact"""
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    bakery_id = Column(Integer, ForeignKey('bakery.id'))
    name = Column(String)
    role = Column(String)


class Shift(Base):
    """description: Scheduled work shifts for employees in bakeries"""
    __tablename__ = 'shift'

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    shift_date = Column(DateTime)
    start_time = Column(DateTime)
    end_time = Column(DateTime)


# end of model classes


try:
    
    
    
    
    # ALS/GenAI: Create an SQLite database
    
    engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    
    Base.metadata.create_all(engine)
    
    
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    
    
    # ALS/GenAI: Prepare for sample data
    
    
    
    session.commit()
    bakery1 = Bakery(name="Sweet Cravings", location="Downtown", established_date=date(2020, 2, 15))
    bakery2 = Bakery(name="Bread Haven", location="Uptown", established_date=date(2018, 5, 12))
    product1 = Product(bakery_id=1, name="Banana Bread", type="Bread", price=5)
    product2 = Product(bakery_id=1, name="Croissant", type="Pastry", price=3)
    customer1 = Customer(name="Alice Walker", preferred_bakery_id=1)
    customer2 = Customer(name="Bob Smith", preferred_bakery_id=1)
    order1 = Order(customer_id=1, bakery_id=1, order_date=date(2023, 10, 2))
    order2 = Order(customer_id=2, bakery_id=1, order_date=date(2023, 10, 3))
    order_detail1 = OrderDetail(order_id=1, product_id=1, quantity=2)
    order_detail2 = OrderDetail(order_id=2, product_id=2, quantity=5)
    supplier1 = Supplier(name="Grain Supplies Ltd.", contact_number="555-1234")
    supplier2 = Supplier(name="Yeast Essentials Inc.", contact_number="555-5678")
    supply1 = Supply(supplier_id=1, bakery_id=1, product_id=1, supply_date=date(2023, 9, 5), quantity=50)
    supply2 = Supply(supplier_id=2, bakery_id=1, product_id=2, supply_date=date(2023, 9, 7), quantity=40)
    inventory1 = Inventory(bakery_id=1, product_id=1, stock_quantity=30)
    inventory2 = Inventory(bakery_id=1, product_id=2, stock_quantity=20)
    employee1 = Employee(bakery_id=1, name="John Doe", role="Baker")
    employee2 = Employee(bakery_id=1, name="Sara Conner", role="Cashier")
    shift1 = Shift(employee_id=1, shift_date=date(2023, 10, 1), start_time=date(2023, 10, 1), end_time=date(2023, 10, 1))
    shift2 = Shift(employee_id=2, shift_date=date(2023, 10, 2), start_time=date(2023, 10, 2), end_time=date(2023, 10, 2))
    
    
    
    session.add_all([bakery1, bakery2, product1, product2, customer1, customer2, order1, order2, order_detail1, order_detail2, supplier1, supplier2, supply1, supply2, inventory1, inventory2, employee1, employee2, shift1, shift2])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
