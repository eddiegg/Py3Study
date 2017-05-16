from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine, Numeric, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("sqlite:///test.sqlite")

Base = declarative_base()

DBSession = sessionmaker(bind=db)


class User(Base):
    __tablename__ = 'User'

    id = Column(String(20), primary_key=True)
    name = Column(VARCHAR)
    age = Column(Integer)


# session = DBSession()
# eddie = User(id='0000002', name='eddie', age=36)
# session.add(eddie)
# session.commit()
# session.close()

session = DBSession()
record = session.query(User).all()
for item in record:
    if item.name=='harvey':
        item.age=5
    else:
        item.age=36
session.commit()
for item in record:
    print(item.name, item.age)
session.close()

