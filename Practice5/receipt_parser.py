import re
import json

with open("raw.txt", "r") as file:
    text = file.read()

# extract prices
prices = re.findall(r"\d+\.\d{2}", text)

# extract product names
products = re.findall(r"[A-Za-z]+\s\d+\.\d{2}", text)

# extract date
date = re.search(r"\d{4}-\d{2}-\d{2}", text)

# extract time
time = re.search(r"\d{2}:\d{2}", text)

# extract payment method
payment = re.search(r"Payment Method:\s(\w+)", text)

# calculate total
total = sum(map(float, prices))

data = {
    "products": products,
    "prices": prices,
    "date": date.group() if date else None,
    "time": time.group() if time else None,
    "payment_method": payment.group(1) if payment else None,
    "calculated_total": total
}

print(json.dumps(data, indent=4))