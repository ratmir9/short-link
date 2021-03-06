"""alter column

Revision ID: 8061da7c2f3b
Revises: b14b7e4eee18
Create Date: 2022-01-16 23:55:58.963937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8061da7c2f3b'
down_revision = 'b14b7e4eee18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('links', sa.Column('short_link', sa.String(), nullable=True))
    op.drop_constraint('links_short_libk_key', 'links', type_='unique')
    op.create_unique_constraint(None, 'links', ['id'])
    op.create_unique_constraint(None, 'links', ['short_link'])
    op.drop_column('links', 'short_libk')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('links', sa.Column('short_libk', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'links', type_='unique')
    op.drop_constraint(None, 'links', type_='unique')
    op.create_unique_constraint('links_short_libk_key', 'links', ['short_libk'])
    op.drop_column('links', 'short_link')
    # ### end Alembic commands ###
