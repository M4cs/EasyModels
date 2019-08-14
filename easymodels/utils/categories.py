import requests as r
import json
from terminaltables import AsciiTable
from .constants import *
from webbrowser import open_new_tab

test = r.get(API_URL + 'categories/', headers=HEADERS)


class Categories:
    
    @staticmethod
    def get_all_categories():
        res = r.get(API_URL + 'categories/', headers=HEADERS)
        return res.json()
    
    @staticmethod
    def get_category_info(category):
        res0 = r.get(API_URL + 'categories/{}/0/'.format(category), headers=HEADERS).json()
        res1 = r.get(API_URL + 'categories/{}/50/'.format(category), headers=HEADERS).json()
        full_dict = dict(res0, **res1)
        return full_dict
    
    @staticmethod
    def categories_to_table():
        categories = Categories.get_all_categories()
        table_data = [
            ['ID#', 'Title', 'Description']
        ]
        count = 0
        for k, v in categories.items():
            table_data.append([count, v['title'], v['description']])
            count += 1
        table = AsciiTable(table_data, 'Categories')
        return table.table
    
    @staticmethod
    def get_github_link_from_category(category_info, choice):
        link = category_info['models'][choice].get('link')
        if link:
            open_new_tab(link)
        else:
            print('\nNo Link Available!\n')
    
    @staticmethod
    def create_table_from_category_info(category_info):
        titles = []
        descriptions = []
        links = []
        frameworks = []
        for model in category_info['models']:
            if model.get('title'):
                titles.append(model['title'][0:60])
            else:
                titles.append('null')
            if model.get('description'):
                description = model['description'][0:30].replace('<p>', '')
                descriptions.append(description + ('...' if not '</p>' in description else ''))
            else:
                descriptions.append('null')
            if model.get('link'):
                links.append(model['link'].replace('https://github.com/', ''))
            else:
                links.append('null')
            if model.get('framework'):
                frameworks.append(model['framework'])
            else:
                frameworks.append('null')
        count = 0
        table_data = [
            ['ID#', 'Title', 'Description', 'GitHub Link', 'Framework']
        ]
        while count <= (len(titles) - 1):
            table_data.append([count, titles[count], descriptions[count], links[count], frameworks[count]])
            count += 1
        table = AsciiTable(table_data, 'Available Models')
        return table.table
            
            