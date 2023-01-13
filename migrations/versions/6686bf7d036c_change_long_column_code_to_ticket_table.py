"""change_long_column_code_to_ticket_table

Revision ID: 6686bf7d036c
Revises: 947e2958bf3f
Create Date: 2023-01-13 11:19:38.010577

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6686bf7d036c'
down_revision = '947e2958bf3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ticket', schema=None) as batch_op:
        batch_op.alter_column('code',
               existing_type=mysql.VARCHAR(length=15),
               type_=sa.String(length=36),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ticket', schema=None) as batch_op:
        batch_op.alter_column('code',
               existing_type=sa.String(length=36),
               type_=mysql.VARCHAR(length=15),
               existing_nullable=True)

    # ### end Alembic commands ###
