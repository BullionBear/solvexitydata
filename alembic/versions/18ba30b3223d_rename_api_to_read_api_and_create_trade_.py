"""rename api to read_api and create trade_api

Revision ID: 18ba30b3223d
Revises: e81fafe40733
Create Date: 2024-11-03 14:32:47.033003

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '18ba30b3223d'
down_revision: Union[str, None] = 'e81fafe40733'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Rename 'api' table to 'read_api'
    op.rename_table('api', 'read_api')

    # Create 'trade_api' table with the same schema as 'api'
    op.create_table(
        'trade_api',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(255), unique=True, nullable=False),
        sa.Column('exchange', sa.String(255), nullable=False),
        sa.Column('api_key', sa.String(255), nullable=False),
        sa.Column('api_secret', sa.String(255), nullable=False),
        sa.Column('passphrase', sa.String(255), nullable=True)
    )

def downgrade():
    # Drop 'trade_api' table
    op.drop_table('trade_api')
    
    # Rename 'read_api' table back to 'api'
    op.rename_table('read_api', 'api')