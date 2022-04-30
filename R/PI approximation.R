# There are several ways to determine the precision of the calculus but to keep things easy we will calculate PI within epsilon of your language Math::PI constant.
# In other words, given as input a precision of epsilon we will stop the iterative process when the absolute value of the difference between our calculation using the Leibniz series and the Math::PI constant of your language is less than epsilon.

# Your function returns an array or a string or a tuple depending on the language (See sample tests) with

# your number of iterations
# your approximation of PI with 10 decimals

iterPi <- function(epsilon) {
  r = 0.0
  for (n in 0:100000000){
    r = r + (-1.0)**n/(2.0*n+1.0)
    if ((abs(pi - 4*r)) <= epsilon){
      res = c(n+1, 4*r)
      return(res)
      break
    }
    }
}
