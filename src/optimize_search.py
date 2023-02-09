
class OptimizeSearch():

    def __init__(self,data):
        self.data = data
        self.search_root=None
        self.indexing()
        

    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None  

    #insering data into binary tree
    def insert(self,node,key):
        if node is None:
            return self.Node(key)
        if key["Section"] < node.key["Section"]:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
        return node


    def search(self,key):
        if(self.search_root is None or self.search_root.key["Section"]==key):
            return self.search_root
        if(self.search_root.key["Section"]<key):
            self.search_root=self.search_root.right
            return self.search(key)
        self.search_root=self.search_root.left
        return self.search(key)
    
    #sorting json data for search
    def indexing(self):
        root=None
        for i in self.data.keys():
            root=self.insert(root,{"Section":(str(self.data[i]['Section'])),"key":i})
        self.search_root=root