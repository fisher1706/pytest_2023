"""
to create session -> "sessionmaker"
to create engine -> "create_engine"
to create models -> "declarative_base"

echo=True -> to see "sql-request" created by alchemy
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from configuration import CONNECTION_ROW


Model = declarative_base(name='Model')

engine = create_engine(
    CONNECTION_ROW,
    # echo=True
)

Session = sessionmaker(
    engine,
    autoflush=False,
    autocommit=False
)

