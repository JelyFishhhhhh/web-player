from sqlmodel import SQLModel, Field, select
from sqlmodel.main import SQLModelMetaclass
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from typing import Optional

ENGINE = create_async_engine("sqlite+aiosqlite:///user.db")

class User_Profile(SQLModel, table = True):
    __tablename__ = "UserData"


    uid : str = Field(default=None, unique = True, primary_key=True, nullable=False, description = "user-id")
    name : str = Field(nullable = False, description = "user-name")
    email : str = Field(nullable = False, description = "user-mail")
    password : str = Field(nullable = False, description = "user-password")
    role : str = Field(default = "NULL", nullable = False, description = "permission")

class method():

    async def sql_init(debug:bool = False):

        async with ENGINE.begin() as connection:
            if debug:
                await connection.run_sync(SQLModel.metadata.drop_all)
            await connection.run_sync(SQLModel.metadata.create_all)

        if debug:

            async with AsyncSession(ENGINE) as session:
                
                session.add(
                        User_Profile(**{
                            "uid": "000",
                            "name": "admin",
                            "email": "admin@gmail.com",
                            "password": "admin",
                            "role": "ADMIN",
                        })
                    )


                session.add(
                        User_Profile(**{
                            "uid": "001",
                            "name": "alice",
                            "email": "alice@gmail.com",
                            "password": "alice",
                            "role": "NORMAL",
                        })
                    )
                
                await session.commit()
    
    async def sql_insert(name:str = "Username", email:str = "example@gmail.com", password:str = "0X0X0X0X", role: str = "NORMAL"):

        async with AsyncSession(ENGINE) as session:

            session.add(
                    User_Profile(**{
                        "uid": "215",
                        "name": name,
                        "email": email,
                        "password": password,
                        "role": role,
                    })
                )
            
            await session.commit()

    async def sql_where_by_ID(t_name: SQLModelMetaclass, uid: str):

        async with AsyncSession(ENGINE) as session:

            statemnt = select(t_name).where(t_name.uid == uid)

            results = await session.exec(statement=statemnt)

            return results.first()
        
    async def sql_where_by_NAME(t_name: SQLModelMetaclass, name: str):

        async with AsyncSession(ENGINE) as session:

            statement = select(t_name).where(t_name.name == name)
            
            results = await session.exec(statement=statement)

            return results.first()
        
    async def sql_where_by_MAIL(t_name: SQLModelMetaclass, mail: str):

        async with AsyncSession(ENGINE) as session:

            statement = select(t_name).where(t_name.email == mail)
            
            results = await session.exec(statement=statement)

            return results.first()