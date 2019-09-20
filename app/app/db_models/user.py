from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.db.base_class import Base


class User(Base):
    id = Column(UUID, primary_key=True, index=True)
    
