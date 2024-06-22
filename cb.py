#underprocess...
class Contact:
    
    def _init_(self,name,phone_no,email,address):
        self.name =name
        self.phone = phone_no
        self.email = email
        self.address = address

    def add():
        print("Enter the following details to create a new contact -")
        name = input("Enter Name :")
        phone_no = input("Enter Phone no  :")
        email = input("Enter your email address  :")
        address = input("Enter your  Address  ")
        print("YOur details are successfully added..:)")
        c1 = Contact(name,phone_no,email,address)
        

    def view():
        print("These are the details of the Contact ",id)
        print("\tName :",phone[id].name)
        print("\tphone_no :",phone[id].phone_no)
        print("\temail :",phone[id].email)
        print("\taddress :",phone[id].address)



print("Welcome to Contact Book Program")
print("Enter 1 to add new contact \nEnter 2 to view")
answer = input()
if answer =='1':
    phone[id].add()
    id+=1
elif answer=='2':
    print("Enter the id :")
    id = int(input())
    phone[id].view()
else:
    print("Please enter write input ...")