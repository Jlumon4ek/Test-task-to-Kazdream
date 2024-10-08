"""create logs table

Revision ID: e605ff6b26d0
Revises: 
Create Date: 2024-08-25 14:17:29.417517

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e605ff6b26d0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('logs',
    sa.Column('uuid', sa.UUID(), nullable=False),
    sa.Column('domain_name', sa.String(), nullable=False),
    sa.Column('client_ip', sa.String(), nullable=False),
    sa.Column('date', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('logs')
    # ### end Alembic commands ###
