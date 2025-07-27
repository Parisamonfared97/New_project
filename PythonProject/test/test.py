from tools.data_validation import *

#اسم
assert name_checker("pari123")== False

assert name_checker("pari")== True
#---------------------------------------------
#فامیلی
assert family_checker("monfared")== True

assert family_checker("mon%r d")==False
#---------------------------------------------
#موبایل
assert mobile_checker("09125106774")== True

assert mobile_checker("12510677409")== False
