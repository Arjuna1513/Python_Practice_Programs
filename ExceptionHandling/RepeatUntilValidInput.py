while True:
    try:
        value = int(input("Enter the integer input-->>>"))
        # The above code throws exception if non-integer value is entered so put that in try and handle.
    except:
        print("Please enter the integer value...")
    else:
        print("Yes!. It's a number")
        break
    finally:
        print("End of try except blocks")
