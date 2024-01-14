def fourthTask():
    import string
    import secrets
    print("You have chosen fourth Task!")
    print("It's a Password Generator!")
    write_number = input("How long should the password be? (Please write a number of 15-20) ")
    write_number = int(write_number)
    if write_number > 20 or write_number < 15:
            print("Please write number of 15-20")
    else:
            digits_and_letters = string.ascii_uppercase + string.ascii_lowercase + string.digits
            random_digit = [secrets.choice(digits_and_letters) for i in range(write_number)]
            rndm_string_digits = "".join(random_digit)
            print(rndm_string_digits)
fourthTask()