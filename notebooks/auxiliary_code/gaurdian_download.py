from tqdm import tqdm
from datetime import date, timedelta
from os.path import join, exists
from os import makedirs
import requests
import json
from login_data import GAURDIAN_API_KEY

countries = ['Afghanistan',
             'Angola',
             'Burundi',
             'Central African Republic',
             'Congo',
             'Djibouti',
             'El Salvador',
             'Eswatini',
             'Ethiopia',
             'Guatemala',
             'Haiti',
             'Honduras',
             'Kenya',
             'Lesotho',
             'Madagascar',
             'Malawi',
             'Mozambique',
             'Namibia',
             'Pakistan',
             'Somalia',
             'South Sudan',
             'Sudan',
             'Tanzania',
             'Uganda',
             'Yemen',
             'Zambia',
             'Zimbabwe',
             'South Africa',
             'Mauritania',
             'Niger',
             'Mali',
             'Burkina Faso',
             'Chad',
             'Nigeria']


class GaurdianApi:
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = 'http://content.guardianapis.com/search'

    def get_articles(self, keyword, from_date, to_date):
        # initial request
        resp_dict = self.__make_request(keyword, from_date, to_date, 1)
        pages = resp_dict['pages']
        data = resp_dict['results']
        for page in tqdm(range(2, pages + 1)):
            resp_dict = self.__make_request(keyword, from_date, to_date, page)
            if(resp_dict['status'] != 'ok'):
                print(resp_dict)
                continue
            data += resp_dict['results']
        return data

    def __make_request(self, keyword, from_date, to_date, page):
        params = {
            'from-date': from_date,
            'to-date': to_date,
            'order-by': "newest",
            'show-fields': 'all',
            'api-key': self.api_key,
            'q': keyword,
            'page': page,
            'page-size': 50,
        }
        resp = requests.get(self.endpoint, params)
        resp_dict = resp.json()['response']
        return resp_dict


if __name__ == '__main__':
    api = GaurdianApi(GAURDIAN_API_KEY)

    articles_per_country = dict()

    for country in countries:
        results = api.get_articles(country, "2008-01-01", "2013-05-31")
        results += api.get_articles(country, "2013-06-01", "2018-05-31")
        results += api.get_articles(country, "2018-06-01", "2022-06-01")
        articles_per_country[country] = results

    with open('guardian.json', 'w') as outfile:
        json.dump(articles_per_country, outfile)

    print('\nDone!')
