/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>


bool function(int8_t input1,uint8_t input2){
     if(input1<(int16_t)input2){
         return true;
         }
     
     return false;
 }


int main()
{
 int32_t x=0;
 uint32_t y=0;
 scanf("%d%du", &x,&y);
 bool result=function(x,y);
 if(result){
     printf("true");
 } else printf("false");
 
 return 0;
}


