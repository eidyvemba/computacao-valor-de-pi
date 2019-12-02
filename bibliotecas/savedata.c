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
	#include "savedata.h"


	void gravarDados(FILE *file, TSerie serie)
	{
		int i;
		fprintf(file, "%d %.66Lf %f\n",serie.n, serie.valorPi, serie.tempoFeito);
	}
