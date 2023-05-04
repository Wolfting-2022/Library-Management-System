#!/usr/bin/python3

# import modules
import sys
import psycopg2

# Menu display function
def show_menu():
    print ("Menu options:")
    print ("1.Display all books, sorted by title:")
    print ("2.Display all book copies for a given book:")
    print ("3.Display all currrent library loans:")
    print ("q.Quit")
    return

# Menu selection function
def get_menu_option(prompt):
    selection = input(prompt)
    return selection

# Menu get_field_value function
def get_field_value(prompt):
    selection = input(prompt)
    return selection  

# Dispaly all books function
def query_books():
    sql_query = "SELECT title, rental_days FROM book_detail ORDER BY title"
    cursor.execute(sql_query)
    record = cursor.fetchone()
    while record:
        print(*record)
        record = cursor.fetchone()
    return

# Display all book copies for a given book function
def query_copies_by_title(book_title):    
    book_title = input(“Enter member last name: “)
    sql_data(book_title,)
    sql_query = "SELECT acquisition_date FROM book_detail JOIN book_copy ON book_detail.isbn = book_copy.isbn WHERE title=%s "
    cursor.execute(sql_query,sql_data)
    record = cursor.fetchone()
    while record:
        print(*record)
        record = cursor.fetchone()
    return						
--------------------------------------------------------------------
def query_copies_by_title(book_title):
    sql_data(book_title,)
    sql_query = "SELECT acquisition_date FROM book_detail JOIN book_copy ON book_detail.isbn = book_copy.isbn WHERE title='1984' "
    cursor.execute(sql_query,'1984')
    record = cursor.fetchone()
    while record:
        print(*record)
        record = cursor.fetchone()
    return
--------------------------------------------------------------------
# Dispaly all current library loans function
def query_loans():
    sql_query = "SELECT member.member_id, last_name, isbn, loan_date, return_date FROM book_copy JOIN loan ON loan.copy_id = book_copy.copy_id JOIN member ON member.member_id = loan.member_id WHERE return_date IS NULL ORDER BY member_id ASC"
    cursor.execute(sql_query)
    record = cursor.fetchone()
    while record:
        print(*record)
        record = cursor.fetchone() 
   return

# Main body
def main():

    # Call menu display function                                                                                                       
    show_menu()
    # Prompt users to enter selection 
    user_selection = get_menu_option ("Enter menu option:").upper()
    while user_selection !="Q":

        # Displaying all books
        if user_selection == "1":
            #Call get_field_value function
            query_books()

        # Displaying member first name
        elif user_selection == "2":
            #Call get_field_value function
            title=get_field_value("Please input a book_title:")    
            #Call all book copies for a given book function
            query_copies_by_title(title)

           # prompt for user input
member_name = input(“Enter member last name: “)
# store value
sql_data(member_name,) # trailing comma with single data item
# form query
sql_query = “SELECT * FROM member WHERE last_name=%s”
# execute query
cursor.execute(sql_query, sql_data)

            sql_query = "SELECT acquisition_date FROM book_detail JOIN book_copy ON book_detail.isbn = book_copy.isbn WHERE title=title "
            cursor.execute(sql_query,title)
            record = cursor.fetchone()
            while record:
                print(*record)
                record = cursor.fetchone()

        # Displaying return date information
        elif user_selection =="3":
            #Call all current library loans function
            query_loans()

        # Display wrong menu option
        else:
            print ("Invalid menu option")

        # Call menu display function   
        show_menu()
        # Prompt users to enter selection 
        user_selection = get_menu_option("Enter menu option: ").upper()

    # Program ends with closing message
    print ("Thanks and wish to use again!")

# Database connection
try:
    connection=psycopg2.connect(database='lib_chen0869', user='dbadmin')
except psycopg2.DatabaseError:
    print("Error: Connection no established.")
    sys.exit(1) 
print("Database connection established")

# setup the cursor
cursor = connection.cursor()

# Main program
if __name__ == "__main__":
    main()

# closed the cursor and connection
cursor.close()
connection.close()
-------------------------------------------------------------------------------------------
SELECT member.member_id, last_name, isbn, loan_date, return_date				
  FROM book_copy
  JOIN loan ON loan.copy_id = book_copy.copy_id
  JOIN member ON member.member_id = loan.member_id
  WHERE return_date IS NULL
  ORDER BY member_id ASC
------------------------------------------------------------------------------------------
