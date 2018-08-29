import itertools

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cross_validation import KFold
# importing packages
from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import recall_score
from sklearn.model_selection import train_test_split
#### 1. Normalising the amount column.
from sklearn.preprocessing import StandardScaler


class HW34:

    def __init__(self):
        self.creditcard = pd.read_csv("creditcard.csv")
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

    def preprocessing(self):
        self.creditcard['normAmount'] = StandardScaler().fit_transform(
            np.array(self.creditcard['Amount']).reshape(-1, 1))
        self.creditcard = self.creditcard.drop(['Time', 'Amount'], axis=1)
        self.creditcard.head()
        #### 3. Resampling.
        X = self.creditcard.loc[:, self.creditcard.columns != 'Class']
        y = self.creditcard.loc[:, self.creditcard.columns == 'Class']
        # Number of data points in the minority class
        number_records_fraud = len(self.creditcard[self.creditcard.Class == 1])
        fraud_indices = np.array(self.creditcard[self.creditcard.Class == 1].index)
        # Picking the indices of the normal classes
        normal_indices = self.creditcard[self.creditcard.Class == 0].index
        # Out of the indices we picked, randomly select "x" number (number_records_fraud)
        random_normal_indices = np.random.choice(normal_indices, number_records_fraud, replace=False)
        random_normal_indices = np.array(random_normal_indices)

        # Appending the 2 indices
        under_sample_indices = np.concatenate([fraud_indices, random_normal_indices])
        under_sample_data = self.creditcard.iloc[under_sample_indices, :]
        X_undersample = under_sample_data.loc[:, under_sample_data.columns != 'Class']
        y_undersample = under_sample_data.loc[:, under_sample_data.columns == 'Class']
        # Showing ratio
        print("Percentage of normal transactions: ",
              len(under_sample_data[under_sample_data.Class == 0]) / len(under_sample_data))
        print("Percentage of fraud transactions: ",
              len(under_sample_data[under_sample_data.Class == 1]) / len(under_sample_data))
        print("Total number of transactions in resampled data: ", len(under_sample_data))

        # Whole dataset
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

        print("Number transactions train dataset: ", len(X_train))
        print("Number transactions test dataset: ", len(X_test))
        print("Total number of transactions: ", len(X_train) + len(X_test))

        # Undersampled dataset
        X_train_undersample, X_test_undersample, y_train_undersample, y_test_undersample = train_test_split(
            X_undersample
            , y_undersample
            , test_size=0.3
            , random_state=0)
        print("")
        print("Number transactions train dataset: ", len(X_train_undersample))
        print("Number transactions test dataset: ", len(X_test_undersample))
        print("Total number of transactions: ", len(X_train_undersample) + len(X_test_undersample))

        # Score 계산
        best_c = self.printing_Kfold_scores(X_train_undersample, y_train_undersample)

    def printing_Kfold_scores(self, x_train_data, y_train_data):
        fold = KFold(len(y_train_data), 5, shuffle=False)
        # fold = KFold(5,  shuffle=False)

        # >> > kf = KFold(n_splits=2)
        # >> > kf.get_n_splits(X)

        # Different C parameters
        c_param_range = [0.01, 0.1, 1, 10, 100]

        results_table = pd.DataFrame(index=range(len(c_param_range), 2), columns=['C_parameter', 'Mean recall score'])
        results_table['C_parameter'] = c_param_range

        # the k-fold will give 2 lists: train_indices = indices[0], test_indices = indices[1]
        j = 0
        for c_param in c_param_range:
            print('-------------------------------------------')
            print('C parameter: ', c_param)
            print('-------------------------------------------')
            print('')

            recall_accs = []
            for iteration, indices in enumerate(fold, start=1):
                # for iteration, indices in enumerate(fold.get_n_splits(y_train_data), start=1):
                # Call the logistic regression model with a certain C parameter
                lr = LogisticRegression(C=c_param, penalty='l1')

                # Use the training data to fit the model. In this case, we use the portion of the fold to train the model
                # with indices[0]. We then predict on the portion assigned as the 'test cross validation' with indices[1]
                lr.fit(x_train_data.iloc[indices[0], :], y_train_data.iloc[indices[0], :].values.ravel())

                # Predict values using the test indices in the training data
                y_pred_undersample = lr.predict(x_train_data.iloc[indices[1], :].values)

                # Calculate the recall score and append it to a list for recall scores representing the current c_parameter
                recall_acc = recall_score(y_train_data.iloc[indices[1], :].values, y_pred_undersample)
                recall_accs.append(recall_acc)
                print('Iteration ', iteration, ': recall score = ', recall_acc)

            # The mean value of those recall scores is the metric we want to save and get hold of.
            results_table.ix[j, 'Mean recall score'] = np.mean(recall_accs)
            j += 1
            print('')
            print('Mean recall score ', np.mean(recall_accs))
            print('')

        best_c = results_table.loc[results_table['Mean recall score'].argmax()]['C_parameter']

        # Finally, we can check which C parameter is the best amongst the chosen.
        print('*********************************************************************************')
        print('Best model to choose from cross validation is with C parameter = ', best_c)
        print('*********************************************************************************')

        return best_c

    # Create a function to plot a fancy confusion matrix
    def plot_confusion_matrix(cm, classes,
                              normalize=False,
                              title='Confusion matrix',
                              cmap=plt.cm.Blues):
        """
        This function prints and plots the confusion matrix.
        Normalization can be applied by setting `normalize=True`.
        """
        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=0)
        plt.yticks(tick_marks, classes)

        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
            # print("Normalized confusion matrix")
        else:
            1  # print('Confusion matrix, without normalization')

        # print(cm)

        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, cm[i, j],
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")

        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')



if __name__ == '__main__':
    hw34 = HW34()
    hw34.preprocessing()

    # hw34.checkTarget() #target Check 해보기
    # hw34.plotMix(28,30) # 전체 그림 그려보는것 arg(0) = 그림수 2~30
