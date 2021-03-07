from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


POSTGRES_DB = 'postgres'
POSTGRES_SERVER = 'postgres'
POSTGRES_PORT = '5432'
POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'postgres'
SQLALCHAMY_DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@/{POSTGRES_DB}?host={POSTGRES_SERVER}&port={POSTGRES_PORT}'

engine = create_engine(SQLALCHAMY_DATABASE_URL, echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    def __repr__(self):
        return f'<User(name={self.name}, email={self.email})>'

# Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

# ed_user = User(name='ed', email='ed@test.com', password='test')
# session.add(ed_user)

session.add_all([
    User(name='test1', email='test1@test.com', password='test'),
    User(name='test2', email='test2@test.com', password='test'),
    User(name='test3', email='test3@test.com', password='test'),
])

our_user = session.query(User)
for user in our_user:
    print(user)