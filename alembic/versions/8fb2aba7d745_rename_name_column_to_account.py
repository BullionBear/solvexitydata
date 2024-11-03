"""Rename name column to account

Revision ID: 8fb2aba7d745
Revises: 18ba30b3223d
Create Date: 2024-11-03 19:34:57.658375

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8fb2aba7d745'
down_revision: Union[str, None] = '18ba30b3223d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Rename column in balance table
    op.alter_column('balance', 'name', new_column_name='account')

    # Rename column in read_api table
    op.alter_column('read_api', 'name', new_column_name='account')

    # Rename column in trade_api table
    op.alter_column('trade_api', 'name', new_column_name='account')

def downgrade():
    # Revert column rename in balance table
    op.alter_column('balance', 'account', new_column_name='name')

    # Revert column rename in read_api table
    op.alter_column('read_api', 'account', new_column_name='name')

    # Revert column rename in trade_api table
    op.alter_column('trade_api', 'account', new_column_name='name')

