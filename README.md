# Computação do Valor PI


# Projeto de Sistemas Operativos
	
	Descrição: O problema destina-se a uma pesquisa acadêmica realizada fim de mostrar como é feito o paralelismo 
	e concorrencia entre processos, dentro de um sistema operativo. Tendo como caso de estudo “ computação do valor pi “, 
	utilizando as fórmulas de recorrência das séries matemáticas Lambert, Nilakantha, Viete e Leibnniz, 
	computando de forma serial, processos e implementação de thread, utilizando recursos de programação em tempo real, 
	na plataforma GNU Linux (Ubuntu).
	Data: 21/06/2018

# Objectivos
	Gerais: Comparar a eficiência em termos de tempo de execução e aproximação do valor pi das séries matematicas nos 3 modos;
	Especificos: Comparar a eficiência em termos de tempo de execução das séries, evidenciando assim os demais artefactos p
		ouco paorveitados no modelo serial, e comparar relativamente ao uso de Processos e Threads.  

//Desenvolvimento das séries em C
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

# Autores/Desenvolvedores:
	- João Paulo 
	- Fábio Bazióta   
	- Áureo Roberto 	    
	- Sebastião Paulo 
	- Inocência Daniel
	- Eidy Vemba 

# Orientador: 
	- Prof. Solander Agostinho
