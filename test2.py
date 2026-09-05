import json
import os
import webbrowser
import flet as ft
from PIL import Image, ImageDraw, ImageFont

# تعريف الدورات مع محتوى الدروس والأسئلة والكلمات المفتاحية
COURSES = {
        
    "python": {
        "link": "https://www.sololearn.com/en/learn/courses/python-introduction",
        "content_text": "Python is a popular, high-level programming language known for its simple English-like syntax. It is widely used in web development, data science, artificial intelligence, and task automation. Python code uses indentation for blocks and supports multiple programming paradigms.",
        "questions": [
            "What kind of programming language is Python considered to be?",
            "What type of syntax does Python use that makes it easy to learn?",
            "Is Python widely used in data science and artificial intelligence?",
            "What field involves building websites and web applications using Python?",
            "What feature does Python use instead of curly braces for blocks?",
            "Can Python be used to automate repetitive tasks?",
            "Is Python suitable for beginners with no prior coding experience?",
            "Does Python support multiple programming paradigms?",
            "Is Python a high-level programming language?",
            "Does Python make writing code faster and more readable?"
        ],
        "keywords": [
            "programming language",
            "english-like",
            "yes",
            "web development",
            "indentation",
            "yes",
            "yes",
            "yes",
            "high-level",
            "yes"
        ]
    },
    "literature": {
        "link": "https://www.noredink.com",
        "content_text": "Literature helps us explore human nature, stories, poems, and creative writing across different historical eras.",
        "questions": [
            "What does literature help us explore regarding people?",
            "Does literature include stories and fictional narratives?",
            "Are poems a part of what literature allows us to discover?",
            "What form of writing involves artistic expression and imagination?",
            "Across what kind of periods or eras do we study literature?",
            "Does literature give us insight into human nature?",
            "Can we read creative writing in literary works?",
            "Does literature cover different historical eras?",
            "Is exploring stories and poems part of studying literature?",
            "Does literature include creative writing?"
        ],
        "keywords": [
            "human nature",
            "yes",
            "yes",
            "creative writing",
            "historical eras",
            "yes",
            "yes",
            "yes",
            "yes",
            "yes"
        ]
    },
    "science": {
        "link": "https://bio.libretexts.org",
        "content_text": "Science studies the physical and natural world through observation, experimentation, and evidence-based research.",
        "questions": [
            "What world does science study and seek to understand?",
            "What method involves watching and carefully looking at nature?",
            "What process involves testing hypotheses through laboratory or field tests?",
            "Is evidence-based research important in scientific studies?",
            "Does science study the physical aspects of our world?",
            "Can we learn about the natural world through observation?",
            "Are experiments used to gather scientific data?",
            "Does scientific research rely heavily on solid evidence?",
            "Is studying the natural world a core part of science?",
            "Do scientists use experimentation to test their ideas?"
        ],
        "keywords": [
            "natural world",
            "observation",
            "experimentation",
            "yes",
            "yes",
            "yes",
            "yes",
            "yes",
            "yes",
            "yes"
        ]
    },
    "Languages": {
        "link": "https://www.clozemaster.com",
        "content_text": "Learning languages opens doors to new cultures, improves cognitive skills, and enhances global communication.",
        "questions": [
            "What do learning languages open doors to for individuals?",
            "What kind of skills does studying a new language improve?",
            "What type of communication is enhanced by knowing multiple languages?",
            "Do new languages help us understand different cultures?",
            "Can mastering a new language boost your brain and cognitive abilities?",
            "Is global communication improved when people speak foreign languages?",
            "Does language learning provide access to new traditions and societies?",
            "Are cognitive skills enhanced through regular language practice?",
            "Does studying languages help people connect across the globe?",
            "Is learning languages a valuable tool for personal growth?"
        ],
        "keywords": [
            "cultures",
            "cognitive skills",
            "global",
            "yes",
            "yes",
            "yes",
            "yes",
            "yes",
            "yes",
            "yes"
        ]
    },
    "warfars": {
        "link": "https://cain.ulster.ac.uk",
        "content_text": "The study of conflicts and history helps society understand peace-building processes and historical impacts.",
        "questions": [
            "What do the study of conflicts and history help society understand?",
            "What processes are better understood by examining past conflicts?",
            "What kind of impacts do we analyze when studying historical events and wars?",
            "Does studying past conflicts help society build a better future?",
            "Are peace-building processes linked to understanding historical conflicts?",
            "Can history teach us important lessons about avoiding future wars?",
            "Does examining past conflicts reveal the deep impacts of history?",
            "Is understanding peace-building essential for societies affected by conflict?",
            "Do historical studies cover the impacts of past conflicts?",
            "Does studying conflicts contribute to long-term peace?"
        ],
        "keywords": [
            "peace-building",
            "peace-building",
            "historical impacts",
            "yes",
            "yes",
            "yes",
            "yes",
            "yes",
            "yes",
            "yes"
        ]
    },
    "Knitting": {
        "link": "https://www.ravelry.com",
        "content_text": "Knitting is a handicraft method where yarn is manipulated using needles to create cozy garments like scarves and sweaters.",
        "questions": [
            "What tool is used in knitting with yarn?",
            "Can you make scarves using this handicraft method?",
            "What general category of craft does knitting belong to?",
            "What material is primarily manipulated during the knitting process?",
            "What type of cozy items or clothing can be produced with this technique?",
            "How does the text define the physical action performed on the yarn?",
            "Are sweaters considered one of the final garments created through knitting?",
            "Does the method rely on rigid instruments to shape the yarn into garments?",
            "In what way do the needles interact with the yarn according to the definition?",
            "What is the ultimate functional purpose of manipulating yarn with needles in this context?"
        ],
        "keywords": [
            "needles",
            "yes",
            "handicraft",
            "yarn",
            "sweaters",
            "manipulated",
            "yes",
            "yes",
            "manipulated",
            "create cozy garments"
        ]
    },
    "Drawing": {
        "link": "https://drawabox.com",
        "content_text": "Drawing builds fundamental skills in perspective, lines, shapes, and visual expression using pencils and paper.",
        "questions": [
            "What tools are typically used for basic drawing?",
            "Does drawing build perspective skills?",
            "What type of foundational elements and dimensions are developed through drawing?",
            "How does drawing help artists express themselves visually?",
            "What physical medium and surface are mentioned as standard tools for this craft?",
            "Are lines considered part of the core skills built by this practice?",
            "Does the training enhance an artist's grasp of geometric forms and shapes?",
            "In what way do pencils and paper contribute to the learning process?",
            "Why are perspective and lines emphasized as fundamental in this context?",
            "What is the ultimate creative outcome of practicing with pencils and paper according to the text?"
        ],
        "keywords": [
            "pencils",
            "yes",
            "perspective",
            "visual expression",
            "paper",
            "yes",
            "yes",
            "fundamental skills",
            "fundamental skills",
            "visual expression"
        ]
    },
    "Physics": {
        "link": "https://www.nasa.gov/kidsclub",
        "content_text": "Physics explores matter, energy, motion, and the fundamental forces governing the universe around us.",
        "questions": [
            "What does physics explore besides energy?",
            "Does it study motion?",
            "What physical components and dynamic properties are investigated in physics?",
            "What type of forces are described as governing the universe around us?",
            "How does physics help us understand the broader environment or cosmos?",
            "Is matter considered a central topic of exploration in this field?",
            "Does the study of motion include how objects move through space?",
            "In what scale or scope do the fundamental forces operate according to the text?",
            "Why are fundamental forces essential for understanding the universe in physics?",
            "What is the comprehensive scope of concepts that physics examines regarding our reality?"
        ],
        "keywords": [
            "matter",
            "yes",
            "matter and motion",
            "fundamental forces",
            "governing the universe",
            "yes",
            "yes",
            "universe",
            "governing the universe",
            "matter, energy, motion"
        ]
    },
    "Self-development": {
        "link": "https://www.coursera.org",
        "content_text": "Self-development focuses on improving personal skills, productivity, emotional intelligence, and lifelong learning habits.",
        "questions": [
            "What does self-development focus on improving?",
            "Is lifelong learning considered a habit?",
            "What kind of intelligence related to emotions and feelings does self-development target?",
            "How does self-development affect an individual's efficiency and daily output?",
            "What type of abilities and talents are enhanced through personal growth?",
            "Are habits of continuous learning central to this practice?",
            "Does emotional intelligence help individuals manage their interpersonal relations better?",
            "In what way do productivity and personal skills work together in self-development?",
            "Why is cultivating lifelong learning habits essential for long-term growth?",
            "What is the comprehensive objective of focusing on these specific areas of self-improvement?"
        ],
        "keywords": [
            "personal skills",
            "yes",
            "emotional intelligence",
            "productivity",
            "personal skills",
            "yes",
            "yes",
            "productivity",
            "lifelong learning",
            "improving personal skills"
        ]
    },
   "Public Speaking": {
        "link": "https://www.virtualorator.com",
        "content_text": "Public speaking involves delivering structured presentations clearly, engaging audiences, and building persuasive communication skills.",
        "questions": [
            "What does public speaking involve delivering?",
            "Should communication be persuasive?",
            "How should presentations be organized and delivered according to the text?",
            "What group of people does a speaker need to interact with and connect to?",
            "What type of communication skills are built through public speaking practice?",
            "Are structured formats important when presenting information to others?",
            "Does public speaking require clarity in how messages are conveyed?",
            "In what way does engaging listeners affect the overall delivery?",
            "Why is building persuasive skills a key outcome of mastering public speaking?",
            "What is the combined objective of structuring presentations and engaging listeners?"
        ],
        "keywords": [
            "presentations",
            "yes",
            "structured",
            "audiences",
            "persuasive communication",
            "yes",
            "yes",
            "engaging audiences",
            "persuasive communication",
            "delivering structured presentations"
        ]
    },
    "Reading": {
        "link": "https://unesdoc.unesco.org",
        "content_text": "Reading transcends the mere mechanical decoding of symbols; it is an active, cognitive synthesis wherein the human intellect navigates complex semantic landscapes. Through the intricate architecture of syntax and lexicon, literary and informational texts function as catalysts for critical consciousness, expanding cognitive horizons, refining abstract reasoning, and challenging ontological assumptions. Far from being a passive receptacle of information, the proficient reader engages in a dialectical negotiation with the text, deconstructing underlying ideologies, evaluating rhetorical validity, and assimilating multifaceted perspectives that ultimately reconstruct their worldview.",
        "questions": [
            "According to the text, what is reading considered to be beyond mechanical decoding?",
            "What do literary and informational texts function as for critical consciousness?",
            "How do complex semantic landscapes get navigated by the human intellect?",
            "What specific aspects of reasoning and cognition are refined through advanced reading?",
            "In what manner does a proficient reader approach a text rather than acting as a passive recipient?",
            "What does the text state that advanced reading actively challenges regarding human thought?",
            "What specific role do syntax and lexicon play within the architecture of a text?",
            "How does the dialectical negotiation between the reader and the text affect underlying ideologies?",
            "What is the ultimate psychological and cognitive outcome of assimilating multifaceted perspectives through reading?",
            "Why is the process of deconstructing rhetorical validity essential to the reader's engagement with complex texts?"
        ],
        "keywords": [
            "active, cognitive synthesis",
            "catalysts for critical consciousness",
            "intricate architecture of syntax and lexicon",
            "abstract reasoning",
            "dialectical negotiation",
            "ontological assumptions",
            "catalysts",
            "deconstructing underlying ideologies",
            "reconstruct their worldview",
            "evaluating rhetorical validity"
        ]
    }
}

