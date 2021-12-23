# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# CLi,12.14.2021,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Data -------------------------------------------------------------------- #
file_name_str = "EmployeeData.txt"
file_data_lst = []
table_lst = []
choice_str = ''
# Data -------------------------------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of employee objects when script starts
file_data_lst = Fp.read_data_from_file(file_name_str)
table_lst.clear()
for line in file_data_lst:
    table_lst.append(Emp(line[0], line[1], line[2].strip()))

while True:
    # Show user a menu of options
    Eio.print_menu_items()

# Get user's menu option choice
    choice_str = Eio.input_menu_options()
    # Show user current data in the list of employee objects
    if choice_str.strip() == '1':
        Eio.print_current_list_items(table_lst)
        continue

    # Let user add data to the list of employee objects
    elif choice_str.strip() == '2':
        try:
            employee = Eio.input_employee_data()
            table_lst.append(employee)
        except UnboundLocalError:
            print('Please try again.')
        continue

    # let user save current data to file
    elif choice_str.strip() == '3':
        Fp.save_data_to_file(file_name_str, table_lst)
        continue

    # Let user exit program
    elif choice_str.strip() == '4':
        print('Goodbye!')
        break

# Main Body of Script  ---------------------------------------------------- #
