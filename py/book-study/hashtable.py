def searchContact(contact_name, contact_list):
    try:
        return contact_list[contact_name]
    except KeyError as key_error:
        print(key_error)
        print("Contact name not found")

contact_list = dict()
contact_list["Valdemiro"] = 9139283834
contact_list["Ladalberto"] = 937744322
contact_list["Marcileo"] = 938433213
contact_list["Bruno"] = 938636482
name = input("inform a name:")
print(searchContact(name, contact_list))