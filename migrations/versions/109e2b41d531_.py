"""empty message

Revision ID: 109e2b41d531
Revises: 96832a4665c
Create Date: 2017-11-05 21:03:39.834101

"""

# revision identifiers, used by Alembic.
revision = '109e2b41d531'
down_revision = '96832a4665c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sqlite_sequence')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sqlite_sequence',
    sa.Column('name', sa.NullType(), nullable=True),
    sa.Column('seq', sa.NullType(), nullable=True)
    )
    ### end Alembic commands ###
