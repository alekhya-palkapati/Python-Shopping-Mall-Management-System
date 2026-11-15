product_list = ['Saree', 'Tops', 'Jeans', 'T-Shirts', 'Lehanga']
marked_price = [800, 500, 600, 300, 1500]
product_price = [1000, 750, 850, 500, 2000]

user_list = []
user_list1 = []
order_list = []
order_price = []
order_profit = []
bill = []

print(" " * 10, "ANU SHOPPING MALL", " " * 10)

while True:
    print("\n1. Admin")
    print("2. User")
    print("3. Exit")

    Role = input("Select one option (1/2/3): ")

    if Role == '1':

        while True:
            print("\n1. Add Product")
            print("2. Update Product")
            print("3. Remove Product")
            print("4. View Product")
            print("5. View Users")
            print("6. Exit")

            Admin = input("Choose one option (1/2/3/4/5/6): ")

            if Admin == '1':
                product = input("Enter new product: ").strip()

                if product == "":
                    print("Product name cannot be empty")

                elif product.lower() in [p.lower() for p in product_list]:
                    print("Product already exists")

                else:
                    price = int(input("Enter price of product: "))
                    mrk = int(input("Enter marked price: "))

                    product_list.append(product)
                    product_price.append(price)
                    marked_price.append(mrk)

                    print("Product added successfully")

            elif Admin == '2':
                j = int(input("Enter serial number of product to update: "))
                i = j - 1

                if i < 0 or i >= len(product_list):
                    print("Out of index")

                else:
                    new_product = input("Enter product: ").strip()

                    if new_product == "":
                        print("Product name cannot be empty")

                    elif new_product.lower() in [
                        p.lower() for k, p in enumerate(product_list) if k != i
                    ]:
                        print("Product already exists")

                    else:
                        product_list[i] = new_product
                        product_price[i] = int(input("Enter price: "))
                        marked_price[i] = int(input("Enter marked price: "))

                        print("Product updated successfully")

            elif Admin == '3':
                it = int(input("Enter serial number to remove product: "))
                item = it - 1

                if 0 <= item < len(product_list):
                    product_list.pop(item)
                    product_price.pop(item)
                    marked_price.pop(item)

                    print("Product removed successfully")

                else:
                    print("Enter correct index")

            elif Admin == '4':
                print("\nANU SHOPPING MALL")
                print("-" * 48)
                print(f'{"No":<5}{"Product":<18}{"Price":<12}{"Marked Price"}')
                print("-" * 48)

                for i in range(len(product_list)):
                    print(
                        f'{i+1:<5}{product_list[i]:<18}'
                        f'{product_price[i]:<12}{marked_price[i]}'
                    )

                print("-" * 48)

            elif Admin == '5':
                print("\nANU SHOPPING MALL - CUSTOMER ORDERS")
                print("=" * 45)

                if user_list == []:
                    print("No users")

                else:
                    for i in range(len(user_list)):
                        print("\nOrder No:", i + 1)
                        print("-" * 45)
                        print("Customer Name :", user_list[i])
                        print("Mobile Number :", user_list1[i])
                        print("Products      :", ", ".join(order_list[i]))
                        print("Prices        :", order_price[i])
                        print("Profit        :", order_profit[i])
                        print("Total Bill    :", bill[i])
                        print("-" * 45)

            elif Admin == '6':
                break

            else:
                print("Choose correct option")

    elif Role == '2':

        # Separate cart for each user session
        cart_product = []
        cart_price = []
        cart_profit = []

        while True:
            print("\n1. View Products")
            print("2. Add to Cart")
            print("3. Remove from Cart")
            print("4. View Cart")
            print("5. Checkout")
            print("6. Exit")

            user = input("Choose one option (1/2/3/4/5/6): ")

            if user == '1':
                print("\nAVAILABLE PRODUCTS")
                print("-" * 35)
                print(f'{"No":<5}{"Product":<20}{"Price"}')
                print("-" * 35)

                for i in range(len(product_list)):
                    print(
                        f'{i+1:<5}{product_list[i]:<20}'
                        f'{product_price[i]}'
                    )

                print("-" * 35)

            elif user == '2':
                product = input("Enter product: ").strip()

                if product.lower() in [p.lower() for p in product_list]:
                    idx = [
                        p.lower() for p in product_list
                    ].index(product.lower())

                    cart_product.append(product_list[idx])
                    cart_price.append(product_price[idx])
                    cart_profit.append(
                        product_price[idx] - marked_price[idx]
                    )

                    print("Product added to cart successfully")

                else:
                    print("Out of Stock")

            elif user == '3':
                if cart_product == []:
                    print("Your cart is empty")

                else:
                    idx = int(input("Enter serial number to remove from cart: "))
                    idx1 = idx - 1

                    if 0 <= idx1 < len(cart_product):
                        cart_product.pop(idx1)
                        cart_price.pop(idx1)
                        cart_profit.pop(idx1)

                        print("Product removed from cart")

                    else:
                        print("Product not found in cart")

            elif user == '4':
                print("\nANU SHOPPING MALL - YOUR CART")
                print("-" * 40)
                print(f'{"No":<5}{"Product":<20}{"Price"}')
                print("-" * 40)

                for i in range(len(cart_product)):
                    print(
                        f'{i+1:<5}{cart_product[i]:<20}'
                        f'{cart_price[i]}'
                    )

                print("-" * 40)

                total = sum(cart_price)
                print("Total Bill:", total)
                print("-" * 40)

            elif user == '5':
                if cart_product == []:
                    print("Your cart is empty. Add products first.")

                else:
                    details = input("Enter customer name: ").strip()

                    if details == "":
                        print("Name cannot be empty")
                        continue

                    while True:
                        number = input("Enter mobile number: ")

                        if (
                            len(number) == 10
                            and number.isdigit()
                            and number[0] in '6789'
                        ):

                            user_list.append(details)
                            user_list1.append(number)

                            order_list.append(cart_product.copy())
                            order_price.append(cart_price.copy())
                            order_profit.append(cart_profit.copy())

                            total = sum(cart_price)
                            bill.append(total)

                            cart_product.clear()
                            cart_price.clear()
                            cart_profit.clear()

                            print("\nYour order is placed successfully!")
                            print("Total Bill:", total)

                            break

                        else:
                            print("Enter correct 10-digit mobile number")

            elif user == '6':
                break

            else:
                print("Choose correct option")

    elif Role == '3':
        print("\nThank you for visiting ANU Shopping Mall!")
        break

    else:
        print("Choose correct option")
