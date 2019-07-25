def intToMonth(argument):

    dict1 = {
                    1: "January",
                    2: "February",
                    3: "March",
                    4: "April",
                    5: "May",
                    6: "June",
                    7: "July",
                    8: "August",
                    9: "September",
                    10: "October",
                    11: "November",
                    12: "December"
               }
    return dict1.get(argument, "Invalid month")

# Take the input integer from user
option = int(input("Enter Integer input here>>>>"))
if option < 0 or option > 12:
    print("Please enter the value greater than 0 and lesser than or equal to 12")

else:
    month = intToMonth(option)
    print(month)