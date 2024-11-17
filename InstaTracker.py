# Instagram
# More > Settings > Personal details >  Profiles > Your information and permissions > 
# Download your information > Download or transfer information > Select information > Followers and following > Next > 
# Extract your zip file


import os

def read_txt(file_path):
    """อ่านข้อมูลจากไฟล์ TXT และเก็บเป็นชุดข้อมูล (set)"""
    with open(file_path, 'r', encoding='utf-8') as file:
        # อ่านแต่ละบรรทัดในไฟล์และแปลงเป็น lowercase
        return {line.strip().lower() for line in file}

def main():
    # ตั้งค่าที่อยู่ของไฟล์
    followers_file_path = r'C:\Users\admin\OneDrive\Documents\project\InstagramStalker\followers_1.txt'
    following_file_path = r'C:\Users\admin\OneDrive\Documents\project\InstagramStalker\following.txt'

    # ตรวจสอบว่ามีไฟล์ทั้งสองอยู่ในตำแหน่งที่กำหนด
    if not os.path.exists(followers_file_path):
        print(f"ไฟล์ {followers_file_path} ไม่พบ.")
        return

    if not os.path.exists(following_file_path):
        print(f"ไฟล์ {following_file_path} ไม่พบ.")
        return
    
    # อ่านข้อมูลจากไฟล์ followers.txt และ following.txt
    followers = read_txt(followers_file_path)
    following = read_txt(following_file_path)
    
    print("---------------------------------The people I follow but don't follow me back.---------------------------------")
    
    # เปรียบเทียบทุกคนที่เรากำลังติดตาม
    for user in following:
        # ถ้าผู้ใช้ที่เราติดตามไม่มีใน followers แสดงว่าเขาไม่ติดตามเรากลับ
        if user not in followers:
            print(user)

# เรียกใช้ฟังก์ชัน main
if __name__ == "__main__":
    main()
