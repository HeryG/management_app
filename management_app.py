from tabels import create_tables,hostname,database,user_db,pwd,port_id
from raports import create_file1, create_file2
from customtkinter import *
import psycopg2
import psycopg2.extras
from datetime import datetime

def create_frame1():
    global frame1_scroll
    global menu_dict
    global widgets_list
    frame1 = CTkFrame(screen,width=450,height=550,corner_radius=50,border_width=4,border_color="black",fg_color='#F5F5F5')
    frame1.place(x=20,y=118)
    CTkLabel(frame1,text="MENU",font=("Century Gothic",40),text_color='black').place(x=160,y=20)
    frame1_scroll = CTkScrollableFrame(frame1,border_color="black", border_width=3, orientation="vertical", scrollbar_button_color="black",width=372,height=400,corner_radius=20,fg_color="#CED2D6")
    frame1_scroll.place(x=20,y=80)

    try:
        conn = psycopg2.connect(host=hostname, dbname=database, user=user_db, password=pwd, port=port_id)
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        query = "SELECT product_name, price FROM menu"

        cur.execute(query)
        rows_as_dict = cur.fetchall()

        menu_dict = {}
        for row in rows_as_dict:
            menu_dict[row['product_name']] = row['price']

    except psycopg2.Error as e:
        print("Error:", e)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    widgets_list = []
    for key, value in menu_dict.items():
        n = 35 - len(key) - 2
        dots = "." * n
        if len(key+dots)+2 <= 38:
            widget = CTkLabel(frame1_scroll,font=("Century Gothic",25,'bold'),fg_color="#CED2D6",text=f"{key+dots+str(value)}",text_color='black')
            widgets_list.append(widget)
            widget.pack(pady=10,expand=True)
        else:
            print("Error")

def create_frame2():
    global widgets_list2
    global entrys_list
    global frame2_scroll

    frame2 = CTkFrame(screen,width=450,height=550,corner_radius=50,border_width=4,border_color="black",fg_color='#F5F5F5')
    frame2.place(x=520,y=118)
    CTkLabel(frame2,text="QUANTITY",font=("Century Gothic",40),text_color='black').place(x=133,y=20)

    frame2_scroll = CTkScrollableFrame(frame2,border_color="black", border_width=3, orientation="vertical", scrollbar_button_color="black",width=372,height=400,corner_radius=20, fg_color="#CED2D6")
    frame2_scroll.place(x=20,y=80)

    row_number_label = 0 
    widgets_list2 = []
    for key, value in menu_dict.items():
        widget = CTkLabel(frame2_scroll,font=("Century Gothic",25,'bold'),text=key,text_color='black')
        widgets_list2.append(widget)
        widget.grid(row=row_number_label,column=0,padx=40,pady=8)
        row_number_label = row_number_label + 1

    row_number_entry = 0
    entrys_list = []
    for key, value in menu_dict.items():
        entry = CTkEntry(frame2_scroll,font=("Century Gothic",25,'bold'),width=60,fg_color='white',text_color='black',placeholder_text='0')
        entrys_list.append(entry)
        entry.grid(row=row_number_entry,column=1,padx=10)
        row_number_entry = row_number_entry + 1

