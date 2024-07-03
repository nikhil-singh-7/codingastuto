import sqlalchemy as sa
from src.orm_models.base import Base


class Organization(Base):
    __tablename__ = 'organization'
    id = sa.Column(
        sa.Integer(),
        primary_key=True,
        autoincrement=True,
    )
    name = sa.Column(sa.String(256), nullable=False)
    category = sa.Column(sa.String(256), nullable=False)
    location = sa.Column(sa.String(512), nullable=False)
    