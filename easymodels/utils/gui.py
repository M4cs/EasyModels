import PySimpleGUIQt as g
import sys
from easymodels.utils import Categories
from webbrowser import open_new_tab


class GUI:
    
    def category_to_layout(category_info):
        titles = []
        links = []
        frameworks = []
        col1 = []
        col2 = []
        count = 0
        for model in category_info['models']:
            if model.get('title'):
                titles.append(model['title'][0:60])
            else:
                titles.append('null')
            if model.get('link'):
                links.append(model['link'].replace('https://github.com/', ''))
            else:
                links.append('null')
            if model.get('framework'):
                frameworks.append(model['framework'])
            else:
                frameworks.append('null')
        for x in range(len(titles)):
            if (count % 2) != 0:
                col1.append([g.Button(titles[x] + ' | ' + frameworks[x], key='https://github.com/' + links[x])])
            else:
                col2.append([g.Button(titles[x] + ' | ' + frameworks[x], key='https://github.com/' + links[x])])
            count += 1
        
        return col1, col2
    
    def gui(dark=False):
        if 'win' in sys.platform:
            titlebar = True
        else:
            titlebar = False
        if dark:
            background_color="#262626"
            input_elements_background_color="#262626"
            button_color=('white', '#171717')
            text_color="white"
            text_element_background_color="#262626"
            input_text_color="white"
        else:
            background_color='white'
            input_elements_background_color='#474747'
            button_color=('black', 'white')
            text_color='black'
            text_element_background_color='white'
            input_text_color='black'
        g.SetOptions(background_color=background_color, input_elements_background_color=input_elements_background_color, button_color=button_color,
                     text_color=text_color, text_element_background_color=text_element_background_color, border_width=0, input_text_color=input_text_color,
                     auto_size_buttons=True, auto_size_text=True)
        layout = [
            [g.T('EasyModels', font=('Arial', 15))],
            [g.T('Please pick a category from below:')]
        ]
        cat_json = Categories.get_all_categories()
        titles = []
        cat_to_id = {
            'Computer Vision': 'computer-vision',
            'Natural Language Processing': 'natural-language-processing',
            'Generative Models': 'generative-models',
            'Reinforcement Learning': 'reinforcement-learning',
            'Unsupervised Learning': 'unsupervised-learning',
            'Audio and Speech': 'audio-speech'
        }
        for k, v in cat_json.items():
            titles.append([v['title']])
        for title in titles:
            layout.append([g.Button(str(title[0]), key=cat_to_id[title[0]])])
        layout.append([g.Cancel('Close')])

        window = g.Window('EasyModels', layout=layout, keep_on_top=True, grab_anywhere=True, no_titlebar=titlebar)

        while True:
            event, values = window.Read()
            print(event)
            if event == 'Close':
                exit()
            else:
                category_info = Categories.get_category_info(event)
                new_layout = [
                    [g.T('Available Projects', font=('Arial', 15))]
                ]
                col1, col2 = GUI.category_to_layout(category_info)
                new_layout.append([g.Column(col2), g.Column(col1)])
                new_layout.append([g.Cancel('Close')])
                new_window = g.Window('Projects', layout=new_layout, keep_on_top=True, grab_anywhere=True, no_titlebar=titlebar)
                while True:
                    event1, values1 = new_window.Read()
                    if event1 == 'Close':
                        new_window.Close()
                        break
                    else:
                        open_new_tab(event1)