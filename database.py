from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:///Data.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = scoped_session(sessionmaker(bind=engine))

def add_User(username,phone,address, password,cash):
    try:
        user_object = User(username=username,phone=phone,address=address,
        password=password,cash=round(cash,2))
        session.add(user_object)
        session.commit()
    except:
        session.rollback()
        raise

def add_Farm(Farm_name,bank_name,bank_account,phone,address,password):
    try:
        Farm_object = Farm(Farm_name=Farm_name,bank_name=bank_name,bank_account=bank_account,phone=phone,address=address,password=password)
        session.add(Farm_object)
        session.commit()
    except:
        session.rollback()
        raise    

def add_Product(Type,Owner,cost):
  try:
    product_object = Product(Type=Type,Owner=Owner,cost=round(cost,2))
    session.add(product_object)
    session.commit()
  except:
    session.rollback()
    raise

def query_product_by_id(id):
   return  session.query(
       Product).filter_by(
       id_table=id).first() 


def update_cost_product_by_id(id):
    product = session.query(
       Product).filter_by(
       id_table=id).first()
    product.cost = 0
    session.commit()

def update_cash_user_by_username(username,cost):
    user = session.query(
       User).filter_by(
       username=username).first()
    user.cash -= cost
    session.commit()

def query_user_by_username(username):
    a=session.query(User)
    print a
    b= a.filter_by(username=username)
    print b
    c=b.first()
    
    
    print c 

    return c
  # a = session.query
  # print a
  # b = a.filter_by
  # c = b.first

def query_by_farmname(farmname):
    return session.query(Farm).filter_by(Farm_name = farmname).first()

def delete_product_by_id(id):
    product = session.query(Product).filter_by(id_table=id).delete()
    session.commit()

def buy_product(username,product_id):
    user_cash = query_user_by_username(username).cash
    product_cost = query_product_by_id(product_id).cost

    if user_cash == product_cost or user_cash > product_cost:
        update_cash_user_by_username(username,product_cost)
        delete_product_by_id(product_id)
        return "bought"
    else:
        return "not enough cash"

def get_all_products():
    return session.query(Product).all()


def get_owner_products(Owner):
    return session.query(Product).filter_by(Owner=Owner).all()


def get_all_users():
    return session.query(User).all()

def get_all_farms():
    return session.query(Farm).all()

def query_by_username_and_password(username, password):
    return session.query(User).filter_by(username = username, password = password).first()

def query_by_farmname_and_password(farmname, password):
    return session.query(Farm).filter_by(Farm_name = farmname, password = password).first()

def delete_all_users():
    session.query(User).delete()
    session.commit()

def delete_all_products():
    session.query(Product).delete()
    session.commit()

##########################################################################

def get_all_Types():
    return session.query(Type).all()

def query_type_by_name(Name):
   return  session.query(Type).filter_by(Name=Name).first()

def get_minPrice(Name):
  return  session.query(Type).filter_by(Name=Name).first().Min_price

def get_maxPrice(Name):
  return  session.query(Type).filter_by(Name=Name).first().Max_price

def set_minPrice(Name,newMinPrice):
  type = session.query(
       Type).filter_by(
       Name=Name).first()
  type.Min_price = newMinPrice
  session.commit()

def set_maxPrice(Name,newMaxPrice):
  type = session.query(
       Type).filter_by(
       Name=Name).first()
  type.Max_price = newMaxPrice
  session.commit()

def add_type(Name,img,min_price, max_price):
  try:
    product_object = Type(Name=Name,Img=img,Min_price=min_price, Max_price=max_price)
    session.add(product_object)
    session.commit()
  except:
    session.rollback()
    raise

def get_type_products_lowestPrice(Type):
    number = 0
    all = session.query(Product).filter_by(Type=Type).all()
    if all != []:
      number = all[0].cost
    for product in all:
      if product.cost < number:
        number = product.cost
    return number

def get_type_products_highestPrice(Type):
    number = 0
    all = session.query(Product).filter_by(Type=Type).all()
    if all != []:
      number = all[0].cost
    for product in all:
      if product.cost > number:
        number = product.cost
    return number

def get_type_products(Type):
  return session.query(Product).filter_by(Type=Type).all()

def query_product_by_id(id):
   return  session.query(
       Product).filter_by(
       id_table=id).first()  

def update_min_max_types():
    types = session.query(Type).all()
    for item in types:
      item.Min_price = get_type_products_lowestPrice(item.Name)
      item.Max_price = get_type_products_highestPrice(item.Name)




print(get_type_products("5ara"))