"""add relation form many to many

Revision ID: c9d00a4fdd67
Revises: d00cd5f81fa8
Create Date: 2023-02-08 18:12:23.035515

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9d00a4fdd67'
down_revision = 'd00cd5f81fa8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('readers_books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('readear_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ),
    sa.ForeignKeyConstraint(['readear_id'], ['readers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('ix_books_readear_id', table_name='books')
    op.drop_constraint('books_readear_id_fkey', 'books', type_='foreignkey')
    op.drop_column('books', 'readear_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('readear_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('books_readear_id_fkey', 'books', 'readers', ['readear_id'], ['id'])
    op.create_index('ix_books_readear_id', 'books', ['readear_id'], unique=False)
    op.drop_table('readers_books')
    # ### end Alembic commands ###
