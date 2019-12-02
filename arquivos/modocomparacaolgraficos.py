#Projecto de SO - Projecao dos Graficos
#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt


print "Resultado Grafico do Projecto de SO2 - 2018"

# Lambert, Leibniz, Viete, Nilakantha

# Num termos valor de pi e tempo exec (4 series)



# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



#											Modo Serial



# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ----------------------------------------------  --- ---
#					Leitura de arquivos 
# ----------------------------------------------  --- ---
# Arquivo Lambert
numTermosLambertSerial = []
valorPiLambertSerial = []
tempoExecLambertSerial = []
arq = open('serial/Lambert.txt', 'r+b')

for linha in arq:
	linha = linha.strip()
	termo,pi,tempo = linha.split(' ')
	numTermosLambertSerial.append(termo)
	valorPiLambertSerial.append(pi)
	tempoExecLambertSerial.append(tempo)

arq.close()
# ----------------------------------------------  --- ---

# ----------------------------------------------  --- ---
# Arquivo Leibniz
numTermosLeibnizSerial = []
valorPiLeibnizSerial = []
tempoExecLeibnizSerial = []
arq = open('serial/Leibniz.txt', 'r+b')

for linha in arq:
	linha = linha.strip()
	termo,pi,tempo = linha.split(' ')
	numTermosLeibnizSerial.append(termo)
	valorPiLeibnizSerial.append(pi)
	tempoExecLeibnizSerial.append(tempo)

arq.close()
# ----------------------------------------------  --- ---

# ----------------------------------------------  --- ---
# Arquivo Viete
numTermosVieteSerial = []
valorPiVieteSerial = []
tempoExecVieteSerial = []
arq = open('serial/Viete.txt', 'r+b')

for linha in arq:
	linha = linha.strip()
	termo,pi,tempo = linha.split(' ')
	numTermosVieteSerial.append(termo)
	valorPiVieteSerial.append(pi)
	tempoExecVieteSerial.append(tempo)

arq.close()
# ----------------------------------------------  --- ---

# ----------------------------------------------  --- ---
# Arquivo Nilakantha
numTermosNilakanthaSerial = []
valorPiNilakanthaSerial = []
tempoExecNilakanthaSerial = []
arq = open('serial/Nilakantha.txt', 'r+b')

for linha in arq:
	linha = linha.strip()
	termo,pi,tempo = linha.split(' ')
	numTermosNilakanthaSerial.append(termo)
	valorPiNilakanthaSerial.append(pi)
	tempoExecNilakanthaSerial.append(tempo)

arq.close()
# ----------------------------------------------  --- ---

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////













# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



#											Modo Processos



# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ----------------------------------------------  --- ---
#					Leitura de arquivos 
# ----------------------------------------------  --- ---
# Arquivo Lambert
numTermosLambertProcesso = []
valorPiLambertProcesso = []
tempoExecLambertProcesso = []

arq = open('processos/Lambert.txt', 'r+b')

for linha in arq:
	linha = linha.strip()
	termo,pi,tempo = linha.split(' ')
	numTermosLambertProcesso.append(termo)
	valorPiLambertProcesso.append(pi)
	tempoExecLambertProcesso.append(tempo)

arq.close()
# ----------------------------------------------  --- ---

# ----------------------------------------------  --- ---
# Arquivo Leibniz
numTermosLeibnizProcesso = []
valorPiLeibnizProcesso = []
tempoExecLeibnizProcesso = []
arq = open('processos/Leibniz.txt', 'r+b')

for linha in arq:
	linha = linha.strip()
	termo,pi,tempo = linha.split(' ')
	numTermosLeibnizProcesso.append(termo)
	valorPiLeibnizProcesso.append(pi)
	tempoExecLeibnizProcesso.append(tempo)

arq.close()
# ----------------------------------------------  --- ---

# ----------------------------------------------  --- ---
# Arquivo Viete
numTermosVieteProcesso = []
valorPiVieteProcesso = []
tempoExecVieteProcesso = []
arq = open('processos/Viete.txt', 'r+b')

