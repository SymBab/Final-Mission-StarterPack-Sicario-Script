# =====================================================
#  personnel/show_members.py — คนรับผิดชอบ: ______________________
#  หน้าที่: แสดงรายชื่อลูกน้องทั้งหมดในแฟมิลี่
# =====================================================
from data import family_members

def show_members():
    for member in family_members:
        print(f"name: {member["name"]} role: {member["role"]} power: {member["power"]} equipment: {member["equipment"]}")
#   - print ข้อมูลลูกน้องทุกคนใน family_members บรรทัดละคน (ชื่อ, ตำแหน่ง, ความโหด, อาวุธ)
    # TODO: เขียนโค้ดตรงนี้

    pass


# ทดสอบเฉพาะไฟล์ตัวเอง: พิมพ์  python -m personnel.show_members
if __name__ == "__main__":
    show_members()   # ต้องเห็น Tony กับ Luigi คนละบรรทัด
