import numpy as np

def calculate(lst):

  #Reshape into a 3x3 numpy array
  try:
    np_arr = np.reshape(np.array(lst), (3,3))
  except ValueError:
    raise ValueError('List must contain nine numbers.')

  calculations = dict()

  calculations['mean'] = [list(np_arr.mean(axis=0)), list(np_arr.mean(axis=1)), np_arr.mean()] 
  calculations['variance'] = [list(np_arr.var(axis=0)), list(np_arr.var(axis=1)), np_arr.var()]
  calculations['standard deviation'] = [list(np_arr.std(axis=0)), list(np_arr.std(axis=1)), np_arr.std()]
  calculations['min'] = [list(np_arr.min(axis=0)), list(np_arr.min(axis=1)), np_arr.min()]
  calculations['max'] = [list(np_arr.max(axis=0)), list(np_arr.max(axis=1)), np_arr.max()]
  calculations['sum'] = [list(np_arr.sum(axis=0)), list(np_arr.sum(axis=1)), np_arr.sum()]
  
  return calculations