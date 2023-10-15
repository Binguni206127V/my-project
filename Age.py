age <- 20
categorize_age <- function(age) {
  if (age < 18) {
    return("Child")
  } elseif (age < 65) {
    return("Adult")
  } else {
    return("Senior")
  }
}
age_group <- categorize_age(age)
print(paste("Age Group:", age_group))