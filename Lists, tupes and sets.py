l = ["Bob", "Rolf", "Anne"]
# list > can add and remove

t = ("Bob", "Rolf", "Anne")
# tuple > can't modify a tuple

s = {"Bob", "Rolf", "Anne"}
# set >
# 1. can't have duplicate elements for example: two of "Annes"
# 2. don't necessarily keep the order

print(l[2])
print(t[0])
# Bob has index of 0, Rolf of 1, Anne of 2

l[0] = "Smith"
print(l)

l.append("Nowak")  #dodaje na koniec listy nowy element
print(l)

l.remove("Rolf")  #usuwa z listy
print(l)

s.add("Kowalska") #dodaje do seta
print(s)

