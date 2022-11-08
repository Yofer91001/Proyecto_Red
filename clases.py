
 class Router:
  __init__(self):
    self.ip = ip
    self.ip_table = list()
   
  
  class Paquete:
    def __init__(self, load):
      self.load = load
      self.size = 0
      for _ in range(len(load)):
        self.size += 1
        
 
