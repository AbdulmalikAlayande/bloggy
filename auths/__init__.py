# def asserts(exp1: bool, exp2: str):
#     if __debug__:
#         if not exp1:
#             raise AssertionError(exp2)
#
#
# def get_product_discounted_price(product_: dict, discount: float) -> float:
#     new_price = product_.get("price") - (discount / 100) * product_.get("price")
#     # assert 0 <= new_price <= product.get("price"), "Discount Should Not Be More Than 100%"
#     exp_1 = product_.get("price") >= new_price >= 0
#     exp_2 = "shouldn't Fail"
#     asserts(exp_1, exp_2)
#     return new_price
# with open(file="hello.txt", mode="r") as reader:
#     line_counter = 0
#     for line in reader:
#         line_counter += 1
#         print(line_counter, line, end='', sep=' --> ')

with open(file="C:/Users/USER/Pictures/run mad.png", mode="rb") as reader:
    print(reader.read(8), end='\t==||==\t\t')
    print(reader.read(8), end=', ')
    # print(reader.read(3), end=', ')
    # print(reader.read(2), end=', ')
    # print(reader.read(1), end=', ')
    # print(reader.read(1), end=', ')
