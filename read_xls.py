import pandas as pd
import openpyxl as ox

def read_xls(ty,sheet,fle):
 res=""
 ob = ox.load_workbook(fle)
 match ty:
  case "getsheets":
   res = ob.sheetnames
  case "getsheet":
   res = ob[sheet]
  case _:
   res = ""
 return res
