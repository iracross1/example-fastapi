"""add user table

Revision ID: f1b8b4f9d6f1
Revises: 24bbb40330a5
Create Date: 2022-10-07 10:57:57.708966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1b8b4f9d6f1'
down_revision = '24bbb40330a5'
branch_labels = None
depends_on = None


def upgrade(): 
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass



def downgrade():
    op.drop_table('users')
    pass
