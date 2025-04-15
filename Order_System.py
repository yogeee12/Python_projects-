import mysql.connector as sqLtor
import pandas as pd
from datetime import date
sql = sqLtor.connect(host="localhost", user="root", password="Your_Password")

class business:
    def __init__(self) -> None:
        self.todays_date = date.today()
        self.cursor = sql.cursor()
        self.cursor.execute("SHOW DATABASES")
        self.existing_database =[db[0] for db in self.cursor.fetchall()]
        self.DataBase = "menu"
        self.count_number = 0
        if self.DataBase in self.existing_database:
            self.cursor.execute(f"use {self.DataBase}")
        else:
            create_ask = input(f"DataBase {self.DataBase} not exist \nWant to create new DataBase (Yes/No) : ").capitalize()
            if create_ask == "Yes":
                self.cursor.execute(f"create database {self.DataBase}")
                self.cursor.execute(f"use {self.DataBase}")
                sql.commit()
                print(f"DataBase created Successfully....")
                business.New_Table(self)
            else:
                exit()

    def fetch_tables(self):
        self.cursor.execute("show tables")
        table_count = self.cursor.fetchall()
        if not table_count:
            print("No Table Exist.\nEmpty!")
            business.New_Table(self)
        else:
            self.cursor.execute("show tables")
            self.db_tables = list([table[0] for table in self.cursor.fetchall()])
            self.cursor.execute(f"select * from table_info")
            table=self.cursor.fetchall()
            col_name = [col[0] for col in self.cursor.description]
            table_dataframe = pd.DataFrame(table, columns=col_name)
            print(table_dataframe)
    
    def New_Table(self):
        create_ask = input("create New Table (Yes/No) : ").capitalize()
        if create_ask == "Yes":
            self.new_table_name = input("Enter New Table Name : ")
            if self.new_table_name not in self.db_tables:
                self.cursor.execute(f'''create table {self.new_table_name}(
                    S_No int primary key auto_increment,
                    Item varchar(100) unique key,
                    Price float)''') 
                sql.commit()
                self.cursor.execute('''create table table_info(
                    Table_name varchar(100),
                    Date_created date,
                    Date_updated date
                )''')
                sql.commit()
                self.cursor.execute(f'''insert into table_info(Table_name,date_created,date_updated) values 
                ('{self.new_table_name}','{self.todays_date}','{self.todays_date}')''')
                sql.commit()   
                print(f"New Table {self.new_table_name} created Successfully...")
                return  business.insertrow(self,self.new_table_name)
            else: 
                print(f"Table {self.new_table_name} already exist!\nTry Again")
                self.New_Table()

    def update_table_date(self,table_name):
        self.cursor.execute(f'''update  table_info set date_updated = '{self.todays_date}' 
        where table_name = '{table_name}' ''')
        sql.commit()

    def insertrow(self,table_name):
        row_number = int(input("How many items you want to insert : "))
        for i in range(row_number): 
            print("Row Number = ",self.count_number+1)
            item_name = input("Enter Item Name : ").capitalize()
            item_price = int(input(f"Enter {item_name} Price : "))
            self.cursor.execute(f"insert into {table_name}(item, price) values ('{item_name}',{item_price})")
            sql.commit()
            self.count_number+=1
        ask = input(f"Want to insert more rows in Table {table_name}? (Yes/No) : ").capitalize()
        if ask == 'Yes':
            self.insertrow(table_name)
        else:
            print( f"{self.count_number} Rows inserted in {table_name} successfully....")
        show_data = business.fetch_data(self,table_name)
        business.update_table_date(self,table_name)
        print(show_data)

    def fetch_data(self,table_name):
        self.cursor.execute(f"select * from {table_name}")
        table_data = self.cursor.fetchall()
        col_name = [col[0] for col in self.cursor.description]
        self.dataframe = pd.DataFrame(table_data, columns=col_name)
        return self.dataframe

    def select_table(self):
        business.fetch_tables(self)
        self.Table_name = input("Which Table You Want To Continue With : ")
        if self.Table_name in self.db_tables:
            self.cursor.execute(f"select * from {self.Table_name}")
            self.count = self.cursor.fetchall()
            if not self.count:
                print("Table is empty")
                ask_row = input("Do you want to insert row (Yes/No): ").capitalize()
                if ask_row == "Yes":
                    business.insertrow(self,self.Table_name)
            else: 
                _ = self.cursor.fetchall()
                show_data = business.fetch_data(self,self.Table_name)
                print(show_data)
        else:
            print(f"Sorry Table Not exist in {self.DataBase}")
            return self.select_table()

    def delete_row(self):
            del_item = input("Enter Item Name To Delete : ").capitalize()
            if del_item in self.item_list:
                self.cursor.execute(f"delete from {self.Table_name} where item = '{del_item}'")
                sql.commit()
            else:
                print(f"Item '{del_item}' Not Present in {self.Table_name}. Try Again!")
                self.delete_row()
            print("Item Deleted Successfully....")
            business.update_table_date(self,self.Table_name)
            return business.fetch_data(self,self.Table_name)
            
    def update_table(self):
        business.select_table(self)
        print("Do you want to update existing table or Insret new row ?")
        print("To Update Existing Table Type : Update\nTo Insert New Row Type : Insert\nTo delete Item Type : Delete")
        ask = input("Type : ").capitalize()
        self.item_list = list(self.dataframe['Item'])

        #user want to insert new row
        if ask == "Insert":
            business.insertrow(self,self.Table_name)
        #if user want to update new data
        elif ask == "Update":
            no_of_upd = int(input("Enter Number How Many Item you Want To Update : "))
            self.count_number = 0
            for i in range(no_of_upd):
                upd_item = input("Enter Item Name To Update : ").capitalize()
                print(f"Updating Item {upd_item} = ",self.count_number+1)
                if upd_item in self.item_list:
                    upd_type = input(f"To Update Item Name (Type): Name\nTo Update Item Price (Type): Price\nType : ").capitalize()
                    if upd_type == "Name":
                        new_name = input("Enter New Item Name : ").capitalize()
                        self.cursor.execute(f"update {self.Table_name} set item = '{new_name}' where item = '{upd_item}'")
                        sql.commit()
                    elif upd_type == "Price":
                        item_price = int(input(f"Enter {upd_item} New Price : "))
                        self.cursor.execute(f"update {self.Table_name} set price = {item_price} where item = '{upd_item}'")
                        sql.commit()
                    else:
                        print("Somthing went wrong look like you miss spell 'Name' or 'Price'.")
                    self.count_number += 1
                else:
                    print(f"Item '{upd_item}' Not Present in {self.Table_name}. Try Again!")
            print(f"{self.count_number} Items Updated Successfully....")
            business.update_table_date(self,self.Table_name)
            return business.fetch_data(self,self.Table_name)
        #If user want To delete item from table
        elif ask == "Delete":
            no_of_del = int(input("Enter Number How Many Item You Want To Delete : "))
            for i in range (no_of_del):
                business.delete_row(self)
        # If user input wrong string !
        elif ask == "" or (ask != "Insert" and ask != "Update" or ask != "Delete"):
            print("Somthing Went Wrong Try Again !")
            self.update_table()

    def delete_table(self):
        self.cursor.execute("show tables")
        table_count = self.cursor.fetchall()
        if not table_count:
            print("No Table Exist!")
            exit()
        else:
            if self.count_number == 0:
                business.fetch_tables(self)

            table_name = input("Which Table You Want To Delete : ")
            if table_name in self.db_tables:
                priview = input(f"Do you want to preview table {table_name} before deletion (Yes/No): ").capitalize()
                if priview == "Yes":
                    print(business.fetch_data(self,table_name))
                    confirmation = input("Are You Sure, You Want to Delete Table (Yes/No): ").capitalize()
                    if confirmation == "Yes":
                        self.cursor.execute(f"drop table {table_name}")
                        sql.commit()
                        self.cursor.execute(f"delete from table_info where table_name = '{table_name}'")
                        sql.commit()
                        print(f"{table_name} Deleted successfully....")
                    else:
                        print("No Table Deleted.")
                else:
                    self.cursor.execute(f"drop table {table_name}")
                    sql.commit()
                    self.cursor.execute(f"delete from table_info where table_name = '{table_name}'")
                    sql.commit()
                    print(f"{table_name} Deleted successfully....")
            else:
                print(f"Table {table_name} not exist!")
                self.count_number+=1
                self.delete_table(self)


if __name__ == "__main__":
    B_obj=business()
    function_map = {
    "Show Tables" : B_obj.fetch_tables,
    "Show Data": B_obj.select_table,
    "Update": B_obj.update_table,
    "New Table": B_obj.New_Table,
    "Delete Table": B_obj.delete_table,
    }
    fun_list = list(function_map.keys())
    features={
        "Operations": [ "Show Tables","Show Table Data", "Update Table", "create New Table", "Delete Table"],
        "Type" : fun_list,
    }
    features_df = pd.DataFrame(features)
    features_df.index = range(1,len(features_df)+1)
    print(features_df)
    ask = input("What You Want To Do (Type): ").title()
    if ask in fun_list:
        function_map[ask]()
    else:
        print("invalid Option!")

    sql.close()