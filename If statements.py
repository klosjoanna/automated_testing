day_of_week = input("What day of the week is it today? ").lower()

#.lower() przemienia wszystko na male litery bez wzgledu na to jak wpiszemy w odpowiedzi

print(day_of_week == "Monday") #mówię pythonowi że jest poniedziałek

# w zaleznosci od odpowiedzi python odpowiada true or false

# druga opcja:

if day_of_week == "Monday":
    print("Have a great start to your week!")
elif day_of_week == "Tuesday":
    print("It's Tuesday.")
else: # != means 'is not'
    print("Full speed ahead!")

print("This always runs.")

