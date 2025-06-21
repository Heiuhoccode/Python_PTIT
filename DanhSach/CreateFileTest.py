import pickle
import random


# Hàm tạo danh sách ngẫu nhiên
def create_random_list(size, max_value=9999):
    # Tạo danh sách với số lượng ngẫu nhiên từ 1 đến size
    actual_size = random.randint(1, size)
    # Tạo danh sách các số nguyên dương ngẫu nhiên từ 1 đến max_value
    return [random.randint(1, max_value) for _ in range(actual_size)]


# Tham số
max_size = 100000  # Số lượng tối đa mỗi file
max_value = 9999  # Giá trị tối đa của số (4 chữ số)

# Tạo dữ liệu cho DATA1.in
data1 = create_random_list(max_size, max_value)

# Tạo dữ liệu cho DATA2.in
data2 = create_random_list(max_size, max_value)

# Lưu vào file nhị phân
try:
    # Lưu DATA1.in
    with open("DATA1.in", "wb") as f1:
        pickle.dump(data1, f1)

    # Lưu DATA2.in
    with open("DATA2.in", "wb") as f2:
        pickle.dump(data2, f2)

    print("Đã tạo thành công DATA1.in và DATA2.in!")
    print(f"Kích thước DATA1.in: {len(data1)} số")
    print(f"Kích thước DATA2.in: {len(data2)} số")

except Exception as e:
    print(f"Lỗi khi tạo file: {e}")