import math, random, sys
from FractalWorld import*

world = FractalWorld(width=800,height=800,delay=0)
Bob=Fractal(draw=False)

class rule(object):
	def __init__(self):
		self.rule={}
	
	def startrule(self, left, right):
		self.rule[left] = right
		
	def replace(self, orglist, depth):
		self.list=orglist
		while depth !=0:
			idnolist=[]
			for i in orglist:
				if i in self.rule:
					idnolist.extend(self.rule.get(i))
					print '1', idnolist, self.rule[i],self.list
				else:
					idnolist.extend(i)
					print idnolist,self.list
			self.list=idnolist
			depth-=1
			return self.list
		
class command(object):
	def __init__(self, cmd, arg):
		self.cmd=cmd
		self.arg=arg
	
	def execute(self,turtle, length):
		if self.cmd == 'lt':
			lt(turtle, int(self.arg[0]))
		if self.cmd =='rt':
			rt(turtle, int(self.arg[0]))
		if self.cmd == 'fd':
			fd(turtle, length[0])
		if self.cmd == 'bk':
			bk(turtle,length[0])
		if self.cmd == 'scale':
			length[0] = length[0]*float(self.arg[0])

class fractal(object):
	def __init__(self, start, rules, commands, length, depth):
		self.start = start
		self.rules = rules
		self.commands = commands
		self.length = [length]
		self.depth = depth
	
	def draw(self, orglist):
		for i in orglist:
			if type(i) == list:
				self.draw(i)
			else:
				cmd = self.commands[i]
				cmd.execute(Bob, self.length)

def read():
	files = open('tree.fdl')
	commands = {}
	r = rule()
	for line in files:
		line = line.strip()
		orglist = line.split(' ')
		if orglist[0] =='start':
			start = orglist[1:]	
		elif orglist[0] == 'rule':
			r.startrule(orglist[1], orglist[3:])
		elif orglist[0] =='cmd':
			cmd= command(orglist[2], orglist[3:])
			commands[orglist[1]] = cmd
		elif orglist[0] == 'length':
			length = int(orglist[1])
		elif orglist[0] == 'depth':
			depth = int(orglist[1])
	return fractal(start, r, commands, length, depth)

re = read()
print re.commands.keys()

arg= re.rules.replace(re.start, re.depth)
re.draw(arg)

wait_for_user()
			
	
		
		
