class Product:
    def __init__(self, product_type, name, price):
        self.type = product_type
        self.name = name
        self.price = price


class ProductStore:

    def __init__(self, name, location):
        self.product_list = []
        self.income = 0
        self.new_product = None
        self.name = name
        self.location = location

    def __str__(self):
        return f"Shop {self.name} locates in {self.location}"

    def __contains__(self, item):
        for i in self.product_list:
            if i[0].name == item:
                return True
        return False

    def __getitem__(self, item):
        for i in self.product_list:
            if i[0].name == item:
                return {"price": i[0].price, "amount": i[1]}

    def add(self, new_product: Product, amount: int):
        if not (new_product.type.isalnum() or new_product.name.isalnum()):
            raise ValueError("Type of name product is incorrect.")
        elif not isinstance(amount, int) or not isinstance(new_product.price, int):
            raise ValueError("Input correct amount or product price.")
        elif amount < 1 or new_product.price < 0:
            raise ValueError("Price or amount should be more than 0")
        else:
            self.new_product = new_product
            price = self.new_product.price * 1.3
            self.new_product.price = round(price, 2)
            self.product_list.append([self.new_product, amount])

    def set_discount(self, product_id, percent, id_type='name'):
        if percent < 0 or percent > 100:
            raise ValueError("Percent value is incorrect.")
        elif id_type == 'name':
            if product_id not in [p[0].name for p in self.product_list]:
                raise ValueError("No such name to make discount")
            else:
                for i in self.product_list:
                    if i[0].name == product_id:
                        i[0].price = round(i[0].price - i[0].price * percent / 100, 2)

        elif id_type == "type":
            if product_id not in [p[0].type for p in self.product_list]:
                raise ValueError("No such type to make discount")
            else:
                for i in self.product_list:
                    if i[0].type == product_id:
                        i[0].price -= round(i[0].price * percent / 100, 2)
        else:
            raise ValueError("Incorrect id type")

    def sell_product(self, product_name, amount):
        if product_name not in [p[0].name for p in self.product_list]:
            raise ValueError("No such product")
        elif amount < 0:
            raise ValueError("Percent value is incorrect.")
        else:
            for i in self.product_list:
                if i[0].name == product_name:
                    if i[1] >= amount:
                        self.income += amount * i[0].price
                        i[1] -= amount
                    else:
                        raise ValueError("Product is not enough")

    def get_income(self):
        return self.income

    def get_all_products(self):
        for product in self.product_list:
            print(f"Type: {product[0].type}\nName: {product[0].name}\nPrice: {product[0].price}\n\n")

    def get_product_info(self, product_name):
        if product_name not in [p[0].name for p in self.product_list]:
            raise ValueError("No such product")
        else:
            for product in self.product_list:
                if product[0].name == product_name:
                    res = (product_name, product[1])
                    return res


p1 = Product('Sport', 't_shirt', 3)
p2 = Product('Food', 'Ramen', 11)
s = ProductStore("Sport_life", "Kharkiv")
s.add(p1, 1)
s.add(p2, 11)

if "t_shirt" in s:
    print(s["t_shirt"].get("amount"))
    print(str(s))



