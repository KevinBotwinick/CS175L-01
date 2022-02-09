Userint = ""
vegetarian= False
vegan=False
gluten_free=False
vegetarian = input("Is anyone in your party a vegetarian? ")

if vegetarian == "yes" or vegetarian == "no":
    vegan = input("Is anyone in your party a vegan? ")

    if vegan == "yes" or vegan == "no":
        gluten_free = input("Is anyone in your party gluten-free? ")

        if gluten_free == "yes" or gluten_free == "no":
            Userint = "\nHere are your restaurant choices:\n"

            if vegetarian == "yes":
                
                if vegan == "yes":

                    if gluten_free == "yes" or gluten_free == "no":
                        Userint += "Corner Cafe\n" + \
                                   "The Chef's Kitchen\n"
                else: 
                    if gluten_free == "yes":
                        Userint += "Main Street Pizza Company\n" + \
                                   "Corner Cafe\n" + \
                                   "The Chef's Kitchen\n"
                    else:
                        Userint += "Main Street Pizza Company\n" + \
                                   "Corner Cafe\n" + \
                                   "Mama's Fine Italian\n" + \
                                   "The Chef's Kitchen\n"
            else: # vegetarian == "no"

                if vegan == "yes":

                    if gluten_free == "yes" or gluten_free == "no":
                        Userint += "Corner Cafe\nThe Chef's Kitchen\n"

                else: # vegan == "no"

                    if gluten_free == "yes":
                        Userint += "Main Street Pizza Company\n" + \
                                   "Corner Cafe\n" + \
                                   "The Chef's Kitchen\n"
                                   
                    else: # gluten free == "no"
                        Userint += "Joe's Gourmet Burgers\n" + \
                                   "Main Street Pizza Company\n" + \
                                   "Corner Cafe\n" + \
                                   "Mama's Fine Italian\n" + \
                                   "The Chef's Kitchen\n"

        else:
            Userint = "Enter either 'yes' or 'no'.\nRerun the program and try again."
    
    else:
        Userint = "Enter either 'yes' or 'no'.\nRerun the program and try again."

else:
    Userint = "Enter either 'yes' or 'no'.\nRerun the program and try again."
print(Userint)
