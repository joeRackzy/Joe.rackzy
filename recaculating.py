
def caculate_total(tickets):
    return sum(tickets)

def apply_discount(amount, discount=0.10):
    return amount * discount

def print_invoice(customer, tickets):
    subtotal = caculate_total(tickets)
    discount_amount = apply_discount(subtotal)
    final_total = subtotal-discount_amount 

    print(f"\n-----{customer} receipt-----".title())
    print(f"subtotal: {subtotal}.".title())
    print(f"discount: {discount_amount}.".title())
    print(f"total: {final_total}.".title())

print_invoice("john", [1200,2900,2000,3580,])


def caculate_subtotal(items):
    return sum(items)

def caculate_tpis(amount, tip_rate=0.15):
    return amount * tip_rate

def split_bill(total, people):
    return total / people

def print_receipt(customer, items, people):
    all = caculate_subtotal(items)
    tip_amount = caculate_tpis(all)
    total = all+ tip_amount
    split = split_bill(total,people)
    print(customer)
    print(f"subtotal: {all:.2f}")
    print(f"tip: {tip_amount:.2f}")
    print(f"total: {total:.2f}")
    print(f"per person: {split:.2f}")
print_receipt("sara", [100, 200, 300, 400, 1000], 4)




    