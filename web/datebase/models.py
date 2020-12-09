from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, Text, ForeignKey, Unicode
from sqlalchemy.orm import relationship, backref

from datebase import mixins

db = SQLAlchemy()


class User(db.Model, mixins.DictSerializableMixin):
    serializable_fields = ('id', 'login', 'email')

    id = Column(Integer, primary_key=True)
    login = Column(Unicode(255), unique=True, nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    password = Column(String(80), nullable=False)

    # relations
    players = relationship('Player', back_populates='user')


class Player(db.Model, mixins.DictSerializableMixin):
    serializable_fields = ('id', 'name', 'about')

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    about = Column(Text)

    # relations
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='players')

    contents = relationship('Content', back_populates='player')

    sessions = relationship('Session', back_populates='player')


class Content(db.Model, mixins.DictSerializableMixin):
    serializable_fields = ('id', 'name', 'description', 'player_id')

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(Text)
    file_name = Column(String(80), nullable=False)

    # relations
    player_id = Column(Integer, ForeignKey('player.id'), nullable=False)
    player = relationship('Player', back_populates='contents')


class Session(db.Model, mixins.DictSerializableMixin):
    serializable_fields = ('id', 'player_id')

    id = Column(Integer, primary_key=True)

    # relations
    player_id = Column(Integer, ForeignKey('player.id'), nullable=False)
    player = relationship('Player', back_populates='sessions')

    phrases = relationship('Phrase', back_populates='session')


class Phrase(db.Model, mixins.DictSerializableMixin):
    serializable_fields = ('id', 'content_id', 'session_id', 'question_id')

    id = Column(Integer, primary_key=True)

    # relations
    content_id = Column(Integer, ForeignKey('content.id'), nullable=False)
    content = relationship('Content')

    session_id = Column(Integer, ForeignKey('session.id'), nullable=False)
    session = relationship('Session', back_populates='phrases')

    question_id = Column(Integer, ForeignKey('phrase.id'))
    answers = relationship('Phrase', backref=backref('question', remote_side=[id]))
