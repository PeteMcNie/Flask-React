# 6: Create blue prints. A Blueprint is a way to organize a group of related views and other code. Rather than registering views and other code directly with an application, they are registered with a blueprint. Then the blueprint is registered with the application when it is available in the factory function.
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


# 7: Add view (backend) code for a form to register and login players. Add front end templates later.
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        playername = request.form['playername']
        password = request.form['password']
        db = get_db()
        error = None

        if not playername:
            error = 'Name is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM player WHERE playername = ?', (playername,)
        ).fetchone() is not None:
            error = 'Name {} is already registered.'.format(playername)

        if error is None:
            db.execute(
                'INSERT INTO player (playname, password) VALUES (?, ?)',
                (playername, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        playername = request.form['playername']
        password = request.form['password']
        db = get_db()
        error = None
        player = db.execute(
            'SELECT * FROM player WHERE playername = ?', (playername,)
        ).fetchone()

        if player is None:
            error = 'Incorrect name.'
        elif not check_password_hash(player['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['player_id'] = player['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

# 8: Function runs prior to view functions above, NO MATTER what url is requested
@bp.before_app_request
def load_logged_in_user():
    player_id = session.get('player_id')

    if player_id is None:
        g.player = None
    else:
        g.player = get_db().execute(
            'SELECT * FROM player WHERE id = ?', (player_id,)
        ).fetchone()


# 9: Ability to logout and remove session id
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


# 10: Require person to be authorised for other views (to make changes etc)
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
