"""Create transactions table

Revision ID: 079097af63e9
Revises: 032f9f736889
Create Date: 2024-12-12 19:52:09.346928

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '079097af63e9'
down_revision: Union[str, None] = '032f9f736889'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'spot_balance',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('dt', sa.DateTime, nullable=False),
        sa.Column('sid', sa.Integer, nullable=False),
        sa.Column('token', sa.String(length=50), nullable=False),
        sa.Column('amount', sa.Numeric(precision=18, scale=8), nullable=False),
        sa.Column('value_in_usd', sa.Numeric(precision=18, scale=2), nullable=False)
    )

def downgrade():
    op.drop_table('spot_balance')