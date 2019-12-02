#Projecto de SO - Projecao dos Graficos
#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt


print "Resultado Grafico do Projecto de SO2 - 2018"

# Lambert, Leibniz, Viete, Nilakantha

# Num termos valor de pi e tempo exec (4 series)



# ----------------------------------------------  --- ---
#					Leitura de arquivos 
# ----------------------------------------------  --- ---
# Arquivo Lambert
numTermosLambert = []
valorPiLambert = []
tempoExecLambert = []
arq = open('processos/Lambert.txt', 'r+b')

for linha in arq:
	linha = linha.strip()
	termo,pi,tempo = linha.split(' ')
	numTermosLambert.append(termo)
	valorPiLambert.append(pi)
	tempoExecLambert.append(tempo)

arq.close()
# ----------------------------------------------  --- ---

# ----------------------------------------------  --- ---
# Arquivo Leibniz
numTermosLeibniz = []
valorPiLeibniz = []
tempoExecLeibniz = []
arq = open('processos/Leibniz.txt', 'r+b')

for linha in arq:
	linha = linha.strip()
	termo,pi,tempo = linha.split(' ')
	numTermosLeibniz.append(termo)
	valorPiLeibniz.append(pi)
	tempoExecLeibniz.append(tempo)

arq.close()
# ----------------------------------------------  --- ---

# ----------------------------------------------  --- ---
# Arquivo Viete
numTermosViete = []
valorPiViete = []
tempoExecViete = []
arq = open('processos/Viete.txt', 'r+b')

for linha in arq:
	linha = linha.strip()
	termo,pi,tempo = linha.split(' ')
	numTermosViete.append(termo)
	valorPiViete.append(pi)
	tempoExecViete.append(tempo)

arq.close()
# ----------------------------------------------  --- ---

# ----------------------------------------------  --- ---
# Arquivo Nilakantha
numTermosNilakantha = []
valorPiNilakantha = []
tempoExecNilakantha = []
arq = open('processos/Nilakantha.txt', 'r+b')

for linha in arq:
	linha = linha.strip()
	termo,pi,tempo = linha.split(' ')
	numTermosNilakantha.append(termo)
	valorPiNilakantha.append(pi)
	tempoExecNilakantha.append(tempo)

arq.close()
# ----------------------------------------------  --- ---















# ----------------------------------------------  --- ---
#		Graficos - Completos - Valor Pi
# ----------------------------------------------  --- ---

# ----------------------------------------------  --- ---
plt.figure("Grafico - Valor de Pi - Processos")
plt.plot(numTermosLambert,valorPiLambert, label = "Lambert", c='r')
plt.plot(numTermosLeibniz,valorPiLeibniz, label = "Leibniz", c='g')
plt.plot(numTermosViete,valorPiViete, label = "Viete", c='b')
plt.plot(numTermosNilakantha,valorPiNilakantha, label = "Nilakantha", c="#FF9800")
plt.legend()
plt.legend(loc=0)
plt.title("Grafico de Compraracao em Relacao ao Valor de Pi")
plt.xlabel("Numero de Termos")
plt.ylabel("Valor de Pi")
plt.xscale('log')
plt.ylim(2,3.5)
plt.grid(True)

plt.show()
# ----------------------------------------------  --- ---



# ----------------------------------------------  --- ---
#		Graficos - Completos - Tempo de Execucao 
# ----------------------------------------------  --- ---

# ----------------------------------------------  --- ---
plt.figure("Grafico - Tempo de Execucao - Processos")
plt.plot(numTermosLambert,tempoExecLambert, label = "Lambert", c='r')
plt.plot(numTermosLeibniz,tempoExecLeibniz, label = "Leibniz", c='g')
plt.plot(numTermosViete,tempoExecViete, label = "Viete", c='b')
plt.plot(numTermosNilakantha,tempoExecNilakantha, label = "Nilakantha", c="#FF9800")
plt.legend()
plt.legend(loc=2)
plt.title("Tempo de Execucao")
plt.xlabel("Numero de Termos")
plt.ylabel("Tempo de Execucao")
aux = 1 / 100000
plt.xscale('log')
plt.yscale('log')
 
plt.grid(True)
plt.show()
# ----------------------------------------------  --- ---




# ----------------------------------------------  --- ---

# ----------------------------------------------  --- ---

