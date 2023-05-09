yjokes = ["puchna ye tha ki jo baat dimaag mein baith jati hai\nwo darri laga kar baith ti hai ya kursi par","soch rha hun ek pagalkhana khol lun\ndost bahut badh gaye hain mere","shadi sabko karni chahiye\nis duniya mein khushi hi sabkuch nahi hoti"]

import random

def tell_joke():
    joke = random.choice(yjokes)
    print(joke)

response = input("Do you want to hear another joke? (y/n): ")

if response.lower() == "y":
    tell_joke()
