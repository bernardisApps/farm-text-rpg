from sqlalchemy import create_engine
from app.models.db.schemas import Base
from sqlalchemy.orm import sessionmaker

def create_session():
    engine = create_engine('sqlite:///app/models/db/db.sqlite', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session