def create_frame3():
    global tax_value_widget,total_value_widget,entry_paid_widget,change_value_widget
    global frame3_1_1,frame3_2_1,frame3_3,frame3_4_1
    
    frame3 = CTkFrame(screen,width=450,height=550,corner_radius=50,border_width=4,border_color="black",fg_color='#F5F5F5')
    frame3.place(x=1020,y=118)
    CTkLabel(frame3,text="BILL",font=("Century Gothic",40),text_color='black').place(x=190,y=20)

    frame3_1 = CTkFrame(frame3,width=370,height=50,corner_radius=50,border_width=3,border_color="black",fg_color="#CED2D6")
    frame3_1.place(x=40,y=90)
    CTkLabel(master=frame3_1,text="Total amount:",font=("Century Gothic",25,"bold"),text_color='black').place(x=25,y=10)
    frame3_1_1 = CTkFrame(frame3_1,width=160,height=35,border_color="white",fg_color="white",corner_radius=40)
    frame3_1_1.place(x=198,y=7)
    total_value_widget = CTkLabel(frame3_1_1,text=0,font=("Century Gothic",25,"bold"),text_color='black')
    total_value_widget.place(x=15,y=1)
    

    frame3_2 = CTkFrame(frame3,width=370,height=50,corner_radius=50,border_width=3,border_color="black",fg_color="#CED2D6")
    frame3_2.place(x=40,y=160)
    CTkLabel(master=frame3_2,text="Tax amount:",font=("Century Gothic",25,"bold"),text_color='black').place(x=25,y=10)
    frame3_2_1 = CTkFrame(frame3_2,width=160,height=35,border_color="white",fg_color="white",corner_radius=40)
    frame3_2_1.place(x=198,y=7)
    tax_value_widget = CTkLabel(frame3_2_1,text=0,font=("Century Gothic",25,"bold"),text_color='black')
    tax_value_widget.place(x=15,y=1)

    CTkFrame(frame3,width=450,height=4,corner_radius=50,border_width=3,border_color="black",fg_color="black").place(x=0,y=230)

    frame3_3 = CTkFrame(frame3,width=370,height=50,corner_radius=50,border_width=3,border_color="black",fg_color="#CED2D6")
    frame3_3.place(x=40,y=250)
    CTkLabel(master=frame3_3,text="Paid amount:",font=("Century Gothic",25,"bold"),text_color='black').place(x=25,y=10)
    entry_paid_widget = CTkEntry(frame3_3,font=("Century Gothic",25,'bold'),border_color="#CED2D6",width=160,bg_color="#CED2D6",corner_radius=40,text_color='black',fg_color='white',placeholder_text=0)
    entry_paid_widget.bind("<Return>", calculate_change)
    entry_paid_widget.place(x=198,y=7)

    frame3_4 = CTkFrame(frame3,width=370,height=50,corner_radius=50,border_width=3,border_color="black",fg_color="#CED2D6")
    frame3_4.place(x=40,y=320)
    CTkLabel(master=frame3_4,text="Change:",font=("Century Gothic",25,"bold"),text_color='black').place(x=25,y=10)
    frame3_4_1 = CTkFrame(frame3_4,width=160,height=35,border_color="white",fg_color="white",corner_radius=40)
    frame3_4_1.place(x=198,y=7)
    change_value_widget = CTkLabel(frame3_4_1,text=0,font=("Century Gothic",25,'bold'),text_color='black')
    change_value_widget.place(x=15,y=1)

    CTkFrame(frame3,width=450,height=4,corner_radius=50,border_width=3,border_color="black",fg_color="black").place(x=0,y=385)
    
    CTkLabel(master=frame3,text="""Generate \nRaport""",font=("Century Gothic",25,"bold"),text_color='black').place(x=30,y=435)

    CTkButton(frame3,text="""This \nDay""",command=lambda: generate_raport('day'),width=120,height=110,font=("Helvetica",18,"bold"),text_color="black",
              corner_radius=30,border_width=4,fg_color="#FF8A5C", border_color="black").place(x=170,y=412)
    CTkButton(frame3,text="""This \nMonth""",command=lambda: generate_raport('month'),width=120,height=110,font=("Helvetica",18,"bold"),text_color="black",
              corner_radius=30,border_width=4,fg_color="#D966FF", border_color="black").place(x=300,y=412)

def refresh_frame_scroll(widgets_list,frame_number):
    for widget in widgets_list:
        widget.destroy()

    widgets_list.clear()

    if frame_number == 1:
        for key, value in menu_dict.items():
            n = 35 - len(key) - 2
            dots = "." * n
            if len(key+dots)+2 <= 38:
                key = CTkLabel(frame1_scroll,font=("Century Gothic",25,'bold'),fg_color="#CED2D6",text=f"{key+dots+str(value)}",text_color='black')
                widgets_list.append(key)
                key.pack(pady=10,expand=True)
            else:
                print("Error")

    elif frame_number == 2:
        for entry in entrys_list:
            entry.destroy()
        entrys_list.clear()

        for i,(key, value) in enumerate(menu_dict.items()):
            widget = CTkLabel(frame2_scroll,font=("Century Gothic",25,'bold'),text=key,text_color='black')
            widgets_list2.append(widget)
            widget.grid(row=i,column=0,padx=40,pady=8)
            
            entry = CTkEntry(frame2_scroll,font=("Century Gothic",25,'bold'),width=60,placeholder_text='0',fg_color='white',text_color='black')
            entrys_list.append(entry)
            entry.grid(row=i,column=1,padx=10)
            

