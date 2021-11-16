from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from model.tables import Base, Currency

DB_name     = "database.sqlite"

engine      = create_engine("sqlite:///model/{}".format(DB_name))
Base.metadata.create_all(engine)
session = Session(bind=engine)

def input_currency_course_dynamics_into_DB(VAL_NM_RQ:str, name: str, course_dynamics: list):
    dates = session.query(
        Currency.date
    ).filter(Currency.VAL_NM_RQ==VAL_NM_RQ).all()
    dates = [x.date for x in dates]
    for date, _, value in course_dynamics:
        if date in dates:
            c = session.query(Currency).filter(
                Currency.date == date
            ).one()
            c.value = value
        else:
            currency = Currency(
                VAL_NM_RQ=VAL_NM_RQ,
                name=name,
                value=value,
                date=date
            )
            session.add(currency)
    session.commit()
