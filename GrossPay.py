#A program that Calculate and Display the Gross Pay for an Hourly Paid Employee

#Define the main function
def main():
    #1. Get the number of hours worked
    Hours_Worked = int(input('Enter number of hours worked: '))

    # Test for numbers of Hours Worked < 0
    while Hours_Worked < 0:
        # Ask User for Hours Worked again
        Hours_Worked = int(input('Enter number of hours worked: '))

    #2. Get the Hourly Pay Rate
    Hourly_Pay = float(input('Enter Hourly Pay Rate: '))

    # Test for Hourly Pay Rate < 0
    while Hourly_Pay < 0.0:
        # Ask User for Hourly Pay Rate again
        Hourly_Pay = float(input('Enter Hourly Pay Rate: '))

    #3. Multiply number of hours worked by hourly pay rate
    Gross_Pay = float(Hours_Worked * Hourly_Pay)

    #4. Display result of calculation
    print('Your Gross Pay for the Week is: ', Gross_Pay)

    #main_function


# Call the main function
main()

# Print the copyright notice declaring authorship.
print("\n(c) 2018, Tishauna Wilson\n\n")

