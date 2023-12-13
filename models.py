from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from faker import Faker


Base = declarative_base()

class Worker(Base):
    __tablename__ = 'workers'

    id = Column(Integer, primary_key=True)
    name = Column('name',String)
    age = Column('age',Integer)
    gender = Column('gender',String)  
    title = Column('title',String)

    # the salaries relationship
    salaries = relationship('Salary', back_populates='worker')

    def __init__(self,name,age,gender,title):
        self.name = name
        self.age = age
        self.gender = gender 
        self.title = title 

    def __repr__(self):
        return f"{self.id} {self.name} {self.age} {self.gender} {self.title}"


class Salary(Base):
    __tablename__ = 'salaries'

    id = Column(Integer, primary_key=True)
    status = Column(Boolean, default=False) 
    worker_id = Column(Integer, ForeignKey('workers.id'))
    amount = Column(Integer)
    

    # Establishing relationships
    worker = relationship('Worker', back_populates='salaries')

    def __init__(self,status ,worker_id,amount):
        self.status = status
        self.worker_id = worker_id
        self.amount = amount

    def __repr__(self):
        return f"{self.id} {self.status} {self.worker_id} {self.amount}"

if __name__ == '__main__':
    engine = create_engine('sqlite:///manager.db')
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    fake = Faker()

    construction_job_titles = [
        'Casual', 'Foreman', 'Site Engineer', 'Architect', 'Project Manager', 'Electrician', 'Plumber', 'Welder'
    ]

    workers = [
        Worker(
            name=fake.name(),
            age=fake.random_int(min=18, max=65),
            gender=fake.random_element(elements=('Male', 'Female')),
            title=fake.random_element(elements=construction_job_titles)
        ) for _ in range(10)
    ]

    for worker in workers:
        session.add(worker)
        session.commit()

    salaries = [
        Salary(
            status=fake.random_element(elements=(True, False)),
            amount=fake.random_int(min=20000, max=60000),
            worker_id=fake.random_element(elements=workers).id
        ) for _ in range(10)
    ]

    for salary in salaries:
        session.add(salary)

    session.commit()


