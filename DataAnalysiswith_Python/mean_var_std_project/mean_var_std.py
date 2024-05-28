import numpy as np
def calculate(list):
  if(len(list)!=9):
    raise ValueError("List must contain nine numbers.")
  ls=np.array(list)
  print(ls)
  mean_rows=[ls[[0,1,2]].mean(),ls[[3,4,5]].mean(), ls[[6,7,8]].mean()]
  mean_columns=([ls[[0,3,6]].mean(), ls[[1,4,7]].mean()], ls[[2,5,8]].mean())
  var_rows=[ls[[0,1,2]].var(), ls[[3,4,5]].var(), ls[[6,7,8]].var()]
  var_columns=([ls[[0,3,6]].std(), ls[[1,4,7]].std(), ls[[2,5,8]].std()])
  max_rows=([ls[[0,1,2]].max(), ls[[3,4,5]].max(), ls[[6,7,8]].max()])
  max_columns([ls[[0,3,6]].max(), ls[[1,4,7]].max(), ls[[2,5,8]].max()])
  min_rows=([ls[[0,1,2]].min(), ls[[3,4,5]].min(), ls[[6,7,8]].min()])
  min_columns=([ls[[0,3,6]].min(), ls[[1,4,7]].min(), ls[[2,5,8]].min()])
  sum_rows=([ls[[0,1,2]].sum(), ls[[3,4,5]].sum(), ls[[6,7,8]].sum()])
  sum_columns([ls[[0,3,6]].sum(), ls[[1,4,7]].sum(), ls[[2,5,7]].sum()])
  return{
    "mean":[mean_columns, mean_rows, ls.mean()],
    "variance":[var_columns, var_rows, ls.var()], 
    "standard deviation": [std_columns, std_rows, ls.std()],
    "max" : [max_columns, max_rows, ls.max()],
    "min" : [min_columns, min_rows, ls.min()],
    "sum" : [sum_columns, sum_rows, ls.sum()]
  }