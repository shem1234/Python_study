name = "  JOHn  ."
name=name.replace(".","")
name=name.strip()
name=name.lower()

print(name)

sentence_one =  "The Dog Breed is German Shepherd"
print(sentence_one[8:23])

sentence_two = "Defeats for the Clinton forces, this was her moment of triumph" 

# only display “Clinton forces”
print(sentence_two[16:30])

text = "The lazy dog; ran so fast; it hit the wall."
text = text.split(";")
print(len(text))

# first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
first_name="  Joh.n"
last_name="   Do,e"

first_name= first_name.replace(".","")
first_name=first_name.strip()
last_name=last_name.replace(",","")
last_name=last_name.strip()
print(first_name + " " + last_name)

# Having the string r = '["E","W","C"]' #Manipulate it to display EWC
r = '["E","W","C"]'
r=r.replace('"','')
r=r.replace(",","")
r=r.replace("[","")
r=r.replace("]","")
print(r)


