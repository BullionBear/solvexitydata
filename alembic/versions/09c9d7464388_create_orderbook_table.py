"""create orderbook table

Revision ID: 09c9d7464388
Revises: 6d59019ccc29
Create Date: 2025-04-06 23:32:16.902427

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB


# revision identifiers, used by Alembic.
revision: str = '09c9d7464388'
down_revision: Union[str, None] = '6d59019ccc29'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None




def upgrade():
    op.create_table(
        'orderbook',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('symbol', sa.String(255), nullable=False),
        sa.Column('timestamp', sa.BigInteger(), nullable=False),
        sa.Column('bids', JSONB, nullable=False),  # Store as [price, quantity] pairs
        sa.Column('asks', JSONB, nullable=False),  # Store as [price, quantity] pairs
        sa.Column('last_update_id', sa.BigInteger(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create indexes for efficient querying
    op.create_index('ix_orderbook_timestamp', 'orderbook', ['timestamp'])
    op.create_index('ix_orderbook_symbol_timestamp', 'orderbook', ['symbol', 'timestamp'])
    op.create_index('ix_orderbook_symbol', 'orderbook', ['symbol'])


def downgrade():
    op.drop_index('ix_orderbook_symbol_timestamp')
    op.drop_index('ix_orderbook_timestamp')
    op.drop_index('ix_orderbook_symbol')
    op.drop_table('orderbook')