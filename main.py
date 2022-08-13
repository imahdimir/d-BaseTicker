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
  ptr = '\D+'
  msk = ~ df[btic].str.fullmatch(ptr)
  msk &= df[btic].str[:-1].isin(df[btic])

  df1 = df[msk]
  # sxl(df1, 'df1.xlsx')
  df = df[~ msk]

  ##



if __name__ == "__main__" :
  main()