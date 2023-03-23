
# Write a function that returns dates of the 5 upcoming Friday 13ths, with Year, month and date


# def friday13s(from_date=date.today()):
#     d = from_date + timedelta(13 - from_date.day)   # clamp date to the 13th
    
#     def increment_month(d):
#         mm = 1 if d.month == 12 else d.month + 1
#         yy = d.year + 1 if mm == 1 else d.year
#         return date(yy, mm, d.day)

#     if from_date > d:
#         d = increment_month(d)

#     while True:
#         if d.weekday() == 4:
#             yield d
#         d = increment_month(d)



# for d in islice(friday13s(), 10):
#     print(d)

from itertools import islice
 
 
# Slicing the range function
for i in islice(range(20), 5):
    print(i)
     
     
li = [2, 4, 5, 7, 8, 10, 20]
 
# Slicing the list
print(list(islice(li, 1, 6, 2))) 
