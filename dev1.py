print("dev1.py")
print("hello world")
print("this is a test")
print("new line on py file")

class Gato(object):
	
	def __init__(self, nombre="ANONIMO", color="Neutro"):
		self.nombre=nombre
		self.color=color

	def ronronear(self):
		print(self.nombre+" "+"RNRNRNRNRNRNRNRNR")




class GatoSalvaje(Gato):
	def __init__(self, nombre="ANONIMO", color="Neutro", habitat="selva"):
		self.habitat=habitat
		super().__init__(nombre, color)
	
	def cazar(self):
	   	print(self.nombre+" "+"buscando y acechando una presa en "+self.habitat)

g=Gato()
g.ronronear()