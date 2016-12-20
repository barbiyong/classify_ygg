import sqlite3 as db
import json

def get_stock_name_list():
    conn = db.connect('MARKETANYWARE')
    # print('Opened database successfully')
    cur = conn.cursor()
    query_result = cur.execute(
        " SELECT NAME FROM stock WHERE SECURITYTYPE = 'S' OR SECURITYTYPE = 'W' ").fetchall()
    stock_names = []

    for i, tmp in enumerate(query_result):
        append = str(tmp)[2:-3]
        stock_names.append(append)

    return stock_names


def get_stock_name_list_of_set100():
    stock_names = ['AAV', 'ADVANC', 'AMATA', 'ANAN', 'AOT', 'AP', 'BA', 'BANPU', 'BBL', 'BCH', 'BCP', 'BDMS',
                   'BEAUTY', 'BEC', 'BEM', 'BH', 'BJCHI', 'BLA', 'BLAND', 'BTS', 'CBG', 'CENTEL', 'CHG', 'CK',
                   'CKP','COM7', 'CPALL', 'CPF', 'CPN', 'DELTA', 'DTAC', 'EGCO', 'EPG', 'ERW', 'GL', 'GLOBAL',
                   'GLOW','GPSC', 'GUNKUL', 'HANA', 'HMPRO', 'ICHI', 'IFEC', 'INTUCH', 'IRPC', 'ITD', 'IVL',
                   'JWD','KBANK','KCE', 'KKP', 'KTB', 'KTC', 'LH', 'LHBANK', 'LPN', 'MAJOR', 'MINT', 'MTLS',
                   'PLANB', 'PS', 'PTG','PTT', 'PTTEP', 'PTTGC', 'QH', 'ROBINS', 'RS', 'S', 'SAMART', 'SAWAD',
                   'SCB', 'SCC', 'SGP', 'SIRI', 'SPALI', 'SPCG', 'STEC', 'STPI', 'SVI', 'TASCO', 'TCAP',
                   'THAI', 'THCOM', 'TISCO', 'TMB', 'TOP', 'TPIPL', 'TRC', 'TRUE', 'TTA', 'TTCL', 'TTW', 'TU',
                   'TVO', 'UNIQ', 'VGI', 'VNG', 'WHA', 'WORK']

    return stock_names


def get_stock_active_name_list():
    with open('active_stock.json') as data_file:
        stock_names = json.load(data_file)
    return stock_names
