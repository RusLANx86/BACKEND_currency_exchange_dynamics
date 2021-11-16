from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Currency(Base):
    __tablename__ = "currency"

    id          = Column(Integer, primary_key=True, autoincrement=True)
    VAL_NM_RQ   = Column(String, nullable=False)
    name        = Column(String, nullable=False)
    value       = Column(Integer, nullable=False)
    date        = Column(String, nullable=False)

    def __repr__(self):
        return "{name} - {VAL_NM_RQ}".format(
            name=self.name,
            VAL_NM_RQ=self.VAL_NM_RQ
        )

