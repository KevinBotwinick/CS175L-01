#CS175L-01
#Kevin Botwinick
#Restaurant
keep_going = True
while keep_going == True:
    
    
    Userint = ""
    vegetarian= False
    vegan=False
    gluten_free=False
    vegetarian = input("Is anyone in your party a vegetarian? ")

    if vegetarian == "yes" or vegetarian == "no":
        if vegetarian == "yes":
            vegetarian = True
        else:
            vegetarian = False
        vegan = input("Is anyone in your party a vegan? ")

        if vegan == "yes" or vegan == "no":
            if vegan == "yes":
                vegan = True
            else:
                vegan = False
            gluten_free = input("Is anyone in your party gluten-free? ")

            if gluten_free == "yes" or gluten_free == "no":
                if gluten_free == "yes":
                    gluten_free = True
                else:
                    gluten_free = False
                Userint = "\nHere are your restaurant choices:\n"

                if vegetarian == True:

                    if vegan == True:

                        if gluten_free == True or gluten_free == False:
                            Userint += "Corner Cafe\n" + \
                                       "The Chef's Kitchen\n"
                    else: 
                        if gluten_free == True:
                            Userint += "Main Street Pizza Company\n" + \
                                       "Corner Cafe\n" + \
                                       "The Chef's Kitchen\n"
                        else:
                            Userint += "Main Street Pizza Company\n" + \
                                       "Corner Cafe\n" + \
                                       "Mama's Fine Italian\n" + \
                                       "The Chef's Kitchen\n"
                else: # vegetarian == "no"

                    if vegan == True:

                        if gluten_free == True or gluten_free == False:
                            Userint += "Corner Cafe\nThe Chef's Kitchen\n"

                    else: # vegan == "no"

                        if gluten_free == True:
                            Userint += "Main Street Pizza Company\n" + \
                                       "Corner Cafe\n" + \
                                       "The Chef's Kitchen\n"

                        else: # gluten free == "no"
                            Userint += "Joe's Gourmet Burgers\n" + \
                                       "Main Street Pizza Company\n" + \
                                       "Corner Cafe\n" + \
                                       "Mama's Fine Italian\n" + \
                                       "The Chef's Kitchen\n"

    print (Userint)      
    keep_going_switch=input('Do you want to keep going? ')
    if keep_going_switch == "no":
        keep_going = False
    