def add_position_window():
    global entry_name
    global entry_price
    screen2 = CTkToplevel()
    screen2.geometry("300x200+0+600")
    screen2.title("Add Position")
    screen2.resizable(False,False)
    screen2.configure(fg_color='#F5F5F5')

    frame2_1 = CTkFrame(screen2, width=270,height=170,border_width=3,border_color="black",fg_color='#CED2D6')
    frame2_1.place(x=15,y=15)
    CTkLabel(frame2_1,font=("Century Gothic",20,'bold'),text="Name",text_color='black').place(x=23,y=10)
    entry_name=CTkEntry(frame2_1,font=("Century Gothic",20,'bold'),width=150,placeholder_text="Margherita",border_color="black",fg_color='white',text_color='black')
    entry_name.place(x=103,y=10)
    CTkLabel(frame2_1,font=("Century Gothic",20,'bold'),text="Price",text_color='black').place(x=53,y=57)
    entry_price=CTkEntry(frame2_1,font=("Century Gothic",20,'bold'),width=75,placeholder_text="0",border_color="black",fg_color='white',text_color='black')
    entry_price.place(x=123,y=57)
    CTkButton(frame2_1,text="Add",command=add_position,width=130,height=25,font=("Helvetica",18,"bold"),text_color="black",
              corner_radius=30,border_width=2,fg_color="#6EFF97", border_color="black").place(x=70,y=110)
    
def remove_position_window():
    global entry_remove
    screen3 = CTkToplevel()
    screen3.geometry("300x200+0+600")
    screen3.title("Remove Position")
    screen3.resizable(False,False)
    screen3.configure(fg_color = '#F5F5F5')

    frame3_1 = CTkFrame(screen3, width=270,height=170,border_width=3,border_color="black",fg_color='#CED2D6')
    frame3_1.place(x=15,y=15)
    CTkLabel(frame3_1,font=("Century Gothic",20,'bold'),text="Position name to remove",text_color='black').place(x=14,y=15)
    entry_remove=CTkEntry(frame3_1,font=("Century Gothic",20,'bold'),width=150,placeholder_text="Margherita",border_color="black",fg_color='white',text_color='black')
    entry_remove.place(x=58,y=57)
    CTkButton(frame3_1,text="Remove",command=remove_position,width=130,height=25,font=("Helvetica",18,"bold"),text_color="black",
              corner_radius=30,border_width=2,fg_color="#FF5E63", border_color="black").place(x=70,y=110) 
    
def add_position():
    name = entry_name.get()
    price = int(entry_price.get())
    menu_dict[name]=price
    try:
        conn = psycopg2.connect(host=hostname, dbname=database, user=user_db, password=pwd, port=port_id)
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = """INSERT INTO menu(product_name,price) VALUES(%s,%s)"""
        insert_values = (name,price)
        cur.execute(query,insert_values)
        conn.commit()
        
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()    
    
    refresh_frame_scroll(widgets_list,1)
    refresh_frame_scroll(widgets_list2,2)

def remove_position():
    to_remove = entry_remove.get()
    del menu_dict[to_remove]

    try:
        conn = psycopg2.connect(host=hostname, dbname=database, user=user_db, password=pwd, port=port_id)
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = """DELETE FROM menu WHERE product_name = %s"""
        insert_values = to_remove
        cur.execute(query,(insert_values,))
        conn.commit()
        
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    
    refresh_frame_scroll(widgets_list,1)
    refresh_frame_scroll(widgets_list2,2)

def total_value_calculate():
    global quantity_sum
    sum_value = 0
    i = 0
    quantity_sum = 0
    for key, value in menu_dict.items():
        quantity = entrys_list[i]
        i=i+1
        quantity = quantity.get()
        if quantity:
            quantity = int(quantity)
        else:
            quantity = 0
        sum_value = sum_value + (quantity * int(value))
        quantity_sum = quantity_sum + quantity
    return sum_value

def calculate_change(_):
    change_value_widget.destroy()
    change_value = float(entry_paid_widget.get()) - total_value_calculate()
    widget_reset('change',change_value)

def calculate_bill():
    tax_value_widget.destroy()
    total_value_widget.destroy()
    sum_value = total_value_calculate()
    tax_value = sum_value * 0.23
    widget_reset('total',sum_value)
    widget_reset('tax',tax_value)
    save_to_database()

