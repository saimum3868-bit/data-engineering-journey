
# Assignment 4: Variable, Type and String
# Clean three sales records using a loop

raw_records = [
    "  ord100047 ;2026-10-08;  Tanvir Hossain  ; Dim 12pc ;3; ৳ 441.75 ; Cash on Delivery ;DELIVERED",

    "ORD100048 ; 2026-10-08 ; SUMAIYA  KHAN ; Ilish 1kg ;1;৳ 1,520.00; bkash ; cancelled",

    "ord100049;2026-10-09; rakib  mia ;Broiler Murgi 1kg; 4 ;৳ 812.00 ;Card;delivered"
]


for raw in raw_records:

    # Step 1: Split the record
    parts = raw.split(";")

    # Step 2: Clean string values
    order_id = parts[0].strip().upper()
    order_date = parts[1].strip()
    customer_name = " ".join(parts[2].strip().split()).title()
    product = parts[3].strip()
    quantity_text = parts[4].strip()
    amount_text = parts[5].strip()
    payment = parts[6].strip().lower()
    status = parts[7].strip().lower()

    # Step 3: Convert data types
    quantity = int(quantity_text)
    amount = float(amount_text.replace("৳", "").replace(",", "").strip())

    # Step 4: Calculate unit price
    unit_price = amount / quantity

    # Step 5: Check cancelled order
    if status == "cancelled":
        print("সতর্কতা: এই অর্ডারটা বাতিল হয়েছে, হিসাবে ধরবেন না।")
        print()

    # Step 6: Print cleaned record
    print(f"{order_id}  ·  {order_date}")
    print(f"{customer_name} কিনেছেন {product} — {quantity}টা")
    print(f"মোট ৳{amount:.2f}  (প্রতিটা ৳{unit_price:.2f})")
    print(f"পেমেন্ট: {payment}  ·  অবস্থা: {status}")

    # Step 7: Check data types
    print("\ntype পরীক্ষা:")
    print(f"  order_id   {type(order_id).__name__:<6} {order_id}")
    print(f"  quantity   {type(quantity).__name__:<6} {quantity}")
    print(f"  amount     {type(amount).__name__:<6} {amount}")
    print(f"  unit_price {type(unit_price).__name__:<6} {unit_price}")
    print()
