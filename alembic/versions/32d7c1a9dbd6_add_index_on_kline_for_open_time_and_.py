"""add index on kline for open_time and symbol

Revision ID: 32d7c1a9dbd6
Revises: b59ec198f618
Create Date: 2024-11-07 00:06:13.342125

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '32d7c1a9dbd6'
down_revision: Union[str, None] = 'b59ec198f618'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Create an index on `open_time` and `symbol` columns in `kline` table
    op.create_index(
        'ix_kline_open_time_symbol',  # Index name
        'kline',                      # Table name
        ['open_time', 'symbol']       # Columns to index
    )

def downgrade():
    # Drop the index
    op.drop_index('ix_kline_open_time_symbol', table_name='kline')