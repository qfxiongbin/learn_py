from threading import Thread

class ThreadExcuter:
  
  def do_excuter(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads : thread.start()
    for thread in threads : thread.join()
    
    first, *rest = workers
    for worker in rest:
        first.reduce(worker)
    return first.result