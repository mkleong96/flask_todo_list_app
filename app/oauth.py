import os

from flask_login import current_user, login_user
from flask_dance.consumer import oauth_authorized
from flask_dance.contrib.github import github, make_github_blueprint
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
# from flask_dance.contrib.twitter import twitter, make_twitter_blueprint
from sqlalchemy.orm.exc import NoResultFound

from app.models import db, OAuth, User


github_blueprint = make_github_blueprint(
    client_id='efe945aace2bb33c9c0f',
    client_secret='4ef43071efb63619f8f63aa04967f264abf14a7a',
    storage=SQLAlchemyStorage(
        OAuth,
        db.session,
        user=current_user,
        user_required=False,
    ),
)


@oauth_authorized.connect_via(github_blueprint)
def github_logged_in(blueprint, token):
    info = github.get("/user")
    if info.ok:
        account_info = info.json()
        username = account_info["login"]

        query = User.query.filter_by(username=username)
        try:
            user = query.one()
        except NoResultFound:
            user = User(username=username)
            db.session.add(user)
            db.session.commit()
        login_user(user)


