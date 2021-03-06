"""column

Revision ID: 2fd1192706e7
Revises: 83dc9267d154
Create Date: 2018-10-15 16:38:16.965150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fd1192706e7'
down_revision = '83dc9267d154'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('height', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('width', sa.String(length=64), nullable=True))
    op.drop_index('ix_user_email', table_name='user')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.VARCHAR(length=120), nullable=True))
    op.create_index('ix_user_email', 'user', ['email'], unique=1)
    op.drop_column('user', 'width')
    op.drop_column('user', 'height')
    # ### end Alembic commands ###
