"""empty message

Revision ID: d37013ed6658
Revises: 7b1b60883356
Create Date: 2024-11-22 21:35:57.786274

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd37013ed6658'
down_revision: Union[str, None] = '7b1b60883356'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('transaction', 'category_id',
               existing_type=postgresql.ARRAY(sa.INTEGER()),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('transaction', 'category_id',
               existing_type=postgresql.ARRAY(sa.INTEGER()),
               nullable=True)
    # ### end Alembic commands ###
