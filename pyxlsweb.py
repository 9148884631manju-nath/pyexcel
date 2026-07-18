from read_xls import read_xls
import json
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
  wb = read_xls("getsheet","landingpage","website.xlsx")
  #res = self.jsontoelement(wb)
  res = self.rowscolstojsonwithhead(wb)

  tohtml = self.tohtml(res)

  return tohtml
 
 def tohtml(self,jd):
  res=json.loads(jd)
  ald=""
  for da in res:
   ald+=self.conele(da)   
  return ald
 
 def block(self,con):
  res=""
  blk = read_xls("getsheet",con,"website.xlsx")
  res = self.rowscolstojsonwithhead(blk)
  tohtml = self.tohtml(res)
  return tohtml
 
 def caonele(self,da):
  return str(da)
 
 def conele(self,da):
  res=""
  mm=""
  for ele,ff in da.items():
   mm+=ele+'="'+ ff +'" '
  match da["ele"]:
    case "block":
      blk=self.block(da["content"])
      res='<div '+ mm +'>'+ blk +'</div>'
    case "div":
      res='<div '+ mm +'>'+ da["content"] +'</div>'
    case "h1":
      res='<h1 '+ mm +'>'+ da["content"] +'</h1>'
    case "h4":
      res='<h4 '+ mm +'>'+ da["content"] +'</h4>'
    case "img":
      res='<img src='+ da["content"] +' '+ mm +' />'
    case "style":
      res='<style>'+da["id"]+' {'+da["class"]+'}</style>'
    case _:
      res=""    
  return res

 def rowscolstojsonwithhead(self,sn):
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
 
 def rowscolstojson(self,sn):
  jj=""
  for row in sn.iter_rows(min_row=1):
   das=[cell.value for cell in row]
   resx=""   
   for rx in das:
    resx+=str(rx)
   if resx=="None" or resx is None:
    jj+=""
   else: 
    jj+="<div>"+resx+"</div>"
  return jj
 
 def jsontoelement(self,data):
  res=""
  jsondata = self.rowscolstojsonwithhead(data)
  mda = json.loads(jsondata)
  for dd in mda:
   res+=self.ele("a",dd)
  return res

 def ele(self,ele,da):
  res=""
  attr=""
  for key,val in da.items():
   attr+=key+'="'+ val +'" '
  match ele:
   case "meta":
    res='<meta '+ attr +' />'
   case "title":
    res='<title>'+ da["title"] +'</'+ele+'>'
   case "link":
    res='<link '+ attr +' />'
   case "script":
    res='<script '+ attr +'>'+ da["scriptdata"] +'</script>'
   case "img":
    res='<img '+ attr +' />'
   case _:
    res='<'+ele+' '+ attr +'>'+ da["title"] +'</'+ele+'>'
  
  return res