import flet as ft 
import json
import os
import webbrowser
import importlib
from PIL import Image, ImageDraw, ImageFont

# 1. الإعدادات والبيانات
COURSES = {
    "الاخلاق": {
        "link": "https://www.albetaqa.site",
        "content_text": "الأخلاق الجميلة تعني أن نحب أصدقاءنا، ونساعد ماما وبابا، ونقول دائماً الصدق لنكون أطفالاً محبوبين.",
        "questions": [
            "ماذا تعني الأخلاق الجميلة تجاه أصدقائنا؟",
            "هل يجب أن نقول الصدق دائماً لنكون محبوبين؟",
            "من نحب أن نساعد في البيت؟",
            "هل نحب مساعدة ماما وبابا؟",
            "هل الأطفال المؤدبون يقولون الصدق؟",
            "هل تصرفاتنا الطيبة تجعل الآخرين سعداء؟",
            "هل نبتسم في وجوه أصدقائنا؟",
            "هل نحافظ على نظافة ألعابنا وغرفتنا؟",
            "هل نحترم الكبار وساعدهم؟",
            "هل تجعلنا الأخلاق أطفالاً رائعين؟"
        ],
        "keywords": [
            "نحب أصدقاءنا",
            "نعم",
            "ماما وبابا",
            "نعم",
            "نعم",
            "نعم",
            "نعم",
            "نعم",
            "نعم",
            "نعم"
        ]
    },
    "القراءة": {
        "link": "https://darasfarstore.com",
        "content_text": "القراءة مفيدة وجميلة، نتعلم منها قصصاً حلوة وممتعة عن الحيوانات والطيور والنجوم.",
        "questions": [
            "هل القراءة مفيدة وجميلة؟",
            "ماذا نتعلم من القراءة؟",
            "هل تحكي القصص عن الحيوانات؟",
            "هل نقرأ عن الطيور أيضاً؟",
            "هل توجد قصص عن النجوم في الكتب؟",
            "هل تحب قراءة القصص قبل النوم؟",
            "هل الصور في الكتب الملونة جميلة؟",
            "هل تجعلنا القراءة نتعلم كلمات جديدة؟",
            "هل القراءة هواية ممتعة؟",
            "هل تحب أن تقرأ كتاباً كل يوم؟"
        ],
        "keywords": [
            "نعم",
            "قصصاً حلوة",
            "نعم",
            "نعم",
            "نعم",
            "نعم",
            "نعم",
            "نعم",
            "نعم",
            "نعم"
        ]
    },
    "العلوم الاساسية": {
        "link": "https://www.mamystar.com",
        "content_text": "العلوم تجعلنا نعرف كيف تنمو النباتات بالماء والشمس، وكيف تطير الطيور في السماء الجميلة.",
        "questions": [
            "بماذا تنمو النباتات الجميلة؟",
            "ما الذي يحتاجه النبات لكي يكبر؟",
            "أين تطير الطيور العالية؟",
            "هل تحتاج النباتات إلى الماء والشمس؟",
            "هل الشمس تهدينا الدفء والضوء؟",
            "هل للطيور أجنحة تطير بها؟",
            "هل نحب مشاهدة الزهور تتفتح؟",
            "هل الماء مهم لكل الكائنات الحية؟",
            "هل السماء واسعة ومليئة بالسحاب؟",
            "هل العلم يجعلنا نفهم الطبيعة؟"
        ],
        "keywords": [
            "الماء والشمس",
            "الماء",
            "السماء",
            "نعم",
            "نعم",
            "نعم",
            "نعم",
            "نعم",
            "نعم",
            "نعم"
        ]
    },
    "سكراتش": {
        "link": "https://www.scratchjr.org",
        "content_text": "برمجة سكراتش تجعلنا نحرك القط اللطيف على الشاشة ونصنع ألعاباً ملونة ومفرحة لأنفسنا.",
        "questions": [
            "ماذا نحرك على الشاشة في سكراتش؟",
            "هل القط في اللعبة لطيف؟",
            "ماذا نصنع على الشاشة؟",
            "هل الألعاب التي نصنعها ملونة؟",
            "هل تحب اللعب بالبرمجة الملونة؟",
            "هل تجعلنا البرمجة نصنع ألعاباً خاصة بنا؟",
            "هل نضغط على الأزرار لتحريك الشخصيات؟",
            "هل البرمجة تشبه اللعب بالألغاز؟",
            "هل تفرح عندما تتحرك الشخصية بنجاح؟",
            "هل تحب تصميم ألعابك بنفسك؟"
        ],
        "keywords": [
            "القط",
            "نعم",
            "ألعاباً ملونة",
            "نعم",
            "نعم",
            "نعم",
            "نعم",
            "نعم",
            "نعم",
            "نعم"
        ]
    },
    "المهام": {
        "link": "https://benaa.academy/",
        "content_text": "ترتيب الغرفة وتنظيم الألعاب بعد اللعب يساعدنا على أن نكون أطفالاً نشيطين ومرتبين.",
        "questions": [
            "متى نرتب ألعابنا الجميلة؟",
            "ماذا نفعل بغرفتنا لتبقى جميلة؟",
            "هل ترتيب الغرفة يجعلنا أطفالاً نشيطين؟",
            "هل نحافظ على نظافة المكان الذي نلعب فيه؟",
            "هل يساعدنا التنظيم على إيجاد ألعابنا بسرعة؟",
            "هل المساعدة في البيت عمل جميل؟",
            "هل تحب أن تكون مرتباً ونظيفاً؟",
            "هل تضع ألعابك في مكانها المخصص؟",
            "هل يفرح ماما وبابا عندما نساعدهم؟",
            "هل العمل المنظم يجعل يومنا سعيداً؟"
        ],
        "keywords": [
            "بعد اللعب",
            "ترتيب الغرفة",
            "نعم",
            "نعم",
            "نعم",
            "نعم",
            "نعم",
            "نعم",
            "نعم",
            "نعم"
        ]
    },
    "الطبخ": {
        "link": "https://poki.com/ar/%D8%B7%D8%B8%D8%AE",
        "content_text": "الطبخ صنع طعام لذيذ ومفيد في المطبخ، مثل صنع كعكة حلوة بالفواكه الطازجة.",
        "questions": [
            "ماذا يصنع في المطبخ ليكون لذيذاً؟",
            "هل الطعام الذي نصنعه مفيد ولذيذ؟",
            "ماذا يمكننا أن نصنع من الحلويات؟",
            "هل نضع الفواكه الطازجة على الكعكة؟",
            "هل تحب مساعدة ماما في المطبخ؟",
            "هل رائحة الطعام الذكي جميلة؟",
            "هل تغسل يديك قبل تناول الطعام؟",
            "هل الأكل الصحي يقوي أجسامنا؟",
            "هل تحب تناول الكعكة الحلوة؟",
            "هل الطبخ هواية ممتعة ولذيذة؟"
        ],
        "keywords": [
            "طعام لذيذ",
            "نعم",
            "كعكة حلوة",
            "نعم",
            "نعم",
            "نعم",
            "نعم",
            "نعم",
            "نعم",
            "نعم"
        ]
    },
    "التاريخ": {
        "link": "https://kidzzstory.com/story-category/historical-stories-kids/",
        "content_text": "قصص زمان تحكي لنا عن أجدادنا الأبطال وكيف كانوا يعيشون في البيوت القديمة الجميلة.",
        "questions": [
            "عن ماذا تحكي لنا قصص زمان؟",
            "من هم الأبطال الذين نسمع عنهم في الحكايات؟",
            "أين كانت تساكن العائلات قديماً؟",
            "هل تحب الاستماع إلى القصص القديمة؟",
            "هل كان للأجداد حياة جميلة وبسيطة؟",
            "هل تعلمنا القصص التاريخية أشياء مفيدة؟",
            "هل تحب معرفة كيف كان يعيش الناس قديماً؟",
            "هل تخبرنا الجدة قصصاً حلوة عن الماضي؟",
            "هل الماضي مليء بالحكايات الممتعة؟",
            "هل تحب سماع قصص الأبطال قبل النوم؟"
        ],
        "keywords": [
            "أجدادنا الأبطال",
            "أجدادنا",
            "البيوت القديمة",
            "نعم",
            "نعم",
            "نعم",
            "نعم",
            "نعم",
            "نعم",
            "نعم"
        ]
    }
}

