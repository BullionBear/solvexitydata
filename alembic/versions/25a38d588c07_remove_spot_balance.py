"""remove spot balance

Revision ID: 25a38d588c07
Revises: 28a017072a6a
Create Date: 2024-12-12 20:26:22.583180

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25a38d588c07'
down_revision: Union[str, None] = '28a017072a6a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table('spot_balance')


def downgrade() -> None:
    pass
