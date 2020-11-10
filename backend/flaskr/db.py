# 2: Need db file to access the database
import sqlite3

from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


# 4: Py functions that will run the SQL commands in this file
import click

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Pablo: Initialized the database.')


# 5: Register close_db() and init_db_command() with the application otherwise they are not used
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)