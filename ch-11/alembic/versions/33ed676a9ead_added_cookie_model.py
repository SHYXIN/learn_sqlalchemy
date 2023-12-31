"""Added Cookie Model

Revision ID: 33ed676a9ead
Revises: c24dd7cdf6ee
Create Date: 2024-01-04 09:55:31.935436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33ed676a9ead'
down_revision = 'c24dd7cdf6ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cookies',
    sa.Column('cookie_id', sa.Integer(), nullable=False),
    sa.Column('cookie_name', sa.String(length=50), nullable=True),
    sa.Column('cookie_recipe_url', sa.String(length=255), nullable=True),
    sa.Column('cookie_sku', sa.String(length=55), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('unit_cost', sa.Numeric(precision=12, scale=2), nullable=True),
    sa.PrimaryKeyConstraint('cookie_id')
    )
    op.create_index(op.f('ix_cookies_cookie_name'), 'cookies', ['cookie_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cookies_cookie_name'), table_name='cookies')
    op.drop_table('cookies')
    # ### end Alembic commands ###
