import sqlalchemy as sa
from sqlalchemy.orm import RelationshipProperty, relationship
from src.orm_models.base import Base


class Employee(Base):
    __tablename__ = 'employee'
    id = sa.Column(
        sa.Integer(),
        primary_key=True,
        autoincrement=True,
    )
    name = sa.Column(sa.String(256), nullable=False)
    organization_id = sa.Column(
        sa.Integer(),
        sa.ForeignKey('organization.id', name='org_empl_fkey'),
        nullable=False
    )

    location = sa.Column(sa.String(512), nullable=False)
    organization: RelationshipProperty = relationship('Organization')
    