#!/usr/bin/python3
"""Write a script that adds the State object
Louisiana to the database hbtn_0e_6_usa"""

import sys
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
from model_state import Base
from model_state import State

if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:\
    {sys.argv[2]}@localhost/{sys.argv[3]}", pool_pre_ping=True)

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        state = State(name="Louisiana")
        session.add(state)
        session.commit()
        print(state.id)
