import matplotlib.pyplot as plt
import nltk
import numpy as np
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import gutenberg as gu
from matplotlib.colors import ListedColormap

tokenizer = nltk.RegexpTokenizer(r'\w+')  # 문장기호 제거하기
mycor = 'C:\git\ganjiron\jupyter\PythonClass'
files = PlaintextCorpusReader(mycor, '.*')
a = files.raw('doyle_fear.txt')  # 돌레 소설 읽어오기
slw = tokenizer.tokenize(a.lower())  # 제거된 돌레

# 문장기호(punctuation) 제거
cbw = [w.lower() for w in gu.words('chesterton-brown.txt') if w[0].isalpha()]

# 많이 쓰인 상위 50개 단어 추출해서 top50 변수에 저장
top50_all = nltk.FreqDist(cbw+slw)
top50 = []
for word, frequency in top50_all.most_common(50):
    top50.append(word)

# 각 작가별로 top50에 해당하는 단어가 작품에 몇 개나 나오는지 세서 M에 저장한다
M = []

for corp in [slw, cbw]:
    for i in range(len(corp) // 5000):
        # words = [w for w in corp[5000 * i:5000 * (i + 1)] if w in top50]
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
# plt.show()

# 표준화
M = np.array(M)
M = M - np.mean(M, axis=0)[None, :]  # 컬럼별 mean, 즉 단어별 평균 빈도
M = M / np.std(M, axis=0)  # 단어별 표준 점수화

M = M - np.mean(M, axis=1)[:, None]  # word block 별 평균 표준 점수를 구해서 빼준다(표준화?)

# SVD 수행
U, S, Vt = np.linalg.svd(M,full_matrices=False)

# U, S의 dot product 수행
smat = np.diag(S)
US = np.dot(U,smat)

# Vt를 transpose 해서 S와 dot product 수행
Vttras = np.transpose(Vt)

VS = np.dot(Vttras,smat)

# 문서 분포 그래프
plt.plot(US[:12, 0], US[:12, 1], 'ob')
plt.plot(US[12:, 0], US[12:, 1], 'og')
plt.xlim(-8, 8)
plt.ylim(-6, 6)

plt.title('Sherlock                            Father Brown')

# 단어 분포 그래프
cmap_light = ListedColormap(['#0000FF', '#00FF00'])

plt.figure(figsize=(8, 6))
plt.scatter(VS[:, 0], VS[:, 1], c=VS[:, 0], cmap=cmap_light)
for k in range(len(top50)):
    plt.text(VS[k][0] + .05, VS[k][1] + .05, top50[k])
plt.title('Sherlock words                       Father Brown words')
plt.show()