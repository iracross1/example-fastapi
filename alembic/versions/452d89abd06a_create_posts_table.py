"""create posts table

Revision ID: 452d89abd06a
Revises: 
Create Date: 2022-10-07 10:38:41.216268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '452d89abd06a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
