from .categories import Categories
import sys
from crayons import *
class Menu:
    
    @staticmethod
    def main(colors):
        cat_to_id = {
            '0': 'computer-vision',
            '1': 'natural-language-processing',
            '2': 'generative-models',
            '3': 'reinforcement-learning',
            '4': 'unsupervised-learning',
            '5': 'audio-speech'
        }
        while True:
            if colors == True:
                print(white("""\
        \n\n
        EasyModels v1.6.1\n
        \tEasyModels is a tool to quickly, and easily find pre-trained AI
        \tmodels for your project. It uses the modelzoo.co API and offers
        \tinformation about the pre-trained models in an easy to view way.

        Created By: @maxbridgland\n""", bold=True))
            else:
                print("""\
        \n\n
        EasyModels v1.6.1\n
        \tEasyModels is a tool to quickly, and easily find pre-trained AI
        \tmodels for your project. It uses the modelzoo.co API and offers
        \tinformation about the pre-trained models in an easy to view way.

        Created By: @maxbridgland\n""")
            print(Categories.categories_to_table(colors))
            if colors == True:
                print(white('\nPlease Choose A Category by ID # From Above To Find Models or Type "exit" to Exit the Program\n', bold=True))
                category_id = input(green('$easymodels~ ', bold=True))
            else:
                print('\nPlease Choose A Category by ID # From Above To Find Models or Type "exit" to Exit the Program\n')
                category_id = input('$easymodels~ ')
            if category_id.lower() == 'exit':
                sys.exit()
            else:
                if not cat_to_id.get(category_id):
                    if colors == True:
                        print(red('\nInvalid Option! Please choose an ID # from the table above!\n', bold=True))
                    else:
                        print('\nInvalid Option! Please choose an ID # from the table above!\n')
                else:
                    if colors == True:
                        print(green('\nGrabbing Models Based On Choice...\n',bold=True))
                        category_info = Categories.get_category_info(cat_to_id[category_id])
                        print(Categories.create_table_from_category_info(category_info, colors))
                        print(white('\nPlease Choose A Project by ID # From Above To Find Models or Type "exit" to Exit the Program\n', bold=True))
                    else:
                        print('\nGrabbing Models Based On Choice...\n')
                        category_info = Categories.get_category_info(cat_to_id[category_id])
                        print(Categories.create_table_from_category_info(category_info, colors))
                        print('\nPlease Choose A Project by ID # From Above To Find Models or Type "exit" to Exit the Program\n')
                    while True:
                        if colors == True:
                            model_id = input(green('$easymodels~ ', bold=True))
                        else:
                            model_id = input('$easymodels~ ')
                        if model_id.lower() == "exit":
                            break
                        else:
                            try:
                                new_id = int(model_id)
                                Categories.get_github_link_from_category(category_info, new_id)
                                break
                            except:
                                print(Categories.create_table_from_category_info(category_info))
                                if colors == True:
                                    print(red('\nInvalid Option! Please choose an ID # from the table above!\n', bold=True))
                                else:
                                    print('\nInvalid Option! Please choose an ID # from the table above!\n')
                sys.stdout.flush()
    