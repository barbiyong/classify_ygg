import json
from collections import OrderedDict
from datetime import date, timedelta
from decimal import Decimal
from time import strftime

from get_name import get_stock_active_name_list, get_stock_name_list_of_set100
from read_data import get_chunk_data_by_name_and_date


def calculate_profit(data):
    return ((data[-1] - data[0]) / data[0]) * 100


def get_stock_name_of_growth_more_than_percent_with_period(growth: Decimal, periods):
    """
    get Stock Name that have growth more than growth(unit = %) in period(unit = day).
    :param growth: (type: decimal)
    :param periods: (type: int)
    :return: stock_name, growth,
    """
    yesterday = date.today() - timedelta(1)

    # get all stock name
    stock_names = get_stock_active_name_list()
    # stock_names = get_stock_name_list_of_set100()
    # stock_names = ['AOT']
    ret_json = []
    dictionary = OrderedDict()
    template_name = 'stock growth more than ' + str(int(growth)) + ' in ' + str(int(periods)) + ' day'
    dictionary['template_name'] = template_name
    dictionary['stock_name'] = []
    dictionary['growth'] = []
    for s in stock_names:
        stock_data = get_chunk_data_by_name_and_date(s, 'day', yesterday.strftime("%m/%d/%Y"), periods)[1]
        # stock_data = get_chunk_data_by_name_and_date(s, '12/16/2016', periods)[1]
        try:
            cp = calculate_profit(stock_data)
        except TypeError:
            pass
            # print("can't calculate for'" + s)
        if cp > growth:
            dictionary['stock_name'] = s
            dictionary['growth'] = cp
            # ret_json.append(json.dumps(dictionary, ensure_ascii=False))
            ret_json.append(s)
    return ret_json

# print(get_stock_name_of_growth_more_than_percent_with_period(Decimal(5), 5))
# print(get_stock_name_of_growth_more_than_percent_with_period(Decimal(20.0), 20))
print(get_stock_name_of_growth_more_than_percent_with_period(Decimal(20.0), 90))

# with open('tmp.json') as data_file:
#     ret_val = json.load(data_file)

