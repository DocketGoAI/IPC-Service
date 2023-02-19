import random
import string
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# db configuration
engine = create_engine('sqlite:///Tokens.db', echo=True)
Session = sessionmaker(bind=engine)

# Create a base class for the ORM model
Base = declarative_base()


class ApiToken(Base):
    __tablename__ = 'Tokens'
    token_text = Column(String, primary_key=True)

    def generate_token(cls):
        '''
        generate random alpha-numeric string with length 50 and check whether it already exist or not
        '''
        token = ''.join(random.choices(string.ascii_letters+string.digits, k=40))
        with Session() as session:
            result = session.query(cls).filter_by(token_text=token).first()
            while result:
                token = ''.join(random.choices(string.ascii_letters+string.digits, k=50))
                result = session.query(cls).filter_by(token_text=token).first()
            new_token = cls(token_text=token)
            session.add(new_token)
            session.commit()
            return token

    def is_valid_token(cls, token_to_check):
        with Session() as session:
            result = session.query(cls).filter_by(token_text=token_to_check).first()
        if result:
            return True
        return False

# create the table (if it doesn't already exist)
Base.metadata.create_all(engine)
