
from operator import itemgetter 
c = []

print("Hello! Welcome to your personal to do list, please enter the day of the week: (1:M, 2:T, 3:W, 4:Th, 5:F, 6:Sat, 7:Sun) ")
day = float(input())
print("How many classes are you taking? ")
num_classes = int(input())

script = ["Please enter a class: ", "Please enter day of the week HW is due: (1:M, 2:T, 3:W, 4:Th, 5:F, 6:Sat, 7:Sun) ", "Please enter time of due date: (24hr time)"]

for i in range(num_classes):
	c.append([])
	for j in range(3):
		print(script[j])
		c[i].append(float(input()))

print("TO DO: ")

sorted_c = sorted(c, key = itemgetter(1)) # sorts by day due


days = ["today", "tommrow", "later this week"]
today = []
tommrow = []
later = []

for k in range(num_classes):
	if day == c[k][1]:
		today.append(c[k])
	elif day + 1 == c[k][1]:
		tommrow.append(c[k])
	else:
		later.append(c[k])

#sort later data assignments 
later.sort(key=itemgetter(1))

ds = [today, tommrow, later]
for j in range(len(days)):
	print(days[j], " : ", ds[j])


