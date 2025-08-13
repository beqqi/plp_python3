def calculate_discount(price, discount_percent):
    """
    Calculate the discounted price based on the original price and discount percentage.

    :param price: Original price of the item
    :param discount_percent: Discount percentage to apply
    :return: Discounted price or original price if discount is less than 20%
    """
    if discount_percent >= 0.2:
        # Apply a discount only if the discount percentage is 20% or more
        return price * (1 - discount_percent)
    return price


price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percent in decimals: "))
print(f"The price of this item is {calculate_discount(price, discount_percent)}")