"""create colum readers and add relationship one to many

Revision ID: d00cd5f81fa8
Revises: 7f9e4c28af6f
Create Date: 2023-02-08 17:34:12.305800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd00cd5f81fa8'
down_revision = '7f9e4c28af6f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('readers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('books', sa.Column('readear_id', sa.Integer(), nullable=False))
    op.create_index(op.f('ix_books_readear_id'), 'books', ['readear_id'], unique=False)
    op.create_foreign_key(None, 'books', 'readers', ['readear_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'books', type_='foreignkey')
    op.drop_index(op.f('ix_books_readear_id'), table_name='books')
    op.drop_column('books', 'readear_id')
    op.drop_table('readers')
    # ### end Alembic commands ###