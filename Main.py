import random

divide   = "&divide;"
multiply = "&times;"

def html_start():
    print("<html>\n<body>\n")

def html_stop():
    print("<body/>\n<html/>\n")

def get_fraction(proper=True, low=1, high=10):  # inclusiv, inclusive range
    fraction = (1,1)
    while (True):
        fraction = random.randint(low,high), random.randint(low,high)
        if fraction[0] == fraction[1]:
            continue
        if proper and (fraction[0] > fraction[1]):
            continue
        break
        

    return fraction

def get_medium_fraction(proper=True):  # inclusiv, inclusive range
    return get_fraction(proper=proper, low=1, high=10)

def get_basic_fraction():
    return random.choice(((1,2), (1,3), (1,4), (1,5), (2,3), (2,5), (3,4), (3,5), (4,5)))

def fraction_to_str(fraction):
    if fraction[1] == 1:
        return "{}".format(fraction[0])
    else:
        return "<sup>{}</sup>&frasl;<sub>{}</sub>".format(fraction[0], fraction[1])

def divide_or_multiply():
    if (random.randint(0,1) == 0):
        return divide
    else:
        return multiply

def get_person():
    return random.choice(("John", "Paul", "Matthew", "Luke", "Bobby", "Fred", "Tommy", "Nick", "Peter", "Dennis"))

def get_short_length_unit():
    return random.choice(("yard", "foot", "meter"))

def get_material():
    return random.choice(("ribbon", "string", "tape"))

def get_item():
    return random.choice(("pencils", "cookies", "donuts", "flowers"))

def get_drink():
    return random.choice(("milk", "water", "juice", "Sprite", "root beer"))

def get_toy():
    return random.choice(("Lego set", "Nerf gun", "race track", "Rubik's cube"))

def get_pet():
    return random.choice(("Suki", "Shadow", "Shitzu", "Ninja Kitty"))

def get_ith():
    return random.choice(( ("halves",2), ("thirds",3), ("fourths",4), ("fifths",5), ("sixths",6)    ))

def print_big_space():
    print("<p><br><br><br><br><br><br><br><br><br><br>")

    
html_start()
for i in range(0,9):
    fraction1 = (1,1)
    fraction2 = (1,1)
    while (fraction1[1] == 1 and fraction2[1] == 1):
        fraction1 = get_medium_fraction(proper=True)
        fraction2 = get_medium_fraction(proper=True)

    print("<p>")
    print("{} {} {} = ".format(fraction_to_str(fraction1), divide_or_multiply(), fraction_to_str(fraction2)))
    print("</p>")
    print("<br>")

print("<p style=\"page-break-before: always\">")

print("<p>")
print("{} cuts {} {} of {} into {} equal pieces. What is the length of each piece".format(
    get_person(), 
    fraction_to_str(get_medium_fraction(proper=True)), 
    get_short_length_unit(), 
    get_material(), 
    random.randint(2,8)))

print_big_space()

while True:
    start_count = random.randint(10,40)
    first_give_count = random.randint(2, start_count-1)
    remaining = start_count - first_give_count
    fraction = get_basic_fraction()
    if ((remaining * fraction[0]) % fraction[1]) == 0:
        print("{0} had {1} {2}. He gave {3} {2} to his friends. {4} of his remaining {2} will be saved for tomorrow. How many {2} will {0} have tomorrow".format(
            get_person(),
            start_count,
            get_item(),
            first_give_count,
            fraction_to_str(fraction)
        ))
        break

print_big_space()

print("{0} and {1} friends are sharing {2} of a quart of {3} equally. What fraction of a quart of {3} does each person get".format(
    get_person(),
    random.randint(2, 6),
    fraction_to_str(get_basic_fraction()),
    get_drink()
))

print_big_space()

ith = get_ith()
print("{} makes {} sandwhiches that he cuts into {}. How many {}-size sandwhich pieces does he have".format(
    get_person(),
    random.randint(2, 8),
    ith[0],
    fraction_to_str((1,ith[1])),
))

print_big_space()

while True:
    _gift=random.randint(20,100)
    _fraction1=get_basic_fraction()
    _fraction2=get_basic_fraction()
    if (_gift * _fraction1[0]) % _fraction1[1] != 0:
        continue 
    left_over1 = (_gift * _fraction1[0]) / _fraction1[1]
    if (left_over1 * _fraction2[0]) % _fraction2[1] != 0:
        continue
    print("{person} received ${gift} for Christmas. He spent {fraction1} of it on a {toy}. Of the remainin money, he gave {fraction2} to charity, and put the rest in the bank. How much did {person} put in the bank".format(
        person=get_person(),
        gift=_gift,
        fraction1=fraction_to_str(_fraction1),
        toy=get_toy(),
        fraction2=fraction_to_str(_fraction2)
    ))
    break
    
print_big_space()

_pet = get_pet()
while True:
    _friend_count=random.randint(2,8)
    _ounces=random.randint(20,60)
    if _ounces % (_friend_count + 1) != 0:
        continue
    print("{pet} invited {friend_count} friends and asked them to stay for dinner. {pet} was given {ounces} of food, and wants to share the food evenly. How much food will each pet get?".format(
        pet=_pet,
        friend_count=_friend_count,
        ounces=_ounces))
    break

html_stop()
