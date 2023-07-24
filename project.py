

from datetime import datetime
import random
import mysql.connector 

db_config = {
    'host': 'your_database_host',
    'user': 'your_database_username',
    'password': 'your_database_password',
    'database': 'your_database_name',
}
# Electronic devices available in the store with their prices, descriptions, and specifications
devices = {
    "Laptop": {
        "price": 1000,
        "description": "A portable computer suitable for various tasks.",
        "specifications": "Processor: Intel Core i5, RAM: 8GB, Storage: 256GB SSD"
    },
    "Smartphone": {
        "price": 800,
        "description": "A mobile phone with advanced features and internet connectivity.",
        "specifications": "Display: 6.5-inch OLED, Camera: 12MP, Storage: 128GB"
    },
    "Tablet": {
        "price": 500,
        "description": "A handheld device with a touchscreen display for multimedia and browsing.",
        "specifications": "Screen Size: 10.1 inches, RAM: 4GB, Storage: 64GB"
    },
    "Headphones": {
        "price": 200,
        "description": "Wireless headphones for an immersive audio experience.",
        "specifications": "Connectivity: Bluetooth 5.0, Battery Life: Up to 20 hours"
    },
    "Smartwatch": {
        "price": 300,
        "description": "A wearable device with fitness tracking and smartphone connectivity.",
        "specifications": "Display: 1.4-inch AMOLED, Water Resistance: 50 meters"
    },
    "Digital Camera": {
        "price": 600,
        "description": "A high-resolution camera for capturing memorable moments.",
        "specifications": "Resolution: 24MP, Sensor Type: CMOS, Zoom: 10x optical"
    },
    "Gaming Console": {
        "price": 400,
        "description": "A gaming system for immersive gaming experiences.",
        "specifications": "Graphics: 4K Ultra HD, Storage: 1TB, Controller: Wireless"
    },
    "Wireless Speaker": {
        "price": 150,
        "description": "A portable speaker for wireless audio streaming.",
        "specifications": "Connectivity: Bluetooth, Battery Life: Up to 10 hours"
    },
    "Fitness Tracker": {
        "price": 100,
        "description": "A wearable device for tracking fitness and health metrics.",
        "specifications": "Heart Rate Monitoring: Yes, Water Resistance: 30 meters"
    }
}

# Function to display the available devices and their prices
def display_devices():
    print("Available Devices:")
    for device, info in devices.items():
        print(f"{device}: ${info['price']}\n")

# Function to display the description of a device
def display_description(device):
    if device in devices:
        print(f"Device: {device}")
        print(f"Description: {devices[device]['description']}\n")
    else:
        print("Device not available.\n")

# Function to display the specifications of a device
def display_specifications(device):
    if device in devices:
        print(f"Device: {device}")
        print(f"Specifications: {devices[device]['specifications']}\n")
    else:
        print("Device not available.\n")

# Function for validating the device selection
def validate_device(device):
    while device not in devices:
        print("Invalid device selection.")
        device = input("Enter the device you want to purchase: ")
    return device

# Function for validating the quantity
def validate_quantity(quantity):
    while not quantity.isdigit() or int(quantity) <= 0:
        print("Invalid quantity.")
        quantity = input("Enter the quantity: ")
    return int(quantity)

# Function for validating the credit card number
def validate_card_number(card_number):
    while len(card_number) != 16 or not card_number.isdigit():
        print("Invalid credit card number.")
        card_number = input("Enter your credit card number: ")
    return card_number

# Function for validating the credit card name
def validate_card_name(card_name):
    while not all(part.isalpha() or part.isspace() for part in card_name.split()):
        print("Invalid credit card name.")
        card_name = input("Enter the name on the credit card: ")
    return card_name


