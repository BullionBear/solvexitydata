"""create table spot_balance

Revision ID: 28a017072a6a
Revises: c3a575237ee4
Create Date: 2024-12-12 20:04:02.065819

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '28a017072a6a'
down_revision: Union[str, None] = 'c3a575237ee4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'spot_balance',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('dt', sa.DateTime, nullable=False),
        sa.Column('sid', sa.Integer, nullable=False),
        sa.Column('account', sa.String(length=50), nullable=False),
        sa.Column('token', sa.String(length=50), nullable=False),
        sa.Column('amount', sa.Numeric(precision=18, scale=8), nullable=False),
        sa.Column('value_in_usd', sa.Numeric(precision=18, scale=2), nullable=False)
    )

def downgrade():
    op.drop_table('spot_balance')