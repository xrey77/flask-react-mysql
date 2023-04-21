from sqlalchemy import Column, Integer, String, DateTime, LargeBinary, Numeric, text
from sqlalchemy.sql import func
from config import Base

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    lastname = Column(String(32),nullable=False)
    firstname = Column(String(32),nullable=False)
    email = Column(String(100),nullable=False, unique=True)
    mobileno = Column(String(32))
    username = Column(String(32),nullable=False, unique=True)
    password = Column(String(200),nullable=False)    
    role = Column(String(10), server_default="USER")
    picture = Column(String(100))
    isactivated = Column(Integer, server_default=text("0"))
    isblocked = Column(Integer, server_default=text("0"))
    qrcodeurl = Column(String(100))
    secretkey = Column(LargeBinary(length=60))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    descriptions=Column(String(100))
    qty=Column(Integer)
    unit = Column(String(10))
    cost_price = Column(Numeric(10,2))
    sell_price = Column(Numeric(10,2))
    prod_pic=Column(String(20))    
    category = Column(String(20))
    sale_price = Column(Numeric(10,2))
    alert_level=Column(Integer, server_default=text("0"))
    critical_level=Column(Integer, server_default=text("0"))
    datecreated = Column(DateTime(timezone=True), server_default=func.now())
    dateupdated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    # def __repr__(self):

    def __repr__(self,descriptions,qty,unit,cost_price,sell_price,prod_pic,category,sale_price,alert_level,critical_level,datecreated,dateupdated):
        self.descriptions = descriptions
        self.qty = qty
        self.unit = unit
        self.cost_price = cost_price
        self.sell_price = sell_price
        self.prod_pic = prod_pic
        self.category   = category
        self.sale_price = sale_price
        self.alert_level = alert_level
        self.critical_level = critical_level
        self.datecreated = datecreated
        self.dateupdated = dateupdated
        # return "<Products(id='{}', descriptions={},qty={},unit={},cost_price={},sell_price={},prod_pic={},category={},sale_price={},alert_level={},critical_level={},datecreated={},dateupdated={})>"\
        # .format(self.id,self.descriptions,self.qty,self.unit,self.cost_price,self.sell_price,self.prod_pic,self.category,self.sale_price,self.alert_level,self.critical_level,self.datecreated,self.dateupdated)


