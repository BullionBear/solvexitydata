"""Add account column to transactions table

Revision ID: 8c4fe9f055e1
Revises: 079097af63e9
Create Date: 2024-12-12 19:55:32.012237

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c4fe9f055e1'
down_revision: Union[str, None] = '079097af63e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    # Add the 'account' column to the 'transactions' table
    op.add_column('spot_balance', sa.Column('account', sa.String(length=100), nullable=True))

def downgrade():
    # Remove the 'account' column if we downgrade
    op.drop_column('spot_balance', 'account')