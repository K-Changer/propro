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
        print("\n상품명:", product.product_name)
        print("구매 수량:", quantity, "개")
        print("남은 수량:", product.remaining_quantity, "개")
        print("총액:", total_amount, "원")

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
        coupon_use = input("할인 쿠폰 적용 가능 (y/n)? ")
        if self.level == "Friends" and coupon_use.lower() == "y":
            print("쿠폰 사용으로 1만원이 차감되었습니다.")
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
        print("할인 쿠폰 적용 가능: Yes" if self.level == "Friends" else "할인 쿠폰 적용 가능: No")
        self.check_review_event(quantity)
        return total_amount

    def check_review_event(self, quantity):
        review_participation = input("리뷰 이벤트 참여 (y/n)? ")
        if review_participation.lower() == "y":
            review = input("리뷰를 입력하세요: ")
            print("리뷰 포인트를 적립합니다.")
        else:
            exit()

# Initialize product details
shrimp_crackers = Product('새우깡', 700, 2000)
potato_crackers = Product('포테이토깡', 700, 2000)
corn_crackers = Product('옥수수깡', 700, 2000)

# Example usage with user input for previous month's purchase and quantity of snacks:
try:
    previous_month_purchase = float(input("이전 달 구매 금액을 만원 단위로 입력하세요: "))
    quantity_of_shrimp_crackers = int(input("새우깡을 몇 개 구매하시겠습니까? "))
    quantity_of_potato_crackers = int(input("포테이토깡을 몇 개 구매하시겠습니까? "))
    quantity_of_corn_crackers = int(input("옥수수깡을 몇 개 구매하시겠습니까? "))
except ValueError:
    print("유효한 숫자를 입력하세요.")
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
print("\n합계:", total_amount_all, "원")