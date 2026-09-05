import json
import os
import webbrowser
import flet as ft
from PIL import Image, ImageDraw, ImageFont

# إعدادات الدورات بالمستوى المعقد والمتقدم جداً
COURSES = {
    "AI": {
        "link": "https://www.fast.ai",
        "content_text": "Artificial Intelligence involves the cybernetic simulation of synthetic cognition, leveraging multidimensional vector spaces, deep neural backpropagation, and heuristic optimization landscapes to autonomously approximate complex empirical phenomena.",
        "questions": [
            "What cybernetic process does Artificial Intelligence fundamentally involve?",
            "What mathematical structures are leveraged for synthetic cognition in vector spaces?",
            "How do deep neural networks optimize learning through structural feedback loops?",
            "What kind of landscapes are navigated by heuristic optimization algorithms?",
            "What is the ultimate empirical objective of approximating complex phenomena autonomously?",
            "In what manner do vector spaces handle multidimensional data representation?",
            "Why is backpropagation considered crucial for neural network adaptation?",
            "How do heuristic methods bypass traditional computational bottlenecks?",
            "What distinguishes synthetic cognition from organic information processing?",
            "What is the overarching epistemological goal of automated heuristic approximation?"
        ],
        "keywords": [
            "simulation of synthetic cognition",
            "multidimensional vector spaces",
            "backpropagation",
            "heuristic optimization landscapes",
            "empirical phenomena",
            "multidimensional",
            "adaptation",
            "optimization",
            "synthetic",
            "epistemological"
        ]
    },
    "Java": {
        "link": "https://java-programming.moc.fi/",
        "content_text": "Java architecture relies on platform-independent bytecode execution via the Java Virtual Machine, enforcing strict object-oriented modularity, memory management through garbage collection, and robust type safety across enterprise systems.",
        "questions": [
            "What mechanism enables platform-independent execution in Java architecture?",
            "How does the Java Virtual Machine process compiled source code?",
            "What core programming paradigm is strictly enforced across system design?",
            "How is memory allocation and deallocation dynamically handled in the runtime environment?",
            "What attribute ensures variable consistency and reduces runtime bugs across enterprise systems?",
            "Why is bytecode considered central to Java's 'write once, run anywhere' philosophy?",
            "What structural benefits does object-oriented modularity provide to large codebases?",
            "How does automated garbage collection prevent memory leaks during execution?",
            "What role do types play in maintaining structural integrity during compilation?",
            "What is the ultimate architectural outcome of combining bytecode with virtual machine execution?"
        ],
        "keywords": [
            "bytecode execution",
            "Java Virtual Machine",
            "object-oriented modularity",
            "garbage collection",
            "type safety",
            "platform-independent",
            "modularity",
            "garbage collection",
            "structural integrity",
            "virtual machine execution"
        ]
    },
    "C++": {
        "link": "https://www.sololearn.com",
        "content_text": "C++ provides low-level memory manipulation and high-performance execution through deterministic resource management, supporting multi-paradigm software engineering via templates, metaprogramming, and direct hardware abstraction.",
        "questions": [
            "What level of memory control and system interaction does C++ grant developers?",
            "How does the language achieve exceptionally high-performance execution?",
            "What resource management philosophy ensures predictable destruction cycles?",
            "Which programming paradigms are unified under multi-paradigm software engineering?",
            "What advanced compile-time feature allows generic and type-independent code generation?",
            "How does metaprogramming shift computational weight from runtime to compile-time?",
            "What enables C++ code to interface directly with physical device architecture?",
            "Why is deterministic resource management critical for systems-level applications?",
            "In what ways do templates optimize code reusability without sacrificing speed?",
            "What is the primary architectural trade-off of having direct hardware abstraction?"
        ],
        "keywords": [
            "low-level memory manipulation",
            "high-performance execution",
            "deterministic resource management",
            "multi-paradigm software engineering",
            "templates",
            "compile-time",
            "hardware abstraction",
            "deterministic",
            "reusability",
            "hardware control"
        ]
    },
    "cybersecurity": {
        "link": "https://www.cybrary.it",
        "content_text": "Cybersecurity engineering defends distributed systems against adversarial exploitation by enforcing cryptographic protocols, zero-trust network architectures, vulnerability remediation, and continuous threat intelligence synthesis.",
        "questions": [
            "What primary threat does cybersecurity engineering protect distributed systems against?",
            "What mathematical mechanisms form the bedrock of data confidentiality and integrity?",
            "What modern architectural model assumes breach and verifies every access request?",
            "How does proactive vulnerability remediation alter an organization's security posture?",
            "What role does continuous threat intelligence synthesis play in defensive strategies?",
            "Why is perimeter-only defense inadequate against sophisticated adversarial exploitation?",
            "How do cryptographic protocols ensure non-repudiation in digital transactions?",
            "What operational principles govern a strict zero-trust network environment?",
            "In what ways does telemetry analysis aid in anomaly detection?",
            "What is the ultimate systemic objective of unifying intelligence with infrastructure defense?"
        ],
        "keywords": [
            "adversarial exploitation",
            "cryptographic protocols",
            "zero-trust network architectures",
            "vulnerability remediation",
            "threat intelligence synthesis",
            "sophisticated",
            "non-repudiation",
            "zero-trust",
            "anomaly detection",
            "infrastructure defense"
        ]
    },
    "Politics": {
        "link": "https://plato.stanford.edu",
        "content_text": "Political philosophy dissects the legitimacy of sovereign authority, distributive justice frameworks, institutional power dynamics, and the dialectical tensions between individual liberty and collective coercion.",
        "questions": [
            "What core aspect of sovereign power does political philosophy critically dissect?",
            "What philosophical frameworks evaluate the fair allocation of societal resources?",
            "How do institutional power dynamics shape civil obedience and state control?",
            "What dynamic tension exists between personal freedom and state-mandated restrictions?",
            "How does normative justification validate or invalidate governing institutions?",
            "What distinguishes legitimate authority from mere coercive dominance?",
            "In what ways do distributive justice models address structural inequality?",
            "Why are dialectical tensions central to understanding political evolution?",
            "How do social contract theories rationalize the inception of government?",
            "What is the ultimate philosophical aim of balancing liberty against collective coercion?"
        ],
        "keywords": [
            "legitimacy of sovereign authority",
            "distributive justice frameworks",
            "institutional power dynamics",
            "individual liberty and collective coercion",
            "normative justification",
            "coercive dominance",
            "structural inequality",
            "dialectical tensions",
            "social contract",
            "balancing liberty"
        ]
    },
    "Advanced Sciences": {
        "link": "https://arxiv.org",
        "content_text": "Advanced scientific inquiry transcends empirical observation, formulating rigorous mathematical models to unify quantum mechanics with general relativity while probing emergent cosmological anomalies.",
        "questions": [
            "Beyond empirical observation, what do advanced scientific inquiries formulate?",
            "What theoretical unification represents the holy grail of modern physics?",
            "Which two major theoretical frameworks struggle to reconcile at Planck scales?",
            "What types of unexplained cosmic phenomena are targeted by researchers?",
            "How do rigorous mathematical models validate unobservable subatomic interactions?",
            "Why is quantum gravity considered mathematically incompatible with smooth spacetime?",
            "What role do emergent properties play in complex physical systems?",
            "How do astrophysical anomalies challenge established standard models?",
            "In what ways does theoretical physics rely on abstract topological spaces?",
            "What is the overarching objective of synthesizing quantum mechanics with relativity?"
        ],
        "keywords": [
            "rigorous mathematical models",
            "unify quantum mechanics with general relativity",
            "quantum mechanics with general relativity",
            "cosmological anomalies",
            "mathematical models",
            "incompatible",
            "emergent properties",
            "standard models",
            "topological spaces",
            "synthesizing"
        ]
    },
    "University Prep": {
        "link": "https://www.coursera.org",
        "content_text": "Elite academic preparation demands the cultivation of metacognitive self-regulation, epistemological skepticism, advanced historiographical critique, and multidisciplinary synthesis for higher scholarly pursuits.",
        "questions": [
            "What higher-order cognitive tracking is cultivated during elite preparation?",
            "What philosophical stance encourages questioning underlying knowledge claims?",
            "How does historiographical critique transform the analysis of primary sources?",
            "Why is multidisciplinary synthesis essential for breakthrough academic research?",
            "In what manner does metacognitive self-regulation enhance autonomous studying?",
            "How does epistemological skepticism protect against dogmatic assumptions?",
            "What distinguishes advanced historiography from standard chronological retelling?",
            "How do disparate academic fields intersect during multidisciplinary synthesis?",
            "Why must scholarly aspirants master both quantitative and qualitative reasoning?",
            "What is the ultimate intellectual transformation expected from elite university prep?"
        ],
        "keywords": [
            "metacognitive self-regulation",
            "epistemological skepticism",
            "historiographical critique",
            "multidisciplinary synthesis",
            "metacognitive",
            "skepticism",
            "historiography",
            "intersect",
            "reasoning",
            "intellectual transformation"
        ]
    },
    "Advanced Literature": {
        "link": "https://www.poetryfoundation.org",
        "content_text": "Advanced literary hermeneutics deconstructs subtextual ideological matrices, narrative fragmentation, and ontological subversion, exposing how texts act as mirrors of existential angst and sociopolitical subversion.",
        "questions": [
            "What do advanced literary hermeneutics deconstruct within a text?",
            "How does narrative fragmentation affect the reader's linear comprehension?",
            "What philosophical disruption is caused by textual ontological subversion?",
            "In what ways do literary works function as mirrors of human condition?",
            "How does subtextual ideological critique reveal hidden power structures?",
            "Why is existential angst a recurring motif in modernist and postmodern texts?",
            "What mechanisms enable literature to act as an instrument of sociopolitical critique?",
            "How do structural shifts in poetry reflect deeper shifts in cultural consciousness?",
            "What is the significance of analyzing meta-narrative elements in prose?",
            "What is the ultimate objective of rigorous literary deconstruction?"
        ],
        "keywords": [
            "subtextual ideological matrices",
            "narrative fragmentation",
            "ontological subversion",
            "existential angst",
            "ideological critique",
            "existential angst",
            "sociopolitical critique",
            "cultural consciousness",
            "meta-narrative",
            "deconstruction"
        ]
    },
    "Reading": {
        "link": "https://gutenberg.org",
        "content_text": "Transcending passive decoding, advanced reading is an active dialectical confrontation where the intellect interrogates semantic structures, dismantles underlying rhetorical fallacies, and reconstructs overarching paradigms.",
        "questions": [
            "How does advanced reading differ fundamentally from passive decoding?",
            "What kind of intellectual confrontation occurs between reader and text?",
            "What precise elements of the text are actively interrogated by the mind?",
            "How does a critical reader handle underlying rhetorical fallacies?",
            "What is the ultimate structural outcome of engaging in this cognitive process?",
            "Why is dialectical engagement superior to linear information absorption?",
            "How does dismantling semantic structures expand a reader's intellectual framework?",
            "In what way do rhetorical fallacies compromise the validity of an argument?",
            "What mental faculty is required to reconstruct entire conceptual paradigms?",
            "What is the profound cognitive culmination of master-level text analysis?"
        ],
        "keywords": [
            "active dialectical confrontation",
            "dialectical confrontation",
            "semantic structures",
            "dismantles underlying rhetorical fallacies",
            "reconstructs overarching paradigms",
            "dialectical engagement",
            "intellectual framework",
            "validity",
            "conceptual paradigms",
            "cognitive culmination"
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
    page.title = "Smart Academy - Extreme Academic Level"
    page.rtl = False  
    
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
            ft.Text("Extreme Academic Track", size=16),
            ft.Divider(height=20),
            course_dropdown,
            ft.Row([
                ft.ElevatedButton("▶ Start Lesson", on_click=start_lesson),
                ft.ElevatedButton("📝 Take Hard Exam", on_click=goto_exam)
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
            label="Your precise academic answer",
            width=300,
            hint_text="Type technical answer..."
        )
        exam_status = ft.Text("", size=16)
        
        def python_auto_correct(e):
            user_ans = answer_input.value.lower().strip()
            if not user_ans:
                exam_status.value = "⚠️ Please type a technical answer before submitting!"
                page.update()
                return

            if expected_keyword in user_ans or user_ans in lesson_text.lower():
                score = 100.0
                exam_status.value = "🎉 Phenomenal! Deep academic insight verified."
            else:
                score = 0.0
                exam_status.value = "❌ Incorrect. Re-analyze the complex text structures."

            avg = update_results(course_name, score)
            if generate_certificate("Student", avg):
                exam_status.value += "\n🏆 Elite Certificate issued successfully!"

            page.update()

        main_container.controls.extend([
            ft.Text(f"Extreme Exam Track: {course_name}", size=22, weight="bold"),
            ft.Divider(),
            ft.Text(f"📖 Advanced Text:\n'{lesson_text}'", size=13, italic=True, text_align=ft.TextAlign.CENTER),
            ft.Divider(),
            ft.Text(f"❓ Complex Question: {question_text}", size=15, weight="w500", text_align=ft.TextAlign.CENTER),
            answer_input,
            ft.Row([
                ft.ElevatedButton("Submit & Validate Analysis", on_click=python_auto_correct),
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
            ft.Text(f"Opening advanced reference for: {course_dropdown.value}", size=20, weight="bold"),
            ft.ElevatedButton("🌐 Open research link in browser", on_click=lambda _: webbrowser.open(selected_link)),
            ft.OutlinedButton("Back to Menu", on_click=show_home),
            status_text
        ])
        page.update()

    show_home()
    page.add(main_container)

if __name__ == "__main__":
    ft.app(target=main)