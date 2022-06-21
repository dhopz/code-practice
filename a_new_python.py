class NewClass:

    def __init__(self,new_array=[],an_integer=0):
        self.list_of_strings = new_array
        self.an_integer = an_integer

    def do_something_in_class(self):
        return self.list_of_strings * self.an_integer
        
    def create_json(self):
        return {'new_json':self.list_of_strings}