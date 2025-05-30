"""add noticia

Revision ID: 1d470fb3ffb6
Revises: 
Create Date: 2025-05-16 11:37:28.566236

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d470fb3ffb6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorias',
    sa.Column('id_categoria', sa.Integer(), nullable=False),
    sa.Column('fecha_creacion', sa.Date(), nullable=True),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.Column('nombre', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id_categoria')
    )
    op.create_table('roles',
    sa.Column('id_rol', sa.Integer(), nullable=False),
    sa.Column('fecha_creacion', sa.Date(), nullable=True),
    sa.Column('nombre', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id_rol')
    )
    op.create_table('noticias',
    sa.Column('id_noticia', sa.Integer(), nullable=False),
    sa.Column('fecha_creacion', sa.Date(), nullable=True),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.Column('nombre', sa.String(length=60), nullable=True),
    sa.Column('descripcion', sa.String(length=200), nullable=True),
    sa.Column('categoria_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['categoria_id'], ['categorias.id_categoria'], ),
    sa.PrimaryKeyConstraint('id_noticia')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('noticias')
    op.drop_table('roles')
    op.drop_table('categorias')
    # ### end Alembic commands ###
