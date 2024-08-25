from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from config import settings
from sqlalchemy.future import select
from .models import Logs

class SQLDatabase:
    def __init__(self):
        self.engine = create_async_engine(settings.POSTGRES_URL, echo=True)
        self.SessionLocal = sessionmaker(self.engine, class_=AsyncSession, expire_on_commit=False)
    
    async def add_logs(self, domain_name, client_ip):
        async with self.SessionLocal() as session:
            async with session.begin():
                log = Logs(domain_name=domain_name, client_ip=client_ip)
                session.add(log)
                await session.commit()
                return log
    


db = SQLDatabase()