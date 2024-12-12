"""create spot balance with dt contains timezone

Revision ID: c908dabdb89f
Revises: 25a38d588c07
Create Date: 2024-12-12 20:27:13.611428

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c908dabdb89f'
down_revision: Union[str, None] = '25a38d588c07'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'spot_balance',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('dt', sa.DateTime(timezone=True), nullable=False),
        sa.Column('sid', sa.Integer, nullable=False),
        sa.Column('account', sa.String(length=50), nullable=False),
        sa.Column('token', sa.String(length=50), nullable=False),
        sa.Column('amount', sa.Numeric(precision=18, scale=8), nullable=False),
        sa.Column('value_in_usd', sa.Numeric(precision=18, scale=2), nullable=False)
    )

def downgrade():
    op.drop_table('spot_balance')