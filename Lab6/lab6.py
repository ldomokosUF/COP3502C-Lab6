def encode(raw_pw):
    encoded_pw = ""
    for i in range(len(raw_pw)):
        encoded_pw = encoded_pw + str((int(raw_pw[i]) + 3) % 10)
    print("Your password has been encoded and stored!\n")
    return encoded_pw

decode(raw_pw)

if __name__ == "__main__":
    selection = 1
    while selection != 0:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        selection = int(input("Please enter an option: "))
        

        if selection == 1:
            password = input("Please enter your password to encode: ")
            password = encode(password)
        elif selection == 2:
            password = decode(password)