# ----------------------------------------------  --- ---


# ----------------------------------------------  --- ---
#Graficos Individuais  Lambert

plt.figure("Grafico Lambert - Valor de Pi - Processos")
plt.plot(numTermosLambert,valorPiLambert, label = "Lambert", c='r')
plt.legend()
plt.legend(loc=0)
plt.title("Grafico de Compraracao em Relacao ao Valor de Pi")
plt.xlabel("Numero de Termos")
plt.ylabel("Valor de Pi")
plt.xscale('log')
plt.ylim(2,3.5)
plt.grid(True)

plt.show()

plt.figure("Grafico Lambert - Tempo de Execucao - Processos")
plt.plot(numTermosLambert,tempoExecLambert, label = "Lambert", c='r')
plt.legend()
plt.legend(loc=2)
plt.title("Tempo de Execucao")
plt.xlabel("Numero de Termos")
plt.ylabel("Tempo de Execucao")
aux = 1 / 100000
plt.xscale('log')
plt.yscale('log')
 
plt.grid(True)
plt.show()
# ----------------------------------------------  --- ---


# ----------------------------------------------  --- ---
#Graficos Individuais  Leibniz

plt.figure("Grafico Leibniz - Valor de Pi - Processos")
plt.plot(numTermosLeibniz,valorPiLeibniz, label = "Leibniz", c='g')
plt.legend()
plt.legend(loc=0)
plt.title("Grafico de Compraracao em Relacao ao Valor de Pi")
plt.xlabel("Numero de Termos")
plt.ylabel("Valor de Pi")
plt.xscale('log')
plt.ylim(2,3.5)
plt.grid(True)

plt.show()

plt.figure("Grafico Leibniz - Tempo de Execucao - Processos")
plt.plot(numTermosLeibniz,tempoExecLeibniz, label = "Leibniz", c='g')
plt.legend()
plt.legend(loc=2)
plt.title("Tempo de Execucao")
plt.xlabel("Numero de Termos")
plt.ylabel("Tempo de Execucao")
aux = 1 / 100000
plt.xscale('log')
plt.yscale('log')
 
plt.grid(True)
plt.show()
# ----------------------------------------------  --- ---



# ----------------------------------------------  --- ---
#Graficos Individuais  Viete

plt.figure("Grafico Viete - Valor de Pi - Processos")
plt.plot(numTermosViete,valorPiViete, label = "Viete", c='b')
plt.legend()
plt.legend(loc=0)
plt.title("Grafico de Compraracao em Relacao ao Valor de Pi")
plt.xlabel("Numero de Termos")
plt.ylabel("Valor de Pi")
plt.xscale('log')
plt.ylim(2,3.5)
plt.grid(True)

plt.show()

plt.figure("Grafico Viete - Tempo de Execucao - Processos")
plt.plot(numTermosViete,tempoExecViete, label = "Viete", c='b')
plt.legend()
plt.legend(loc=2)
plt.title("Tempo de Execucao")
plt.xlabel("Numero de Termos")
plt.ylabel("Tempo de Execucao")
aux = 1 / 100000
plt.xscale('log')
plt.yscale('log')
 
plt.grid(True)
plt.show()
# ----------------------------------------------  --- ---



# ----------------------------------------------  --- ---
#Graficos Individuais  Nilakantha

plt.figure("Grafico Nilakantha - Valor de Pi - Processos")
plt.plot(numTermosNilakantha,valorPiNilakantha, label = "Nilakantha", c="#FF9800")
plt.legend()
plt.legend(loc=0)
plt.title("Grafico de Compraracao em Relacao ao Valor de Pi")
plt.xlabel("Numero de Termos")
plt.ylabel("Valor de Pi")
plt.xscale('log')
plt.ylim(2,3.5)
plt.grid(True)

plt.show()

plt.figure("Grafico Nilakantha - Tempo de Execucao - Processos")
plt.plot(numTermosNilakantha,tempoExecNilakantha, label = "Nilakantha", c="#FF9800")
plt.legend()
plt.legend(loc=2)
plt.title("Tempo de Execucao")
plt.xlabel("Numero de Termos")
plt.ylabel("Tempo de Execucao")
aux = 1 / 100000
plt.xscale('log')
plt.yscale('log')
 
plt.grid(True)
plt.show()
# ----------------------------------------------  --- ---


