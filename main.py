#Integracao Numerica - Quadratura de Gauss
#Universidade Federal do Ceara
#Metodos Numericos 2 - Prof. Creto Vidal
#@franzejr

from QuadraturaGauss import *
import sys,math

def main():
	
	#Tratamento da Entrada
	if len(sys.argv) == 3:
		metodo = sys.argv[1]
		numPontos = int(sys.argv[2])

	else:
		print "Voce deve inserir: <metodo>  numPontos \n"
		print  "<metodo> = hermite, laguerre, chebyshev\n"
		return

	#Escolhendo qual metodo utilizar de acordo com o usuario
	if(metodo.lower() == "hermite"):
	 	metodoIntegracao = GaussHermite()
	elif(metodo.lower() == "laguerre"):
	 	metodoIntegracao = GaussLaguerre()
	elif(metodo.lower() == "chebyshev"):
	 	metodoIntegracao = GaussChebyshev()

	
	valor_atual = metodoIntegracao.calcular(numPontos)

	print  valor_atual
		

main()
