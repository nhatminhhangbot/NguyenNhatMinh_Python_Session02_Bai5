patient_name = input("Nhập họ và tên bệnh nhân: ")
patient_age = int(input("Nhập tuổi bệnh nhân: "))
spo2_level = int(input("Nhập nồng độ oxy trong máu (SpO2): "))
heart_rate = int(input("Nhập nhịp tim (nhịp/phút): "))
medical_insurance = input("Có thẻ Bảo hiểm Y tế không? (yes/no): ").lower()

if spo2_level < 90 or heart_rate > 120:
    triage = "Báo động ĐỎ (Cấp cứu khẩn)"
elif 90 <= spo2_level <= 95 or 100 <= heart_rate <= 120:
    triage = "Báo động VÀNG (Theo dõi sát)"
else:
    triage = "XANH (Khám thường)"

if patient_age < 6 or patient_age >= 80:
    fee = 0
elif medical_insurance == "yes":
    fee = 250000
else:
    fee = 500000

print("--- PHIẾU KHÁM BỆNH ĐIỆN TỬ ---")
print(f"Họ và tên: {patient_name}")
print(f"Tuổi: {patient_age}")
print(f"Phân luồng: {triage}")
print(f"Viện phí: {fee} VND")

print("--- LOG HỆ THỐNG ---")
print("patient_name:", type(patient_name))
print("patient_age:", type(patient_age))
print("triage:", type(triage))
print("fee:", type(fee))