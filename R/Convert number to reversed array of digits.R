# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

digitize <- function(n){
  digit_count = 1
  div = 1
  while ( div <= n / 10 ) {
    digit_count = digit_count + 1;
    div = div * 10;
  }
  digits = digit_count
  vec <- vector()
while ( digit_count > 0 ) {
    vec = append(vec, as.integer(n / div));
    n = n %% div;
    div = div / 10;
    digit_count = digit_count -1;
  }
  vec2 = rev(vec)

return(vec2)
}
