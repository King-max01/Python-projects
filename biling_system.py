import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from pathlib import Path
import random
import os



try:
    import win32print
    WINDOWS_PRINTING_AVAILABLE = True
except ImportError:
    WINDOWS_PRINTING_AVAILABLE = False



APP_NAME = "LE DOC RETAIL POS"
CURRENCY = "UGX"

RECEIPT_FOLDER = Path("receipts")
RECEIPT_FOLDER.mkdir(exist_ok=True)


# TAX RATES

TAX_RATES = {
    "Groceries": 5,
    "Beverages": 10,
    "Medical": 5,
    "Personal Care": 5,
    "Household": 5,
    "Electronics": 10,
    "Stationery": 5,
    "Bakery": 5,
    "Baby Products": 5,
    "Other": 5
}


# PRODUCTS - 100+


PRODUCTS = {

    "Groceries": {
        "Rice 1kg": 4500,
        "Rice 5kg": 21000,
        "Rice 10kg": 40000,
        "Wheat Flour 1kg": 5000,
        "Wheat Flour 2kg": 9500,
        "Maize Flour 1kg": 3500,
        "Maize Flour 2kg": 6500,
        "Sugar 1kg": 4500,
        "Sugar 2kg": 8500,
        "Sugar 5kg": 20000,
        "Cooking Oil 1L": 7000,
        "Cooking Oil 2L": 13500,
        "Cooking Oil 5L": 32000,
        "Salt 500g": 2000,
        "Salt 1kg": 3500,
        "Beans 1kg": 5000,
        "Beans 2kg": 9500,
        "Peas 1kg": 5500,
        "Lentils 1kg": 6000,
        "Spaghetti 500g": 5000,
        "Macaroni 500g": 5000,
        "Maggi Pack": 2500,
        "Tea Leaves 250g": 7000,
        "Tea Leaves 500g": 13000,
        "Coffee 250g": 9000,
        "Coffee 500g": 17000,
        "Peanut Butter": 8000,
        "Tomato Sauce": 7000,
        "Mayonnaise": 9000,
        "Tomatoes 1kg": 4000,
        "Onions 1kg": 3500,
        "Potatoes 1kg": 3000
    },

    "Beverages": {
        "Coca Cola 500ml": 2500,
        "Coca Cola 1.5L": 4500,
        "Fanta 500ml": 2500,
        "Fanta 1.5L": 4500,
        "Sprite 500ml": 2500,
        "Sprite 1.5L": 4500,
        "Pepsi 500ml": 2500,
        "Pepsi 1.5L": 4500,
        "Mirinda 500ml": 2500,
        "Mountain Dew 500ml": 2500,
        "Mountain Dew 1.5L": 4500,
        "Minute Maid": 3500,
        "Mango Juice": 4000,
        "Orange Juice": 4000,
        "Apple Juice": 4500,
        "Energy Drink": 5000,
        "Red Bull": 7000,
        "Water 500ml": 1000,
        "Water 1.5L": 2000,
        "Water 5L": 5000,
        "Malted Drink": 4500
    },

    "Medical": {
        "Face Mask": 1000,
        "Face Masks Pack": 8000,
        "Hand Gloves": 500,
        "Gloves Pack": 10000,
        "Hand Sanitizer 100ml": 3000,
        "Hand Sanitizer 500ml": 8000,
        "Dettol 250ml": 5000,
        "Dettol 500ml": 9000,
        "Dettol 1L": 16000,
        "Thermal Gun": 35000,
        "Digital Thermometer": 15000,
        "First Aid Kit": 35000,
        "Cotton Wool": 5000,
        "Medical Tape": 3000,
        "Bandage": 3000,
        "Plasters Pack": 4000,
        "Antiseptic Solution": 7000,
        "Alcohol Swabs": 5000,
        "Surgical Cap": 1000,
        "Surgical Gown": 12000,
        "Syringe Pack": 10000
    },

    "Personal Care": {
        "Bathing Soap": 3000,
        "Laundry Soap": 3500,
        "Body Lotion": 10000,
        "Body Spray": 12000,
        "Deodorant": 10000,
        "Shampoo": 9000,
        "Conditioner": 9000,
        "Toothpaste": 6000,
        "Toothbrush": 3000,
        "Mouthwash": 10000,
        "Petroleum Jelly": 5000,
        "Hair Oil": 7000,
        "Hair Gel": 6000,
        "Hair Comb": 2000,
        "Hair Brush": 5000,
        "Baby Powder": 7000,
        "Face Wash": 12000,
        "Hand Cream": 7000,
        "Nail Cutter": 3000,
        "Tissue Pack": 5000
    },

    "Household": {
        "Washing Powder 500g": 5000,
        "Washing Powder 1kg": 9000,
        "Dishwashing Liquid": 7000,
        "Bleach 500ml": 4000,
        "Bleach 1L": 7000,
        "Toilet Cleaner": 8000,
        "Floor Cleaner": 9000,
        "Glass Cleaner": 7000,
        "Air Freshener": 8000,
        "Sponge Pack": 4000,
        "Scrubbing Brush": 5000,
        "Broom": 7000,
        "Mop": 15000,
        "Bucket": 10000,
        "Dustpan": 5000,
        "Garbage Bags": 6000,
        "Clothes Hangers": 5000,
        "Plastic Container": 7000,
        "Aluminium Foil": 6000,
        "Kitchen Towel": 5000
    },

    "Electronics": {
        "USB Cable": 5000,
        "Type-C Cable": 8000,
        "Lightning Cable": 10000,
        "Phone Charger": 15000,
        "Fast Charger": 25000,
        "Power Bank": 45000,
        "Earphones": 15000,
        "Bluetooth Earbuds": 45000,
        "Computer Mouse": 18000,
        "Keyboard": 25000,
        "USB Flash 16GB": 12000,
        "USB Flash 32GB": 18000,
        "USB Flash 64GB": 28000,
        "Memory Card 32GB": 18000,
        "Memory Card 64GB": 28000,
        "HDMI Cable": 15000,
        "Extension Cable": 25000,
        "Power Extension": 20000,
        "LED Bulb": 7000,
        "Rechargeable Lamp": 30000
    },

    "Stationery": {
        "Ball Pen": 1000,
        "Blue Pen Pack": 5000,
        "Notebook Small": 3000,
        "Notebook Large": 6000,
        "Exercise Book": 2500,
        "A4 Paper Ream": 18000,
        "A3 Paper Ream": 30000,
        "Pencil": 1000,
        "Pencil Pack": 5000,
        "Eraser": 1000,
        "Sharpener": 1000,
        "Ruler": 2000,
        "Marker Pen": 2500,
        "Marker Pack": 10000,
        "Stapler": 8000,
        "Staples": 3000,
        "Glue Stick": 3000,
        "Scissors": 5000,
        "Calculator": 15000,
        "File Folder": 3000
    },

    "Bakery": {
        "White Bread": 5000,
        "Brown Bread": 5500,
        "Large Bread": 7000,
        "Buns Pack": 4000,
        "Doughnuts Pack": 5000,
        "Cupcake": 3000,
        "Cake Slice": 5000,
        "Cookies Pack": 5000,
        "Biscuits Pack": 4000,
        "Croissant": 4500
    },

    "Baby Products": {
        "Baby Diapers Small": 25000,
        "Baby Diapers Medium": 30000,
        "Baby Diapers Large": 35000,
        "Baby Diapers XL": 40000,
        "Baby Wipes": 7000,
        "Baby Soap": 4000,
        "Baby Lotion": 9000,
        "Baby Shampoo": 8000,
        "Baby Oil": 7000,
        "Baby Bottle": 12000,
        "Baby Bib": 5000,
        "Baby Powder": 7000
    },

    "Other": {
        "Umbrella": 15000,
        "Shopping Bag": 1000,
        "Torch": 10000,
        "Match Box": 1000,
        "Candle": 2000,
        "Battery AA": 3000,
        "Battery AAA": 3000,
        "Padlock": 12000,
        "Rope": 5000,
        "Shoe Polish": 5000,
        "Shoe Brush": 4000,
        "Mosquito Net": 25000,
        "Mosquito Coil": 3000,
        "Torch Batteries": 5000
    }
}


