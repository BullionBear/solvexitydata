"""Remove balance table

Revision ID: 032f9f736889
Revises: 156bc1adc531
Create Date: 2024-12-12 19:49:27.697925

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '032f9f736889'
down_revision: Union[str, None] = '156bc1adc531'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade():
    op.drop_table('balance')

def downgrade():
    # Recreate the table if you need a downgrade path:
    op.create_table(
        'balance',
        sa.Column('id', sa.Integer, primary_key=True),
        # Add any other columns your original table had
    )