for linha in arq:
	linha = linha.strip()
	termo,pi,tempo = linha.split(' ')
	numTermosVieteProcesso.append(termo)
	valorPiVieteProcesso.append(pi)
	tempoExecVieteProcesso.append(tempo)

arq.close()
# ----------------------------------------------  --- ---

# ----------------------------------------------  --- ---
# Arquivo Nilakantha
numTermosNilakanthaProcesso = []
valorPiNilakanthaProcesso = []
tempoExecNilakanthaProcesso = []
arq = open('processos/Nilakantha.txt', 'r+b')

for linha in arq:
	linha = linha.strip()
	termo,pi,tempo = linha.split(' ')
	numTermosNilakanthaProcesso.append(termo)
	valorPiNilakanthaProcesso.append(pi)
	tempoExecNilakanthaProcesso.append(tempo)

arq.close()
# ----------------------------------------------  --- ---

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////






# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



#											Modo Threads



# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ----------------------------------------------  --- ---
#					Leitura de arquivos 
# ----------------------------------------------  --- ---
# Arquivo Lambert
numTermosLambertThread = []
valorPiLambertThread = []
tempoExecLambertThread = []
arq = open('threads/Lambert.txt', 'r+b')

for linha in arq:
	linha = linha.strip()
	termo,pi,tempo = linha.split(' ')
	numTermosLambertThread.append(termo)
	valorPiLambertThread.append(pi)
	tempoExecLambertThread.append(tempo)

arq.close()
# ----------------------------------------------  --- ---

# ----------------------------------------------  --- ---
# Arquivo Leibniz
numTermosLeibnizThread = []
valorPiLeibnizThread = []
tempoExecLeibnizThread = []
arq = open('threads/Leibniz.txt', 'r+b')

for linha in arq:
	linha = linha.strip()
	termo,pi,tempo = linha.split(' ')
	numTermosLeibnizThread.append(termo)
	valorPiLeibnizThread.append(pi)
	tempoExecLeibnizThread.append(tempo)

arq.close()
# ----------------------------------------------  --- ---

# ----------------------------------------------  --- ---
# Arquivo Viete
numTermosVieteThread = []
valorPiVieteThread = []
tempoExecVieteThread = []
arq = open('threads/Viete.txt', 'r+b')

for linha in arq:
	linha = linha.strip()
	termo,pi,tempo = linha.split(' ')
	numTermosVieteThread.append(termo)
	valorPiVieteThread.append(pi)
	tempoExecVieteThread.append(tempo)

arq.close()
# ----------------------------------------------  --- ---

# ----------------------------------------------  --- ---
# Arquivo Nilakantha
numTermosNilakanthaThread = []
valorPiNilakanthaThread = []
tempoExecNilakanthaThread = []
arq = open('threads/Nilakantha.txt', 'r+b')

for linha in arq:
	linha = linha.strip()
	termo,pi,tempo = linha.split(' ')
	numTermosNilakanthaThread.append(termo)
	valorPiNilakanthaThread.append(pi)
	tempoExecNilakanthaThread.append(tempo)

arq.close()
# ----------------------------------------------  --- ---

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////















# ----------------------------------------------  --- ---

# ----------------------------------------------  --- ---


# ----------------------------------------------  --- ---
#Graficos Individuais  Lambert

plt.figure("Grafico Lambert - Valor de Pi - Todos Modos")
plt.plot(numTermosLambertSerial,valorPiLambertSerial, label = "Lambert - Serial", c='r')
plt.plot(numTermosLambertProcesso,valorPiLambertProcesso, label = "Lambert - Processos", c='g')
plt.plot(numTermosLambertThread,valorPiLambertThread, label = "Lambert - Threads", c='b')
plt.legend()
plt.legend(loc=0)
plt.title("Grafico de Compraracao em Relacao ao Valor de Pi")
plt.xlabel("Numero de Termos")
plt.ylabel("Valor de Pi")
plt.xscale('log')
plt.ylim(2,3.5)
plt.grid(True)

plt.show()

