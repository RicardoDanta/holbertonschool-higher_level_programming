#!/usr/bin/python3
"""Script that lists all State objects from the database hbtn_0e_6_usa"""

import MySQLdb
import sys
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
from model_state import Base
from model_state import State

if __name__ == "__main__":

    engine = create_engine(f"mysql+mysqldb://{argv[1]}:\
    {argv[2]}@localhost/{argv[3]}")
    with Session(bind=engine) as session:
        x = session.query(State).all()
        for i in x:
            print(f"{i.id}: {i.name}")
