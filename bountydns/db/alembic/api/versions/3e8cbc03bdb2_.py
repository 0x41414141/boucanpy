"""empty message

Revision ID: 3e8cbc03bdb2
Revises: ecbf1df79782
Create Date: 2019-04-01 17:57:28.578841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e8cbc03bdb2'
down_revision = 'ecbf1df79782'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dns_requests', sa.Column('dns_server_name', sa.String(), nullable=True))
    op.create_index(op.f('ix_dns_requests_dns_server_name'), 'dns_requests', ['dns_server_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_dns_requests_dns_server_name'), table_name='dns_requests')
    op.drop_column('dns_requests', 'dns_server_name')
    # ### end Alembic commands ###
