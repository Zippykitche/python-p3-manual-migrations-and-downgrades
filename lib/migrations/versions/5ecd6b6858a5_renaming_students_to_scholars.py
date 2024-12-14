"""Renaming students to scholars

Revision ID: 5ecd6b6858a5
Revises: 791279dd0760
Create Date: 2024-12-15 00:10:42.127832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ecd6b6858a5'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')



def downgrade() -> None:
    op.rename_table('scholars', 'students')