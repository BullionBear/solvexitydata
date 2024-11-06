"""Create KLine table

Revision ID: c802e6448ef0
Revises: 29011ae2f7ca
Create Date: 2024-11-05 20:59:40.487342

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c802e6448ef0'
down_revision: Union[str, None] = '29011ae2f7ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'kline',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('symbol', sa.String, nullable=False),
        sa.Column('interval', sa.String, nullable=False),
        sa.Column('open_time', sa.BigInteger, nullable=False),
        sa.Column('close_time', sa.BigInteger, nullable=False),
        sa.Column('open', sa.Float, nullable=False),
        sa.Column('high', sa.Float, nullable=False),
        sa.Column('low', sa.Float, nullable=False),
        sa.Column('close', sa.Float, nullable=False),
        sa.Column('number_of_trades', sa.Integer, nullable=False),
        sa.Column('base_asset_volume', sa.Float, nullable=False),
        sa.Column('quote_asset_volume', sa.Float, nullable=False),
        sa.Column('taker_buy_base_asset_volume', sa.Float, nullable=False),
        sa.Column('taker_buy_quote_asset_volume', sa.Float, nullable=False),
    )

def downgrade():
    op.drop_table('kline')