# MAIN 

class RetailPOS:

    def __init__(self, root):

        self.root = root

        self.root.title(APP_NAME)
        self.root.geometry("1450x850")
        self.root.minsize(1100, 700)

        self.receipt_number = self.generate_receipt_number()

        self.quantity_entries = {}

        self.current_receipt_text = ""

        self.create_variables()
        self.create_styles()
        self.create_header()
        self.create_customer_section()
        self.create_main_area()
        self.create_bottom_buttons()

        self.refresh_printers()
        self.show_empty_receipt()


    # VARIABLES
    
    def create_variables(self):

        self.customer_name = tk.StringVar()
        self.customer_phone = tk.StringVar()

        self.receipt_var = tk.StringVar(
            value=self.receipt_number
        )

        self.printer_var = tk.StringVar()

        self.subtotal_var = tk.StringVar(
            value="UGX 0"
        )

        self.tax_var = tk.StringVar(
            value="UGX 0"
        )

        self.total_var = tk.StringVar(
            value="UGX 0"
        )


    # STYLES
    
    def create_styles(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure(
            "Treeview",
            rowheight=27,
            font=("Arial", 10)
        )

        style.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold")
        )


    # HEADER
   

    def create_header(self):

        header = tk.Frame(
            self.root,
            bg="#222222",
            height=75
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        tk.Label(
            header,
            text="LE DOC RETAIL POS",
            font=("Arial", 23, "bold"),
            bg="#222222",
            fg="white"
        ).pack(
            pady=(10, 0)
        )

        tk.Label(
            header,
            text="Point of Sale & Receipt System",
            font=("Arial", 10),
            bg="#222222",
            fg="white"
        ).pack()


    # CUSTOMER SECTION
    

    def create_customer_section(self):

        frame = ttk.LabelFrame(
            self.root,
            text="Sale Information",
            padding=8
        )

        frame.pack(
            fill="x",
            padx=12,
            pady=8
        )

        ttk.Label(
            frame,
            text="Customer:"
        ).grid(
            row=0,
            column=0,
            padx=5
        )

        ttk.Entry(
            frame,
            textvariable=self.customer_name,
            width=25
        ).grid(
            row=0,
            column=1,
            padx=5
        )

        ttk.Label(
            frame,
            text="Phone:"
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        ttk.Entry(
            frame,
            textvariable=self.customer_phone,
            width=20
        ).grid(
            row=0,
            column=3,
            padx=5
        )

        ttk.Label(
            frame,
            text="Receipt No:"
        ).grid(
            row=0,
            column=4,
            padx=5
        )

        ttk.Entry(
            frame,
            textvariable=self.receipt_var,
            width=22,
            state="readonly"
        ).grid(
            row=0,
            column=5,
            padx=5
        )


    # MAIN AREA
   
    def create_main_area(self):

        main = tk.Frame(
            self.root
        )

        main.pack(
            fill="both",
            expand=True,
            padx=12,
            pady=3
        )

        # ----------------------------------------------------
        # LEFT: PRODUCTS
        # ----------------------------------------------------

        products_box = ttk.LabelFrame(
            main,
            text="Products",
            padding=6
        )

        products_box.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 6)
        )

        canvas = tk.Canvas(
            products_box,
            highlightthickness=0
        )

        scrollbar = ttk.Scrollbar(
            products_box,
            orient="vertical",
            command=canvas.yview
        )

        self.products_frame = ttk.Frame(
            canvas
        )

        self.products_frame.bind(
            "<Configure>",
            lambda event: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window(
            (0, 0),
            window=self.products_frame,
            anchor="nw"
        )

        canvas.configure(
            yscrollcommand=scrollbar.set
        )

        canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.create_product_fields()


        # ----------------------------------------------------
        # RIGHT: RECEIPT
        # ----------------------------------------------------

        receipt_box = ttk.LabelFrame(
            main,
            text="Receipt Preview",
            padding=6
        )

        receipt_box.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(6, 0)
        )

        self.receipt_text = tk.Text(
            receipt_box,
            font=("Courier New", 9),
            bg="white",
            fg="black",
            wrap="none"
        )

        self.receipt_text.pack(
            fill="both",
            expand=True
        )

        # Summary

        summary = ttk.Frame(
            receipt_box
        )

        summary.pack(
            fill="x",
            pady=5
        )

        ttk.Label(
            summary,
            text="Subtotal:"
        ).grid(
            row=0,
            column=0,
            sticky="e",
            padx=5
        )

        ttk.Label(
            summary,
            textvariable=self.subtotal_var
        ).grid(
            row=0,
            column=1,
            sticky="e",
            padx=5
        )

        ttk.Label(
            summary,
            text="Tax:"
        ).grid(
            row=1,
            column=0,
            sticky="e",
            padx=5
        )

        ttk.Label(
            summary,
            textvariable=self.tax_var
        ).grid(
            row=1,
            column=1,
            sticky="e",
            padx=5
        )

        ttk.Label(
            summary,
            text="TOTAL:",
            font=("Arial", 11, "bold")
        ).grid(
            row=2,
            column=0,
            sticky="e",
            padx=5
        )

        ttk.Label(
            summary,
            textvariable=self.total_var,
            font=("Arial", 11, "bold")
        ).grid(
            row=2,
            column=1,
            sticky="e",
            padx=5
        )


    # CREATE PRODUCT FIELDS
   
    def create_product_fields(self):

        row = 0

        for category, products in PRODUCTS.items():

            category_frame = ttk.LabelFrame(
                self.products_frame,
                text=f"{category}  |  Tax {TAX_RATES[category]}%",
                padding=6
            )

            category_frame.grid(
                row=row,
                column=0,
                sticky="ew",
                padx=4,
                pady=4
            )

            ttk.Label(
                category_frame,
                text="Product",
                font=("Arial", 9, "bold")
            ).grid(
                row=0,
                column=0,
                padx=6
            )

            ttk.Label(
                category_frame,
                text="Price",
                font=("Arial", 9, "bold")
            ).grid(
                row=0,
                column=1,
                padx=6
            )

            ttk.Label(
                category_frame,
                text="Qty",
                font=("Arial", 9, "bold")
            ).grid(
                row=0,
                column=2,
                padx=6
            )

            product_row = 1

            for product, price in products.items():

                ttk.Label(
                    category_frame,
                    text=product,
                    width=27
                ).grid(
                    row=product_row,
                    column=0,
                    sticky="w",
                    padx=6,
                    pady=2
                )

                ttk.Label(
                    category_frame,
                    text=self.money(price),
                    width=15
                ).grid(
                    row=product_row,
                    column=1,
                    padx=6
                )

                entry = ttk.Entry(
                    category_frame,
                    width=8
                )

                entry.grid(
                    row=product_row,
                    column=2,
                    padx=6
                )

                self.quantity_entries[product] = (
                    entry,
                    price,
                    category
                )

                product_row += 1

            row += 1


    # PRINTER SECTION + BUTTONS
  

    def create_bottom_buttons(self):

        outer = tk.Frame(
            self.root,
            bg="#eeeeee"
        )

        outer.pack(
            fill="x",
            padx=12,
            pady=(5, 12)
        )

        # Printer controls

        printer_frame = tk.Frame(
            outer,
            bg="#eeeeee"
        )

        printer_frame.pack(
            side="left"
        )

        tk.Label(
            printer_frame,
            text="Printer:",
            bg="#eeeeee",
            font=("Arial", 10, "bold")
        ).pack(
            side="left",
            padx=(0, 5)
        )

        self.printer_combo = ttk.Combobox(
            printer_frame,
            textvariable=self.printer_var,
            width=32,
            state="readonly"
        )

        self.printer_combo.pack(
            side="left",
            padx=3
        )

        tk.Button(
            printer_frame,
            text="Refresh Printers",
            command=self.refresh_printers,
            width=15
        ).pack(
            side="left",
            padx=3
        )

        tk.Button(
            printer_frame,
            text="Test Print",
            command=self.test_print,
            width=12
        ).pack(
            side="left",
            padx=3
        )

        # Main actions

        action_frame = tk.Frame(
            outer,
            bg="#eeeeee"
        )

        action_frame.pack(
            side="right"
        )

        tk.Button(
            action_frame,
            text="CALCULATE",
            command=self.calculate_sale,
            width=13,
            font=("Arial", 10, "bold")
        ).pack(
            side="left",
            padx=3
        )

        tk.Button(
            action_frame,
            text="GENERATE RECEIPT",
            command=self.generate_receipt,
            width=17,
            font=("Arial", 10, "bold")
        ).pack(
            side="left",
            padx=3
        )

        tk.Button(
            action_frame,
            text="PRINT RECEIPT",
            command=self.print_receipt,
            width=16,
            font=("Arial", 10, "bold")
        ).pack(
            side="left",
            padx=3
        )

        tk.Button(
            action_frame,
            text="NEW SALE",
            command=self.new_sale,
            width=12
        ).pack(
            side="left",
            padx=3
        )

        tk.Button(
            action_frame,
            text="EXIT",
            command=self.exit_application,
            width=9
        ).pack(
            side="left",
            padx=3
        )


    # RECEIPT NUMBER
   

    def generate_receipt_number(self):

        now = datetime.now()

        return (
            f"LD-{now.strftime('%Y%m%d%H%M%S')}-"
            f"{random.randint(100, 999)}"
        )


    
    # MONEY
   
    def money(self, amount):

        return f"{CURRENCY} {amount:,.0f}"


    # GET QUANTITY
    

    def get_quantity(self, product):

        entry, price, category = self.quantity_entries[product]

        value = entry.get().strip()

        if value == "":
            return 0

        try:

            quantity = int(value)

            if quantity < 0:
                raise ValueError

            return quantity

        except ValueError:

            messagebox.showerror(
                "Invalid Quantity",
                f"Enter a valid quantity for:\n{product}"
            )

            entry.focus()

            raise


    # CALCULATE
   
    def calculate_sale(self):

        subtotal = 0
        total_tax = 0
        items = []

        try:

            for product, (
                entry,
                price,
                category
            ) in self.quantity_entries.items():

                quantity = self.get_quantity(product)

                if quantity <= 0:
                    continue

                line_total = price * quantity

                tax_rate = TAX_RATES[category]

                tax_amount = (
                    line_total *
                    tax_rate /
                    100
                )

                subtotal += line_total
                total_tax += tax_amount

                items.append({
                    "product": product,
                    "price": price,
                    "quantity": quantity,
                    "category": category,
                    "total": line_total,
                    "tax": tax_amount
                })

        except ValueError:

            return None

        total = subtotal + total_tax

        self.subtotal_var.set(
            self.money(subtotal)
        )

        self.tax_var.set(
            self.money(total_tax)
        )

        self.total_var.set(
            self.money(total)
        )

        self.build_receipt(
            items,
            subtotal,
            total_tax,
            total
        )

        return (
            items,
            subtotal,
            total_tax,
            total
        )


    # BUILD RECEIPT
   
    def build_receipt(
        self,
        items,
        subtotal,
        tax,
        total
    ):

        now = datetime.now()

        lines = []

        lines.append("=" * 48)
        lines.append("             LE DOC RETAIL")
        lines.append("               SALES RECEIPT")
        lines.append("=" * 48)

        lines.append(
            f"Receipt: {self.receipt_number}"
        )

        lines.append(
            f"Date:    {now.strftime('%d/%m/%Y')}"
        )

        lines.append(
            f"Time:    {now.strftime('%H:%M:%S')}"
        )

        customer = (
            self.customer_name.get().strip()
            or "Walk-in Customer"
        )

        phone = (
            self.customer_phone.get().strip()
            or "-"
        )

        lines.append(
            f"Customer: {customer}"
        )

        lines.append(
            f"Phone:    {phone}"
        )

        lines.append("-" * 48)

        lines.append(
            f"{'ITEM':20}{'QTY':>5}{'PRICE':>10}{'TOTAL':>11}"
        )

        lines.append("-" * 48)

        for item in items:

            name = item["product"]

            if len(name) > 19:
                name = name[:19]

            lines.append(
                f"{name:<20}"
                f"{item['quantity']:>5}"
                f"{item['price']:>10,.0f}"
                f"{item['total']:>11,.0f}"
            )

        lines.append("-" * 48)

        lines.append(
            f"{'SUBTOTAL':>37} {subtotal:>10,.0f}"
        )

        lines.append(
            f"{'TAX':>37} {tax:>10,.0f}"
        )

        lines.append("-" * 48)

        lines.append(
            f"{'TOTAL':>37} {total:>10,.0f}"
        )

        lines.append("=" * 48)

        lines.append(
            "        Thank you for shopping with us!"
        )

        lines.append(
            "             Please come again."
        )

        lines.append("=" * 48)

        receipt = "\n".join(lines)

        self.current_receipt_text = receipt

        self.receipt_text.delete(
            "1.0",
            tk.END
        )

        self.receipt_text.insert(
            tk.END,
            receipt
        )


   
    # GENERATE RECEIPT
    
    def generate_receipt(self):

        result = self.calculate_sale()

        if result is None:
            return

        items, subtotal, tax, total = result

        if not items:

            messagebox.showwarning(
                "No Products",
                "Please enter a quantity for at least one product."
            )

            return

        path = self.save_receipt()

        if path:

            messagebox.showinfo(
                "Receipt Generated",
                f"Receipt generated successfully.\n\n"
                f"Receipt No: {self.receipt_number}\n\n"
                f"Saved in:\n{path}"
            )


  
    # SAVE RECEIPT
   

    def save_receipt(self):

        if not self.current_receipt_text:

            return None

        filename = (
            RECEIPT_FOLDER /
            f"{self.receipt_number}.txt"
        )

        try:

            with open(
                filename,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(
                    self.current_receipt_text
                )

            return filename

        except Exception as error:

            messagebox.showerror(
                "Save Error",
                str(error)
            )

            return None


    # REFRESH PRINTERS
    

    def refresh_printers(self):

        if not WINDOWS_PRINTING_AVAILABLE:

            self.printer_combo["values"] = [
                "pywin32 not installed"
            ]

            self.printer_var.set(
                "pywin32 not installed"
            )

            return

        try:

            printers = win32print.EnumPrinters(
                win32print.PRINTER_ENUM_LOCAL |
                win32print.PRINTER_ENUM_CONNECTIONS
            )

            names = []

            for printer in printers:

                name = printer[2]

                if name not in names:
                    names.append(name)

            names.sort()

            self.printer_combo["values"] = names

            if names:

                try:

                    default_printer = (
                        win32print.GetDefaultPrinter()
                    )

                    if default_printer in names:

                        self.printer_var.set(
                            default_printer
                        )

                    else:

                        self.printer_var.set(
                            names[0]
                        )

                except:

                    self.printer_var.set(
                        names[0]
                    )

            else:

                self.printer_var.set(
                    "No printer found"
                )

                messagebox.showwarning(
                    "Printer",
                    "No Windows printer was found.\n\n"
                    "Connect your printer and click Refresh Printers."
                )

        except Exception as error:

            messagebox.showerror(
                "Printer Error",
                f"Could not load printers.\n\n{error}"
            )


    # TEST PRINT
    

    def test_print(self):

        if not WINDOWS_PRINTING_AVAILABLE:

            messagebox.showerror(
                "Printer Library Missing",
                "Please install pywin32 first:\n\n"
                "pip install pywin32"
            )

            return

        printer_name = self.printer_var.get()

        if not printer_name or printer_name == "No printer found":

            messagebox.showwarning(
                "Printer",
                "Please connect and select a printer."
            )

            return

        test_receipt = (
            "\n"
            "================================\n"
            "          LE DOC RETAIL\n"
            "            TEST PRINT\n"
            "================================\n"
            "Printer connection is working.\n"
            f"Date: {datetime.now().strftime('%d/%m/%Y')}\n"
            f"Time: {datetime.now().strftime('%H:%M:%S')}\n"
            "================================\n\n"
        )

        try:

            self.send_to_printer(
                printer_name,
                test_receipt,
                cut=False
            )

            messagebox.showinfo(
                "Test Print",
                "Test print sent successfully."
            )

        except Exception as error:

            messagebox.showerror(
                "Print Error",
                f"Test print failed.\n\n{error}"
            )


    # PRINT RECEIPT
   
    def print_receipt(self):

        if not WINDOWS_PRINTING_AVAILABLE:

            messagebox.showerror(
                "Printer Library Missing",
                "Install pywin32 first:\n\n"
                "pip install pywin32"
            )

            return

        printer_name = self.printer_var.get()

        if not printer_name or printer_name == "No printer found":

            messagebox.showwarning(
                "Printer",
                "Please select a printer first."
            )

            return

        # Automatically calculate if necessary

        if not self.current_receipt_text:

            result = self.calculate_sale()

            if result is None:
                return

            items, subtotal, tax, total = result

            if not items:

                messagebox.showwarning(
                    "No Products",
                    "Please add at least one product."
                )

                return

        # Save a copy

        self.save_receipt()

        try:

            self.send_to_printer(
                printer_name,
                self.current_receipt_text,
                cut=True
            )

            messagebox.showinfo(
                "Print Successful",
                f"Receipt sent to:\n\n{printer_name}"
            )

        except Exception as error:

            messagebox.showerror(
                "Printing Error",
                f"Could not print receipt.\n\n{error}"
            )


   
    # SEND TO WINDOWS PRINTER
   

    def send_to_printer(
        self,
        printer_name,
        text,
        cut=True
    ):

        handle = None

        try:

            handle = win32print.OpenPrinter(
                printer_name
            )

            job = win32print.StartDocPrinter(
                handle,
                1,
                (
                    "LE DOC RETAIL POS",
                    None,
                    "RAW"
                )
            )

            win32print.StartPagePrinter(
                handle
            )

            # ESC/POS initialization

            data = b"\x1b\x40"

            # Center alignment

            data += b"\x1b\x61\x01"

            # Convert receipt text

            receipt_bytes = text.encode(
                "cp437",
                errors="replace"
            )

            data += receipt_bytes

            # Feed paper

            data += b"\n\n\n\n"

            # Cut paper
            # Supported by many thermal printers.

            if cut:

                data += b"\x1d\x56\x00"

            win32print.WritePrinter(
                handle,
                data
            )

            win32print.EndPagePrinter(
                handle
            )

            win32print.EndDocPrinter(
                handle
            )

        finally:

            if handle:

                win32print.ClosePrinter(
                    handle
                )


    
    # EMPTY RECEIPT
    

    def show_empty_receipt(self):

        self.receipt_text.delete(
            "1.0",
            tk.END
        )

        self.receipt_text.insert(
            tk.END,
            "\n"
            "===============================================\n"
            "              LE DOC RETAIL\n"
            "                SALES RECEIPT\n"
            "===============================================\n\n"
            "   Select your products and enter quantities.\n\n"
            "   1. Click CALCULATE\n"
            "   2. Click GENERATE RECEIPT\n"
            "   3. Click PRINT RECEIPT\n\n"
            "===============================================\n"
        )


   
    # NEW SALE
    
    def new_sale(self):

        answer = messagebox.askyesno(
            "New Sale",
            "Start a new sale?"
        )

        if not answer:
            return

        self.customer_name.set("")
        self.customer_phone.set("")

        self.receipt_number = (
            self.generate_receipt_number()
        )

        self.receipt_var.set(
            self.receipt_number
        )

        self.current_receipt_text = ""

        self.subtotal_var.set(
            "UGX 0"
        )

        self.tax_var.set(
            "UGX 0"
        )

        self.total_var.set(
            "UGX 0"
        )

        for entry, price, category in self.quantity_entries.values():

            entry.delete(
                0,
                tk.END
            )

        self.show_empty_receipt()


    
    # EXIT
   

    def exit_application(self):

        if messagebox.askyesno(
            "Exit",
            "Are you sure you want to exit?"
        ):

            self.root.destroy()



# RUN APPLICATION


if __name__ == "__main__":

    root = tk.Tk()

    app = RetailPOS(root)

    root.mainloop()