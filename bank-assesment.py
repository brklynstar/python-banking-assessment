def load_data(file_name):
    f = open(file_name, "r")
    user_list = f.readlines()
    f.close()

    return user_list

def login(user_list):
    username_input = input("\n" "Enter your username homie! " "\n" "Enter Username: ")
    password_input = input("\n" "Gimme yo' password Now!" "\n" "Enter Password: ")
    user_accessed ={}

    for user in user_list:
        username, password, full_name, balance = user.strip().split(",")
        if username_input == username and password_input == password:
            user_accessed = {"Government Name": full_name, "Your Stash":"$" + str(balance)}
            
    return user_accessed

def dollar_line():
    print(" -$-" * 7)

def border_line():
    print("\n"+"-" * 30 ,"\n")

invalid_credintials_message = False
def view_user_account(user, invalid_credintials_message):
    while user == {} and invalid_credintials_message == False:
      print("If you don't have the right creditinials, bounce!" "\n")
      return
    else:
        user_account = f'Government Name: {user["Government Name"]}\nYour Stash: {user["Your Stash"]}'
        print(user_account , "\n")
        return(hustle_harder_message)
    quit()


def hustle_harder_message():
        print("*** Step your game up! Hustle harder ***!")
   
    
        
dollar_line()
print("Welcome to The Hustlers Bank")
dollar_line()

user_list = load_data("data.txt")
user = login(user_list)
border_line()

view_user_account(user, invalid_credintials_message)
hustle_harder_message()


