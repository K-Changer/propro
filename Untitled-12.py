#!/usr/bin/env python3
 # -*- coding: EUC-KR -*-
 
 class Product:
    next_serial_number = 1

    def __init__(self, product_name, quantity, price):
        self.serial_number = Product.next_serial_number
        Product.next_serial_number += 1
        self.product_name = product_name
        self.initial_quantity = quantity
        self.remaining_quantity = quantity
        self.price = price

class Membership:
    def __init__(self, previous_month_purchase=0):
        self.previous_month_purchase = previous_month_purchase
        self.level = None

    def set_membership_level(self):
        raise NotImplementedError("Subclasses must implement the 'set_membership_level' method.")

    def buy(self, product, quantity):
        raise NotImplementedError("Subclasses must implement the 'buy' method.")

    def print_details(self, product, quantity, total_amount):
        print("\n��ǰ��:", product.product_name)
        print("���� ����:", quantity, "��")
        print("���� ����:", product.remaining_quantity, "��")
        print("�Ѿ�:", total_amount, "��")

class Plain(Membership):
    def set_membership_level(self):
        if self.previous_month_purchase < 15:
            self.level = "Plain"
        elif self.previous_month_purchase >= 100:
            self.level = "Purple"
        else:
            self.level = "Friends"

    def buy(self, product, quantity):
        total_amount = product.price * quantity
        product.remaining_quantity -= quantity
        self.print_details(product, quantity, total_amount)
        return total_amount

class Friends(Membership):
    def set_membership_level(self):
        if self.previous_month_purchase >= 15:
            self.level = "Friends"
        elif self.previous_month_purchase >= 100:
            self.level = "Purple"
        else:
            self.level = "Plain"

    def buy(self, product, quantity):
        total_amount = product.price * quantity
        product.remaining_quantity -= quantity
        self.print_details(product, quantity, total_amount)
        coupon_use = input("���� ���� ���� ���� (y/n)? ")
        if self.level == "Friends" and coupon_use.lower() == "y":
            print("���� ������� 1������ �����Ǿ����ϴ�.")
            total_amount -= 10000
        return total_amount

class Purple(Membership):
    def set_membership_level(self):
        if self.previous_month_purchase >= 100:
            self.level = "Purple"
        elif self.previous_month_purchase >= 15:
            self.level = "Friends"
        else:
            self.level = "Plain"

    def buy(self, product, quantity):
        total_amount = product.price * quantity
        product.remaining_quantity -= quantity
        self.print_details(product, quantity, total_amount)
        print("���� ���� ���� ����: Yes" if self.level == "Friends" else "���� ���� ���� ����: No")
        self.check_review_event(quantity)
        return total_amount

    def check_review_event(self, quantity):
        review_participation = input("���� �̺�Ʈ ���� (y/n)? ")
        if review_participation.lower() == "y":
            review = input("���並 �Է��ϼ���: ")
            print("���� ����Ʈ�� �����մϴ�.")
        else:
            exit()

# Initialize product details
shrimp_crackers = Product('�����', 700, 2000)
potato_crackers = Product('���������', 700, 2000)
corn_crackers = Product('��������', 700, 2000)

# Example usage with user input for previous month's purchase and quantity of snacks:
try:
    previous_month_purchase = float(input("���� �� ���� �ݾ��� ���� ������ �Է��ϼ���: "))
    quantity_of_shrimp_crackers = int(input("������� �� �� �����Ͻðڽ��ϱ�? "))
    quantity_of_potato_crackers = int(input("����������� �� �� �����Ͻðڽ��ϱ�? "))
    quantity_of_corn_crackers = int(input("���������� �� �� �����Ͻðڽ��ϱ�? "))
except ValueError:
    print("��ȿ�� ���ڸ� �Է��ϼ���.")
    exit()

plain_member = Plain(previous_month_purchase)
friends_member = Friends(previous_month_purchase)
purple_member = Purple(previous_month_purchase)

plain_member.set_membership_level()
friends_member.set_membership_level()
purple_member.set_membership_level()

total_amount_shrimp = plain_member.buy(shrimp_crackers, quantity_of_shrimp_crackers)
total_amount_potato = friends_member.buy(potato_crackers, quantity_of_potato_crackers)
total_amount_corn = purple_member.buy(corn_crackers, quantity_of_corn_crackers)

total_amount_all = total_amount_shrimp + total_amount_potato + total_amount_corn
print("\n�հ�:", total_amount_all, "��")