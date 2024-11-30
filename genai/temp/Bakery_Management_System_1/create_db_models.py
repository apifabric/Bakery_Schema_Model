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


class Bakery(Base):\n    """description: Represents a bakery where products are produced and sold."""\n    __tablename__ = 'bakeries'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    name = Column(String)\n    established_date = Column(Date)\n    location = Column(String)\n


class Product(Base):\n    """description: Represents a product such as bread, pastry, or cake produced by the bakery."""\n    __tablename__ = 'products'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    bakery_id = Column(Integer, ForeignKey('bakeries.id'))\n    name = Column(String)\n    price = Column(Integer)\n    in_stock = Column(Integer)\n


class Ingredient(Base):\n    """description: Represents an ingredient used in the products by the bakery."""\n    __tablename__ = 'ingredients'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    name = Column(String)\n    quantity_available = Column(Integer)\n


class Employee(Base):\n    """description: Represents an employee working at the bakery."""\n    __tablename__ = 'employees'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    bakery_id = Column(Integer, ForeignKey('bakeries.id'))\n    name = Column(String)\n    position = Column(String)\n    start_date = Column(Date)\n


class Supplier(Base):\n    """description: Represents a supplier that provides ingredients to the bakery."""\n    __tablename__ = 'suppliers'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    name = Column(String)\n    contact = Column(String)\n


class SupplierIngredient(Base):\n    """description: Represents the link between suppliers and ingredients they provide."""\n    __tablename__ = 'supplier_ingredients'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    supplier_id = Column(Integer, ForeignKey('suppliers.id'))\n    ingredient_id = Column(Integer, ForeignKey('ingredients.id'))\n


class Customer(Base):\n    """description: Represents a customer who buys products from the bakery."""\n    __tablename__ = 'customers'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    name = Column(String)\n    contact = Column(String)\n


class Order(Base):\n    """description: Represents a customer order within the bakery."""\n    __tablename__ = 'orders'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    customer_id = Column(Integer, ForeignKey('customers.id'))\n    order_date = Column(Date)\n    total_amount = Column(Integer)\n


class OrderItem(Base):\n    """description: Represents the product items for a customer order."""\n    __tablename__ = 'order_items'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    order_id = Column(Integer, ForeignKey('orders.id'))\n    product_id = Column(Integer, ForeignKey('products.id'))\n    quantity = Column(Integer)\n    line_price = Column(Integer)\n


class ProductIngredient(Base):\n    """description: Represents the ingredients required for a product."""\n    __tablename__ = 'product_ingredients'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    product_id = Column(Integer, ForeignKey('products.id'))\n    ingredient_id = Column(Integer, ForeignKey('ingredients.id'))\n    amount_needed = Column(Integer)\n


class Promotion(Base):\n    """description: Represents a promotional offer by the bakery for customers."""\n    __tablename__ = 'promotions'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    description = Column(String)\n    start_date = Column(Date)\n    end_date = Column(Date)\n    discount_percentage = Column(Integer)\n


class EmployeePerformance(Base):\n    """description: Represents performance records for the employees."""\n    __tablename__ = 'employee_performance'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    employee_id = Column(Integer, ForeignKey('employees.id'))\n    performance_date = Column(Date)\n    rating = Column(Integer)\n


# end of model classes


