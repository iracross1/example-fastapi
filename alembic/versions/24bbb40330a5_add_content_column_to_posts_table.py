"""add content column to posts table

Revision ID: 24bbb40330a5
Revises: 452d89abd06a
Create Date: 2022-10-07 10:52:16.830698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24bbb40330a5'
down_revision = '452d89abd06a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
