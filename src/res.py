import json



class Fetcher():
    """
    The fetcher class implements a method to fetch data from the json file.
    It is as simple as that.

    """
    


    def __init__(self)-> None:

        self.data = None
        self.load_data()

    def load_data(self):
        with open('ipc.json', 'r') as f:

            self.data = json.load(f)

    def ret_id(self, section:str, *args, **kwargs) -> dict:
        return self.data[section]
                
    
