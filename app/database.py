from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings




# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='firstfastapi',
#         user='postgres', password='Sameer5842', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print('Database connection successful.')
#         break
#     except Exception as error:
#         print('Connection to database failed!')
#         print('Error: ', error)
#         time.sleep(2)


#'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()