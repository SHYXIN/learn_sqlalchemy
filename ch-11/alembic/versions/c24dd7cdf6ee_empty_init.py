"""Empty Init

The migration message we specified

Revision ID: c24dd7cdf6ee
Revises:
Create Date: 2024-01-04 09:28:44.908393

"""


from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c24dd7cdf6ee'  # 2、The Alembic revision ID
down_revision = None  # 3、The previous revision used to determine how to downgrade
branch_labels = None  # 4、 The branch associated with this migration
depends_on = None  # 5、Any migrations that this one depends on


def upgrade():
    pass


def downgrade():
    pass
