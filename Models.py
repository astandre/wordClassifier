from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import exists

Base = declarative_base()


# association_table = Table('sentence_word', Base.metadata,
#                           Column('sentence_id', Integer, ForeignKey('sentence.id')),
#                           Column('word_id', Integer, ForeignKey('word.id'))
#                           )


class Sentence(Base):
    __tablename__ = 'sentence'

    id = Column(Integer, primary_key=True)
    sentence = Column(String(300), nullable=False)
    word = relationship("Word", back_populates="sentence")

    def __repr__(self):
        return "<Sentence(sentence='%s')>" % self.sentence

    __mapper_args__ = {
        'polymorphic_identity': 'sentence',
    }


class Word(Base):
    __tablename__ = 'word'

    id = Column(Integer, primary_key=True)
    word = Column(String(100), nullable=False)
    # lemma = Column(Integer, ForeignKey('word.id'), nullable=True)
    pos = Column(String(10), nullable=False)
    order = Column(Integer, nullable=False)
    # synonym = Column(Integer, ForeignKey('word.id'), nullable=True)
    sentence_id = Column(Integer, ForeignKey('sentence.id'))
    sentence = relationship("Sentence", back_populates="word")

    # sentence = relationship(
    #     "Sentence",
    #     secondary=association_table,
    #     back_populates="word")

    def __repr__(self):
        return "<Word(word='%s', pos='%s')>" % (
            self.word, self.pos)

    @staticmethod
    def check_word(session, word):
        return session.query(exists().where(Word.word == word)).scalar()

    __mapper_args__ = {
        'polymorphic_identity': 'word',
    }
