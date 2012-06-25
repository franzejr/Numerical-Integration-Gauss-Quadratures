#Quadratura de Gauss 
from Funcao import *
import math

#Gauss Hermite
#Para funcoes e^x(-2)*f(x)
class GaussHermite():

	def __init__(self):
		#Vetores com [raiz,peso]
		self.n2 = [ -0.70710678, 0.88622692 ],[ 0.70710678, 0.88622692 ]
		self.n3 = [ -1.22474487, 0.29540897 ],[ 0, 1.18163590 ],[ 1.22474487, 0.29540897 ]
		self.n4 = [ -1.65068012, 0.08131283 ],[ -0.52464762, 0.80491409 ],[ 0.52464762, 0.80491409 ],[ 1.65068012, 0.08131283 ]

	def calcular(self,numPontos):
		
		resultadoSubIntervalo = 0
		
			
		if numPontos == 2:
			raiz1 = self.n2[0][0]
			peso1 = self.n2[0][1]

			resultadoSubIntervalo += peso1*f(raiz1)

			raiz2 = self.n2[1][0]
			peso2 = self.n2[1][1]
			
			resultadoSubIntervalo += peso2*f(raiz2)

			return resultadoSubIntervalo

		elif numPontos == 3:

			raiz1 = self.n3[0][0]
			peso1 = self.n3[0][1]

			resultadoSubIntervalo += peso1*f(raiz1)

			raiz2 = self.n3[1][0]
			peso2 = self.n3[1][1]
			
			resultadoSubIntervalo += peso2*f(raiz2)


			raiz3 = self.n3[2][0]
			peso3 = self.n3[2][1]
			
			resultadoSubIntervalo += peso3*f(raiz3)

			return resultadoSubIntervalo

		elif numPontos == 4:

			raiz1 = self.n4[0][0]
			peso1 = self.n4[0][1]

			resultadoSubIntervalo += peso1*f(raiz1)

			raiz2 = self.n4[1][0]
			peso2 = self.n4[1][1]
			
			resultadoSubIntervalo += peso2*f(raiz2)


			raiz3 = self.n4[2][0]
			peso3 = self.n4[2][1]
			
			resultadoSubIntervalo += peso3*f(raiz3)

			raiz4 = self.n4[3][0]
			peso4 = self.n4[3][1]
			
			resultadoSubIntervalo += peso4*f(raiz4)
		
			return resultadoSubIntervalo


#Gauss Laguerre
#Para funcoes e^-x*f(x)
class GaussLaguerre():

	def __init__(self):
	
		#Vetores com [raiz,peso]
		self.n2 = [ 0.58578643, 0.85355339 ],[ 3.41421356, 0.14644660 ]
		self.n3 = [ 0.41577455, 0.71109300 ],[ 2.29428036, 0.27851773 ],[ 6.28994508, 0.010389256 ]
		self.n4 = [ 0.32254768, 0.60315410 ],[ 1.74576110, 0.35741869 ],[ 4.53662029, 0.038887908 ],[ 9.39507091, 0.00053929470 ]
		
		
	def calcular(self,numPontos):	
		resultadoSubIntervalo = 0
		raiz = 0
		peso = 0
		
		if numPontos == 2:
			raiz1 = self.n2[0][0]
			peso1 = self.n2[0][1]

			resultadoSubIntervalo += peso1*f(raiz1)

			raiz2 = self.n2[1][0]
			peso2 = self.n2[1][1]
			
			resultadoSubIntervalo += peso2*f(raiz2)

			return resultadoSubIntervalo

		elif numPontos == 3:

			raiz1 = self.n3[0][0]
			peso1 = self.n3[0][1]

			resultadoSubIntervalo += peso1*f(raiz1)

			raiz2 = self.n3[1][0]
			peso2 = self.n3[1][1]
			
			resultadoSubIntervalo += peso2*f(raiz2)


			raiz3 = self.n3[2][0]
			peso3 = self.n3[2][1]
			
			resultadoSubIntervalo += peso3*f(raiz3)

			return resultadoSubIntervalo

		elif numPontos == 4:

			raiz1 = self.n4[0][0]
			peso1 = self.n4[0][1]

			resultadoSubIntervalo += peso1*f(raiz1)

			raiz2 = self.n4[1][0]
			peso2 = self.n4[1][1]
			
			resultadoSubIntervalo += peso2*f(raiz2)


			raiz3 = self.n4[2][0]
			peso3 = self.n4[2][1]
			
			resultadoSubIntervalo += peso3*f(raiz3)

			raiz4 = self.n4[3][0]
			peso4 = self.n4[3][1]
			
			resultadoSubIntervalo += peso4*f(raiz4)
		
			return resultadoSubIntervalo

#GaussChebyshev
#Utilizando intervalo de integracao -1 a 1
class GaussChebyshev():
	
	def calcular(self,numPontos):
		resultadoSubIntervalo = 0
		
		w = math.pi/numPontos
		for i in range(1,numPontos+1):
			xk = math.cos(((i - 1/2)*math.pi)/numPontos)
			resultadoSubIntervalo += w*f(xk)
		return resultadoSubIntervalo
			
