import psycopg2
hostname = "localhost"
database = ""
user_db = ""
pwd = ""
port_id = 5432

def create_tables():
    try:
        conn = psycopg2.connect(host=hostname, dbname=database, user=user_db, password=pwd, port=port_id)
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        query1 = """CREATE TABLE IF NOT EXISTS elements(
                        order_id SERIAL,
                        product_name character varying(40) NOT NULL,
                        quantity integer,
                        price integer NOT NULL)"""
        
        cur.execute(query1)
        query2 = """CREATE TABLE IF NOT EXISTS orders(
                        order_id SERIAL NOT NULL,
                        amount_of_products integer,
                        order_date date NOT NULL,
                        order_price integer)"""
        cur.execute(query2)
        
        cur.execute("""
            SELECT EXISTS (
                SELECT 1
                FROM information_schema.tables 
                WHERE table_name = 'menu'
            )
        """)
        menu_exists = cur.fetchone()[0]

        if not menu_exists:
            cur.execute("""
                CREATE TABLE menu(
                    product_id SERIAL NOT NULL,
                    product_name character varying(40) NOT NULL,
                    price integer NOT NULL
                )
            """)

            add_pizza_script = """ INSERT INTO menu(product_name, price) VALUES(%s,%s)"""
            insert_values = {'Margherita':25,'Capriciosa':28,'Salami':26,'Parma':30,'Diavola':29,'Verona':28,'Hawaiana':28,'Napoletana':29,'Marinara':25,'Vegetariana':28,'Jalapeno':28}
            for key, value in insert_values.items():
                cur.execute(add_pizza_script,(key,value))

        conn.commit()

    except psycopg2.Error as e:
        print("Error:", e)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()