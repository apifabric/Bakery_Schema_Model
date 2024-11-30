# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 30, 2024 15:27:12
# Database: sqlite:////tmp/tmp.NOALnYvrOx-01JDYTT18BXQFZBD8TA1ZWJ5D9/Bakery_Management_System/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Bakery(SAFRSBaseX, Base):
    """
    description: Store information about different bakeries
    """
    __tablename__ = 'bakery'
    _s_collection_name = 'Bakery'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    established_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    CustomerList : Mapped[List["Customer"]] = relationship(back_populates="preferred_bakery")
    EmployeeList : Mapped[List["Employee"]] = relationship(back_populates="bakery")
    ProductList : Mapped[List["Product"]] = relationship(back_populates="bakery")
    InventoryList : Mapped[List["Inventory"]] = relationship(back_populates="bakery")
    OrderList : Mapped[List["Order"]] = relationship(back_populates="bakery")
    SupplyList : Mapped[List["Supply"]] = relationship(back_populates="bakery")



class Supplier(SAFRSBaseX, Base):
    """
    description: Information about suppliers for the bakeries
    """
    __tablename__ = 'supplier'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact_number = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    SupplyList : Mapped[List["Supply"]] = relationship(back_populates="supplier")



class Customer(SAFRSBaseX, Base):
    """
    description: Customer information including names and preferred bakery
    """
    __tablename__ = 'customer'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    preferred_bakery_id = Column(ForeignKey('bakery.id'))

    # parent relationships (access parent)
    preferred_bakery : Mapped["Bakery"] = relationship(back_populates=("CustomerList"))

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")



class Employee(SAFRSBaseX, Base):
    """
    description: Details about bakery employees, including their role and contact
    """
    __tablename__ = 'employee'
    _s_collection_name = 'Employee'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    bakery_id = Column(ForeignKey('bakery.id'))
    name = Column(String)
    role = Column(String)

    # parent relationships (access parent)
    bakery : Mapped["Bakery"] = relationship(back_populates=("EmployeeList"))

    # child relationships (access children)
    ShiftList : Mapped[List["Shift"]] = relationship(back_populates="employee")



class Product(SAFRSBaseX, Base):
    """
    description: Represent baked products available in various bakeries
    """
    __tablename__ = 'product'
    _s_collection_name = 'Product'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    bakery_id = Column(ForeignKey('bakery.id'))
    name = Column(String)
    type = Column(String)
    price = Column(Integer)

    # parent relationships (access parent)
    bakery : Mapped["Bakery"] = relationship(back_populates=("ProductList"))

    # child relationships (access children)
    InventoryList : Mapped[List["Inventory"]] = relationship(back_populates="product")
    SupplyList : Mapped[List["Supply"]] = relationship(back_populates="product")
    OrderDetailList : Mapped[List["OrderDetail"]] = relationship(back_populates="product")



class Inventory(SAFRSBaseX, Base):
    """
    description: Inventory details for each bakery for stock keeping
    """
    __tablename__ = 'inventory'
    _s_collection_name = 'Inventory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    bakery_id = Column(ForeignKey('bakery.id'))
    product_id = Column(ForeignKey('product.id'))
    stock_quantity = Column(Integer)

    # parent relationships (access parent)
    bakery : Mapped["Bakery"] = relationship(back_populates=("InventoryList"))
    product : Mapped["Product"] = relationship(back_populates=("InventoryList"))

    # child relationships (access children)



class Order(SAFRSBaseX, Base):
    """
    description: Orders placed by customers in bakeries
    """
    __tablename__ = 'order'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'))
    bakery_id = Column(ForeignKey('bakery.id'))
    order_date = Column(DateTime)

    # parent relationships (access parent)
    bakery : Mapped["Bakery"] = relationship(back_populates=("OrderList"))
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    OrderDetailList : Mapped[List["OrderDetail"]] = relationship(back_populates="order")



class Shift(SAFRSBaseX, Base):
    """
    description: Scheduled work shifts for employees in bakeries
    """
    __tablename__ = 'shift'
    _s_collection_name = 'Shift'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    employee_id = Column(ForeignKey('employee.id'))
    shift_date = Column(DateTime)
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    # parent relationships (access parent)
    employee : Mapped["Employee"] = relationship(back_populates=("ShiftList"))

    # child relationships (access children)



class Supply(SAFRSBaseX, Base):
    """
    description: Supplies provided by suppliers to bakeries
    """
    __tablename__ = 'supply'
    _s_collection_name = 'Supply'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    supplier_id = Column(ForeignKey('supplier.id'))
    bakery_id = Column(ForeignKey('bakery.id'))
    product_id = Column(ForeignKey('product.id'))
    supply_date = Column(DateTime)
    quantity = Column(Integer)

    # parent relationships (access parent)
    bakery : Mapped["Bakery"] = relationship(back_populates=("SupplyList"))
    product : Mapped["Product"] = relationship(back_populates=("SupplyList"))
    supplier : Mapped["Supplier"] = relationship(back_populates=("SupplyList"))

    # child relationships (access children)



class OrderDetail(SAFRSBaseX, Base):
    """
    description: Details of each order placed, including product and quantity
    """
    __tablename__ = 'order_detail'
    _s_collection_name = 'OrderDetail'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('order.id'))
    product_id = Column(ForeignKey('product.id'))
    quantity = Column(Integer)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("OrderDetailList"))
    product : Mapped["Product"] = relationship(back_populates=("OrderDetailList"))

    # child relationships (access children)