try:
    
    
    
    
    # ALS/GenAI: Create an SQLite database
    
    engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    
    Base.metadata.create_all(engine)
    
    
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    
    
    # ALS/GenAI: Prepare for sample data
    
    
    
    session.commit()
    bakery1 = Bakery(name="Baker's Delight", established_date=date(2010, 5, 15), location="123 Baker St.")
    bakery2 = Bakery(name="Bread Heaven", established_date=date(2015, 7, 20), location="456 Bakery Lane")
    bakery3 = Bakery(name="Pastry Paradise", established_date=date(2018, 9, 10), location="789 Dessert Rd.")
    bakery4 = Bakery(name="Cake Corner", established_date=date(2020, 11, 12), location="321 Cupcake Ave.")
    product1 = Product(bakery_id=1, name="Sourdough Bread", price=5, in_stock=50)
    product2 = Product(bakery_id=2, name="Croissant", price=3, in_stock=100)
    product3 = Product(bakery_id=3, name="Chocolate Cake", price=20, in_stock=30)
    product4 = Product(bakery_id=4, name="Bagel", price=2, in_stock=200)
    ingredient1 = Ingredient(name="Flour", quantity_available=500)
    ingredient2 = Ingredient(name="Sugar", quantity_available=300)
    ingredient3 = Ingredient(name="Butter", quantity_available=250)
    ingredient4 = Ingredient(name="Yeast", quantity_available=150)
    employee1 = Employee(bakery_id=1, name="John Doe", position="Baker", start_date=date(2011, 6, 1))
    employee2 = Employee(bakery_id=2, name="Jane Smith", position="Cashier", start_date=date(2016, 8, 14))
    employee3 = Employee(bakery_id=3, name="Alex Johnson", position="Manager", start_date=date(2019, 10, 9))
    employee4 = Employee(bakery_id=4, name="Emily Davis", position="Pastry Chef", start_date=date(2021, 12, 2))
    supplier1 = Supplier(name="Supplier One", contact="111-222-3333")
    supplier2 = Supplier(name="Supplier Two", contact="222-333-4444")
    supplier3 = Supplier(name="Supplier Three", contact="333-444-5555")
    supplier4 = Supplier(name="Supplier Four", contact="444-555-6666")
    supplier_ingredient1 = SupplierIngredient(supplier_id=1, ingredient_id=1)
    supplier_ingredient2 = SupplierIngredient(supplier_id=2, ingredient_id=2)
    supplier_ingredient3 = SupplierIngredient(supplier_id=3, ingredient_id=3)
    supplier_ingredient4 = SupplierIngredient(supplier_id=4, ingredient_id=4)
    customer1 = Customer(name="Michael Brown", contact="555-123-4567")
    customer2 = Customer(name="Lisa White", contact="555-234-5678")
    customer3 = Customer(name="Kevin Green", contact="555-345-6789")
    customer4 = Customer(name="Karen Blue", contact="555-456-7890")
    order1 = Order(customer_id=1, order_date=date(2022, 5, 5), total_amount=30)
    order2 = Order(customer_id=2, order_date=date(2022, 6, 15), total_amount=45)
    order3 = Order(customer_id=3, order_date=date(2022, 7, 25), total_amount=25)
    order4 = Order(customer_id=4, order_date=date(2022, 8, 20), total_amount=60)
    order_item1 = OrderItem(order_id=1, product_id=1, quantity=2, line_price=10)
    order_item2 = OrderItem(order_id=2, product_id=2, quantity=5, line_price=15)
    order_item3 = OrderItem(order_id=3, product_id=3, quantity=1, line_price=20)
    order_item4 = OrderItem(order_id=4, product_id=4, quantity=10, line_price=20)
    product_ingredient1 = ProductIngredient(product_id=1, ingredient_id=1, amount_needed=2)
    product_ingredient2 = ProductIngredient(product_id=2, ingredient_id=2, amount_needed=1)
    product_ingredient3 = ProductIngredient(product_id=3, ingredient_id=3, amount_needed=3)
    product_ingredient4 = ProductIngredient(product_id=4, ingredient_id=4, amount_needed=1)
    promotion1 = Promotion(description="Summer Sale", start_date=date(2023, 6, 1), end_date=date(2023, 7, 31), discount_percentage=10)
    promotion2 = Promotion(description="Holiday Discount", start_date=date(2023, 12, 1), end_date=date(2023, 12, 31), discount_percentage=15)
    promotion3 = Promotion(description="Halloween Special", start_date=date(2023, 10, 25), end_date=date(2023, 11, 1), discount_percentage=20)
    promotion4 = Promotion(description="Black Friday", start_date=date(2023, 11, 25), end_date=date(2023, 11, 25), discount_percentage=25)
    performance1 = EmployeePerformance(employee_id=1, performance_date=date(2022, 9, 30), rating=4)
    performance2 = EmployeePerformance(employee_id=2, performance_date=date(2022, 10, 30), rating=5)
    performance3 = EmployeePerformance(employee_id=3, performance_date=date(2022, 11, 30), rating=3)
    performance4 = EmployeePerformance(employee_id=4, performance_date=date(2022, 12, 30), rating=4)
    
    
    
    session.add_all([bakery1, bakery2, bakery3, bakery4, product1, product2, product3, product4, ingredient1, ingredient2, ingredient3, ingredient4, employee1, employee2, employee3, employee4, supplier1, supplier2, supplier3, supplier4, supplier_ingredient1, supplier_ingredient2, supplier_ingredient3, supplier_ingredient4, customer1, customer2, customer3, customer4, order1, order2, order3, order4, order_item1, order_item2, order_item3, order_item4, product_ingredient1, product_ingredient2, product_ingredient3, product_ingredient4, promotion1, promotion2, promotion3, promotion4, performance1, performance2, performance3, performance4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
