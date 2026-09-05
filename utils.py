import json
import os
from PIL import Image, ImageDraw, ImageFont

# 1. تم استيراد المكتبات الناقصة (Image, ImageDraw, ImageFont)
# 2. تم حذف ft من الاستيرادات هنا لأن هذا الملف للمنطق فقط وليس للواجهة (UI)

def cirtificate_input(student_name, combined_results):
    if combined_results >= 60:
        # تأكدي من مسار الصورة
        image = Image.open("template.png.png")
        draw = ImageDraw.Draw(image)
        # استخدام خط افتراضي (يمكنك لاحقاً تحميل خط .ttf احترافي)
        font = ImageFont.load_default()
        draw.text((400, 500), f"{student_name} - Avg: {combined_results:.2f}", fill="black", font=font)
        image.save(f"Certificate_{student_name}.png")
        return True
    return False

def update_results(course_name, score):
    results = {}
    if os.path.exists("results.json"):
        with open("results.json", "r") as f:
            try:
                results = json.load(f)
            except json.JSONDecodeError:
                results = {} # في حال كان الملف تالفاً
    
    results[course_name] = score
    
    with open("results.json", "w") as f:
        json.dump(results, f)
        
    return sum(results.values()) / len(results)