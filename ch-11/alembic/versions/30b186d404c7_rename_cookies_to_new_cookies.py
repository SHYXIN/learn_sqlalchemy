"""Rename cookies to new_cookies

Revision ID: 30b186d404c7
Revises: 33ed676a9ead
Create Date: 2024-01-04 10:20:12.534364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30b186d404c7'
down_revision = '33ed676a9ead'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('cookies', 'new_cookies')



def downgrade():
    op.rename_table('new_cookies', 'cookies')
