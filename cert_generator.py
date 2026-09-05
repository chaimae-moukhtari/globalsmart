from PIL import Image, ImageDraw, ImageFont

def cirtificate_input(student_name, combined_results):
    # المقارنة الرقمية
    if combined_results > 60:
        # 1. فتح الصورة (تأكدي أن اسم الملف في المجلد هو template.png)
        image = Image.open("template.png")
        draw = ImageDraw.Draw(image)

        # 2. إعداد الخط (تأكدي أن ملف الخط موجود أو استخدمي الافتراضي)
        try:
            font = ImageFont.truetype("arial.ttf", 60)
        except:
            font = ImageFont.load_default()

        # 3. كتابة الاسم
        draw.text((400, 500), student_name, fill="black", font=font)

        # 4. حفظ الشهادة باسم جديد لتجنب مسح القالب
        output_filename = f"Certificate_{student_name}.png"
        image.save(output_filename)
        return f"Certificate issued successfully! Saved as {output_filename}"
    else:
        return "Sorry, you failed."

# مثال لكيفية تجربة الدالة (شغلي هذا الجزء للتجربة):
# print(cirtificate_input("Ali", 80))