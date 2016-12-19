from sklearn.mixture import GaussianMixture as GMM
import matplotlib.pyplot as plt

from back.data.get_ohlcv import get_last_data_by_name_and_date

STOCKS = ['APURE', 'AH', 'AMC', 'AI', 'GL', 'PAP', 'PTL', 'SAT', 'KSL', 'MIPF', 'SALEE', 'PERM', 'ESSO', 'STPI',
          'GREEN', 'TUCC', 'KASET', 'ACAP', 'CSP', 'AS', 'SYNEX', 'CHARAN', 'CPI', 'CTW', 'ECL', 'FANCY', 'FMT', 'INOX',
          'UNIQ', 'WIIK', 'LHK', 'LPN', 'LST', 'ML', 'NKI', 'PE', 'ROCK', 'SINGER', 'SPI', 'SSC', 'STA', 'TPIPL', 'TPP',
          'TR', 'TRS', 'TSI', 'TVI', 'TWP', 'THANI', 'TRUBB', 'UPOIC', 'UT', 'UVAN', 'WORK', 'YCI', 'ZMICO', 'MPG',
          'EFORL', 'TPOLY', 'CIMBT', 'SENA', '2S', 'AMANAH', 'TNPF', 'KAMART', 'KBS', 'SRICHA', 'PPS', 'GSTEL-W1',
          'BEAUTY', 'DNA', 'ARROW', 'M-II', 'TCC-W4', 'NBC-W1', 'AUCT', 'POLAR-W2', 'OCEAN', 'PCSGH', 'KTIS',
          'TAPAC-W2', 'PCA', 'M-PAT', 'XO', 'GLAND-W3', 'BRR', 'PAE-W1', 'VPO', 'DNA-W1', 'KCM', 'MILL-W3', 'SCN',
          'ECL-W2', 'MFC-W1', 'SLP', 'TVT', 'SVI-W3', 'WIIK-W1', 'MPG-W1', 'BWG-W3', 'MOONG-W1', 'JAS-W3', 'TSI-W2',
          'GREEN-W4', 'KOOL', 'TMILL-W1', 'BTC-W3', 'PSTC-W1', 'BM', 'TVT-W1']


def get_feature(symbol):
    for symbol in STOCKS:
        get_last_data_by_name_and_date(symbol, '12/13/2016')

    s = Stock(symbol, auto_update=False, limit=50)

    features = numpy.hstack([
        s.scaled_RSI()[-1],
        s.scaled_MACD()[0][-1],
        s.scaled_EMA(25)[-1]])
    return features


def prepare_data():
    X = []
    for symbol in SET50:
        X.append(get_feature(symbol))
    X = numpy.asarray(X)
    return X


def fit_predict(X_train, X_test):
    m = GMM(n_components=2)
    m.fit(X_train)
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


# X = prepare_data()
# X_train = X[:30, :]
# X_test  = X[30:, :]
#
# y_train, y_test = fit_predict(X_train, X_test)
# view1(X_train, y_train)
# view2(X_test, y_test)
# plt.show()
