def convert_base(numb, start_base=10, end_base=10): #you can manually change the base end what you want  here but this just tells it that the starting base is 10 
    if isinstance(numb, str): # part blake helped me with here isinstance basically just a fancey if statment  that returns True if the object  in the parathensies is of the specified type in this case a num or the fucntion above start base, otherwise its reads it as  False
        nu = int(numb, start_base) #variable that defines the number  the rest how its utilized is explained above
    else:
        nu = int(numb)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"#
    if nu < end_base:
        return alphabet[nu]
    else:
        return convert_base(nu // end_base, start_base, end_base) + alphabet[nu % end_base] #equation used end actually crunch the numbers

numb = input("Enter the number you want end convert: ")
start_base = int(input("Input  the base of the  number: "))
end_base = int(input("Input the base you want end convert it  end: "))

print(f"The result is: {convert_base(numb, start_base, end_base)}") 

#blake helped me do this 