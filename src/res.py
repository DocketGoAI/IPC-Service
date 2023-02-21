import json
from .optimize_search import OptimizeSearch

class Fetcher():
    """
    The fetcher class implements a method to fetch data from the json file.
    It is as simple as that.

    """

    def __init__(self)-> None:
        self.data = None
        self.load_data()
        #class for optimized section search
        self.optimal=OptimizeSearch(self.data)

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
        # searching section in json data
        result=self.optimal.search(section)
        if(result!=None):
           return self.data[(result.key["key"])]

        return {'error': 'No such section found'},422
    
    def ret_keyword_section(self,keyword:str,*args,**kwargs):
        #searching for section using keywords
        keyword=self.optimal.search(keyword)
        keyword_lower=keyword.lower()

        for i in self.data.keys():
            sec_title_lower=self.data[i]['section_title'].lower()

            section_desc_lower= self.data[i]['section_desc'].lower()
           
            if keyword_lower in sec_title_lower or keyword_lower in section_desc_lower:
                
                return self.data[i]['Section']
            
            return {'error' : 'No matching sections found'},422
        

        
        

    
