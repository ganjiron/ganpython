import matplotlib.pyplot as plt
import nltk
import numpy as np
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import gutenberg as gu

tokenizer = nltk.RegexpTokenizer(r'\w+')  # 문장기호 제거하기
mycor = 'C:\world_news'
files = PlaintextCorpusReader(mycor, '.*')
a = files.raw('doyle_fear.txt')  # 돌레 소설 읽어오기
slw = tokenizer.tokenize(a.lower())  # 제거된 돌레

# 문장기호(punctuation) 제거
cbw = [w.lower() for w in gu.words('chesterton-brown.txt') if w[0].isalpha()]

# 많이 쓰인 상위 50개 단어 추출해서 top50 변수에 저장
top50 = nltk.FreqDist(cbw + slw).most_common(50)

# 각 작가별로 top50에 해당하는 단어가 작품에 몇 개나 나오는지 세서 M에 저장한다
M = []

for corp in [slw, cbw]:
    for i in range(len(corp) // 5000):
        words = [w for w in corp[5000 * i:5000 * (i + 1)] if w in top50]
        fdist = nltk.FreqDist(words)
        M.append([fdist[w] for w in top50])

# 단어 평균 빈도 그래프
plt.figure(figsize=(15, 4))
plt.plot(np.mean(M[:12], axis=0), 'b')
plt.plot(np.mean(M[12:], axis=0), 'g')

for i in range(50):
    plt.text(i, np.mean(M[12:], axis=0)[i], top50[i])

plt.legend(['Doyle', 'Chesterton'])
plt.title('means')
