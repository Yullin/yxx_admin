"""empty message

Revision ID: 3b6f1905dd63
Revises: cf66c13e272b
Create Date: 2018-06-04 10:17:10.134539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b6f1905dd63'
down_revision = 'cf66c13e272b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'tb_role_admin', 'tb_admin', ['admin_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'tb_role_admin', 'tb_role', ['role_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tb_role_admin', type_='foreignkey')
    op.drop_constraint(None, 'tb_role_admin', type_='foreignkey')
    # ### end Alembic commands ###
