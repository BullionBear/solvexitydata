"""rename instrument to market

Revision ID: 156bc1adc531
Revises: 28503a581efb
Create Date: 2024-12-06 08:41:21.131227

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '156bc1adc531'
down_revision: Union[str, None] = '28503a581efb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    # Rename the column 'instrument' to 'market' in the 'financial_instruments' table
    op.alter_column(
        'instrument',  # Table name
        'instrument',             # Existing column name
        new_column_name='market'  # New column name
    )

def downgrade():
    # Revert the column name back to 'instrument' in case of rollback
    op.alter_column(
        'financial_instruments',
        'market',
        new_column_name='instrument'
    )