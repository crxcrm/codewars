# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces. 

library(stringr)

get_count <- function(input_str){
  a1 = str_count(input_str,"a")
  e1 = str_count(input_str,"e")
  i1 = str_count(input_str,"i")
  o1 = str_count(input_str,"o")
  u1 = str_count(input_str,"u")
  return(a1+e1+i1+o1+u1)
}
