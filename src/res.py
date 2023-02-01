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
        with open('ipc_id.json', 'r') as f:

            self.data = json.load(f)

    def ret_all(self):
        return self.data

    
    def ret_id_exact(self,section:str, *args, **kwargs):

        for i in self.data.keys():
            if str(self.data[i]['Section']) == section:
                return self.data[i]

        return {'error': 'No such section found'},422

    def ret_id(self, section:str, *args, **kwargs):
        # Fetch the Section for exact JSON
        for i in self.data.keys():
            if str(self.data[i]['Section']) == section:
                return self.data[i]

        return {'error': 'No such section found'},422
    
