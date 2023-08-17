
class GenericWorker:
    
   def __init__(self, input_data):
        self.input_data = input_data
        self.result = None
    
   def map(self):
        raise NotImplementedError
    
   def reduce(self, other):
        raise NotImplementedError
   
   @classmethod
   def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers
 
class LineCountWorker(GenericWorker):
  
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')
      
    def reduce(self, other):
        self.result += other.result 