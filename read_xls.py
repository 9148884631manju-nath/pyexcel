import pandas as pd
import openpyxl

def read_xls(ty,sheet,fle):
 res=""
 ob = openpyxl.load_workbook(fle, data_only=True)
 match ty:
  case "getsheets":
   res = ob.sheetnames
  case "getsheet":
   res = ob[sheet]
  case "rowscolstojson":
   res = rowscolstojson()
  case _:
   res = "none"
 return res
