from itertools import chain
class rule(object):
 
 def __init__(self, left=[],right=[]):
  self.left=left
  self.right=right
 
def depthx(left,listex, depth):
 if depth<=0:
  return listex
 liste=[]
 for i in listex:
  if i not in left:
   liste.append(i)
  else:
   liste.append(depthx(left,listex,depth-1))
 print liste
"""
rule(["F"],["F", "L", "F", "R", "F", "L", "F"])
"""
depthx(["F"],["F", "L", "F", "R", "F", "L", "F"],2)

