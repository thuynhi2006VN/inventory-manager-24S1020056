# Biến lưu trữ dữ liệu: Mỗi sản phẩm là một dict {'name': '...', 'price': 0, 'qty': 0}
products = []

def add_product():
    name = input("Tên sản phẩm: ")
    price = int(input("Giá bán: "))
    quantity = int(input("Số lượng: "))

    product = {
        'name': name,
        'price': price,
        'qty': quantity
    }

    products.append(product)
    print(f"Đã nhập hàng: {name} - SL: {quantity}")


def view_inventory():
    # Duyệt list products và in ra
    # Ví dụ: Mì tôm - Giá: 5000 - SL: 100
    pass

def check_low_stock():
    # Duyệt list, kiểm tra nếu qty < 5 thì in ra cảnh báo
    pass

