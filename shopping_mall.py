product_list = ['Saree', 'Tops', 'Jeans', 'T-Shirts', 'Lehanga']
marked_price = [800, 500, 600, 300, 1500]
product_price = [1000, 750, 800, 500, 2000]

user_list = []
user_list1 = []
cart_product = []
cart_profit = []
cart_price = []
order_list = []
order_price = []
order_profit = []
bill = []

print(" " * 10, "ANU SHOPPING MALL", " " * 10)

while True:
    print("1.Admin")
    print("2.User")
    print("3.Exit")

    Role = input("Select one option(1/2/3): ")

    if Role == '1':

        while True:
            print("1.Add Product")
            print("2.Update Product")
            print("3.Remove Product")
            print("4.View Product")
            print("5.View Users")
            print("6.Exit")

            Admin = input("Choose one option(1/2/3/4/5/6): ")

            if Admin == '1':
                product = input("Enter new product: ")

                if product in product_list:
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
                    product_list[i] = input("Enter product: ")
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

                    print("Product removed from the list")
                else:
                    print("Enter correct index")

            elif Admin == '4':
                print()
                print(f'{"No": <5}{"Products": <15}{"Price": <8}{"Markedprice":}')
                print("-" * 30)

                count = 1
                for product, price, mrk in zip(product_list, product_price, marked_price):
                    print(f'{count: <5}{product: <15}{price: <8}{mrk}')
                    count += 1

                print()

            elif Admin == '5':
                print()
                print(" " * 30, "ANU SHOPPING MALL")
                print()

                if user_list == []:
                    print("No users")
                else:
                    print(f'{"Name": <12}{"Number": <12}{"Products": <23}{"Price": <20}{"Profit": <15}{"Total":}')
                    print("-" * 100)

                    for user, number, prod, pr, mrk, bill_amt in zip(
                        user_list, user_list1, order_list,
                        order_price, order_profit, bill
                    ):
                        print(f'{user: <12}{number: <12}{str(prod): <23}{str(pr): <20}{str(mrk): <15}{bill_amt}')

                    print("-" * 100)

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
            print("1.View Products")
            print("2.Add to Cart")
            print("3.Remove from Cart")
            print("4.View Cart")
            print("5.Checkout")
            print("6.Exit")

            user = input("Choose one option(1/2/3/4/5/6): ")

            if user == '1':
                print()
                print(f'{"No": <5}{"Products": <22}{"Price":}')
                print("-" * 35)

                count = 1
                for product, price in zip(product_list, product_price):
                    print(f'{count: <5}{product: <22}{price}')
                    count += 1

                print()

            elif user == '2':
                product = input("Enter product: ")

                if product in product_list:
                    idx = product_list.index(product)

                    cart_product.append(product_list[idx])
                    cart_price.append(product_price[idx])
                    cart_profit.append(product_price[idx] - marked_price[idx])

                    print("Product added to cart")
                else:
                    print("Out of Stock")

            elif user == '3':
                if cart_product == []:
                    print("Your cart is empty")
                else:
                    idx = int(input("Enter the serial number to remove from cart: "))
                    idx1 = idx - 1

                    if 0 <= idx1 < len(cart_product):
                        cart_product.pop(idx1)
                        cart_price.pop(idx1)
                        cart_profit.pop(idx1)

                        print("Product removed from the cart")
                    else:
                        print("Product not in cart")

            elif user == '4':
                print()
                print(" " * 10, "ANU SHOPPING MALL")
                print("-" * 35)

                print(f'{"No": <5}{"Products": <22}{"Price":}')
                print("-" * 35)

                count = 1
                for product, price in zip(cart_product, cart_price):
                    print(f'{count: <5}{product: <22}{price}')
                    count += 1

                print("-" * 35)

                s = sum(cart_price)
                print(" " * 20, "Total:", s)

            elif user == '5':
                if cart_product == []:
                    print("Your cart is empty. Add products first.")
                else:
                    details = input("Enter name: ")

                    while True:
                        number = input("Enter mobile number: ")

                        if len(number) == 10 and number.isdigit() and number[0] in '6789':

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

                            print("Your order is placed successfully")
                            break

                        else:
                            print("Enter correct mobile number")

            elif user == '6':
                break

            else:
                print("Choose correct option")

    elif Role == '3':
        print("Thank you for visiting ANU Shopping Mall")
        break

    else:
        print("Choose correct option")
