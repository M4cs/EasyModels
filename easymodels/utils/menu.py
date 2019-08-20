from .categories import Categories
import sys
from crayons import *
class Menu:
    
    @staticmethod
    def main():
        cat_to_id = {
            '0': 'computer-vision',
            '1': 'natural-language-processing',
            '2': 'generative-models',
            '3': 'reinforcement-learning',
            '4': 'unsupervised-learning',
            '5': 'audio-speech'
        }
        while True:
            print(white("""\
    \n\n
    EasyModels v1.6\n
    \tEasyModels is a tool to quickly, and easily find pre-trained AI
    \tmodels for your project. It uses the modelzoo.co API and offers
    \tinformation about the pre-trained models in an easy to view way.

    Created By: @maxbridgland\n""", bold=True))
            print(Categories.categories_to_table())
            print(white('\nPlease Choose A Category by ID # From Above To Find Models or Type "exit" to Exit the Program\n', bold=True))
            category_id = input(green('$easymodels~ ', bold=True))
            if category_id.lower() == 'exit':
                sys.exit()
            else:
                if not cat_to_id.get(category_id):
                    print(red('\nInvalid Option! Please choose an ID # from the table above!\n', bold=True))
                else:
                    print(green('\nGrabbing Models Based On Choice...\n',bold=True))
                    category_info = Categories.get_category_info(cat_to_id[category_id])
                    print(Categories.create_table_from_category_info(category_info))
                    print(white('\nPlease Choose A Project by ID # From Above To Find Models or Type "exit" to Exit the Program\n', bold=True))
                    while True:
                        model_id = input(green('$easymodels~ ', bold=True))
                        if model_id.lower() == "exit":
                            break
                        else:
                            try:
                                new_id = int(model_id)
                                Categories.get_github_link_from_category(category_info, new_id)
                                break
                            except:
                                print(Categories.create_table_from_category_info(category_info))
                                print(red('\nInvalid Option! Please choose an ID # from the table above!\n', bold=True))
                sys.stdout.flush()
    