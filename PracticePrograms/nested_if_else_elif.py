marks = int(input("Enter the marks u have scored \n"))


if marks >= 0 and marks < 35:
    print("Failed")

elif marks >= 35 and marks < 60:
    print("second class")

elif marks >=60 and marks < 70:
    print("First class")

elif marks >= 70 and marks <= 100:
    print("Distinction")