from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class MsgSchedules(Base):
    __tablename__ = "MSGSCHEDULES"

    id = Column("id", Integer, autoincrement=True, primary_key=True)
    scheduled_date = Column("SCHEDULED_DATE", DateTime, nullable=False)
    type = Column("TYPE", String(10), nullable=False)
    destination = Column("DESTINATION", String(30), nullable=False)
    message = Column("MESSAGE", String(255), nullable=False)
    status = Column("STATUS", String(10), nullable=False)
    created = Column("CREATED", DateTime, default=datetime.now())

    def __repr__(self):
        return f"{self.id!r}: {self.scheduled_date} {self.destination!r}"
