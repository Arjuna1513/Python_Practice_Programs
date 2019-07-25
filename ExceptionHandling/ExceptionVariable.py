
try:
    var = 10 / 0
except ZeroDivisionError as zde:
    print(zde)


# except ZeroDivisionError as zde:
# here ZeroDivisionError as zde is similar to (Exception e)s.o.p(e) in java here zde is a variable
# given to the exception type.