def generate_certificate(student_name, avg_score):
    if avg_score >= 60 and os.path.exists("template_arabic.png"):
        try:
            image = Image.open("template_arabic.png")
            draw = ImageDraw.Draw(image)
            font = ImageFont.load_default()
            draw.text((400, 500), f"{student_name} - Avg: {avg_score:.2f}", fill="black", font=font)
            image.save(f"Certificate_{student_name}.png")
            return True
        except Exception:
            return False
    return False

def update_results(course_name, score):
    results = {}
    if os.path.exists("results.json"):
        with open("results.json", "r", encoding="utf-8") as f:
            try: 
                results = json.load(f)
            except json.JSONDecodeError: 
                results = {}
    results[course_name] = score
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False)
    return sum(results.values()) / len(results) if results else 0

def main(page: ft.Page):
    page.title = "Smart Academy - التعلم التكيفي"
    page.rtl = True  # دعم اتجاه الواجهة من اليمين لليسار
    
    main_container = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    
    course_dropdown = ft.Dropdown(
        label="اختر مساراً أو دورة",
        options=[ft.dropdown.Option(k) for k in COURSES.keys()],
        width=300
    )
    status_text = ft.Text("", size=16)

    def show_home(e=None):
        main_container.controls.clear()
        main_container.controls.extend([
            ft.Text("Smart Academy", size=30, weight="bold"),
            ft.Text("منصتك التعليمية الذكية", size=16),
            ft.Divider(height=20),
            course_dropdown,
            ft.Row([
                ft.ElevatedButton("▶ بدء الدرس", on_click=start_lesson),
                ft.ElevatedButton("📝 تقديم اختبار", on_click=goto_exam)
            ], alignment=ft.MainAxisAlignment.CENTER),
            status_text
        ])
        page.update()

    def show_exam_mode(course_name):
        main_container.controls.clear()
        score_input = ft.TextField(label="ادخل معدلك (0-100)", keyboard_type=ft.KeyboardType.NUMBER, width=300)
        
        def save_and_certify(e):
            if not score_input.value.replace('.', '', 1).isdigit():
                status_text.value = "⚠️ معدل غير صالح، أدخل رقماً صحيحاً!"
            else:
                score = float(score_input.value)
                if 0 <= score <= 100:
                    avg = update_results(course_name, score)
                    status_text.value = f"✅ تم الحفظ بنجاح، المعدل التراكمي: {avg:.2f}"
                    if generate_certificate("الطالبة", avg):
                        status_text.value += "\n🎉 تم إصدار الشهادة بنجاح!"
                else:
                    status_text.value = "⚠️ يجب أن يكون المعدل بين 0 و 100!"
            page.update()

        main_container.controls.extend([
            ft.Text(f"اختبار مسار: {course_name}", size=22, weight="bold"),
            score_input,
            ft.Row([
                ft.ElevatedButton("إنهاء الاختبار والحفظ", on_click=save_and_certify),
                ft.OutlinedButton("العودة للقائمة", on_click=show_home)
            ], alignment=ft.MainAxisAlignment.CENTER),
            status_text
        ])
        page.update()

    def goto_exam(e):
        if not course_dropdown.value:
            status_text.value = "⚠️ من فضلك اختر دورة أولاً!"
            page.update()
            return
        show_exam_mode(course_dropdown.value)

    def start_lesson(e):
        if not course_dropdown.value:
            status_text.value = "⚠️ من فضلك اختر دورة أولاً!"
            page.update()
            return
        
        selected_link = COURSES[course_dropdown.value]['link']
        main_container.controls.clear()
        main_container.controls.extend([
            ft.Text(f"جاري فتح الدرس لـ: {course_dropdown.value}", size=20, weight="bold"),
            ft.ElevatedButton("🌐 فتح رابط الدرس في المتصفح", on_click=lambda _: webbrowser.open(selected_link)),
            ft.OutlinedButton("العودة للقائمة", on_click=show_home),
            status_text
        ])
        page.update()

    show_home()
    page.add(main_container)

if __name__ == "__main__":
    ft.app(target=main)