# Function for validating the credit card expiration date
def validate_card_expiry(expiry_date):
    while len(expiry_date) != 5 or not expiry_date[:2].isdigit() or not expiry_date[3:].isdigit() or expiry_date[2] != '/':
        print("Invalid credit card expiration date.")
        expiry_date = input("Enter the expiration date (MM/YY): ")
        expiry_date=validate_card_expiry(expiry_date)

    # Extracting month and year from the input
    month, year = expiry_date.split('/')
    current_year = datetime.now().year
    current_month = datetime.now().month
    if not (1 <= int(month) <= 12) or not (int(year) >= current_year % 100):
        print("Invalid credit card expiration date.")
        expiry_date = input("Enter the expiration date (MM/YY): ")
        expiry_date=validate_card_expiry(expiry_date)
    elif int(year) < current_year % 100 or (int(year) == current_year % 100 and int(month) < current_month):
        print("Invalid credit card expiration date.")
        expiry_date = input("Enter the expiration date (MM/YY): ")
        expiry_date=validate_card_expiry(expiry_date)

    return expiry_date



# Function for validating the credit card CVV
def validate_card_cvv(cvv):
    while len(cvv) != 3 or not cvv.isdigit():
        print("Invalid credit card CVV.")
        cvv = input("Enter the CVV: ")
    return cvv


# Function to generate a random order number
def generate_order_number():
    order_number = ''.join(random.choices('0123456789', k=7))
    return order_number

# Function to process the purchase and credit card payment
def process_purchase(cart):
    total_amount = sum([device["price"] * quantity for device, quantity in cart])
    print("Items in Cart:")
    for device, quantity in cart:
        print(f"Device: {device}, Quantity: {quantity}, Price: ${device['price'] * quantity}\n")
    print(f"Total Amount: ${total_amount}\n")

    choice = input("Would you like to proceed with the purchase? (Y/N): ")
    if choice.lower() == "y":
        card_name = input("Enter the name on the credit card: ")
        card_name = validate_card_name(card_name)

        card_number = input("Enter your credit card number: ")
        card_number = validate_card_number(card_number)

        expiry_date = input("Enter the expiration date (MM/YY): ")
        expiry_date = validate_card_expiry(expiry_date)

        cvv = input("Enter the CVV: ")
        cvv = validate_card_cvv(cvv)

        print(f"Processing payment with card: {card_name}, Card Number: {card_number}, Expiry Date: {expiry_date}, CVV: {cvv}\n")
        print("Payment successful. Thank you for your purchase!\n")
        order_number = generate_order_number()
        print(f"Your order number is: {order_number}\n")
    else:
        print("Purchase cancelled.\n")

# FAQ section
faq = [
    ("Q: Can I return a purchased device?", "A: Yes, you can return a device within 30 days of purchase with the original receipt."),
    ("Q: Do the devices come with a warranty?", "A: Yes, all devices come with a one-year manufacturer warranty."),
    ("Q: Can I pay with cash?", "A: Currently, we only accept credit card payments."),
    ("Q: How long does shipping take?", "A: Shipping usually takes 3-5 business days.")
]

# Function to display the FAQ section
def display_faq():
    print("Frequently Asked Questions:")
    for question, answer in faq:
        print(f"{question}\n{answer}\n")

# Shopping cart
cart = []

# Main program loop
while True:
    print("Welcome to Shophouse!")
    print("1. Display available devices\n")
    print("2. Display device description\n")
    print("3. Display device specifications\n")
    print("4. Add device to cart\n")
    print("5. Purchase\n")
    print("6. FAQ\n")
    print("7. Exit\n")
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        display_devices()
    elif choice == "2":
        display_devices()
        device = input("Enter the device to display description: ")
        display_description(device)
    elif choice == "3":
        display_devices()
        device = input("Enter the device to display specifications: ")
        display_specifications(device)
    elif choice == "4":
        display_devices()
        device = input("Enter the device you want to add to the cart: ")
        device = validate_device(device)

        quantity = input("Enter the quantity: ")
        quantity = validate_quantity(quantity)

        cart.append((devices[device], quantity))
        print(f"{quantity} {device}(s) added to the cart.\n")
    elif choice == "5":
        process_purchase(cart)
        cart = []
    elif choice == "6":
        display_faq()
        pass
    elif choice == "7":
        print("Thank you for visiting Shophouse. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
