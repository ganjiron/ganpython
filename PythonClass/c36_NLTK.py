import nltk
from nltk.corpus import gutenberg

a = len(gutenberg.raw('austen-emma.txt'))
b = len(gutenberg.words('austen-emma.txt'))
c = len(gutenberg.sents('austen-emma.txt'))

macbeth = gutenberg.sents('shakespeare-macbeth.txt')

# print(gutenberg.fileids())
# print(a ,b, c,macbeth)
######################### brown

from nltk.corpus import brown

print(brown.categories())
a = brown.words(categories='news')
b = brown.words(fileids=['cg22'])
c = brown.sents(categories=['news', 'editorial'])
fdist = nltk.FreqDist([w.lower() for w in a])
print(fdist)
print(fdist['can'])

cfd = nltk.ConditionalFreqDist((genre, word)
                               for genre in brown.categories()
                               for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfd.tabulate(conditions=genres, samples=modals)

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "This is a sample sentence, showing off the stop words filtration."

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)
