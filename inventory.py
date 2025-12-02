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


def view_inventory(products):
    """
    Duyệt danh sách products và in thông tin từng sản phẩm.
    products: list các dict hoặc object sản phẩm
    """
    if not products:
        print("Kho hiện đang trống.")
        return

    for product in products:
        print(f"Mã: {product['id']}, Tên: {product['name']}, Số lượng: {product['quantity']}, Giá: {product['price']}")

def check_low_stock(products, threshold=5):
    """
    Duyệt danh sách products và in ra những sản phẩm có số lượng dưới threshold.
    products: list các dict hoặc object sản phẩm
    threshold: mức cảnh báo (mặc định 5)
    """
    low_stock_items = [p for p in products if p['quantity'] < threshold]
    
    if not low_stock_items:
        print("Hiện tại không có sản phẩm nào sắp hết hàng.")
        return

    print("Các sản phẩm sắp hết hàng:")
    for product in low_stock_items:
        print(f"Mã: {product['id']}, Tên: {product['name']}, Số lượng: {product['quantity']}")


