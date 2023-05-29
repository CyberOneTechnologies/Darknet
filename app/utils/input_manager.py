def get_user_input():
    # Prompt user for input
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone_number = input("Phone number (numbers only): ")
    country = input("Country: ")
    email_address = input("Email address: ")
    address = input("Address: ")
    city = input("City: ")
    state = input("State: ")
    zip_code = input("ZIP code: ")

    return first_name, last_name, phone_number, country, email_address, address, city, state, zip_code
