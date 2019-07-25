# try:
#     value = 99 + 'str'
#     # Above one throws type error
#     value1 = 99 / 0
#
#     with open('text.txt', 'r') as f:
#         pass
# except (TypeError, ZeroDivisionError, FileNotFoundError):
#     print("Exception raised")


try:
    value = 99 + 100
    # Above one throws type error
    value1 = 99 / 0

    with open('text.txt', 'r') as f:
        pass
except (TypeError):
    print("Type Mismatch exceptin raised")
except (ZeroDivisionError):
    print("divide by zero exception raised")
except (FileNotFoundError):
    print("File not found exception raised")

finally:
    print("I have been called irrespective of exception...")
#  just like in java u can have many catch blocks or u can mention all the exceptions at once
#  as a tuple. Ex : except (TypeError, ZeroDivisionError, FileNotFoundError):
#  If an exception occurs at some line in try block rest of the code block is skipped and will go to the
#  except block and if the there are five except blocks and if the first one catches then remaining
#  except clauses will be ignored.