####################################################################################
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░Darknet OSINT░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░#
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░Developed by Aarsyth░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░#
#░░░░░░░░░░░░GitHub Repository: https://github.com/CyberOneTechnologies/░░░░░░░░░░░#
#░░░░░░░░░░░░░░░░░For support, reach out on Discord: Aarsyth#0563░░░░░░░░░░░░░░░░░░#
####################################################################################
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░#
#░░░░░░░░█████╗░██╗░░░██╗██████╗░███████╗██████╗░░█████╗░███╗░░██╗███████╗░░░░░░░░░#
#░░░░░░░██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗░██║██╔════╝░░░░░░░░░#
#░░░░░░░██║░░╚═╝░╚████╔╝░██████╦╝█████╗░░██████╔╝██║░░██║██╔██╗██║█████╗░░░░░░░░░░░#
#░░░░░░░██║░░██╗░░╚██╔╝░░██╔══██╗██╔══╝░░██╔══██╗██║░░██║██║╚████║██╔══╝░░░░░░░░░░░#
#░░░░░░░╚█████╔╝░░░██║░░░██████╦╝███████╗██║░░██║╚█████╔╝██║░╚███║███████╗░░░░░░░░░#
#░░░░░░░░╚════╝░░░░╚═╝░░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝░░░░░░░░░#
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░#
####################################################################################

import datetime
import os
from app.scrapers.tor_scraper import TorScraper

def main():
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

    # Create a TorScraper instance
    tor_scraper = TorScraper()

    # Perform darknet search
    results = tor_scraper.search(first_name, last_name, phone_number, country, email_address, address, city, state, zip_code)

    # Get current date/time
    now = datetime.datetime.now()

    # Generate output file name
    filename = f"darknetquery.{first_name}.{last_name}.{now.strftime('%Y%m%d%H%M%S')}.txt"

    # Save results to output file
    with open(filename, "w") as file:
        file.write(results)

    print(f"Results saved to {filename}")

if __name__ == "__main__":
    main()
