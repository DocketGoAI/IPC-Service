import json



class Fetcher():

    


    def __init__(self)-> None:

        self.data = None
        self.load_data()

    def load_data(self):
        with open('ipc.json', 'r') as f:

            self.data = json.load(f)

    def ret_id(self, section, *args, **kwargs):
        return self.data[section]
                
    
