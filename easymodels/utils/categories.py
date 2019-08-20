import requests as r
import json
from terminaltables import AsciiTable
from .constants import *
from webbrowser import open_new_tab
from crayons import *
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
    def categories_to_table(colors):
        categories = {'computer-vision': {'id': 1, 'slug': 'computer-vision', 'title': 'Computer Vision', 'short_title': 'CV', 'description': 'Computer Vision: Object detection, boundary labelling, segmentation.'}, 'natural-language-processing': {'id': 2, 'slug': 'natural-language-processing', 'title': 'Natural Language Processing', 'short_title': 'NLP', 'description': 'Natural Language Processing (NLP).'}, 'generative-models': {'id': 3, 'slug': 'generative-models', 'title': 'Generative Models', 'short_title': 'Generative', 'description': 'Generative Models, such as Generative Adversarial Networks (GANs), Variational Autoencoders (VAE), and more.'}, 'reinforcement-learning': {'id': 4, 'slug': 'reinforcement-learning', 'title': 'Reinforcement Learning', 'short_title': 'RL', 'description': 'Where an agent learn how to behave in a environment by performing actions and seeing the results.'}, 'unsupervised-learning': {'id': 5, 'slug': 'unsupervised-learning', 'title': 'Unsupervised Learning', 'short_title': 'Unsupervised', 'description': 'Unsupervised learning is a type of machine learning algorithm to draw inferences from datasets consisting of input data without labels.'}, 'audio-speech': {'id': 6, 'slug': 'audio-speech', 'title': 'Audio and Speech', 'short_title': 'Audio', 'description': 'Models and code that perform audio processing, speech synthesis, and other audio related tasks.'}}
        table_data = [
            ['ID#', 'Title', 'Description']
        ]
        count = 0
        for k, v in categories.items():
            if colors == True:
                table_data.append([str(blue(str(count), bold=True)), str(green(str(v['title']), bold=True)), str(white(str(v['description'][0:100]), bold=True))])
            else:
                table_data.append([count, v['title'], v['description'][0:100]])
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
    def create_table_from_category_info(category_info, colors):
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
            if colors == True:
                table_data.append([str(blue(str(count), bold=True)), str(blue(str(titles[count]), bold=True)), str(white(str(descriptions[count]), bold=True)), str(green(str(links[count]), bold=True)), str(yellow(str(frameworks[count]), bold=True))])
            else:
                table_data.append([count, titles[count], descriptions[count], links[count], frameworks[count]])
            count += 1
        table = AsciiTable(table_data, 'Available Models')
        return table.table
            
            