from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from model.tables import Base, Currency

DB_name     = "database.sqlite"

engine      = create_engine("sqlite:///model/{}".format(DB_name))
Base.metadata.create_all(engine)
session = Session(bind=engine)

def input_currency_course_dynamics_into_DB(VAL_NM_RQ:str, name: str, course_dynamics: list):
    for n in course_dynamics:
        date    = n[0]
        value   = n[2]
        currency = Currency(
            VAL_NM_RQ   = VAL_NM_RQ,
            name        = name,
            value       = value,
            date        = date
        )
        session.query(Currency)
        session.add(currency)
    session.commit()
