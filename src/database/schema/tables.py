from sqlalchemy import Column, Integer, String, Float, DateTime , Table
from src.database.dbconfig import Base,metadata

class UserAddress(Base):
    __tablename__=""
    id = Column(Integer, primary_key=True)
    name = Column(String,nullable=False)
    fullname = Column(String,nullable=True)
    nickname = Column(String,nullable=True)
    address = Column(String,nullable=False)
    latitude =  Column(Float)
    longitude =  Column(Float)
    last_modified_at = Column(DateTime,nullable=True) 
    created_at = Column(DateTime,nullable=False)
		
    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name,
            self.fullname,
            self.nickname,
        )

UserAddreses= Table(
    "address", metadata,
    Column('name',String,nullable=False),
    Column('fullname',String,nullable=False),
    Column('nickname',String,nullable=False),
    Column('address',String,nullable=False),
    Column('latitude',Float),
    Column('latitude',Float),
    Column("last_modified_at",DateTime,nullable=True),
    Column("created_at",DateTime,nullable=False) 
)
