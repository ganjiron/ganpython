import pandas as pd


class HW34:
    def __init__(self):
        pass

    def readCsv(self):
        creditcard = pd.read_csv("creditcard.csv")
        creditcard.head()


if __name__ == '__main__':
    hw34 = HW34()
    hw34.readCsv()