def widget_reset(widget,value):
    if widget == 'total':
        global total_value_widget
        total_value_widget = CTkLabel(frame3_1_1,text=value,font=("Century Gothic",25,"bold"),text_color='black')
        total_value_widget.place(x=15,y=1)
    elif widget == 'tax':
        global tax_value_widget
        tax_value_widget = CTkLabel(frame3_2_1,text=round(value,2),font=("Century Gothic",25,"bold"),text_color='black')
        tax_value_widget.place(x=15,y=1)
    elif widget == 'change':
        global change_value_widget
        change_value_widget = CTkLabel(frame3_4_1,text=round(value,2),font=("Century Gothic",25,'bold'),text_color='black')
        change_value_widget.place(x=15,y=1)
    elif widget == 'paid':
        if value == 0:
            global entry_paid_widget
            entry_paid_widget = CTkEntry(frame3_3,font=("Century Gothic",25,'bold'),border_color="#CED2D6",width=160,bg_color="#CED2D6",corner_radius=40,placeholder_text=0,fg_color='white',text_color='black')
            entry_paid_widget.bind("<Return>", calculate_change)
            entry_paid_widget.place(x=198,y=7)

def reset():
    for entry in entrys_list:
        entry.destroy()

    entrys_list.clear()

    row_number_entry = 0
    for key, value in menu_dict.items():
        entry = CTkEntry(frame2_scroll,font=("Century Gothic",25,'bold'),width=60,placeholder_text='0',fg_color='white',text_color='black')
        entrys_list.append(entry)
        entry.grid(row=row_number_entry,column=1,padx=10)
        row_number_entry = row_number_entry + 1
    
    tax_value_widget.destroy()
    widget_reset('tax',0)
    total_value_widget.destroy()
    widget_reset('total',0)
    entry_paid_widget.destroy()
    widget_reset('paid',0)
    change_value_widget.destroy()
    widget_reset('change',0)

def save_to_database():
    try:
        conn = psycopg2.connect(host=hostname, dbname=database, user=user_db, password=pwd, port=port_id)
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        add_script = """INSERT INTO orders(order_price,amount_of_products,order_date) VALUES(%s,%s,%s)"""
        order_price = total_value_calculate()
        amount_of_products = quantity_sum
        order_date = datetime.now()

        insert_values = (order_price,amount_of_products,order_date)
        cur.execute(add_script,insert_values)

        get_order_script = """SELECT MAX(order_id) FROM orders"""
        cur.execute(get_order_script)
        for row in cur:
            order_id = row[0]

        add_script_2 = """INSERT INTO elements(order_id,product_name,quantity,price) VALUES(%s,%s,%s,%s)"""

        entry_number = 0
        for key, value in menu_dict.items():
            quantity = entrys_list[entry_number]
            entry_number=entry_number+1
            quantity = quantity.get()
            if quantity:
                quantity = int(quantity)
                price = quantity * value
                insert_values = (order_id,key,quantity,price)
                cur.execute(add_script_2,insert_values)
            else:
                continue
        
        conn.commit()

    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

def generate_raport(time):
    if time == 'day':
        create_file1(menu_dict)
    elif time == 'month':
        create_file2(menu_dict)
    else:
        None

def main_screen():
    global screen
    screen = CTk()
    screen.geometry("1520x780+200+100")
    screen.title("MANAGMENT APPLICATION")
    screen.resizable(False,False)
    screen.configure(fg_color='#F5F5F5')
    CTkLabel(screen,text="BILL MANAGMENT",bg_color="#385F87",fg_color="#385F87",font=("Century Gothic",80),text_color='black',width=1520,height=8).pack()

    create_frame1()
    CTkButton(screen,text="Add Position",command=add_position_window,width=220,height=45,font=("Helvetica",18,"bold"),text_color="black",
              corner_radius=30,border_width=4,fg_color="#6EFF97", border_color="black").place(x=20,y=675)
    CTkButton(screen,text="Remove Position",command=remove_position_window,width=220,height=45,font=("Helvetica",18,"bold"),text_color="black",
              corner_radius=30,border_width=4,fg_color="#FF5E63", border_color="black").place(x=250,y=675)
    
    create_frame2()
    CTkButton(screen,text="Calculate",command=calculate_bill,width=220,height=45,font=("Helvetica",18,"bold"),text_color="black",
              corner_radius=30,border_width=4,fg_color="#6EFF97", border_color="black").place(x=520,y=675)
    CTkButton(screen,text="Reset",command=reset,width=220,height=45,font=("Helvetica",18,"bold"),text_color="black",
              corner_radius=30,border_width=4,fg_color="#FF5E63", border_color="black").place(x=750,y=675)
    
    create_frame3()

    screen.mainloop()

if __name__ == "__main__":
    create_tables()
    main_screen()
