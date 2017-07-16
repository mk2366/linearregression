import csv
import numpy as np

class ColumnError(Exception):
   def __init__(self, value):
      self.value = value
   def __str__(self):
      return repr(self.value)

def T_X_from_csv( filename, T_columnname, sample_columnnames, delimiter = ',' ):
   """read the column <T_columnname> of csv file <filename> into T
   and the columns with names given in list <sample_columnnames> into matrix X
   and returns (T,X)"""
   file_content = np.genfromtxt( filename, delimiter = delimiter, names = True)
   headers = file_content.dtype.names
   if not type(sample_columnnames) == type([]):
      raise ColumnError('<sample_columnnames> not a list')
   if len(sample_columnnames) == 0:
      raise ColumnError('<sample_columnnames> is empty')
   for h in sample_columnnames:
       if not h in headers:
          raise ColumnError('Column in <sample_columnnames> does not exist in file')
   if not T_columnname in headers:
      raise ColumnError('<T_columnname> does not exist in file')

   X = np.array([linetuple[column] for column in sample_columnnames for linetuple in file_content]).reshape(len(sample_columnnames),-1).T
   T = np.array([linetuple[T_columnname] for linetuple in file_content])
   return (T , X)
