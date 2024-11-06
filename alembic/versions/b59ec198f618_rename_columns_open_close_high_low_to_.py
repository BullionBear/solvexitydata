"""Rename columns open, close, high, low to open_px, close_px, high_px, low_px

Revision ID: b59ec198f618
Revises: c802e6448ef0
Create Date: 2024-11-05 22:20:58.060373

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b59ec198f618'
down_revision: Union[str, None] = 'c802e6448ef0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade():
    # Rename columns in the kline_data table
    op.alter_column('kline', 'open', new_column_name='open_px')
    op.alter_column('kline', 'close', new_column_name='close_px')
    op.alter_column('kline', 'high', new_column_name='high_px')
    op.alter_column('kline', 'low', new_column_name='low_px')


def downgrade():
    # Revert column names back to original
    op.alter_column('kline', 'open_px', new_column_name='open')
    op.alter_column('kline', 'close_px', new_column_name='close')
    op.alter_column('kline', 'high_px', new_column_name='high')
    op.alter_column('kline', 'low_px', new_column_name='low')