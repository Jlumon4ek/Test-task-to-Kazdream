from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger, String, TIMESTAMP, ForeignKey, Boolean
from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
from zoneinfo import ZoneInfo

Base = declarative_base()

utc_plus_5 = ZoneInfo("Asia/Almaty")

class Logs(Base):
    __tablename__ = 'logs'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    domain_name = Column(String, nullable=False)
    client_ip = Column(String, nullable=False)
    date = Column(TIMESTAMP(timezone=True), default=datetime.now(utc_plus_5))

    