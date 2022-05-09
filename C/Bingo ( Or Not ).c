# For this game of BINGO, you will receive a single array of 10 numbers from 1 to 26 as an input. Duplicate numbers within the array are possible.

# Each number corresponds to their alphabetical order letter (e.g. 1 = A. 2 = B, etc). Write a function where you will win the game if your numbers can spell "BINGO". They do not need to be in the right order in the input array). Otherwise you will lose. Your outputs should be "WIN" or "LOSE" respectively. 
  
#include <stdio.h>
#include <string.h>

enum outcome { WIN = 1, LOSE = 2};

enum outcome bingo (const int numbers[10])
{
  int i;
  int cadena[5] = {0,0,0,0,0};
    for(i=0;i<=10;i++){
      if(numbers[i]==2){
        cadena[0] = 1;
      }
      if(numbers[i]==7){
        cadena[1] = 1;
      }
      if(numbers[i]==9){
        cadena[2] = 1;
      }
      if(numbers[i]==14){
        cadena[3] = 1;
      }
      if(numbers[i]==15){
        cadena[4] = 1;
      }
    }
  if(cadena[0]+cadena[1]+cadena[2]+cadena[3]+cadena[4]==5){
    return WIN;
  }else{
    return LOSE;
  }
}
