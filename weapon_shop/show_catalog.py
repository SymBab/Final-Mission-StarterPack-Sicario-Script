# =====================================================
#  weapon_shop/show_catalog.py — คนรับผิดชอบ: Tang
#  หน้าที่: แสดงรายการอาวุธทั้งหมดที่มีขาย
# =====================================================
from data import weapons_catalog

def show_catalog():
#   - print อาวุธทุกชิ้นใน weapons_catalog บรรทัดละชิ้น (รหัส, ชื่อ, ราคา, พลังโบนัส)
    # TODO: เขียนโค้ดตรงนี้
    print("========================== WEAPON CATALOG ==========================")
    for i, weapon in weapons_catalog.items():
        print(f"CODE ({i}) | NAME | {weapon['name']} | PRICE {weapon['price']}$ | POWER_BONUS -> {weapon['bonus']} |")
    print("====================================================================")

# ทดสอบเฉพาะไฟล์ตัวเอง: พิมพ์  python -m weapon_shop.show_catalog
if __name__ == "__main__":
    show_catalog()   # ต้องเห็นอาวุธครบ 3 ชิ้น
