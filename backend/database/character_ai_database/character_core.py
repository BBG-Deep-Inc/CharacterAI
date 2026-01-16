from sqlalchemy import select,exc,String,cast
from character_models import metadata_obj,character_table
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from datetime import datetime,timedelta
from typing import List,Optional
from sqlalchemy.orm import sessionmaker
import asyncpg
import os
from dotenv import load_dotenv
import asyncio
import atexit
import uuid




load_dotenv()



async_engine = create_async_engine(
    f"postgresql+asyncpg://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@localhost:5432/character_ai_main_data",
    pool_size=20,           
    max_overflow=50,       
    pool_recycle=3600,      
    pool_pre_ping=True,     
    echo=False
)


AsyncSessionLocal = sessionmaker(
    async_engine, 
    class_=AsyncSession,
    expire_on_commit=False
)

async def create_table():
    async with async_engine.begin() as conn:
        await conn.run_sync(metadata_obj.create_all)


async def drop_table():
    async with async_engine.begin() as conn:
        await conn.run_sync(metadata_obj.drop_all) 
        

async def get_all_data() -> List:
    async with AsyncSession(async_engine) as conn:
        try:
            stmt = select(character_table)
            res = await conn.execute(stmt)
            return list(res.fetchall())
        except exc.SQLAlchemyError:
            raise exc.SQLAlchemyError("Error while executing")


        
async def create_model(username:str,model_name:str,promt:str):
    async with AsyncSession(async_engine) as conn:
        async with conn.begin():
            try:
                stmt = character_table.insert().values(
                   username = username,
                   name = model_name,
                   promt = promt,
                   id = str(uuid.uuid4()) 
                )
                await conn.execute(stmt)
            except exc.SQLAlchemyError:
                raise exc.SQLAlchemyError("Error while executing")