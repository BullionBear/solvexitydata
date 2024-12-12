"""create perp balance table

Revision ID: b79a2480fa08
Revises: c908dabdb89f
Create Date: 2024-12-12 21:07:23.426473

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b79a2480fa08'
down_revision: Union[str, None] = 'c908dabdb89f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'perp_balance',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('dt', sa.DateTime(timezone=True), nullable=False),
        sa.Column('sid', sa.Integer, nullable=False),
        sa.Column('account', sa.String(length=50), nullable=False),
        sa.Column('token', sa.String(length=50), nullable=False),
        sa.Column('amount', sa.Numeric(precision=18, scale=8), nullable=False),
        sa.Column('value_in_usd', sa.Numeric(precision=18, scale=2), nullable=False)
    )

def downgrade():
    op.drop_table('perp_balance')