# I have a cat and a dog.

# I got them at the same time as kitten/puppy. That was humanYears years ago.

# Return their respective ages now as [humanYears,catYears,dogYears]

# NOTES:
# humanYears >= 1
# humanYears are whole numbers only
# Cat Years
# 15 cat years for first year
# +9 cat years for second year
# +4 cat years for each year after that
# Dog Years
# 15 dog years for first year
# +9 dog years for second year
# +5 dog years for each year after that

human_years_cat_years_dog_years <- function(human_years){
  cats = 0
  dogs = 0
  
  if (human_years == 1){
    cats = cats + 15
    dogs = dogs + 15
  }else{
    if (human_years == 2){
      cats = cats + 15 + 9
      dogs = dogs + 15 + 9
    }else{
      cats = cats + 15 + 9 + 4*(human_years-2)
      dogs = dogs + 15 + 9 + 5*(human_years-2)
      }
    }
  
  result = c(human_years, cats, dogs)
  print(result)
  return(result)
}
