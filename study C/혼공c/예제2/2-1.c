#include<stdio.h>
int main()
{
    int SY=24;
    int SH=25;
    int a = (float)SY/SH*100;
    float result=(float)a/100;
    printf("%.2f", result+1);

    return 0;
}
