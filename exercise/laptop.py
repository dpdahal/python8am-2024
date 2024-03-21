print("=============Computer Bazar==================")
print("1. Dell(Rs:20000) 2. Mac(Rs:50000) 3. HP(Rs:30000)")
dell_price=0
mac_price=0
hp_price=0
product_name=""
quantity=0
delivery_charge=0
plastic_price=0
bag_price=0
git_box_price=0
tax_amount=0
total_price=0
grand_total=0
option=int(input("Enter your choice:"))
if option==1:
    quantity=int(input("Enter the quantity:"))
    dell_price=20000*quantity
    product_name="Dell"
elif option==2:
    quantity=int(input("Enter the quantity:"))
    mac_price=50000*quantity
    product_name="Mac"
elif option==3:
    quantity=int(input("Enter the quantity:"))
    hp_price=30000*quantity
    product_name="HP"

else:
    print("Invalid choice")
    exit()


print("Delivery Option: 1. Home Delivery (Rs:1000) 2. Pick up(Free)")
delivery_option=int(input("Enter the delivery option:"))
if delivery_option==1:
    delivery_charge=1000

print("Packing: 1. Plastic Bag(Rs:500) 2. Bag(Rs:1000) 3. Gift Box(Rs:5000) 4.None")
packing_option=int(input("Enter the packing option:"))
if packing_option==1:
    plastic_price=500
elif packing_option==2:
    bag_price=1000
elif packing_option==3:
    git_box_price=5000


total = dell_price+mac_price+hp_price
print("Location: 1. KTM(13%) 2. Lalitpur 3. Bhaktapur")
location_option=int(input("Enter the location:"))
if location_option==1:
    tax_amount=total*0.13



grand_total=total+delivery_charge+plastic_price+bag_price+git_box_price+tax_amount
print("=============Invoice==================")
print("Product Name:",product_name)
print("Quantity:",quantity)
print("Tax Amount:",tax_amount)
print("Delivery Charge:",delivery_charge)
print("Plastic Price:",plastic_price)
print("Bag Price:",bag_price)
print("Gift Box Price:",git_box_price)
print("Grand Total:",grand_total)