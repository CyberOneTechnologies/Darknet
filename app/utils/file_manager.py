import datetime

def generate_filename(first_name, last_name):
    # Get current date/time
    now = datetime.datetime.now()

    # Generate output file name
    filename = f"darknetquery.{first_name}.{last_name}.{now.strftime('%Y%m%d%H%M%S')}.txt"

    return filename

def save_results(filename, results):
    # Save results to output file
    with open(filename, "w") as file:
        file.write(results)
