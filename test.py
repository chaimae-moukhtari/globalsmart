import json
import os
import urllib.parse
import webbrowser
import flet as ft
from PIL import Image, ImageDraw, ImageFont

# 1. إعدادات الدورات مع المحتوى النصي والأسئلة والكلمات المفتاحية
COURSES = {
    "Ethics": {
        "link": "https://www.sesamestreet.org/games",
        "content_text": "Ethics and values mean being kind, sharing toys with friends, helping others, and telling the truth always.",
        "questions": [
            "According to the lessons, what should you do with friends?",
            "Is it important to be helpful with your family?",
            "What do you say to your friend when they share a nice toy with you?",
            "If you take a toy from your friend without asking, what should you do?",
            "Do you like sharing your toys and colors with your friends and siblings?",
            "When mommy or daddy asks you to clean up your toys, do you help them?",
            "If you see your friend crying or falling down, what can you do to help?",
            "Do you always tell the truth, even if you made a mistake?",
            "When you meet someone new or enter a room, what friendly greeting do you say?",
            "Is it nice to use a soft, gentle voice with our friends instead of shouting?"
        ],
        "keywords": [
            "sharing",
            "yes",
            "thank you",
            "sorry",
            "sharing",
            "help",
            "kind",
            "truth",
            "hello",
            "soft voice"
        ]
    },
    "Reading": {
        "link": "https://www.getepic.com",
        "content_text": "Once upon a time, a little brown bear lived in a green forest. He loved eating sweet honey and playing with his friends under the big tree every sunny day.",
        "questions": [
            "What kind of animal lived in the green forest?",
            "What did the little bear love to eat?",
            "Where did the bear play with his friends?",
            "Did they play under the big tree?",
            "How was the weather in the story?",
            "What color was the little bear?",
            "How did the bear describe the taste of the honey?",
            "Who did the bear play with?",
            "Did the bear play with his friends every sunny day?",
            "What color was the forest where he lived?"
        ],
        "keywords": [
            "bear",
            "honey",
            "tree",
            "yes",
            "sunny",
            "brown",
            "sweet",
            "friends",
            "yes",
            "green"
        ]
    },
    "Basic Science": {
        "link": "https://peepandthebigwideworld.com",
        "content_text": "Peep is a yellow chick, Chirp is a pink duck, and Quack is a blue fish who lives in a pond. They explore nature together, learning that plants need water and the sun gives us warmth. They also notice shadows following them on sunny days and rain falling from the grey clouds.",
        "questions": [
            "What is the name of the yellow little chick who loves to explore the big wide world?",
            "Who is Peep's best friend that is a pink duck?",
            "What is the name of the funny blue fish who lives in a pond?",
            "What do plants need every day to grow big and strong?",
            "What bright star shines in the sky during the day to give us light and warmth?",
            "What follows you around on the ground when you walk outside on a sunny day?",
            "What falls from the sky when the clouds get heavy and grey?",
            "What do birds use to fly high up in the blue sky?",
            "Where does the blue fish Quack live?",
            "Is science fun when we look at nature and ask questions?"
        ],
        "keywords": [
            "peep",
            "chirp",
            "quack",
            "water",
            "sun",
            "shadow",
            "rain",
            "wings",
            "pond",
            "yes"
        ]
    },
    "Scratch": {
        "link": "https://www.scratchjr.org",
        "content_text": "ScratchJr programming uses colorful visual blocks to build stories and games. You click the green flag to start scripts, use sprites like characters to move around, and can make things jump, grow, or disappear on the screen.",
        "questions": [
            "What kind of blocks are used in ScratchJr programming?",
            "What flag is clicked to start scripts and make things move?",
            "What are the characters in the app called?",
            "Can you use visual blocks to build fun stories and games?",
            "What color is the flag that starts the script?",
            "What can you make your sprites do on the screen, like jumping?",
            "Is ScratchJr used to create fun animations?",
            "Do you touch or click blocks to snap them together?",
            "Can you make characters grow or disappear?",
            "Is coding with blocks fun for kids?"
        ],
        "keywords": [
            "visual blocks",
            "green flag",
            "sprites",
            "yes",
            "green",
            "jump",
            "animations",
            "click",
            "grow",
            "yes"
        ]
    },
    "Chores": {
        "link": "https://habitica.com",
        "content_text": "Habitica is a fun gamified app that turns daily chores and tasks into a game. Learning chores involves cleaning your room, organizing desks, completing habits, and helping parents with daily home tasks to win gold and rewards.",
        "questions": [
            "What kind of app is Habitica that turns daily chores into a game?",
            "What does learning chores involve doing to your room?",
            "Which place in the house should you clean according to the text?",
            "What should you do with your desks?",
            "Who should you help with daily home tasks?",
            "What do you win when you complete tasks and habits in the game?",
            "Are these tasks related to home or school?",
            "Do you help your parents with tasks?",
            "Is learning chores and habits a fun activity?",
            "What is the main platform name used for gamifying tasks?"
        ],
        "keywords": [
            "gamified",
            "cleaning",
            "room",
            "organizing",
            "parents",
            "gold",
            "home",
            "yes",
            "yes",
            "habitica"
        ]
    },
    "Cooking": {
        "link": "https://kitchenlittle.com",
        "content_text": "Cooking basics include washing hands before preparing food, using safe tools, wearing a small apron, and following simple recipes to make healthy meals and delicious snacks.",
        "questions": [
            "What should you do with your hands before cooking?",
            "What kind of tools should you use while preparing food?",
            "What do you wear to keep your clothes clean while cooking?",
            "What kind of recipes should you follow when making food?",
            "Should you wash your hands before preparing food?",
            "Are healthy meals and delicious snacks made in the kitchen?",
            "Is kitchen safety important for kids?",
            "Do we use safe tools to cut soft food?",
            "Is cooking a fun activity to learn at home?",
            "What is the main topic of this cooking lesson?"
        ],
        "keywords": [
            "washing hands",
            "safe tools",
            "apron",
            "simple",
            "yes",
            "meals",
            "yes",
            "safe",
            "yes",
            "cooking"
        ]
    },
    "History": {
        "link": "https://historyforkids.net",
        "content_text": "History for kids explores fascinating ancient civilizations, grand pyramids built by Egyptians, maps of old kingdoms, and the amazing stories of people from the past.",
        "questions": [
            "Who built the pyramids according to history lessons?",
            "What kind of civilizations does history for kids explore?",
            "What grand structures did the Egyptians build?",
            "What do we look at to find old kingdoms?",
            "Are there maps of old kingdoms in the lessons?",
            "Does history tell amazing stories of people from the past?",
            "Did ancient Egyptians build the pyramids?",
            "Is exploring old kingdoms and civilizations fun?",
            "What is the main subject of these lessons?",
            "Do kids learn about the past in history?"
        ],
        "keywords": [
            "egyptians",
            "ancient",
            "pyramids",
            "maps",
            "yes",
            "yes",
            "yes",
            "yes",
            "history",
            "yes"
        ]
    }
}


