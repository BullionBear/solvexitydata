"""create perp position table

Revision ID: 6d59019ccc29
Revises: b79a2480fa08
Create Date: 2024-12-12 21:46:17.351975

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6d59019ccc29'
down_revision: Union[str, None] = 'b79a2480fa08'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'position',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('dt', sa.DateTime(timezone=True), nullable=False),
        sa.Column('sid', sa.Integer, nullable=False),
        sa.Column('account', sa.String(length=50), nullable=False),
        sa.Column('symbol', sa.String(length=50), nullable=False),
        sa.Column('amount', sa.Numeric(precision=18, scale=8), nullable=False),
        sa.Column('unrealized_profit', sa.Numeric(precision=18, scale=8), nullable=False),
        sa.Column('initial_margin', sa.Numeric(precision=18, scale=8), nullable=False),
        sa.Column('entry_px', sa.Numeric(precision=18, scale=8), nullable=False),
        sa.Column('mark_px', sa.Numeric(precision=18, scale=8), nullable=False),
        sa.Column('notional', sa.Numeric(precision=18, scale=8), nullable=False),
    )

def downgrade():
    op.drop_table('position')