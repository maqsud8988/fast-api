from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


ENGINE = create_engine(f"postgresql://postgres:maqsud8988@lacalhost/fast_api", echo=True)
Base = declarative_base()
Session = sessionmaker()

