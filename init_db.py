from sqlmodel import create_engine, Session
import os

# DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = "postgresql://stevenwu@localhost:5432/vtrade"

engine = create_engine(DATABASE_URL)

def get_db():
    with Session(engine) as session:
        yield session



