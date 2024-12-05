"""create instrument table

Revision ID: 28503a581efb
Revises: 32d7c1a9dbd6
Create Date: 2024-12-05 23:39:32.979100

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '28503a581efb'
down_revision: Union[str, None] = '32d7c1a9dbd6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Create the table
    op.create_table(
        'instrument',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),  # Primary key
        sa.Column('symbol', sa.String(50), nullable=False),
        sa.Column('instrument', sa.String(100), nullable=False)
    )

def downgrade():
    # Drop the table
    op.drop_table('instrument')