##

"""

  """

##

import json
from pathlib import Path

from mirutil.funcs import save_df_as_a_nice_xl as sxl
from mirutil.funcs import read_data_according_to_type as rdata
from mirutil.funcs import norm_fa_str as norm


btic = 'BaseTicker'

def main() :


  pass

  ##
  with open('META.json' , 'r') as fi :
    meta = json.load(fi)

  fpn = Path(meta['fn'])
  ##
  df = rdata(fpn)
  ##
  df = df.applymap(norm)
  ##
  df = df.drop_duplicates()
  ##
  df = df.sort_values(btic)
  ##
  sxl(df , fpn)
  ##


  ptr = '\D+'
  msk = ~ df[btic].str.fullmatch(ptr)
  df1 = df[msk]
  ##
  ptr = '\D+'
  msk = ~ df[btic].str.fullmatch(ptr)
  msk &= df[btic].str[:-1].isin(df[btic])

  df1 = df[msk]
  # sxl(df1, 'df1.xlsx')
  # df = df[~ msk]

  ##
  ptr = r'.+' + r'ح'
  msk = df[btic].str.fullmatch(ptr)
  df1 = df[msk]

  ##
  ptr = r'ض' + '.+'
  msk = df[btic].str.fullmatch(ptr)
  df1 = df[msk]

  ##
  ptr = r'ج' + '.+'
  msk = df[btic].str.fullmatch(ptr)
  df1 = df[msk]

  ##

##


if __name__ == "__main__" :
  main()