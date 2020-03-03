#dateconvert2.py

#This program converts a date in form "mm/dd/yyyy" to "month day, year"

def main():
    # Get the date
    date = str(input("Enter a date (mm/dd/yyyy): "))

    # Split into components
    month, day, year = date.split("/")

    # Convert monthStr to month name
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month = months[int(str(month))-1]
    # Output result in month day, year format
    print("The converted date is:", str(month), str(day)+",", str(year))
main()