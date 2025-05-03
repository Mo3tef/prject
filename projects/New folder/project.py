import random
import string


def read_users_file():
    try:
        with open("user.txt", "r") as file:
            users = [line.strip().split(",") for line in file]
        return users
    except FileNotFoundError:
        return []

"""************************************************************************************************************************"""

def check_duplicate(username):
    users = read_users_file()
    for registered_username, _ in users:
        if username == registered_username:
            print("This username is already taken.")
            return True
    return False

"""************************************************************************************************************************"""

def create_account():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if check_duplicate(username):
        print("Please choose a different username.")
        return create_account()
    
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")
    
    print("Account created successfully!")
    print(f"Hello {username}, protecting your data is our mission!")

"""************************************************************************************************************************"""

def check_account(username, password):
    users = read_users_file()
    for registered_username, registered_password in users:
        if username == registered_username and password == registered_password:
            return True
    return False

"""************************************************************************************************************************"""

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if check_account(username, password):
        print("Login successful!")
        print(f"Hello {username}, protecting your data is our mission!")
        return True
    else:
        print("Login failed! Incorrect username or password.")
        return False

"""************************************************************************************************************************"""

def User_options():
    while True:
        print("\nChoose one of the following options:")
        print("1. SandBox")
        print("2. VPN")
        print("3. Scan virus & remove Malware")
        print("4. Webfilter")
        print("5. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("You've selected the SandBox option!")
            sandbox_operation()
            
        elif choice == "2":
            print("You've selected the VPN option!")
            Vpn_operation()
        elif choice == "3":
            print("You've selected the Scan virus & remove Malware option!")
            Scan_virus_and_remove_Malware()
        elif choice == "4":
            print("You've selected the Webfilter option!")
            Webfilter()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

"""************************************************************************************************************************"""         

def sandbox_operation():
    def sandbox_function(text):
        words = text.split()
        num_words = len(words)
        num_chars = len(text)
        return num_words, num_chars

    text = input("Enter a sentence: ")

    if not isinstance(text, str) or text.isdigit():
        print("Input must be a valid string containing letters.")
        sandbox_operation()        
    else:
        word_count, char_count = sandbox_function(text)
        print(f"Number of words in the text: {word_count}")
        print(f"Number of characters in the text: {char_count}")
        back_to_the_main_menu_or_exit()
    
"""************************************************************************************************************************"""

def Vpn_operation():

    all_chars = string.ascii_letters + string.digits + string.punctuation + " "
    all_chars = list(all_chars)
    key = all_chars.copy()
    random.shuffle(key)


 
    print("----- Encryption ------")
    plain_text = input("Enter Your Message to encrypt: ")
    cipher_text = ""

    for letter in plain_text:
        index = all_chars.index(letter)
        cipher_text += key[index]

    print(f"Ecrypted Message: {cipher_text}")

   
    print("----- Decryption ------")
    cipher_text = input("Enter Your Message to dencrypt: ")
    plain_text = ""

    for letter in cipher_text:
        index = key.index(letter)
        plain_text += all_chars[index]

    print(f"Decrypted Message: {plain_text}")
    back_to_the_main_menu_or_exit()
    
"""************************************************************************************************************************"""

def Scan_virus_and_remove_Malware():
    def scan_for_viruses(text, virus_signatures):
        print(text_to_scan)
        found_viruses = []
        for virus in virus_signatures:
            if virus in text:
                found_viruses.append(virus)
        return found_viruses

    def remove_viruses_interactive(text, virus_signatures):

        for virus in virus_signatures:
            if virus in text:
                user_input = input(f"The virus '{virus}' was found. Do you want to remove it? (yes/no): ").strip().lower()
                if user_input == 'yes':
                    text = text.replace(virus, "")
                    print(f"Removed '{virus}' from the text.")
                else:
                    print(f"Kept '{virus}' in the text.")
        return text


    virus_signatures = ["malware", "virus"]


    text_to_scan = "This document contains a virus and some malware that needs to be removed."


    found_viruses = scan_for_viruses(text_to_scan, virus_signatures)
    print(f"Found viruses: {found_viruses}")


    cleaned_text = remove_viruses_interactive(text_to_scan, virus_signatures)
    print(f"Final cleaned text: {cleaned_text}")
    back_to_the_main_menu_or_exit()

"""************************************************************************************************************************"""

def Webfilter():
    blocked_sites = ["Daily News Egypt.com", "CNN.com"]

    text = "You should visit example.com and badwebsite.com for more information."

    def web_filter_interactive(text, blocked_sites):

        for site in blocked_sites:
            if site in text:
                if input(f"Block '{site}'? (yes/no): ").strip().lower() == 'yes':
                    text = text.replace(site, "BLOCKED")
        return text

    print(f"{text}")

    filtered_text = web_filter_interactive(text, blocked_sites)

    print(f"{filtered_text}")
    back_to_the_main_menu_or_exit()

"""************************************************************************************************************************"""

def back_to_the_main_menu_or_exit():
    while True:
        decision = input("Do you want to go back to the main menu or exit? (menu/exit): ").strip().lower()
        if decision == "menu":
            return  # Return to the main menu
        elif decision == "exit":
            print("Exiting the program.")
            exit()  # Exit the program
        else:
            print("Invalid input. Please enter 'menu' or 'exit'.")

"""************************************************************************************************************************"""

def main():
    while True:
        option = input("Do you already have an account? (yes/no): ").strip().lower()
        
        if option == "yes":
            if login():
                User_options()
            else:
                print("Login failed. Please try again.")
        elif option == "no":
            create_account()
            User_options()
        else:
            print("Invalid option. Please enter 'yes' or 'no'.")

# Call the main function
main()
