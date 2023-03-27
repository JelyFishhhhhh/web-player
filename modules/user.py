from sqlmodel import SQLModel, Field
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from typing import Optional

ENGINE = create_async_engine("sqlite+aiosqlite:///user.db")

class ID(SQLModel):
    id: Optional[int] = Field(
        None, primary_key=True, unique=True, description="ID")

class User_Profile(SQLModel, table = True):
    __tablename__ = "UserData"


    uid : str = Field(default=None, unique = True, primary_key=True, nullable=False, description = "user-id")
    name : str = Field(nullable = False, description = "user-name")
    email : str = Field(nullable = False, description = "user-mail")
    password : str = Field(nullable = False, description = "user-password")
    role : str = Field(default = "NULL", nullable = False, description = "permission")

class method():

    async def sql_init():

        async with ENGINE.begin() as connection:

            await connection.run_sync(SQLModel.metadata.drop_all)
            await connection.run_sync(SQLModel.metadata.create_all)

        from modules import User_Profile as User

        async with AsyncSession(ENGINE) as session:
            
            session.add(
                    User(**{
                        "uid": "000",
                        "name": "admin",
                        "email": "admin@gmail.com",
                        "password": "admin",
                        "role": "ADMIN",
                    })
                )


            session.add(
                    User(**{
                        "uid": "001",
                        "name": "alice",
                        "email": "alice@gmail.com",
                        "password": "alice",
                        "role": "NORMAL",
                    })
                )
            
            await session.commit()