def generate_certificate(student_name, avg_score):
    if avg_score >= 60 and os.path.exists("template_english.png"):
        try:
            image = Image.open("template_english.png")
            draw = ImageDraw.Draw(image)
            font = ImageFont.load_default()
            draw.text(
                (400, 500),
                f"{student_name} - Avg: {avg_score:.2f}",
                fill="black",
                font=font,
            )
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
    page.rtl = False  # اتجاه الواجهة من اليسار لليمين

    main_container = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    course_dropdown = ft.Dropdown(
        label="Select a track or course",
        options=[ft.dropdown.Option(k) for k in COURSES.keys()],
        width=300,
    )
    status_text = ft.Text("", size=16)

    def show_home(e=None):
        main_container.controls.clear()
        main_container.controls.extend(
            [
                ft.Text("Smart Academy", size=30, weight="bold"),
                ft.Text("Your Smart Learning Platform", size=16),
                ft.Divider(height=20),
                course_dropdown,
                ft.Row(
                    [
                        ft.ElevatedButton(
                            "▶ Start Lesson", on_click=start_lesson
                        ),
                        ft.ElevatedButton("📝 Take Exam", on_click=goto_exam),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                status_text,
            ]
        )
        page.update()

    def show_exam_mode(course_name):
        main_container.controls.clear()

        course_data = COURSES[course_name]
        lesson_text = course_data["content_text"]
        
        # اختيار أول سؤال وكبديله الكلمة المفتاحية الأولى (أو يمكن ربطها بأسئلة متعددة حسب الرغبة)
        question_text = course_data["questions"][0]
        expected_keyword = course_data["keywords"][0].lower()

        answer_input = ft.TextField(
            label="Your Answer based on the lesson",
            width=300,
            hint_text="Type your answer...",
        )
        exam_status = ft.Text("", size=16)

        def python_auto_correct(e):
            user_ans = answer_input.value.lower().strip()
            if not user_ans:
                exam_status.value = (
                    "⚠️ Please type an answer before submitting!"
                )
                page.update()
                return

            if (
                expected_keyword in user_ans
                or user_ans in lesson_text.lower()
            ):
                score = 100.0
                exam_status.value = (
                    "🎉 Correct! Python verified your answer from the lesson text."
                )
            else:
                score = 0.0
                exam_status.value = f"❌ Incorrect. Review the lesson text carefully."

            avg = update_results(course_name, score)
            if generate_certificate("Student", avg):
                exam_status.value += "\n🏆 Certificate issued successfully!"

            page.update()

        main_container.controls.extend(
            [
                ft.Text(
                    f"Exam Track: {course_name}", size=22, weight="bold"
                ),
                ft.Divider(),
                ft.Text(
                    f"📖 Lesson Content Read Today:\n'{lesson_text}'",
                    size=14,
                    italic=True,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Divider(),
                ft.Text(
                    f"❓ Question: {question_text}",
                    size=16,
                    weight="w500",
                    text_align=ft.TextAlign.CENTER,
                ),
                answer_input,
                ft.Row(
                    [
                        ft.ElevatedButton(
                            "Submit & Python Check",
                            on_click=python_auto_correct,
                        ),
                        ft.OutlinedButton(
                            "Back to Menu", on_click=show_home
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                exam_status,
            ]
        )
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

        selected_link = COURSES[course_dropdown.value]["link"]
        main_container.controls.clear()
        main_container.controls.extend(
            [
                ft.Text(
                    f"Opening lesson for: {course_dropdown.value}",
                    size=20,
                    weight="bold",
                ),
                ft.ElevatedButton(
                    "🌐 Open lesson link in browser",
                    on_click=lambda _: webbrowser.open(selected_link),
                ),
                ft.OutlinedButton("Back to Menu", on_click=show_home),
                status_text,
            ]
        )
        page.update()

    show_home()
    page.add(main_container)


if __name__ == "__main__":
    ft.app(target=main)