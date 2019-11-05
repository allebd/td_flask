"""empty message

Revision ID: 58642d78e6e0
Revises: 6f782cf9a59a
Create Date: 2019-11-05 19:55:21.854952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58642d78e6e0'
down_revision = '6f782cf9a59a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###