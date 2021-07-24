MELON_COST = 1.00

def check_if_overpaid(file_name):
    """Check if customer has overpaid. If so, print difference between expected cost and amount paid"""
    customer_order_file = open(file_name)
    for line in customer_order_file:
        order_info = line.split('|')
        name = order_info[1]
        num_melons = int(order_info[2])
        amount_paid = float(order_info[3].rstrip())
        expected_cost = num_melons * MELON_COST
        if expected_cost != amount_paid:
            print(f"{name} paid ${amount_paid:.2f},",
                f"expected ${expected_cost:.2f}")
    customer_order_file.close()

check_if_overpaid('customer-orders.txt')
