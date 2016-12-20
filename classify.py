from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy
from decimal import Decimal
from read_data import get_data
from functionlist import get_rsi_7, get_rsi_14, macd_vs_signal, get_ema
from get_template_result import get_stock_name_of_growth_more_than_percent_with_period
from get_name import get_stock_active_name_list
import datetime


def get_train_feature():
    stocks_all = get_stock_active_name_list()
    stocks_good = get_stock_name_of_growth_more_than_percent_with_period(Decimal(15.0), 90)
    print(stocks_good)
    prev_day = datetime.datetime.strptime(str(datetime.date.today() - datetime.timedelta(90)),
                                          '%Y-%m-%d').strftime('%m/%d/%Y')

    y = []
    feature_rsi_7 = []
    feature_rsi_14 = []
    feature_ema_10 = []
    feature_ema_25 = []
    feature_ema_50 = []
    feature_ema_75 = []

    feature_macd_vs_signal = []
    # print(stocks_good)
    for symbol in stocks_all:
        # print(symbol + ":  " + str(get_data(symbol, 'day', '12/19/2016', '12/19/2016')))
        data = get_data(symbol, 'day', 0, prev_day)
        if data is None:
            pass
            # print('none' + symbol)
        else:
            feature_rsi_7.append([get_rsi_7(data['close'])])
            feature_ema_10.append([data['close'][-1]/float(get_ema(data['close'], 10))])
            feature_ema_25.append([data['close'][-1]/float(get_ema(data['close'], 25))])
            feature_ema_50.append([data['close'][-1]/float(get_ema(data['close'], 50))])
            # feature_ema_75.append([data['close'][-1]/float(get_ema(data['close'], 75))])
            # feature_rsi_14.append([get_rsi_14(data['close'])])
            feature_macd_vs_signal.append([macd_vs_signal(data['close'])])
            if symbol in stocks_good:
                # print('good' + symbol)
                y.append([1])
            else:
                y.append([0])

    features = numpy.hstack([
        numpy.array(feature_rsi_7),
        numpy.array(feature_ema_25),
        numpy.array(feature_ema_10),
        numpy.array(feature_ema_50),
        # numpy.array(feature_ema_75),
        # numpy.array(feature_rsi_14),
        numpy.array(feature_macd_vs_signal)
    ])
    output = numpy.hstack([numpy.array(y)])

    return features, output


def get_test_feature():
    feature_rsi_7 = []
    feature_rsi_14 = []
    feature_ema_10 = []
    feature_ema_25 = []
    feature_ema_50 = []
    feature_ema_75 = []
    feature_macd_vs_signal = []
    stocks_all = get_stock_active_name_list()
    for symbol in stocks_all:
        # print(symbol + ":  " + str(get_data(symbol, 'day', '12/19/2016', '12/19/2016')))
        data = get_data(symbol, 'day', 0, '12/19/2016')
        # print(data)
        if data is None:
            pass
            # print('none' + symbol)
        elif data is not None:
            feature_rsi_7.append([get_rsi_7(data['close'])])
            # feature_rsi_14.append([get_rsi_14(data['close'])])
            feature_ema_10.append([data['close'][-1]/float(get_ema(data['close'], 10))])
            feature_ema_25.append([data['close'][-1]/float(get_ema(data['close'], 25))])
            feature_ema_50.append([data['close'][-1]/float(get_ema(data['close'], 50))])
            # feature_ema_75.append([data['close'][-1]/float(get_ema(data['close'], 75))])
            feature_macd_vs_signal.append([macd_vs_signal(data['close'])])

    features = numpy.hstack([
        numpy.array(feature_rsi_7),
        numpy.array(feature_ema_25),
        numpy.array(feature_ema_10),
        numpy.array(feature_ema_50),
        # numpy.array(feature_ema_75),
        # numpy.array(feature_rsi_14),
        numpy.array(feature_macd_vs_signal)
    ])

    return numpy.asarray(features)


def prepare_data():
    X = []
    Y = []

    features, output = get_train_feature()
    X = numpy.asarray(features)
    # flatten y into a 1-D array
    Y = numpy.ravel(output)
    return X, Y


def fit_predict(X_train, Y, X_test):
    m = LogisticRegression()
    m.fit(X_train, Y)
    y_train = m.predict(X_train)
    y_test = m.predict(X_test)
    return y_train, y_test


def view1(X, y):
    group0 = y == 0
    group1 = y == 1

    x1 = X[group0, 0]
    x2 = X[group0, 1]
    plt.scatter(x1, x2, color='r')
    # print 'group0', [symbol for i, symbol in enumerate(SET50) if y[i] == 0]

    x1 = X[group1, 0]
    x2 = X[group1, 1]
    plt.scatter(x1, x2, color='b')


# print 'group1', [symbol for i, symbol in enumerate(SET50) if y[i] == 1]


def view2(X, y):
    group0 = y == 0
    group1 = y == 1

    x1 = X[group0, 0]
    x2 = X[group0, 1]
    plt.scatter(x1, x2, color='orange')
    # print 'group0', [symbol for i, symbol in enumerate(SET50) if y[i] == 0]

    x1 = X[group1, 0]
    x2 = X[group1, 1]
    plt.scatter(x1, x2, color='green')


# print 'group1', [symbol for i, symbol in enumerate(SET50) if y[i] == 1]


X, Y = prepare_data()
X_train = X
X_test = get_test_feature()

print(X_train)
print(Y)
print(X_test)
y_train, y_test = fit_predict(X_train, Y, X_test)
view1(X_train, y_train)
view2(X_test, y_test)
plt.show()
