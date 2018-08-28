import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
#### 1. Normalising the amount column.
from sklearn.preprocessing import StandardScaler


class HW34:

    def __init__(self):
        self.creditcard = pd.read_csv("C:\ganpython\jupyter\creditcard.csv")

        self.cnt = self.creditcard.columns.size

    def plotHist(self):
        pos = [131, 132, 133]
        for i in range(1, self.cnt - 2):
            plot_lm_1 = plt.figure((i - 1) // 3)
            plt.subplot(pos[(i - 1) % 3])
            plot_lm_1.set_figheight(4)
            plot_lm_1.set_figwidth(15)
            d1 = self.creditcard[self.creditcard.columns[i]][self.creditcard.Class == 1]
            d2 = self.creditcard[self.creditcard.columns[i]][self.creditcard.Class == 0]
            sns.distplot(d1, color="b")
            sns.distplot(d2, color="r")
        plt.show()

    # 전체 그림 그려보는것 arg(0) = 그림수 2~30
    def plotMix(self , s_cnt , e_cnt):
        pos = [141, 142, 143, 144]
        # for i in range(1,creditcard.columns.size):
        for i in range(s_cnt, e_cnt):
            plot_lm_1 = plt.figure(i)
            plot_lm_1.set_figheight(4)
            plot_lm_1.set_figwidth(20)
            d1 = self.creditcard[self.creditcard.columns[i]][self.creditcard.Class == 1]
            d2 = self.creditcard[self.creditcard.columns[i]][self.creditcard.Class == 0]
            print('V{2} : D1 mean {0} , D2 mean {1}'.format(d1.mean(), d2.mean(), i))
            print('V{2} : D1 std {0} , D2 std {1}'.format(d1.std(), d2.std(), i))
            plt.subplot(pos[0])
            sns.distplot(d1, color="b")
            sns.distplot(d2, color="r")

            plt.subplot(pos[1])
            plt.plot(d2, 'r*')
            plt.plot(d1, 'bo')

            plt.subplot(pos[2])
            #     sns.categorical(x="Time", y="V1", data=creditcard);
            # sns.pairplot(self.creditcard, hue="Class")
        plt.show()

    # Class 간의 데이터 양 비교
    def checkTarget(self):
        count_classes = pd.value_counts(self.creditcard['Class'], sort=True)
        count_classes.plot(kind='bar')
        plt.xlabel("Class")
        plt.ylabel("Frequency")




if __name__ == '__main__':
    hw34 = HW34()
    hw34.checkTarget() #target Check 해보기
    hw34.plotMix(28,30) # 전체 그림 그려보는것 arg(0) = 그림수 2~30




