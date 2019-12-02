/*xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/
/x																							                    x/
/x		        Autor: Grupo Toca Aqui                                                                          x/
/x              Integrantes:                                                                                    x/
/x                          João Paulo Zinga    ------------>      1000013678                                   x/
/x                          Fábio Bazióta       ------------>      1000013678                                   x/
/x                          Áureo Carmelino     ------------>      1000013678                                   x/
/x                          Eidy Vemba          ------------>      1000013678                                   x/
/x                          Sebastião Paulo     ------------>      1000013678                                   x/
/x                          Inocência Daniel    ------------>      1000015273                                   x/
/x		        Data: 21/06/2018																	            x/
/x		        Descrição: Neste cabecalho encontra-se a imprmentacao das funcoes usadas para                   x/
x/                         calcular as series de aproximacoes de PI					                            x/
/x			                                    											                    x/
/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx*/


	#include<stdio.h>
	#include<stdlib.h>
	#include<string.h>
	#include <pthread.h>
	#include <unistd.h>
	#include <sys/types.h>
	#include <sys/wait.h>
	#include <errno.h>
	#include <math.h>
	#include <locale.h>
	#include <signal.h>
	#include <time.h>
	
	#include "modoprocessos.h"
	#include "series.h"
	#include "savedata.h"
	
	void processSerie(funcao serie, int numTermos, long double *pi)
	{
		pid_t pid[MAX_NUM_TERMS];
		int fileDescriptor[MAX_FILE_DESCRIPTOR];

		if(pipe(fileDescriptor)<0)
		{
			perror("ERRO no pipe");
			exit(EXIT_FAILURE);
		}

		pid[0] = vfork();
		
		if(pid[0] < 0)
		{
			perror("ERRO: VFORK");
			exit(EXIT_FAILURE);
		}
		
		for(int i = 1, k = 1 ; i <= numTermos/2; i++, k += 2)
		{
			if(pid[i-1] == 0)
			{
				serie(k, k+1, pi);
				write(fileDescriptor[1], pi, sizeof(pi));
				exit(EXIT_SUCCESS);
			}
			
			pid[i] = vfork();
		
			if(pid[i] < 0)
			{
				perror("ERRO: vfork");
				exit(EXIT_FAILURE);
			}
		
			if(pid[i] == 0)
			{
				read(fileDescriptor[0], pi, sizeof(&pi));
			}
		}
	}

