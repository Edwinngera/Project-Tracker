"""Initial migration3.

Revision ID: 2628a6f7ae73
Revises: c260f87a6c28
Create Date: 2022-11-15 16:48:32.784574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2628a6f7ae73'
down_revision = 'c260f87a6c28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Tentative_Projects', schema=None) as batch_op:
        batch_op.alter_column('project_id',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)
        batch_op.alter_column('project_name',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Tentative_Projects', schema=None) as batch_op:
        batch_op.alter_column('project_name',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)
        batch_op.alter_column('project_id',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###
