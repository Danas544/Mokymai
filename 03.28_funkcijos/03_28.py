# print((lambda x: {x, x**2 , x**3}) (2))


# starts_with = lambda x: True if x.startswith('P') else False
# print(starts_with('Python'))


# r = lambda a : a + 15
# print(r(10))

# r = lambda x, y : x * y

# print(r(12, 4))


# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# print("Original list:")
# print(nums1)
# print(nums2)
# result = map(lambda x, y: x + y, nums1, nums2)
# print("\nResult: after adding two list")
# print(list(result))

import datetime
now = datetime.datetime.now()
print(now)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print(year(now))
print(month(now))
print(day(now))
print(t(now))