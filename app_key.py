# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import requests
import smtplib

app = Flask(__name__)

# هذا هو المفتاح الخارق الخاص بكِ أنتِ وحدك!
MY_SUPER_API_KEY = "GSA_SUPER_KEY_CHaimae_2026_999"

@app.route("/")
def home():
    return '''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>Global Smart Academy - السيرفر الخارق</title>
        <style>
            body { background-color: #0f172a; color: #f8fafc; font-family: Tahoma, sans-serif; text-align: center; padding: 30px; }
            h1 { color: #38bdf8; }
            .chat-box { width: 100%; max-width: 500px; margin: 0 auto; background: #1e293b; padding: 15px; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); text-align: right; }
            textarea { width: 100%; height: 80px; background: #0f172a; color: #fff; border: 1px solid #334155; border-radius: 8px; padding: 10px; font-size: 14px; resize: none; box-sizing: border-box; }
            button { background: #0284c7; color: white; border: none; padding: 8px 16px; border-radius: 8px; font-size: 14px; cursor: pointer; margin-top: 10px; width: 100%; }
            button:hover { background: #0ea5e9; }
            #response { margin-top: 15px; background: #334155; padding: 10px; border-radius: 8px; min-height: 40px; text-align: right; white-space: pre-wrap; font-size: 14px; }
        </style>
    </head>
    <body>
        <h1>Global Smart Academy 🚀</h1>
        <p>المساعد الذكي جاهز لمساعدتك!</p>
        
        <div class="chat-box">
            <textarea id="userInput" placeholder="اطرحي سؤالك على جلوبال..."></textarea>
            <button onclick="sendMessage()">إرسال ⚡</button>
            <div id="response">انتظار الرد...</div>
        </div>

        <script>
            async function sendMessage() {
                const text = document.getElementById('userInput').value;
                const resDiv = document.getElementById('response');
                resDiv.innerText = "جاري إرسال الطلب... ⏳";
                
                try {
                    const response = await fetch('/chat', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-API-Key': 'GSA_SUPER_KEY_CHaimae_2026_999'
                        },
                        body: JSON.stringify({message: text})
                    });
                    
                    const data = await response.json();
                    resDiv.innerText = data.reply;
                } catch (err) {
                    resDiv.innerText = "حدث خطأ في الاتصال بالسيرفر.";
                }
            }
        </script>
    </body>
    </html>
    '''

@app.route("/chat", methods=["POST"])
def chat():
    client_key = request.headers.get("X-API-Key")
    if client_key != MY_SUPER_API_KEY:
        return jsonify({"reply": "⛔ مرفوض! عذراً، المفتاح غير صحيح."}), 403

    data = request.get_json()
    user_message = data.get("message", "") if data else ""
    
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "gemma:2b",
        "prompt": user_message,
        "stream": False,
        "options": {
            "num_predict": 120
        }
    }
    
    try:
        response = requests.post(url, json=payload)
        result = response.json()
        reply_text = result.get("response", "عذراً، لم أستطع الرد.")
        return jsonify({"reply": reply_text})
    except Exception as e:
        return jsonify({"reply": f"خطأ في الاتصال بالنموذج المحلي: {str(e)}"})

def run_ai_server():
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)

if __name__ == '__main__':
    run_ai_server()