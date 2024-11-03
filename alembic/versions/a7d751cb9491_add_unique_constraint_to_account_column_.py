"""Add unique constraint to account column in read_api and trade_api tables

Revision ID: a7d751cb9491
Revises: 8fb2aba7d745
Create Date: 2024-11-03 19:51:58.359673

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a7d751cb9491'
down_revision: Union[str, None] = '8fb2aba7d745'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Add unique constraint to account column in read_api table
    op.create_unique_constraint('uq_read_api_account', 'read_api', ['account'])

    # Add unique constraint to account column in trade_api table
    op.create_unique_constraint('uq_trade_api_account', 'trade_api', ['account'])

def downgrade():
    # Remove unique constraint from account column in read_api table
    op.drop_constraint('uq_read_api_account', 'read_api', type_='unique')

    # Remove unique constraint from account column in trade_api table
    op.drop_constraint('uq_trade_api_account', 'trade_api', type_='unique')