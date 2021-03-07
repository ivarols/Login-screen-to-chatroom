from Projects.chatroom_encrypted import encryption_function_for_chatroom


def register():

    print("Registration")
    password_r = ""
    username_r = input("Enter username: ")
    username_split_r = len(username_r.split())
    if username_split_r > 1:
        print("No blank spaces within the username.")
        return register()
    elif username_split_r < 1:
        print("No username entered.")
        return register()
    else:
        reg_completion = False

    with open('#incert .txt-file-name-here#', 'r') as register_r:
        for line in register_r:
            user_info_list = line.split()
            if len(user_info_list) > 0:
                if user_info_list[0] == username_r:
                    print("Username already taken.")
                    return register()

        while not reg_completion:
            password_r = input("Enter password: ")
            password_split_r = username_r.split()
            words_r = space_control(password_split_r)

            for char in password_r:
                if char not in encryption_function_for_chatroom.accessable_digits:
                    print("Password conatians illega charachters.")
                    return register()

            if words_r > 1:
                print("No black spaces within the password.")
                return register()
            elif words_r < 1:
                print("No password entered.")
                return register()

            elif len(password_r) < 7:
                print("Password is too short.")
                return register()
            else:
                reg_completion = True
        with open('#incert .txt-file-name-here#', 'a') as register_r:
            password_r, access_key2 =  encryption_function_for_chatroom.password_encryption(password_r)
            print(f'Your login-info access-key is: {access_key2}')
            register_r.write(f'{username_r} {password_r}\n')
        register_r.close()


def login():
    username_l = input("Enter username: ")
    password_l = input("Enter password: ")
    access = False
    for char in password_l:
        if char not in encryption_function_for_chatroom.accessable_digits:
            print("Username or password is incorrect.")
            return access

    with open('#incert .txt-file-name-here#', 'r') as login_info:
        for line in login_info:

            login_info_list = line.split()
            if len(login_info_list) > 0:
                if login_info_list[0] == username_l and login_info_list[1] == encryption_function_for_chatroom.password_encryption(password_l):
                        access = True

    login_info.close()

    if access:
        return username_l
    else:
        print("Username or password is incorrect.")
        return access

def get_login_info():
    username = input("Enter username: ")
    access_key = input("Enter accesskey: ")
    password_key = encryption_function_for_chatroom.key_decrypter(access_key)

    if len(password_key) != 3:
        print("Invalid access_key")
        return get_login_info()
    elif not password_key[0].isdigit() or not password_key[1].isdigit():
        print("Invalid access_key")
        return get_login_info()
    elif password_key[2] != ".":
        print("Invalid access_key")
        return get_login_info()


    with open('#incert .txt-file-name-here#', 'r') as login_info:
        for line in login_info:
            login_info_list = line.split()
            if len(login_info_list) > 0:
                if login_info_list[0] == username:
                    password_decypted = encryption_function_for_chatroom.message_decryption(login_info_list[1], password_key)
                    return password_decypted

def chatroom(username_c):
    message_c = input("> ")

    if message_c == "_logout":
        return False
    else:
        emoji_converted_message_c = emoji_converter(message_c)
        print(f'{username_c}: {emoji_converted_message_c}')
        return chatroom(username_c)


def emoji_converter(message_ec):
    words_ec = message_ec.split()
    emoji_ec = {

        ":)": "😀",
        ":(": "🙁",
        "B)": "😎",
        ":p": "😜",
        ";)": "😉"
    }
    output_ec = ""
    for word_controll_ec in words_ec:
        output_ec += emoji_ec.get(word_controll_ec, word_controll_ec) + " "
    return output_ec


def space_control(username_sc):
    words_sc = 0
    for word_sc in username_sc:
        words_sc += 1
    return words_sc


def greeting(username_g):
    print(f'Welcome, {username_g}!')
    print("You can now chat.")
    print("Exit chat by typing '_logout'.")

program_running = True
while program_running:
    print("Enter: 'login' to log in.")
    print("Enter: 'reg' to register.")
    print("Enter: 'forgot_password' to obtain password.")
    action = input("Log in or register: ")
    counter = 0
    if action == "login":
        print("Login")
        username = login()
        if username != False:
            greeting(username)
            running_chat = chatroom(username)
            if running_chat == False:
                print("Chat have been exited and you have been logged out.")

    elif action == "forgot_password":
        password = get_login_info()
        if password is None:
            print("Invalid access_key or username")
        else:
           print(f'password: {password}')


    elif action == "reg":
        register()

    elif action == "exit":
        print("You have exited the program.")
        program_running = False