def generate_certificate(student_name, avg_score):
    if avg_score >= 60 and os.path.exists("template_english.png"):
        try:
            image = Image.open("template_english.png")
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
    page.title = "Smart Academy - Adaptive Learning"
    page.rtl = False  # دعم اتجاه الواجهة من اليسار لليمين
    
    main_container = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    
    course_dropdown = ft.Dropdown(
        label="Select a track or course",
        options=[ft.dropdown.Option(k) for k in COURSES.keys()],
        width=300
    )
    status_text = ft.Text("", size=16)

    def show_home(e=None):
        main_container.controls.clear()
        main_container.controls.extend([
            ft.Text("Smart Academy", size=30, weight="bold"),
            ft.Text("Your Smart Learning Platform", size=16),
            ft.Divider(height=20),
            course_dropdown,
            ft.Row([
                ft.ElevatedButton("▶ Start Lesson", on_click=start_lesson),
                ft.ElevatedButton("📝 Take Exam", on_click=goto_exam)
            ], alignment=ft.MainAxisAlignment.CENTER),
            status_text
        ])
        page.update()

    def show_exam_mode(course_name):
        main_container.controls.clear()
        
        course_data = COURSES[course_name]
        lesson_text = course_data["content_text"]
        question_text = course_data["questions"][0]
        expected_keyword = course_data["keywords"][0].lower()

        answer_input = ft.TextField(
            label="Your Answer based on the lesson",
            width=300,
            hint_text="Type your answer..."
        )
        exam_status = ft.Text("", size=16)
        
        def python_auto_correct(e):
            user_ans = answer_input.value.lower().strip()
            if not user_ans:
                exam_status.value = "⚠️ Please type an answer before submitting!"
                page.update()
                return

            if expected_keyword in user_ans or user_ans in lesson_text.lower():
                score = 100.0
                exam_status.value = "🎉 Correct! Verified from the lesson text."
            else:
                score = 0.0
                exam_status.value = "❌ Incorrect. Review the lesson text carefully."

            avg = update_results(course_name, score)
            if generate_certificate("Student", avg):
                exam_status.value += "\n🏆 Certificate issued successfully!"

            page.update()

        main_container.controls.extend([
            ft.Text(f"Exam Track: {course_name}", size=22, weight="bold"),
            ft.Divider(),
            ft.Text(f"📖 Lesson Content:\n'{lesson_text}'", size=14, italic=True, text_align=ft.TextAlign.CENTER),
            ft.Divider(),
            ft.Text(f"❓ Question: {question_text}", size=16, weight="w500", text_align=ft.TextAlign.CENTER),
            answer_input,
            ft.Row([
                ft.ElevatedButton("Submit & Check Answer", on_click=python_auto_correct),
                ft.OutlinedButton("Back to Menu", on_click=show_home)
            ], alignment=ft.MainAxisAlignment.CENTER),
            exam_status
        ])
        page.update()

    def goto_exam(e):
        if not course_dropdown.value:
            status_text.value = "⚠️ Please select a course first!"
            page.update()
            return
        show_exam_mode(course_dropdown.value)

    def start_lesson(e):
        if not course_dropdown.value:
            status_text.value = "⚠️ Please select a course first!"
            page.update()
            return
        
        selected_link = COURSES[course_dropdown.value]['link']
        main_container.controls.clear()
        main_container.controls.extend([
            ft.Text(f"Opening lesson for: {course_dropdown.value}", size=20, weight="bold"),
            ft.ElevatedButton("🌐 Open lesson link in browser", on_click=lambda _: webbrowser.open(selected_link)),
            ft.OutlinedButton("Back to Menu", on_click=show_home),
            status_text
        ])
        page.update()

    show_home()
    page.add(main_container)

if __name__ == "__main__":
    ft.app(target=main)