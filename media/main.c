#include <stdio.h>
#include <time.h>
#include <stdlib.h>
int main() {
    int vet1[6],vet2[3],vet3[20],vet4[9],i,j,k,n;

    srand(time(NULL));

    printf("inserisci 6 valori del primo vettore :\n");

    for(i=0;i<6;i++){
        scanf("%d",&vet1[i]);
    }
    size_t mem = sizeof(vet1);
    printf("Il vettore 1 occupa indirizzo di memoria %d\n",mem);




    printf("vettore 2 generato con numeri random = ");
    for(i=0;i<3;i++){
        n = rand() % 10;
        vet2[i]=n;
        printf("%d ",vet2[i]);
    }
    mem = sizeof(vet2);
    printf("\nIl vettore 2 occupa indirizzo di memoria %d\n",mem);


    printf("vettore intersezione con ripetizioni = ");

    k=0;

    for(i=0;i<6;i++)
    {
        for(j=0;j<3;j++){
            if(vet1[i]==vet2[j])
            {
                vet3[k]=vet1[i];
                printf("%d ",vet3[k]);
                k++;
            }
        }
    }

    if (k==0){
        printf("non esiste");
    }

    mem = sizeof(vet3);
    printf("\nIl vettore occupa indirizzo di memoria %d",mem);


    printf("\nvettore intersezione senza ripetizioni = ");

    if (k==0){
        printf("non esiste");
    }




    int number = k;
    int a,b;

    for(i=0;i<6;i++){
        for(a = i+1; a < number; a++){
            if(vet3[i] == vet3[a]){
                for(b = a; b <number; b++){
                    vet3[b] = vet3[b+1];
                }
                a--;
                number--;
            }
        }
    }
    for(i=0;i<number;i++){
        printf("%d ",vet3[i]);
    }

    mem = sizeof(vet3);
    printf("\nIl vettore occupa indirizzo di memoria %d",mem);

    printf("\nvettore unione = ");

    for(i=0;i<6;i++)
    {
        vet4[i]=vet1[i];
        printf("%d ",vet4[i]);
    }

    i=0;

    for(j=6;j<9;j++){
        vet4[j]=vet2[i];
        printf("%d ",vet4[j]);
        i++;
    }

    mem = sizeof(vet4);
    printf("\nIl vettore occupa indirizzo di memoria %d",mem);

    return 0;
}