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
    
    #include <stdio.h>
    #include "funcoestempo.h"
    #include "series.h"
	#include "savedata.h"
	
	void carregarSerie(TSerie *serie, int n, float tempo, long double pi)
	{
		serie->valorPi = pi;
	    serie->tempoFeito = tempo;
	    serie->n = n;
	}
	
	void carregarNOArquivo(int modo, TSerie serie, char *nomeArquivo, funcao func )
	{
        long double tempo;
        long double x;
        FILE *file = fopen(nomeArquivo,"w");
		if (file == NULL) printf("Erro ao abrir Arquivo");
		for(int i = 1; i <= 100000; i++)
     	{
		    tempo = calcular_tempo_de_execucao(modo, func,  1, i, &x);
		    carregarSerie(&serie, i, tempo, x);
		    gravarDados(file, serie);
		}
		fclose(file);
	}

    int main()
    {
    	
        long double pi;
        long double tempo;
        long double x; 
        TSerie lambert, nilakantha, leibniz, viete;
        
        //tempo = calcular_tempo_de_execucao(MODO_SERIAL, Lambert,  1, 10, &x);
        //printf("Pi calculado por processo = %.66Lf \t Tempo = %.6Lf \n", x, tempo);
        
        
        carregarNOArquivo(MODO_SERIAL, lambert, "arquivos/serial/Lambert.txt", Lambert);
        carregarNOArquivo(MODO_SERIAL, nilakantha, "arquivos/serial/Nilakantha.txt", Nilakantha);
        //carregarNOArquivo(MODO_SERIAL, leibniz, "arquivos/serial/Leibniz.txt", Leibniz);
        carregarNOArquivo(MODO_SERIAL, viete, "arquivos/serial/Viete.txt", Viete);
        
        carregarNOArquivo(MODO_PROCESSOS, nilakantha, "arquivos/processos/Nilakantha.txt", Nilakantha);
        carregarNOArquivo(MODO_PROCESSOS, lambert, "arquivos/processos/Lambert.txt", Lambert);
        //carregarNOArquivo(MODO_PROCESSOS, leibniz, "arquivos/processos/Nilakantha.txt", Leibniz);
        //carregarNOArquivo(MODO_PROCESSOS, viete, "arquivos/processos/Viete.txt", Viete);
    }
