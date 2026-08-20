from src.histogram_retriever.dataset import MyDataset
    

class Retriever:

  def __init__(self, data=MyDataset()):
    self.data = data
    pass

  def retrieve_histogram(self):
    with open(self.data.path_info, "r") as f:

      for line in f:
        if(line[0] == 'N'): # image name
          self.data.like_array.array[0] = line[2:]
        elif(line[0] == 'H'):
          channels = ["R", "G", "B", "A"]
          if(f.read(1) == 'R'):
            
          elif(f.read(1) not in channels):
            print("Error reading dataset info file. Formatting incorrect.")
      
    
