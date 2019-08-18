from .categories import Categories
import sys

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
            print("""\
    \n\n
    EasyModels v1.4.4\n
    \tEasyModels is a tool to quickly, and easily find pre-trained AI
    \tmodels for your project. It uses the modelzoo.co API and offers
    \tinformation about the pre-trained models in an easy to view way.

    Created By: @maxbridgland\n""")
            print(Categories.categories_to_table())
            print('\nPlease Choose A Category by ID # From Above To Find Models or Type "exit" to Exit the Program\n')
            category_id = input('$easymodels~ ')
            if category_id.lower() == 'exit':
                sys.exit()
            else:
                if not cat_to_id.get(category_id):
                    print('\nInvalid Option! Please choose an ID # from the table above!\n')
                else:
                    print('\nGrabbing Models Based On Choice...\n')
                    category_info = Categories.get_category_info(cat_to_id[category_id])
                    print(Categories.create_table_from_category_info(category_info))
                    print('\nPlease Choose A Project by ID # From Above To Find Models or Type "exit" to Exit the Program\n')
                    while True:
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
                                print('\nInvalid Option! Please choose an ID # from the table above!\n')
                sys.stdout.flush()
    