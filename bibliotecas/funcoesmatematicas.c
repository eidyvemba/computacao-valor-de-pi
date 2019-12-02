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
x/                         calcular as series de aproximacoes de PI					                            x/
/x			                                    											                    x/
/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx*/

    #include <math.h>
    #include "funcoesmatematicas.h"
    
    long double raizQuadrada(double x)
	{   return (double)sqrt(x); }
    
    int potencia(int base, int expoente)
	{
		int x = 1;
		for ( ; expoente > 0 ; x *= base, expoente--);
		return x;
	}
    
    int mult(int *n)
    {
        int x = 1 , limite = (*n + 2), k;
        for ( k = *n; k <= limite ; k++ )
            x *= k;
        *n = k-1;
        return x;
    }
