# practicing the input syntax

# asking for user's name
my_name = input("What's your name? ")
final_name = my_name.capitalize()
print(f"""!{final_name}!{final_name}!""")

# asking for user's name and address
first_name = input("Given name: ")
family_name = input("Family name: ")
street_address = input("Street address: ")
postal = input("City and postal code: ")
print(first_name.capitalize() + " " + family_name.capitalize())
print(street_address)
print(postal)

