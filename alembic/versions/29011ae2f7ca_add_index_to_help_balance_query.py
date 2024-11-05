"""Add index to help balance query

Revision ID: 29011ae2f7ca
Revises: a7d751cb9491
Create Date: 2024-11-05 20:16:23.734351

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '29011ae2f7ca'
down_revision: Union[str, None] = 'a7d751cb9491'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Index for Latest Balance and Latest Value Queries
    op.create_index(
        'idx_account_token_dt_desc',
        'balance',
        ['account', 'token', sa.text('dt DESC')],
        unique=False
    )
    
    # Index for Balance Data Query
    op.create_index(
        'idx_dt_account',
        'balance',
        ['dt', 'account'],
        unique=False
    )
    
    # Index for Balance to Time Query
    op.create_index(
        'idx_account_dt',
        'balance',
        ['account', 'dt'],
        unique=False
    )

def downgrade():
    # Drop indexes in downgrade
    op.drop_index('idx_account_token_dt_desc', table_name='balance')
    op.drop_index('idx_dt_account', table_name='balance')
    op.drop_index('idx_account_dt', table_name='balance')