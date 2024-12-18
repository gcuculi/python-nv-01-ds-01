def addNewContact(contact_book, name, telephone, email):
  contact_book.append({
    "name": name,
    "telephone": telephone,
    "email": email,
    "favorite": False
  })
  print("\nContact added with success!")
  return

def hasContacts(contact_book):
  if not contact_book:
    print("\nContact book is empty.")
    return False
  else:
    return True

def isValidInputedContactIndex(contact_book, index):
  if index < 1 or index > len(contact_book):
    print("\nInvalid contact index.")
    return False
  return True

def showAllContacts(contact_book, show_only_favorites=False):
  if show_only_favorites:
    print("\nShowing only favorite contacts:")
  else:
    print("\nShowing all contacts:")

  has_at_least_one_favorite_contact = False
  
  for index, contact in enumerate(contact_book, start=1):
    if not show_only_favorites:
      showContact(contact, index)
    elif show_only_favorites and contact['favorite']:
      showContact(contact, index)
      has_at_least_one_favorite_contact = True

  if show_only_favorites:
    if has_at_least_one_favorite_contact:
      print("\nAll favorite contacts listed!")
    else:
      print("\nNo favorite contacts found.")
  else:
    print("\nAll contacts listed!")  
  return

def showContact(contact, index):
  if not contact:
    print("\nContact not found.")
  else:
    name = contact['name']
    telephone = contact['telephone']
    email = contact['email']
    favorite = "✓" if contact['favorite'] else " "

    print(f"\nContact: {index}:")
    print(f"- Name: {name}")
    print(f"- Telephone: {telephone}")
    print(f"- Email: {email}")
    print(f"- Favorite: [{favorite}]")
  return

def getContact(contact_book, index):
  if isValidInputedContactIndex(contact_book, index):
    return contact_book[index - 1]
  else:
    return

def editContact(contact, index):
  showContact(contact, index)

  print("\nEditing contact info:")
  name = input(f"Enter new name (leave it blank to not change current data): ")
  telephone = input(f"Enter new telephone (leave it blank to not change current data): ")
  email = input(f"Enter new email (leave it blank to not change current data): ")

  if name:
    contact['name'] = name

  if telephone:
    contact['telephone'] = telephone

  if email:
    contact['email'] = email

  print("\nContact updated with success!")
  return

def toggleContactAsFavorite(contact):
  contact['favorite'] = not contact['favorite']
  print("\nFavorite status toggled with success!")
  return

def removeContact(contact_book, contact):
  contact_book.remove(contact)
  print("\nContact removed with success!")
  return

# {Name, Telephone, Email, Favorite}
contact_book = []

while True:
  print("\nMenu:\n")
  print("1. Add a new contact")
  print("2. Show all contacts")
  print("3. Edit a contact")
  print("4. Add/remove contact as favorite")
  print("5. Show favorite contacts")
  print("6. Delete a contact")
  print("7. Exit")

  option = input("\nChoose an option: ")

  if option == "1":
    print("\nAdding new contact info:\n")
    name = input("Name: ")
    telephone = input("Telephone: ")
    email = input("Email: ")
    
    addNewContact(contact_book, name, telephone, email)

  elif option == "2":
    if hasContacts(contact_book):
      showAllContacts(contact_book)

  elif option == "3":
    if hasContacts(contact_book):
      showAllContacts(contact_book)

      index = int(input("\nEnter the index of the contact to edit: "))

      if isValidInputedContactIndex(contact_book, index):
        contact = getContact(contact_book, index)
        if contact:
          editContact(contact, index)

  elif option == "4":
    if hasContacts(contact_book):
      showAllContacts(contact_book)

      index = int(input("\nEnter the index of the contact to toggle favorite status: "))

      if isValidInputedContactIndex(contact_book, index):
        contact = getContact(contact_book, index)
        if contact:
          toggleContactAsFavorite(contact)

  elif option == "5":
    if hasContacts(contact_book):
      showAllContacts(contact_book, True)

  elif option == "6":
    if hasContacts(contact_book):
      showAllContacts(contact_book)

      index = int(input("\nEnter the index of the contact to remove it: "))

      if isValidInputedContactIndex(contact_book, index):
        contact = getContact(contact_book, index)
        if contact:
          removeContact(contact_book, contact)

  elif option == "7":
    break