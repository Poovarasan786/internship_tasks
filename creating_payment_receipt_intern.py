from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch

def generate_receipt(transaction_details, filename="payment_receipt.pdf"):
    # Create a PDF object and set the page size to A4
    pdf = canvas.Canvas(filename, pagesize=A4)
    pdf.setTitle("Payment Receipt")

    # Set fonts and title
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(200, 800, "Payment Receipt")

    # Transaction details (e.g., store name, address, etc.)
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 770, "Store Name: Poovarasan Store")
    pdf.drawString(50, 755, "Address: 123 ABC Road, City XYZ")
    pdf.drawString(50, 740, f"Date: {transaction_details['date']}")
    pdf.drawString(50, 725, f"Transaction ID: {transaction_details['transaction_id']}")
    pdf.drawString(50, 710, f"Customer Name: {transaction_details['customer_name']}")

    # Table header for the receipt
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, 680, "Item")
    pdf.drawString(200, 680, "Quantity")
    pdf.drawString(300, 680, "Price")
    pdf.drawString(400, 680, "Total")

    # Loop through items and add them to the receipt
    y_position = 660
    total_amount = 0
    pdf.setFont("Helvetica", 12)
    for item in transaction_details['items']:
        item_name = item['name']
        quantity = item['quantity']
        price = item['price']
        total = price * quantity
        total_amount += total

        pdf.drawString(50, y_position, item_name)
        pdf.drawString(200, y_position, str(quantity))
        pdf.drawString(300, y_position, f"${price:.2f}")
        pdf.drawString(400, y_position, f"${total:.2f}")
        y_position -= 20

    # Draw a line for total
    pdf.setStrokeColor(colors.black)
    pdf.line(50, y_position, 500, y_position)
    y_position -= 20

    # Print the total amount
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(300, y_position, "Total Amount:")
    pdf.drawString(400, y_position, f"${total_amount:.2f}")

    # Save the PDF
    pdf.save()
    print(f"Receipt generated successfully: {filename}")

# Example transaction details
transaction_details = {
    'date': '2024-09-03',
    'transaction_id': 'TXN123456',
    'customer_name': 'John Doe',
    'items': [
        {'name': 'Product 1', 'quantity': 2, 'price': 15.00},
        {'name': 'Product 2', 'quantity': 1, 'price': 25.00},
        {'name': 'Product 3', 'quantity': 3, 'price': 10.00},
    ]
}

# Generate the receipt
generate_receipt(transaction_details)
