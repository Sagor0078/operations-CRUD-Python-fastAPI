
from datetime import datetime
from sqlalchemy import func
from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
import uuid

class User(SQLModel, table = True):
    __tablename__ = "user_accounts"

    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            primary_key=True,
            unique=True,
            nullable=False,
            default=uuid.uuid4,
            info={"description" : "Unique identifier for the user account"},
        )
    )

    username: str
    first_name: str = Field(nullable = True)
    last_name: str = Field(nullable= True)
    is_varified: bool = False
    email: str
    passsword_hash: str
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=func.now))

    def __repr__(self) -> str:
        return f"<User {self.username}>"

