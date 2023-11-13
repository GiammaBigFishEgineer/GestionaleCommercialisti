
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#define MAX 10

int main(){
    int i,j;
    int count = 0;
    int n,a;
    time_t seed = 0;
    srand(time(&seed));

    // riga      x   y
    int matrice[10][10];

    // Genero un array bidimensionale 10x10 con numeri casuali.
    for(i=0;i<10;i++){
        for(j=0;j<10;j++) {
            n= rand() % 5;
            matrice[i][j] = n;
            printf("%d \t",matrice[i][j]);
        }
        printf("\n");
        }

    // Sapendo che se ho 3 uguali numeri (a) in sequenza, la loro somma sarà uguale ad a*3.
    // Se la condizione é vera allora conto quante volte un numero é in ripetuto in fila per 3 volte.

    for(i=0;i<10;i++){
        for(j=0;j<10;j++){
            a = j;
            if(matrice[i][j] + matrice[i+1][j+1] + matrice[i+2][j+2]== 3*a && i<MAX && j<MAX)
                count++; // diagonale
            if(matrice[i][j] + matrice[i][j+1] + matrice[i][j+2] == 3*a && i<MAX && j<MAX)
                count++; // orrizontale
            if(matrice[i][j] + matrice[i+1][j] + matrice[i+2][j] == 3*a && i<MAX && j<MAX)
                count++; // verticale
        }
    }

    printf("\n \n Conto: %d",count);



    return 0;
}