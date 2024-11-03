"""create api and balance tables

Revision ID: e81fafe40733
Revises: 
Create Date: 2024-11-03 14:13:23.469018

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e81fafe40733'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Create the 'api' table
    op.create_table(
        'api',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(255), unique=True, nullable=False),
        sa.Column('exchange', sa.String(255), nullable=False),
        sa.Column('api_key', sa.String(255), nullable=False),
        sa.Column('api_secret', sa.String(255), nullable=False),
        sa.Column('passphrase', sa.String(255), nullable=True)
    )

    # Create the 'balance' table
    op.create_table(
        'balance',
        sa.Column('dt', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('name', sa.String(255), sa.ForeignKey('api.name'), nullable=False),
        sa.Column('token', sa.String(255), nullable=False),
        sa.Column('amount', sa.Float, nullable=False),
        sa.Column('value_in_btc', sa.Float, nullable=False),
        sa.PrimaryKeyConstraint('dt', 'name', 'token')
    )


def downgrade():
    # Drop the 'balance' table
    op.drop_table('balance')

    # Drop the 'api' table
    op.drop_table('api')