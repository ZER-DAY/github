import os
import datetime

# تحديد مسار المستودع الخاص بك
REPO_PATH = "C:\\Users\\Administrator\\Desktop\\github"

# تغيير المسار إلى المستودع
os.chdir(REPO_PATH)

# إنشاء ملف نصي أو تحديث محتواه
filename = "daily_commit_log.txt"
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# كتابة أو تعديل ملف
with open(filename, "a") as file:
    file.write(f"Commit logged at {current_time}\n")

# أوامر Git لإضافة التغيير وعمل commit
os.system("git add .")
os.system(f'git commit -m "Daily update: {current_time}"')
os.system("git push")
