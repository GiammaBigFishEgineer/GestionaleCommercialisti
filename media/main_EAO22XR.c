#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#define NUM_ESAMI 6
 

struct struct_esami{
    int voto;
};


struct struct_insegnamento {
    char *titolo;
    int codice;
    int annosomministrazione;
    int crediti;
    struct struct_esami pianostudi[NUM_ESAMI];
};

struct struct_alunni{
    char cognome[30];
    char nome[20];
    int matricola;
    int annomatricola;
    struct struct_insegnamento ins[4];
}*a;

 


int main() {
    int l,k,b,x,s,n,i,j,voto,trovato;
    bool done = true;
    int access = 0;
    int count = 0;
    // k,l,j per cicli
    long int mat;
    a=malloc(sizeof(a)*100);

    int media_ponderata = 0;
    int peso_credito;
    int dividendo_media = 0;
    int conta=0;

    x=0;
    i=0;
    n=0;



while(x!=1) {
    printf("1 -aggiungi un nuovo studente\n"
           "2 -visualizza studente\n"
           "3 -modifica piano studi\n"
           "4 -media voti\n"
           "5 -termina programma\n");
    scanf("%d", &s);

    switch (s) {
        case 1:
            
            printf("Inserisci il cognome dell'alunno:");
            scanf("%s", a[i].cognome);
            printf("Inserisci il nome dell'alunno:");
            scanf("%s", a[i].nome);
            
            while(done){
                printf("Inserisci il numero matricola:");
                scanf("%ld", &mat);
                a[i].matricola = mat;
                //printf("n: %d\n",n);
                
                    for(k=n;k>=0;k--){
                        //printf("matricola = %d in posizione = %d\n",a[k].matricola,k);
                        if(a[k].matricola != mat ){
                            printf("%d %ld\n",a[k].matricola, mat);
                            conta++;
                        }
                        if (conta==n){
                        printf("Inserito correttamente \n");
                        
                        done = false;
                        }
                    }
                    
                    printf("n: %d\n",n);
                conta=0;
            }
            done = true;
            
            
            printf("Inserisci l' anno di immatricolazione:");
            scanf("%d", &a[i].annomatricola);
            
            a[i].ins[0].titolo = "analisi";
            a[i].ins[0].codice = 1001;
            a[i].ins[0].annosomministrazione = 2022;
            a[i].ins[0].crediti = 12;

            a[i].ins[1].titolo = "programmazione";
            a[i].ins[1].codice = 2002;
            a[i].ins[1].annosomministrazione = 2022;
            a[i].ins[1].crediti = 12;

            a[i].ins[2].titolo = "inglese";
            a[i].ins[2].codice = 3003;
            a[i].ins[2].annosomministrazione = 2022;
            a[i].ins[2].crediti = 6;

            a[i].ins[3].titolo = "algebra";
            a[i].ins[3].codice = 4004;
            a[i].ins[3].annosomministrazione = 2022;
            a[i].ins[3].crediti = 6;

            for(k=0;k<4;k++){
                for(l=0;l<strlen(a[i].ins[k].pianostudi);l++){
                    printf("%d ",a[i].ins[k].pianostudi[l].voto);
                    a[i].ins[k].pianostudi[l].voto = NULL;
                    printf("%d \n",a[i].ins[k].pianostudi[l].voto);
                }
                printf("\n");
            }
            
            printf("\n\n");
            
            i++;
            n++;
            
            break;

        case 2:
            printf("\nInserisci la matricola dell'alunno da cercare: ");
            scanf("%ld",&mat);

            trovato = 0;

            for (j = 0; j < n; j++) {
                if (a[j].matricola==mat) {
                    printf("\nAlunno trovato in posizione %d\n"
                           "nome : %s\n"
                           "cognome : %s\n"
                           "anno immatricolazione: %d\n\n", j + 1, a[j].nome, a[j].cognome ,a[j].annomatricola);
                    for(k=0;k<4;k++){
                        printf("Materia %s con voti: ",a[j].ins[k].titolo);
                        for(l=0;l<strlen(a[j].ins[k].pianostudi);l++){
                            printf("%d ",a[j].ins[k].pianostudi[l].voto);
                        }
                        printf("\n");
                    }
                    trovato = 1;
                }
            }

            if (trovato==0)
                printf("\nAlunno non trovato.\n\n");
            break;
        case 3:
            printf("\nInserisci il codice matricola dell'alunno da cercare: \n");
            scanf("%ld",&mat);
            printf("\nInserisci il codice materia del piano studio dell'alunno: \n");
            printf("Analisi - 1001\n"
                   "Programmazione - 2002\n"
                   "Inglese - 3003\n"
                   "Algebra - 4004\n");
            scanf("%d",&b);//codice insegnamento

            trovato = 0;
            for(j=0;j<n;j++){
                if (a[j].matricola==mat){
                    for(k=0;k<4;k++){
                        if(a[j].ins[k].codice == b){
                            trovato = 1;
                            printf("Inserisci un voto\n");
                            scanf("%d",&voto);
                           
                            for(l=0;l<strlen(a[j].ins[k].pianostudi)+1;l++){
                                if(a[j].ins[k].pianostudi[l].voto == NULL){
                                    a[j].ins[k].pianostudi[l].voto = voto;
                                    printf("Voto inserito correttamente: %d\n",a[j].ins[k].pianostudi[l].voto);
                                    break;
                                }
                            }
                        }
                        
                    }
                    if(trovato == 0)printf("Nessun risultato trovato");
                }
            }
            
            break;
        
       
        case 4 :
            for(j=0;j<n;j++){
                for(k=0;k<4;k++){
                    if(a[j].ins[k].crediti == 12)
                        peso_credito = 100;
                    if(a[j].ins[k].crediti == 6)
                        peso_credito = 50;
                        
                    for(l=0;l<strlen(a[j].ins[k].pianostudi);l++){
                        if(a[j].ins[k].pianostudi[l].voto >=18) access++;
                        //printf("Access: %d \n",access);
                        if(access >=4){
                            media_ponderata = media_ponderata + a[j].ins[k].pianostudi[l].voto * peso_credito;
                            dividendo_media = dividendo_media + peso_credito;
                        }
                    }
                    
                }
                access = 0;
            }
            
            if(dividendo_media != 0){
                printf("\n La media degli studenti é: %d \n", media_ponderata/dividendo_media);
            }else{
                printf("Nessuna media trovata\n");
            }
           
            break;
            
            
        case 5 :
            x=1;
            break;
    }
}
return 0;
}