plt.figure("Grafico Lambert - Tempo de Execucao - Todos Modos")
plt.plot(numTermosLambertSerial,tempoExecLambertSerial, label = "Lambert - Serial", c='r')
plt.plot(numTermosLambertProcesso,tempoExecLambertProcesso, label = "Lambert - Processos", c='g')
plt.plot(numTermosLambertThread,tempoExecLambertThread, label = "Lambert - Threads", c='b')
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

plt.figure("Grafico Leibniz - Valor de Pi - Todos Modos")
plt.plot(numTermosLeibnizSerial,valorPiLeibnizSerial, label = "Leibniz - Serial", c='r')
plt.plot(numTermosLeibnizProcesso,valorPiLeibnizProcesso, label = "Leibniz - Processos", c='g')
plt.plot(numTermosLeibnizThread,valorPiLeibnizThread, label = "Leibniz - Threads", c='b')
plt.legend()
plt.legend(loc=0)
plt.title("Grafico de Compraracao em Relacao ao Valor de Pi")
plt.xlabel("Numero de Termos")
plt.ylabel("Valor de Pi")
plt.xscale('log')
plt.ylim(2,3.5)
plt.grid(True)

plt.show()

plt.figure("Grafico Leibniz - Tempo de Execucao - Todos Modos")
plt.plot(numTermosLeibnizSerial,tempoExecLeibnizSerial, label = "Leibniz - Serial", c='r')
plt.plot(numTermosLeibnizProcesso,tempoExecLeibnizProcesso, label = "Leibniz - Processos", c='g')
plt.plot(numTermosLeibnizThread,tempoExecLeibnizThread, label = "Leibniz - Threads", c='b')
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

plt.figure("Grafico Viete - Valor de Pi - Todos Modos")
plt.plot(numTermosVieteSerial,valorPiVieteSerial, label = "Viete - Serial", c='r')
plt.plot(numTermosVieteProcesso,valorPiVieteProcesso, label = "Viete - Processos", c='g')
plt.plot(numTermosVieteThread,valorPiVieteThread, label = "Viete - Threads", c='b')
plt.legend()
plt.legend(loc=0)
plt.title("Grafico de Compraracao em Relacao ao Valor de Pi")
plt.xlabel("Numero de Termos")
plt.ylabel("Valor de Pi")
plt.xscale('log')
plt.ylim(2,3.5)
plt.grid(True)

plt.show()

plt.figure("Grafico Viete - Tempo de Execucao - Todos Modos")
plt.plot(numTermosVieteSerial,tempoExecVieteSerial, label = "Viete - Serial", c='r')
plt.plot(numTermosVieteProcesso,tempoExecVieteProcesso, label = "Viete - Processos", c='g')
plt.plot(numTermosVieteThread,tempoExecVieteThread, label = "Viete - Threads", c='b')

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

plt.figure("Grafico Nilakantha - Valor de Pi - Todos Modos")
plt.plot(numTermosNilakanthaSerial,valorPiNilakanthaSerial, label = "Nilakantha - Serial", c='r')
plt.plot(numTermosNilakanthaProcesso,valorPiNilakanthaProcesso, label = "Nilakantha - Processos", c='g')
plt.plot(numTermosNilakanthaThread,valorPiNilakanthaThread, label = "Nilakantha - Threads", c='b')
plt.legend()
plt.legend(loc=0)
plt.title("Grafico de Compraracao em Relacao ao Valor de Pi")
plt.xlabel("Numero de Termos")
plt.ylabel("Valor de Pi")
plt.xscale('log')
plt.ylim(2,3.5)
plt.grid(True)

plt.show()

plt.figure("Grafico Nilakantha - Tempo de Execucao - Todos Modos")
plt.plot(numTermosNilakanthaSerial,tempoExecNilakanthaSerial, label = "Nilakantha - Serial", c='r')
plt.plot(numTermosNilakanthaProcesso,tempoExecNilakanthaProcesso, label = "Nilakantha - Processos", c='g')
plt.plot(numTermosNilakanthaThread,tempoExecNilakanthaThread, label = "Nilakantha - Threads", c='b')
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


