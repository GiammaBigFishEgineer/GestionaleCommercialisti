//
//  main.c
//  settimana5 es1
//
//  Created by Gianmaria Di Fronzo on 07/11/22.
//
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <math.h>


float generazione_float(float min, float max)
{
    return (min + 1) + (((float) rand()) / (float) RAND_MAX) * (max - (min + 1));
}

int generazione_int(int min, int max)
{
    return rand() % (max - min) + min + 1;
}



int main(void) {
    
    time_t seed = 0;
    srand(time(&seed));
    
    int ripetute = 0;
    
    while(ripetute<3){
    
    //intervallo w [0.15, 0.80] --- rand() % (Max + 1 - Min) + Min;
    float w =  generazione_float(0.15,0.80);
    
    // o e y (le fasi) scelti, ancora casualmente, nell’intervallo [0.0, 1.0]
    float o = generazione_float(0.0,1.0);
    float y = generazione_float(0.0,1.0);
    // μ nell’intervallo [0.0, 20.0]   β tra 128 e 256
    float u = generazione_float(0.0,20.0);
    int b = generazione_int(128,256);
    
    
    int i,j;
    double Fji;
    float m[16][16];
        
    
    for(i=0;i<16;i++){
        for(j=0;j<16;j++){
            
            //Fji = sin(ω∙i + φ) + sin(ω∙j + ψ).
            Fji = sin(w * i + o)+ sin(w * j + y);
            
            //m(i, j) = floor ((β + μ)∙(1.0 + Fji / 2.0)) mod β
            int t = floor((b + u)*(1.0 + Fji / 2.0));
            m[i][j] = t%b;
        }
        
    }
        for(i=0;i<16;i++){
            for(j=0;j<16;j++){
                printf("%.0f ",m[i][j]);
            }
            printf("\n");
        }
    // m[x][y] definito in intervallo [0,b-1]
    
        ripetute++;
        printf("\n \n");
    }
    
    return 0;
}



