"""Test Migration

Revision ID: d4f74a0dc255
Revises: fed54c5ee8f1
Create Date: 2024-12-08 13:22:59.815374

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd4f74a0dc255'
down_revision: Union[str, None] = 'fed54c5ee8f1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('delay_reports', 'driver_id',
                    existing_type=sa.INTEGER(),
                    nullable=False)
    op.alter_column('delay_reports', 'trip_id',
                    existing_type=sa.INTEGER(),
                    nullable=False)
    op.alter_column('driver_locations', 'driver_id',
                    existing_type=sa.INTEGER(),
                    nullable=False)
    op.alter_column('intermediate_destinations', 'trip_id',
                    existing_type=sa.INTEGER(),
                    nullable=False)
    op.alter_column('notifications', 'driver_id',
                    existing_type=sa.INTEGER(),
                    nullable=False)

    # Add the `is_active` column with a default value of True
    op.add_column('users', sa.Column('is_active', sa.Boolean(),
                  server_default=sa.text('true'), nullable=False))

    # Optionally, remove the default if it is no longer required
    op.alter_column('users', 'is_active', server_default=None)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_active')
    op.alter_column('notifications', 'driver_id',
                    existing_type=sa.INTEGER(),
                    nullable=True)
    op.alter_column('intermediate_destinations', 'trip_id',
                    existing_type=sa.INTEGER(),
                    nullable=True)
    op.alter_column('driver_locations', 'driver_id',
                    existing_type=sa.INTEGER(),
                    nullable=True)
    op.alter_column('delay_reports', 'trip_id',
                    existing_type=sa.INTEGER(),
                    nullable=True)
    op.alter_column('delay_reports', 'driver_id',
                    existing_type=sa.INTEGER(),
                    nullable=True)
    # ### end Alembic commands ###
