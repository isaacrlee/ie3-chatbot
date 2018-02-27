from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.sql import exists
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(config['DATABASE_URL'], echo=True)
base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class User(base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	messengerID = Column(String)
	targetLanguageKey = Column(String)

	def __init__(self, messengerID, targetLanguageKey):
		self.messengerID = messengerID
		self.targetLanguageKey = targetLanguageKey


	def __repr__(self):
		return ("<User(messengerID = %s, targetLanguageKey = %s)>" %
		(self.firstName + ' ' + self.lastName, self.messengerID, self.targetLanguageKey))

	def addUser(self):
		session.add(self)
		session.commit()

	def updateUser(self, language):
		self.targetLanguageKey = language
		session.commit()

def FindUser(idNumber):
	idString = str(idNumber)
	print(idString)
	if len(session.query(User).filter_by(messengerID=idString).all()) == 0:
		return None

	return session.query(User).filter_by(messengerID=idString).first()

def PrintDB():
	for instance in session.query(User).order_by(User.id):
		print(instance.messengerID, instance.targetLanguageKey)


base.metadata.create_all(engine)
