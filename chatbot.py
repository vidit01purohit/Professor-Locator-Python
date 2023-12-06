import random
import nltk
import string
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
from ttabstract import professors
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Chat:
    def __init__(self):
        self.sentence_tokens = [professor.lower() for professor in professors]
        self.lemmer = nltk.stem.WordNetLemmatizer()
        self.punc_dict = dict((ord(punct), None) for punct in string.punctuation)
        self.greet_inputs = ('hello', 'hi', 'whassup', 'how are you', 'hey', 'hey there!')
        self.greet_responses = ('Hi', 'Hey', 'Hey there!')

    def greet(self, sentence):
        for word in sentence.split():
            if word in self.greet_inputs:
                return random.choice(self.greet_responses)
    def lemtokens(self, tokens):
        return [self.lemmer.lemmatize(token) for token in tokens]

    def lemnormalize(self, text):
        return self.lemtokens(nltk.word_tokenize(text.translate(self.punc_dict)))

    def response(self, text):
        robo_res = ''
        tfidfvec = TfidfVectorizer(tokenizer=self.lemnormalize, stop_words='english')
        self.sentence_tokens.append(text)
        tfidf = tfidfvec.fit_transform(self.sentence_tokens)
        vals = cosine_similarity(tfidf[-1], tfidf)
        idx = vals.argsort()[0][-2]
        flat = vals.flatten()
        flat.sort()
        req_tfidf = flat[-2]
        if req_tfidf == 0:
            robo_res += "Incorrect professor name"
        else:
            robo_res += professors[idx]
        return robo_res

