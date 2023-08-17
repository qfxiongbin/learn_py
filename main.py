
from threading import Thread
from mapreduce.worker import LineCountWorker
from mapreduce.input_data import PathInputData
from mapreduce.excuter import ThreadExcuter as excute 
def excute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads : thread.start()
    for thread in threads : thread.join()
    
    first, *rest = workers
    for worker in rest:
        first.reduce(worker)
    return first.result
  
def do_mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return excute(workers)
  
  
if __name__ == "__main__":
    tempDir = 'test_inputs'
    config = {'data_dir': tempDir}
    # write_test_files(tempDir)
    result = do_mapreduce(LineCountWorker, PathInputData, config)
    print(f'There are {result} lines in {tempDir}')