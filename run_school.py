from school import School


mest = School()
print('add eit')
mest.add_eit()
print('add fellow')
mest.add_fellow()
while True:
    what_to_do = input('fellow actions or eit actions?  f/e: ')
    if what_to_do == 'f':
        fellow_action = input('what should fellows do? teach/eat | t/e: ')
        if fellow_action == 't':
            for fellow in mest.fellows:
                fellow.teach()
        if fellow_action == 'e':
            for fellow in mest.fellows:
                fellow.eat()

    elif what_to_do == 'e':
        for eit in mest.eits:
            eit.say_fun_fact_about_tech_class()

    else:
        with open('eits.csv', 'w') as eit_file:
            eit_file.write('Name,Nationality\n')
            for eit in mest.eits:
                eit_file.write(eit.name+','+eit.nationality+'\n')
        break
