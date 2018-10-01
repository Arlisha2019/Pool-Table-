import json
from datetime import datetime, date, time

class PoolTable:
    def __init__(self, table_number):
        self.table_number = table_number
        self.start_datetime = ''
        self.end_datetime = ''
        self.open = ''

    def json_dictionary(self):
        return self.__dict__

    def available_table(self, open):
         self.open = ''

    def occupied_table(self, open):
         self.open = ''

    def __repr__(self):
        status = ""
        if(self.open == False):
            status = "occupied"
        else:
            status = "available"
        return f"table: {self.table_number}, status: {status}, start: {self.start_datetime}, end: {self.end_datetime} \n"

tables_array = []

table_number_count = 1

for i in range(12):
    new_table = PoolTable(table_number_count)
    table_number_count += 1
    tables_array.append(new_table)
# MENU
def show_main_menu():

    for table in tables_array:
        status = ""
        if(table.open == False):
            status = "occupied"
        else:
            status = "available"

        print("Pool Table", table.table_number, status)

    user_selection = input("V. view, O. check out, I. check in, Q. quit \n")

    if user_selection.lower() == "o":
        check_out_table()

    if user_selection.lower() == "i":
        check_in_table()

    if user_selection.lower() == "v":
        view_tables()

def check_out_table():

    selected_table_number = input("Enter table number from list above: \n")

    selected_table_obj = tables_array[int(selected_table_number)-1]

    if selected_table_obj.open == False:
        print("Table {0} is occupied, select another table!".format(selected_table_number))
    else:
        print("************************")
        print("Table {0} is checked out!".format(selected_table_number))
        print("************************")

    start_datetime = datetime.now()

    selected_table_obj.open = False
    selected_table_obj.start_datetime = start_datetime

    show_main_menu()

def check_in_table():
    returning_table = input("Enter table number you  are returning\n")

    end_datetime = datetime.now()
    returned_table_obj = tables_array[int(returning_table) -1]
    returned_table_obj.end_datetime = end_datetime
    returned_table_obj.open = True
    print("************************")
    print("Table {0} is checked in!".format(returning_table))
    print("************************")
    show_main_menu()

def view_tables():

    print(tables_array)
    show_main_menu()

show_main_menu()

with open("11-22-2017.json", "w") as pool_table_data:
    json.dump(tables_array,pool_table_data)

with open("11-22-2017.json", "r") as pool_table_data:
    pool_table_info = json.load(pool_table_data)
    print(pool_table_info)
