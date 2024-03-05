# management_app
This application is integrated with a PostgreSQL database and designed for restaurant management, allowing users to handle bills, add/remove menu items, calculate the total amount due, and generate daily and monthly reports

### README

#### Features:

1. **Bill Management:**
   - The application allows users to create bills for transactions.
   - It calculates the total amount, tax amount, and change for each bill.

2. **Adding/Removing Positions:**
   - Users can add new positions (menu items) with their respective prices.
   - Existing positions can be removed from the menu.

3. **Calculating Bills:**
   - The application calculates the total bill amount including taxes.
   - It also calculates the change to be returned to the customer.

4. **Generating Reports:**
   - Daily and monthly reports can be generated to analyze sales data.
   - Reports include information on the quantity sold for each product, total earnings, and tax amounts.

5. **Database Integration:**
   - The application integrates with a PostgreSQL database to store menu items, orders, and elements.
   - Tables are created to store menu items, orders, and order details.

#### Files:

1. **management_app.py:**  
   - Contains the main code for the management application.
   - Implements functionalities related to bill management, adding/removing positions, calculating bills, and generating reports.

2. **tables.py:**
   - Contains code to create tables in the PostgreSQL database for storing menu items, orders, and order details.

3. **raports.py:**
   - Contains functions to generate daily and monthly reports.
   - Integrates with the PostgreSQL database to fetch relevant data for generating reports.

#### How to Use:

1. **Setup Database:**
   - Ensure that PostgreSQL is installed and running.
   - Create new database.
   - Modify the database connection parameters:
       (`hostname`, `database`, `user_db`, `pwd`, `port_id`) in `tables.py`

     to match your PostgreSQL setup.

2. **Run the Application:**
   - Execute `management_app.py` to launch the management application.

3. **Interact with the Interface:**
   - Use the graphical interface, the buttons and input fields to perform desired actions such as adding positions, calculating bills, and generating reports.

4. **View Reports:**
   - After generating reports, the files will be saved with filenames indicating the date and type of report (daily or monthly).
   - Reports can be viewed using any text editor or by opening the file directly.

#### Dependencies:

- Python 3.11
- PostgreSQL
- tkinter (for GUI)
- psycopg2 (for PostgreSQL database interaction)

#### Notes:

- Ensure that all dependencies are installed before running the application.
- Modify database connection parameters as needed to match your PostgreSQL setup.
- For any issues or errors, refer to the error messages printed in the console or logs.
