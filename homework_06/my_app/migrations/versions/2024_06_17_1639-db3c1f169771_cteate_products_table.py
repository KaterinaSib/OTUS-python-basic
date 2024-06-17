"""cteate products table

Revision ID: db3c1f169771
Revises: 
Create Date: 2024-06-17 16:39:26.681345

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "db3c1f169771"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "product",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )


def downgrade():
    op.drop_table("product")
