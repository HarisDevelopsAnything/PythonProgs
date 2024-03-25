import datesub as dsub
date_str1 = input("Enter the from date in DD-MM-YYYY: ")
date_str2 = input("Enter the to date in DD-MM-YYYY: ")
sub= dsub.ds(date_str1, date_str2)
print("Difference between the dates:", sub.days, "days")