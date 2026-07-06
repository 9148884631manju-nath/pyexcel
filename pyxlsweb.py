from read_xls import read_xls
class PYXLSWEB:
 def __init__(self,pd,host,fl,path,headers,reqs,sxs):
  self.ss = sxs
  self.pd = pd
  self.host=host
  self.path=path
  self.headers=headers
  self.reqs=reqs
  self.sxs=sxs
  self.fl = fl
 def __str__(self):
  return self.html(self.fl)
 
 def html(self,fl):
  res=""
  wb = read_xls("getsheet","mainlinks","website.xlsx")
  res = self.sheetrows(wb)
  #res = self.links(getsheets)
  return res
 
 def sheetrows(self,sn):
  res=""
  for hds in sn.iter_rows(max_row=1):
    heds=[cell.value for cell in hds]
  jj=""
  res+="["
  for row in sn.iter_rows(min_row=2):
   das=[cell.value for cell in row]
   resx=""
   jj+="{"
   for hx, rx in zip(heds,das):
    resx+='"'+hx+'":"'+str(rx)+'",'
   jj+=resx[:-1]+"},"
  res="["+jj[:-1]+"]"
  return res
  
 def links(self,da):
  res=""
  for ln in da:
   res+='<a href="'+ ln +'">'+ ln +'</a>'
  
  return res