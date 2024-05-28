from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

ENGINE = create_engine(f"postgresql://postgres:maqsud8988@lacalhost/fast_api", echo=True)
# ENGINE = create_engine('postgresql://postgres:maqsud8988@localhost/fast_api', echo=True)
Base = declarative_base()
session = sessionmaker()
