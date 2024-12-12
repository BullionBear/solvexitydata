"""remove spot balance

Revision ID: c3a575237ee4
Revises: 8c4fe9f055e1
Create Date: 2024-12-12 20:02:03.941619

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3a575237ee4'
down_revision: Union[str, None] = '8c4fe9f055e1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.drop_table('spot_balance')

def downgrade():
    # Recreate the table if you need a downgrade path:
    op.create_table(
        'spot_balance',
        sa.Column('id', sa.Integer, primary_key=True),
        # Add any other columns your original table had
    )