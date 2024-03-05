import psycopg2.extras
from tabels import hostname,database,user_db,pwd,port_id
from datetime import datetime
import os

date_time = datetime.now()
formatted_datetime1 = date_time.strftime("%Y-%m-%d")
formatted_datetime2 = date_time.strftime("%Y-%m-%d %H:%M")
file_name1 = f"{formatted_datetime1}-daily_raport.txt"
file_name2 = f"{formatted_datetime1}-monthly_raport.txt"

def create_file1(menu):
    file_name1 = f"{formatted_datetime1}-daily_raport.txt"
    with open(file_name1,'w') as file:
        file.write(f"""DAILY RAPORT {formatted_datetime2}\n--------------------------------------\n(Product) : (Quantity Sold)\n--------------------------------------\n""")
        
        try:
            conn = psycopg2.connect(host=hostname, dbname=database, user=user_db, password=pwd, port=port_id)
            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            quantity_script = """SELECT SUM(quantity) FROM elements as e
                                    INNER JOIN orders as o ON e.order_id = o.order_id
                                    WHERE e.product_name=%s AND NOW()::DATE = o.order_date"""

            for key,value in menu.items():
                cur.execute(quantity_script,(key,))
                for row in cur:
                    quantity = row[0]
                if quantity == None:
                    file.write(f"{key} : 0\n")
                else:
                    file.write(f"{key} : {quantity}\n")

            sum_quantity_script = """SELECT SUM(amount_of_products) FROM orders WHERE NOW()::DATE = order_date"""
            cur.execute(sum_quantity_script)
            for row in cur:
                sum_quantity = row[0]
            
            total_earnings_script = "SELECT SUM(order_price) FROM orders WHERE NOW()::DATE = order_date"
            cur.execute(total_earnings_script)
            for row in cur:
                total_earnings = row[0]
            file.write(f"""--------------------------------------\nTotal quantity of products: {sum_quantity} pieces\nTotal earnings: {total_earnings} €\nTax amount: {round((total_earnings*0.23),2)} €\n--------------------------------------""")
            
            conn.commit()
        except psycopg2.Error as e:
            print("Error:", e)

        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()
    file.close()
    if os.path.exists(file_name1):
        os.startfile(file_name1)
    else:
        print("Error")



def create_file2(menu):
    with open(file_name2,'w') as file:
        file.write(f"""MONTHLY RAPORT {formatted_datetime2}\n--------------------------------------\n(Product) : (Quantity Sold)\n--------------------------------------\n""")
        
        try:
            conn = psycopg2.connect(host=hostname, dbname=database, user=user_db, password=pwd, port=port_id)
            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            current_date = datetime.now()
            first_day_of_month = datetime(current_date.year, current_date.month, 1)

            quantity_script = """SELECT SUM(quantity) FROM elements as e
                                    INNER JOIN orders as o ON e.order_id = o.order_id
                                    WHERE e.product_name=%s AND o.order_date BETWEEN %s AND NOW()::DATE"""

            for key,value in menu.items():
                cur.execute(quantity_script,(key,first_day_of_month))
                for row in cur:
                    quantity = row[0]
                if quantity == None:
                    file.write(f"{key} : 0\n")
                else:
                    file.write(f"{key} : {quantity}\n")

            sum_quantity_script = """SELECT SUM(amount_of_products) FROM orders WHERE order_date BETWEEN %s AND NOW()::DATE"""
            cur.execute(sum_quantity_script,(first_day_of_month,))
            for row in cur:
                sum_quantity = row[0]
            
            total_earnings_script = "SELECT SUM(order_price) FROM orders WHERE order_date BETWEEN %s AND NOW()::DATE"
            cur.execute(total_earnings_script,(first_day_of_month,))
            for row in cur:
                total_earnings = row[0]
            file.write(f"""--------------------------------------\nTotal quantity of products: {sum_quantity} pieces\nTotal earnings: {total_earnings} €\nTax amount: {round((total_earnings*0.23),2)} €\n--------------------------------------""")

        except psycopg2.Error as e:
            print("Error:", e)

        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()
    file.close()
    if os.path.exists(file_name2):
        os.startfile(file_name2)
    else:
        print("Error")

    
