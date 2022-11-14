#!/usr/bin/python3
"""Write a script that lists all State objects that\
contain the letter a from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
from model_state import Base
from model_state import State

if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:\
    {sys.argv[2]}@localhost/{sys.argv[3]}")
    with Session(bind=engine) as session:
        x = session.query(State).filter(State.name == sys.argv[4]).first()
        if x:
            print(x.id)
        else:
            print("Not found")
