


grocery_list = ["toilet paper", "carrots", "apples", "cookies"]


# Your next step should present your grocery list with an item on each line, with an asterisk (*) in front of it so that it appears like this:
for item in grocery_list:
    print("*",item)

# You realize you've forgotten some rice, so add it to your list and output it again. Given that you've already output your list twice, it might be good to consider writing a method to do this. Putting frequently used chunks of code in a method lets you reuse them throughout your program without having to type them out over and over.
def add_item(grocery_list):
    grocery_list.append("rice")
    print(grocery_list)

list = add_item(grocery_list)

# You lost count of how many things you need to pick up. Better output the total number of items on your list.
print("You current have {} items on your grocery list".format(len(grocery_list)))


# Check to see if your list includes "bananas". If it does, output "You need to pick up bananas". Otherwise, output "You don't need to pick up bananas today".

if (item == "bananas"):
    print("You already have bananas")
elif (item != "bananas"):
    print("You need to pick up bananas!")

# Display the second item in the list. (Don't forget that lists indices start at zero!)

print("This is the second item in the list: {}".format(grocery_list[1]))


# It turns out that everything in this grocery store you're visiting is stored alphabetically, so to better plan out what you need to buy you should sort your grocery list and output it with asterisks again.

for i in sorted(grocery_list):
    print("*", i)
