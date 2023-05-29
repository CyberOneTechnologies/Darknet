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

from app.utils.input_manager import get_user_input
from app.utils.file_manager import generate_filename, save_results
from app.scrapers.tor_scraper import TorScraper

def main():
    # Get user input
    first_name, last_name, phone_number, country, email_address, address, city, state, zip_code = get_user_input()

    # Create a TorScraper instance
    tor_scraper = TorScraper()

    # Perform darknet search
    results = tor_scraper.search(first_name, last_name, phone_number, country, email_address, address, city, state, zip_code)

    # Generate output file name
    filename = generate_filename(first_name, last_name)

    # Save results to output file
    save_results(filename, results)

    print(f"Results saved to {filename}")

if __name__ == "__main__":
    main()
