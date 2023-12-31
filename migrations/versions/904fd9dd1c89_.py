"""empty message

Revision ID: 904fd9dd1c89
Revises: 6638dad9acbf
Create Date: 2023-06-19 14:07:39.060735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '904fd9dd1c89'
down_revision = '6638dad9acbf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('micro', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=300),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('micro', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.String(length=300),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###
