# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

duplicate_encode <- function(word){
  w <- word %>% tolower %>% strsplit('') %>% unlist
  dup <- w[duplicated(w)] %>% unique
  d <- w %in% dup
  w[d] <- ")"
  w[!d] <- "("
  w %>% paste0(collapse = '')
}
