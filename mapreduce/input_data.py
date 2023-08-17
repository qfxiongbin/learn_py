import os

class GenericInputData(object):
    
    def __init__(self, path):
        self.path = path
    
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError

class PathInputData(GenericInputData):
    def read(self):
         with open(self.path) as f:
            data = f.read()
         return data

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        print(f'PathInputData: data_dir = {data_dir}')
        for name in os.listdir(data_dir):
            print(f'PathInputData: name = {name}')
            yield cls(os.path.join(data_dir, name))