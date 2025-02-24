import numpy as np

class LinearRegression:
    def __init__(self):
        self.slope = None
        self.intercept = None


    def fit(self, X, y):
        """
        learning function
        :param X: independent variable (2d array format)
        :param y: dependent variable (2d array format)
        :return:
        """
        X_mean = np.mean(X)
        y_mean = np.mean(y)

        denominator = np.sum(pow(X-X_mean, 2)) #분모 계산
        numerator = np.sum((X-X_mean)*(y-y_mean)) #분자 계산

        self.slope = numerator / denominator
        self.intercept = y_mean - (self.slope * X_mean)
        #통계 회귀 분석 mse



    def predict(self, X) -> list:
        """
        predict value for input
        :param X: new indepent variable
        :return: predict value for input (2d array format)
        """

        return self.slope * np.array(X) + self.intercept