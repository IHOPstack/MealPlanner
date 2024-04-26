from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_URL = 'mysql+pymysql://newuser:newpassword@localhost/meal_planner'

engine = create_engine(SQL_URL)

SessionLocal = sessionmaker(autoflush=False)

Base = declarative_base()