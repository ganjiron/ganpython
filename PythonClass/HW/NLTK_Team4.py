import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import gutenberg
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer


class NLTK_Team4:
    def __init__(self):
        stop_words = set(stopwords.words('english'))  # Stop word 가져오기
        tokenizer = RegexpTokenizer(r'\w+')  # 문장기호 제거하기
        a = gutenberg.raw('chesterton-brown.txt')  # 브라운 소설 읽어오기
        self.word_gu = tokenizer.tokenize(a.lower())  # 제거된 브라운
        mycor = 'C:\world_news'
        files = PlaintextCorpusReader(mycor, '.*')
        a = files.raw('doyle_fear.txt')  # 돌레 소설 읽어오기
        self.word_do = tokenizer.tokenize(a.lower())  # 제거된 돌레
        # 상위 50개 만들기 with and without stop word
        word_gu_TopWith = dict(nltk.FreqDist(self.word_gu).most_common(50))
        word_do_TopWith = dict(nltk.FreqDist(self.word_do).most_common(50))
        filtered_word_gu = []
        filtered_word_do = []
        for w in self.word_gu:
            if w not in stop_words:
                filtered_word_gu.append(w)
        for w in self.word_do:
            if w not in stop_words:
                filtered_word_do.append(w)
        word_gu_TopWithout = dict(nltk.FreqDist(filtered_word_gu).most_common(50))
        word_do_TopWithout = dict(nltk.FreqDist(filtered_word_do).most_common(50))

    def makeD(self):
        dxx = [[], []]
        for i in range(0, len(self.word_gu) // 5000 + 1):
            for j in range(5000):
                if i * 5000 + j < 73288:
                    dxx[i].append(self.word_gu[i * 5000 + j])

    def preprocess(sentence):
        sentence = sentence.lower()
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(sentence)
        filtered_words = [w for w in tokens if not w in stopwords.words('english')]
        return " ".join(filtered_words)


if __name__ == '__main__':
    team4 = NLTK_Team4()
    team4.makeD()
