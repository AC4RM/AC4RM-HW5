from homework import *
import urllib.request
import sqlite3
import pandas as pd
import sklearn
import re


def test_python():
    assert list_comp(list(range(1, 11))) == ['c', 'c', 'c', 'c', 'c', 'b', 'b', 'b', 'a', 'a']
    assert list_comp([1, 6, 10]) == ['c', 'b', 'a']


def test_sql():
    urllib.request.urlretrieve('https://github.com/AC4RM/AC4RM-dataset/blob/main/sql/data.db?raw=true', 'data.db')

    con = sqlite3.connect('data.db')

    customer_df = pd.read_sql_query(sql_query, con)

    assert customer_df.shape[0] == 1
    assert customer_df['name'][0] == 'Topiclounge'


def test_model():
    model = train_model()
    iris = datasets.load_iris()
    data = iris.data

    assert isinstance(model, sklearn.cluster._kmeans.KMeans)
    assert set(model.predict(data)) == set([0, 1, 2])


def test_regex():
    result = re.search(regex_pattern, '05/31/2023')
    assert set(result.groupdict().keys()) == set(['month', 'date', 'year'])
    assert result.group('month') == '05' and result.group('date') == '31' and result.group('year') == '2023'


def test_monte_carlo():
    results = []
    np.random.seed(42)
    for i in range(50):
        result = double_bettor(10000, 100, 20)
        results.append(result)

    assert len(list(filter(lambda y: y < 10000, map(lambda x: x[-1], results)))) == 4
    assert max(map(lambda x: x[-1], results)) == 11500
