/*xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/
/x																							                    x/
/x		        Autor: Grupo Toca Aqui                                                                          x/
/x              Integrantes:                                                                                    x/
/x                          João Paulo Zinga    ------------>      1000013678                                   x/
/x                          Fábio Bazióta       ------------>      1000013678                                   x/
/x                          Áureo Carmelino     ------------>      1000013678                                   x/
/x                          Eidy Vemba          ------------>      1000013678                                   x/
/x                          Sebastião Paulo     ------------>      1000015611                                   x/
/x                          Inocência Daniel    ------------>      1000013678                                   x/
/x		        Data: 21/06/2018																	            x/
/x		        Descrição: Neste cabecalho encontra-se a imprmentacao das funcoes usadas para                   x/
/x                         calcular as series de aproximacoes de PI					                            x/
/x			                                    											                    x/
/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx*/

    #include "funcoestempo.h"
    #include "modoprocessos.h"
    #include "modoserial.h"
    #include <stdlib.h>
    #include <time.h>
    
    long double calcular_tempo_de_execucao(int modo, funcao func, int arg1, int arg2, long double *arg3)
    {
    	clock_t t_inicial, t_final;
    	
    	if (modo == MODO_SERIAL)
    	{
		    if (func != NULL)
		    {
		        t_inicial = clock();
		        serialSerie(func, arg1, arg2, arg3);
		        t_final = clock();
		    }
		    return (long double)(t_final - t_inicial) / (long double)(CLOCKS_PER_SEC);
		}
		
		if (modo == MODO_PROCESSOS)
		{
			t_inicial = clock();
			processSerie(func, arg2, arg3);
			t_final = clock();
			return (long double)(t_final - t_inicial) / (long double)(CLOCKS_PER_SEC);
		}
		
    }

    
    
    
