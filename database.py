from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///users.db', echo=True)
base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class User(base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	firstName = Column(String)
	lastName = Column(String)
	messengerID = Column(String)
	targetLanguageKey = Column(String)

	def __repr__(self):
		return ("<User(Name = %s, messengerID = %s, targetLanguageKey = %s" %
		(self.firstName + ' ' + self.lastName, self.messengerID, self.targetLanguageKey))

	def addUser(self):
		session.add(self)

base.metadata.create_all(engine)


joe = User(firstName='Joe', lastName='Adams', messengerID='345', targetLanguageKey='es')
session.add(joe)

print session.query(User).filter_by(firstName='Joe').first()