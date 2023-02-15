/*Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.

Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Requirements
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).
NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow.
*/

#include <stdbool.h>
#include <math.h>

bool is_prime(int num)
{
  if(num<2){ return false;}
  else{
    if(num == 2){return true;}
      else{
        int i;
        float divisor = sqrt(num) + 1;
        for(i = 2; i <= divisor ; i++){
          if((num%i)==0){return false;}
        }
        return true;
      }
  }
}
