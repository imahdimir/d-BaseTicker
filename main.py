##
import pandas as pd
from mirutil.funcs import save_df_as_a_nice_xl as sxl
from mirutil.funcs import read_data_according_to_type as rdata

btic = 'BaseTicker'
fpn = 'Unique-BaseTickers-TSETMC.xlsx'

def main() :


  pass

  ##
  df = rdata(fpn)

  ##
  df = df.drop_duplicates()

  ##
  df = df.sort_values(btic)

  ##
  sxl(df, fpn)

  ##



if __name__ == "__main__" :
  main()