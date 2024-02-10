import mysql.connector as m
import tkinter as tk

def connect_db():
    db = m.connect(
        host='localhost',
        user='root',
        password='pass@123',
        database='hotel'
    )
    return db

def select_db():
    db = connect_db()
    cur = db.cursor()
    cur.execute('SELECT * FROM menu')
    results = cur.fetchall()
    return results

def update_db(name, price):
    if name != '' and price != '':
        db = connect_db()
        cur = db.cursor()
        print(name, price)
        cur.execute('UPDATE menu SET price={} where name=\'{}\''.format(int(price), name))
        db.commit()

def insert_db(name,price):
    if name != '' and price != '':
        db=connect_db()
        cur=db.cursor()
        print(name,price)
        cur.execute("INSERT into menu (name,price) values(\'{}\',{})".format(name, int(price)))
    
        db.commit()
def delete_db(name,price):
      if name != '' and price != '':
        db=connect_db()
        cur=db.cursor()
        print(name,price)
       
        cur.execute("Delete from menu where name=\'{}\'".format(name,int(price)))
        db.commit()

class RestaurantApp:
    def _init_(self, master):
        self.master = master
        master.title("Restaurant Menu")

        self.frame1()

    def destroy(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def frame1(self):
        self.destroy()

       
        border_frame = tk.Frame(self.master, borderwidth=2, relief="solid")
        border_frame.pack(side='left', fill='y', pady=15, padx=15)

        label = tk.Label(border_frame, text='Welcome to Kitchen King Restaurant', font=('Arial', 24))
        label.pack(pady=15)

        # Show Menu button
        show_menu_button = tk.Button(border_frame, text='Show Menu', command=self.frame2, font=('Arial', 18),bg='pink')
        show_menu_button.pack(pady=15,  padx=10)

        # Update button
        update_button = tk.Button(border_frame, text='Update', command=self.update_menu,bg='blue', font=('Arial', 18))
        update_button.pack(pady=15,  padx=10)

        insert_button=tk.Button(border_frame,text='Insert',command=self.insert_menu,bg='green', font=('Arial', 18))
        insert_button.pack(pady=15,padx=10)

        delete_button=tk.Button(border_frame,text='Delete',command=self.delete_menu,bg='yellow', font=('Arial', 18))
        delete_button.pack(pady=15,padx=10)

    def frame2(self):
        self.destroy()

      
        header_frame = tk.Frame(self.master, borderwidth=2, relief="solid")
        header_frame.pack(pady=15)

       
        tk.Label(header_frame, text='Name', font=('Arial', 18)).grid(row=0, column=0, padx=15)
        
        tk.Label(header_frame, text='Price', font=('Arial', 18)).grid(row=0, column=2, padx=15)

       
        data_frame = tk.Frame(self.master, borderwidth=2, relief="solid")
        data_frame.pack(pady=15)

        res = select_db()
        for i in range(len(res)):
          
            tk.Label(data_frame, text=res[i][0], font=('Arial', 14)).grid(row=i, column=0, sticky='w')
            tk.Label(data_frame, text=res[i][1], font=('Arial', 14)).grid(row=i, column=1, sticky='w')

        # Adding a Back button
        back_button = tk.Button(data_frame, text='Back', command=self.frame1)
        back_button.grid(row=i + 1, column=0, columnspan=3, pady=15)

    def update_menu(self):
        self.destroy()
      
        frame = tk.Frame(self.master)
        frame.pack(padx=15, pady=15)

        # Dish name label
        nameL = tk.Label(frame, text='Enter the name of the dish', font=('Arial', 14))
        nameL.grid(row=0, column=0)
        
        #Entry field
        nameE = tk.Entry(frame, font=('Arial', 14))
        nameE.grid(row=0, column=1)

        # Dish price label
        priceL = tk.Label(frame, text='Enter the new price of the dish', font=('Arial', 14))
        priceL.grid(row=1, column=0)
        
        #Entry field
        priceE = tk.Entry(frame, font=('Arial', 14))
        priceE.grid(row=1, column=1)

        # Button
  
        submit = tk.Button(frame, text="Make changes", font=('Arial', 14),bg='grey', command=lambda: update_db(nameE.get(), priceE.get()))
        submit.grid(row=2, columnspan=2)

        back_button = tk.Button(frame, text='Back', command=self.frame1)
        back_button.grid(row=3, column=0, columnspan=2, pady=15)

    def insert_menu(self):
            self.destroy()

            frame1=tk.Frame(self.master)
            frame1.pack(padx=15,pady=15)

            # Dish name label
            nameLa = tk.Label(frame1, text='Enter the name of the new dish', font=('Arial', 14))
            nameLa.grid(row=0, column=0)
        
        #Entry field
            nameEa = tk.Entry(frame1, font=('Arial', 14))
            nameEa.grid(row=0, column=1)

        # Dish price label
            priceLa = tk.Label(frame1, text='Enter the new price of the dish', font=('Arial', 14))
            priceLa.grid(row=1, column=0)
        
        #Entry field
            priceEa = tk.Entry(frame1, font=('Arial', 14))
            priceEa.grid(row=1, column=1)

            submit1= tk.Button(frame1, text="Make changes", font=('Arial', 14),bg='grey', command=lambda: insert_db(nameEa.get(), priceEa.get()))
            submit1.grid(row=2, columnspan=2)

            back_button = tk.Button(frame1, text='Back', command=self.frame1)
            back_button.grid(row=3, column=0, columnspan=2, pady=15)
    def delete_menu(self):
            self.destroy()

            frame1=tk.Frame(self.master)
            frame1.pack(padx=15,pady=15)

            # Dish name label
            nameLa = tk.Label(frame1, text='Enter the name of the dish you want to delete', font=('Arial', 14))
            nameLa.grid(row=0, column=0)
        
        #Entry field
            nameEa = tk.Entry(frame1, font=('Arial', 14))
            nameEa.grid(row=0, column=1)

        # Dish price label
            priceLa = tk.Label(frame1, text='Enter the new price of the dish', font=('Arial', 14))
            priceLa.grid(row=1, column=0)
        
        #Entry field
            priceEa = tk.Entry(frame1, font=('Arial', 14))
            priceEa.grid(row=1, column=1)

            submit1= tk.Button(frame1, text="Make changes", font=('Arial', 14),bg='grey', command=lambda: delete_db(nameEa.get(), priceEa.get()))
            submit1.grid(row=2, columnspan=2)

            back_button = tk.Button(frame1, text='Back', command=self.frame1)
            back_button.grid(row=3, column=0, columnspan=2, pady=15)
       

root = tk.Tk()
app = RestaurantApp(root)
root.mainloop()