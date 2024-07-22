from sqlalchemy import Column, Integer, String, Text, BigInteger, ForeignKey, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    screen_name = Column(String(255))
    description = Column(Text)
    created_at = Column(TIMESTAMP)

class Tweet(Base):
    __tablename__ = 'tweets'
    tweet_id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.user_id'))
    text = Column(Text)
    in_reply_to_user_id = Column(BigInteger)
    retweeted_status_id = Column(BigInteger)
    created_at = Column(TIMESTAMP)
    lang = Column(String(5))

class Hashtag(Base):
    __tablename__ = 'hashtags'
    hashtag_id = Column(BigInteger, primary_key=True, autoincrement=True)
    tweet_id = Column(BigInteger, ForeignKey('tweets.tweet_id'))
    tag = Column(String(255))

class Interaction(Base):
    __tablename__ = 'interactions'
    interaction_id = Column(BigInteger, primary_key=True, autoincrement=True)
    tweet_id = Column(BigInteger, ForeignKey('tweets.tweet_id'))
    user_id = Column(BigInteger, ForeignKey('users.user_id'))
    contact_user_id = Column(BigInteger, ForeignKey('users.user_id'))
    type = Column(String(10))