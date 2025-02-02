"""add date to device

Revision ID: a24304a76191
Revises: b102a73cb332
Create Date: 2024-09-29 01:01:53.425811

"""
from alembic import op
import sqlalchemy as sa
import flask_security


# revision identifiers, used by Alembic.
revision = 'a24304a76191'
down_revision = 'b102a73cb332'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('device', schema=None) as batch_op:
        batch_op.add_column(sa.Column('adding_date', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('device', schema=None) as batch_op:
        batch_op.drop_column('adding_date')

    # ### end Alembic commands ###
