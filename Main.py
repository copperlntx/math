import random

divide   = "&divide;"
multiply = "&times;"

def html_start():
    print("<html>\n<body>\n")

def html_stop():
    print("<body/>\n<html/>\n")

def get_fraction(proper=False):
    fraction = (1,1)
    while (True):
        fraction = random.randint(1,7), random.randint(1,7)
        if fraction[0] == fraction[1]:
            continue
        if proper and (fraction[0] > fraction[1]):
            continue
        break
        

    return fraction

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
    return random.choice(("John", "Paul", "Matthew", "Luke"))

def get_short_length_unit():
    return random.choice(("yard", "foot", "meter"))

def get_material():
    return random.choice(("ribbon", "string", "tape"))

def get_item():
    return random.choice(("pencils", "cookies", "donuts", "flowers"))

def get_drink():
    return random.choice(("milk", "water", "juice"))

def get_ith():
    return random.choice(( ("halves",2), ("thirds",3), ("fourths",4), ("fifths",5), ("sixths",6)    ))

def get_basic_fraction():
    return random.choice(((1,2), (1,3), (1,4), (1,5), (2,3), (2,5), (3,4), (3,5), (4,5)))

def print_big_space():
    print("<p><br><br><br><br><br><br><br><br><br><br>")
    
html_start()
for i in range(0,9):
    fraction1 = (1,1)
    fraction2 = (1,1)
    while (fraction1[1] == 1 and fraction2[1] == 1):
        fraction1 = get_fraction()
        fraction2 = get_fraction()

    print("<p>")
    print("{} {} {} = ".format(fraction_to_str(fraction1), divide_or_multiply(), fraction_to_str(fraction2)))
    print("</p>")
    print("<br>")

print("<p style=\"page-break-before: always\">")

print("<p>")
print("{} cuts {} {} of {} into {} equal pieces. What is the length of each piece".format(
    get_person(), 
    fraction_to_str(get_fraction(proper=True)), 
    get_short_length_unit(), 
    get_material(), 
    random.randint(2,8)))

print_big_space()

person = get_person()
item = get_item()
while True:
    start_count = random.randint(10,40)
    first_give_count = random.randint(2, start_count-1)
    remaining = start_count - first_give_count
    fraction = get_basic_fraction()
    if ((remaining * fraction[0]) % fraction[1]) == 0:
        print("{} had {} {}. He gave {} {} to his friends. {} of his remaining {} will be saved for tomorrow. How many {} will {} have tomorrow".format(
            person,
            start_count,
            item,
            first_give_count,
            item,
            fraction_to_str(fraction),
            item,
            item,
            person
            
        ))
        break

print_big_space()

drink = get_drink()
print("{} and {} friends are sharing {} of a quart of {} equally. What fraction of a quart of {} does each person get".format(
    get_person(),
    random.randint(2, 6),
    fraction_to_str(get_basic_fraction()),
    drink,
    drink
))

print_big_space()

ith = get_ith()
print("{} makes {} sandwhiches that he cuts into {}. How many {}-size sandwhich pieces does he have".format(
    get_person(),
    random.randint(2, 8),
    ith[0],
    fraction_to_str((1,ith[1])),
))

html_stop()