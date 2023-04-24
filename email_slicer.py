#collect email from user
#split email using the @, save first part as the username, second part is gonna save as domain.
#split domain using ., 
def main():
    print("Welcome to the Email Slicer")
    print("")

    email_input = input("Input your email address: ")

    username, domain = email_input.split("@")
    domain, extension = domain.split(".")

    print("Username : ", username)
    print("Domain : ", domain)
    print("Extension: ", extension)


main()