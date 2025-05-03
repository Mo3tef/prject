def read_users_file():
    try:
        with open("users.txt", "r") as file:
            users = [line.strip().split(",") for line in file]
        return users
    except FileNotFoundError:
        return []

def check_duplicate(username):
    users = read_users_file()
    for registered_username, _ in users:
        if username == registered_username:
            print("This username is already taken.")
            return True
    return False

def create_account():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if check_duplicate(username):
        print("Please choose a different username.")
        create_account()
        return
    
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")
    
    print("Account created successfully!")
    print(f"Hello {username}, protecting your data is our mission!")

def check_account(username, password):
    users = read_users_file()
    for registered_username, registered_password in users:
        if username == registered_username and password == registered_password:
            return True
    return False

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if check_account(username, password):
        print("Login successful!")
        print(f"Hello {username}, protecting your data is our mission!")
    else:
        print("Login failed! Incorrect username or password.")

def main():
    while True:
        option = input("Do you already have an account? (yes/no): ").strip().lower()
        
        if option == "yes":
            login()
            break
        elif option == "no":
            create_account()
            break
        else:
            print("Invalid option. Please enter 'yes' or 'no'.")

# Call the main function
main()








def User_options():
    # Display options to the user
    print("Choose one of the following options:")
    print("1.SandBox ")
    print("2.VPN")
    print("3.Webfilter")
    print("4.scan virus & remove Malware ")

# Get the user's choice
choice = input("Enter the number of your choice: ")

# Check the user's choice and display the appropriate message
if choice == "1":
    print("لقد اخترت الخيار الأول!")
    def sandbox_function(text):
  
        words = text.split()
        num_words = len(words)
        num_chars = len(text)
        return num_words, num_chars

    def run_sandbox(text):

        return sandbox_function(text)


    text = input("Enter a sentence: ")

    if not isinstance(text, str) or text.isdigit():
        print("Input must be a valid string containing letters.")
    else:
    
        word_count, char_count = run_sandbox(text)
        print(f"Number of words in the text: {word_count}")
        print(f"Number of characters in the text: {char_count}")



















elif choice == "2":
    print("لقد اخترت الخيار الثاني!")
elif choice == "3":
    print("لقد اخترت الخيار الثالث!")
elif choice == "4":
    print("لقد اخترت الخيار الرابع!")
else:
    print("الاختيار غير صحيح. الرجاء إدخال رقم من 1 إلى 4.")
