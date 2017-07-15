import csv
import numpy as np

def T_X_from_csv( filename, T_columnname, sample_columnnames ):
   """this function reads the column <T_columnname> of csv file <filename> into T
   and the columns with names given in list <sample_columnnames> into matrix X
   and returns (T,X)"""
   T = []
   X = []
   rows = 0
   with open(filename, "rb") as csvfile:
      reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
      for row in reader:
          rows += 1
          T.append(row[T_columnname])
          X.extend([s for r, s in row.iteritems() if sample_columnnames.count(r) > 0])
      T_array = np.array(T, dtype=float);
      X_array = np.array(X, dtype=float).reshape(rows, -1)
      return (T_array,X_array)
