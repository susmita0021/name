#include<stdio.h>

int main(){
    int num;
    printf("Enter the number of rows");
    scanf("%d",&num);
    for(int x=1;x<=num;x++)
        {
        for(int space=0;space<x;space++)
        {
            print(" ");
        }
        for(int y=num-x;y>0;y++)
        {

            printf(" ");
        }


          printf("/n");
        }


    return 0;
}





