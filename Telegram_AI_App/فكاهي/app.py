import textwrap
import ollama
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# دالة تطبيق تعليماتك: تقسيم النص لأسطر لا تتجاوز 40 حرفاً
def smart_wrap(text):
    wrapper = textwrap.TextWrapper(width=40, break_long_words=False)
    return "\n".join(wrapper.wrap(text))

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_query = request.json.get("message", "")

        # --- الجزء الفكاهي المطور ---
        # نستخدم الـ System Prompt لإعطائه الشخصية المطلوبة
        response = ollama.chat(model='llama3', messages=[
            {
                'role': 'system', 
                'content': 'أنت مساعد فكاهي ساخر في قناة الحسام. ردودك قصيرة جداً ومليئة بالمرح.'
            },
            {'role': 'user', 'content': user_query},
        ])

        answer = response['message']['content']
        
        # تطبيق قاعدة لؤي الرازي: جمل قصيرة وسطر جديد
        return jsonify({"answer": smart_wrap(answer)})

    except Exception as e:
        # تعليق السطر القديم الذي يظهر الخطأ التقني
        # return jsonify({"error": str(e)}) 
        return jsonify({"answer": "أوه! يبدو أن Ollama أخذ استراحة شاي. تأكد من تشغيله!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)