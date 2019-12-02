/*xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/
/x																							                    x/
/x		        Autor: Grupo Toca Aqui                                                                          x/
/x              Integrantes:                                                                                    x/
/x                          João Paulo Zinga    ------------>      1000013678                                   x/
/x                          Fábio Bazióta       ------------>      1000013678                                   x/
/x                          Áureo Carmelino     ------------>      1000013678                                   x/
/x                          Eidy Vemba          ------------>      1000013678                                   x/
/x                          Sebastião Paulo     ------------>      1000013678                                   x/
/x                          Inocência Daniel    ------------>      1000013678                                   x/
/x		        Data: 21/06/2018																	            x/
/x		        Descrição: Neste cabecalho encontra-se a imprmentacao das funcoes usadas para                   x/
/x                         calcular as series de aproximacoes de PI					                            x/
/x			                                    											                    x/
/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx*/

    #include <stdio.h>
    #include <stdlib.h>
    #include <time.h>
    #include "funcoesmatematicas.h"
    #include "series.h"
    
    /* Serie para o calculo de PI de Nilakantha*/
    void Nilakantha(int i, int n, long double *x)
    {
        *x = 3;
		for (int k = 2; n > i; n--)
		    *x += (long double)(potencia(-1,-n) * (4.0/(long double)mult(&k)));
    }
    
    /* Serie para o calculo de PI de Lambert*/
    void Lambert(int k, int n, long double *x)
    {
        long double aux = (2 * n - 1) + potencia(n, 2) / (2 * n + 1);
		for ( ; n > 0; n--) 
		    aux = (2 * n - 1) + potencia(n, 2)/ aux;
		*x = 4/aux;
    }

    void Leibniz(int i, int n, long double *x)
    {
        *x = 0;
		for ( ; n >= i - 1; n--)
			*x += (long double)(potencia(-1, n) * 4) / (long double)((2 * n) + 1);
    }
    
    /* Serie para o calculo de PI de Viete*/
    void Viete(int i, int n, long double *x)
    {
	    long double numerador = 0, an = 1.0;
		for ( ; i <= n; i++)
		{
		    numerador = raizQuadrada(2.0 + numerador);
		    an *= numerador/2.0;
		}
		*x = (2.0/an);
    }
   
    

