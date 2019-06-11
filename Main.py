import spacy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import *
import sys
import getopt
import io
from decouple import config

nlp = spacy.load("es_core_news_sm")

engine = create_engine(config('DATA_BASE'), echo=False, encoding='utf8', case_sensitive=True)

Base.metadata.create_all(engine)


def handle_sentences(sentence):
    print("SENTECE: ", sentence)
    new_sentence = Sentence(sentence=sentence)
    session.add(new_sentence)
    session.commit()
    sentence = nlp(sentence)
    order = 0
    for token in sentence:
        word = token.text.lower()
        if not token.is_stop and token.is_punct is False and token.pos_ != "SPACE":
            print("WORD: %s | POS: %s | LEMMA: %s" % (word, token.pos_, token.lemma_))
            new_word = Word(word=word, pos=token.pos_, order=order, lemma=token.lemma_, sentence_id=new_sentence.id)
            session.add(new_word)
            order += 1

    session.commit()


if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "hf:", ["ifile="])
    except getopt.GetoptError:
        print('Required parameters -f <inputfile> ')
        sys.exit(2)
    for opt, arg in opts:
        # print(opt, arg)
        if opt == '-h':
            print('Required parameters -f <inputfile> ')
            sys.exit()
        elif opt in ("-f", "--ifile"):
            ff = io.open(arg, 'r', encoding='utf-8')
            data = nlp(ff.read())
            ff.close()
            for i, token in enumerate(data.sents):
                handle_sentences(token.text)
