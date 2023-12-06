class Product:
    number = 0 
    def __init__(self, name, quantity, price):
        Product.number += 1
        self.number = Product.number
        self.name = name
        self.quantity = quantity
        self.price = price

    def total_value(self):
        return self.quantity * self.price

class Membership:
    def __init__(self):
        self.cart = []

    def buy(self, product, quantity):
        if not isinstance(product, Product):
            print('���ڵ带 ���� �� �����ϴ�.')
            return

        total_price = product.total_value() * quantity
        return total_price

class Plain(Membership):
    def __init__(self):
        super().__init__()
        self.savings_rate = 0.0005

    def buy(self, product, quantity):
        total_price = super().buy(product, quantity)

        if total_price < 150000:
            accumulated_savings = total_price * self.savings_rate
            print(f'{quantity} {product.name}(��)�� īƮ�� �߰��Ǿ����ϴ�.')
            print(f'���� ������: {accumulated_savings:.2f} ��')

class Friends(Membership):
    def __init__(self):
        super().__init__()
        self.accumulation_rate = 0.01
        self.discount_coupons = 3

    def buy(self, product, quantity):
        total_price = super().buy(product, quantity)

        if total_price >= 150000:
            accumulated_points = total_price * self.accumulation_rate
            print(f'{quantity} {product.name}(��)�� īƮ�� �߰��Ǿ����ϴ�.')
            print(f'���� ����Ʈ: {accumulated_points:.2f} ����Ʈ')
            print(f'{self.discount_coupons}���� ���� ������ �����˴ϴ�.')

class Purple(Membership):
    def __init__(self):
        super().__init__()
        self.accumulation_rate = 0.07
        self.discount_coupons = 4

    def buy(self, product, quantity):
        total_price = super().buy(product, quantity)

        if total_price >= 1000000:
            accumulated_points = total_price * self.accumulation_rate
            print(f'{quantity} {product.name}(��)�� īƮ�� �߰��Ǿ����ϴ�.')
            print(f'���� ����Ʈ: {accumulated_points:.2f} ����Ʈ')
            print(f'{self.discount_coupons}���� ���� ������ �����˴ϴ�.')

    def write_review(self):
        print('���䰡 �ۼ��Ǿ����ϴ�. �߰� ����Ʈ�� �ο��˴ϴ�.')
        # ���並 �ۼ��Ͽ� �߰� ����Ʈ�� �ο��ϴ� ����

# Example Usage
saewookkang = Product('�����', 3, 1500)

plain_member = Plain()
plain_member.buy(saewookkang, 2)

friends_member = Friends()
friends_member.buy(saewookkang, 1)

purple_member = Purple()
purple_member.buy(saewookkang, 5)
purple_member.write_review()