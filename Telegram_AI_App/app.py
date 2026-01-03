import json
import os
import re
from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)

# دالة محسنة للبحث داخل مجلد data وملفات result1, result2
def analyze_json_archive(user_query):
    context_data = []
    # المسارات الجديدة للملفات داخل مجلد data
    json_files = [
        os.path.join('data', 'result1.json'),
        os.path.join('data', 'result2.json')
    ]
    
    search_terms = re.findall(r'\w+', user_query.lower())
    
    try:
        for file_path in json_files:
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # ملاحظة: تأكد أن مفتاح الرسائل في ملفاتك هو 'messages'
                    messages = data.get('messages', [])
                    
                    for msg in messages:
                        # تحويل محتوى الرسالة لنص للبحث فيه
                        text_content = str(msg.get('text', '')).lower()
                        sender = msg.get('from', 'عضو مجهول')
                        
                        # إذا احتوت الرسالة على أي كلمة من كلمات البحث
                        if any(term in text_content for term in search_terms):
                            context_data.append(f"{sender}: {msg.get('text')}")
        
        # نأخذ آخر 70 رسالة متعلقة بالبحث لضمان دقة التحليل
        return "\n".join(context_data[-70:])
    except Exception as e:
        return f"خطأ في الوصول للمجلد أو الملفات: {str(e)}"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        question = data.get('question', '')

        # 1. جلب البيانات من المجلد data والملفات المطلوبة
        historical_evidence = analyze_json_archive(question)

        # 2. بناء عقل الموديل التحليلي
        system_prompt = f"""
        أنت "المحلل الذكي" لأرشيف قناة الحسام.
        لديك صلاحية الوصول لـ 20 ألف رسالة مخزنة في مجلد data.
        
        قوانينك:
        1. التحليل العادل: لؤي، حسام، أحمد حاتم، محمد عبدالسلام، محمد زياد، النهاري، وسلطان هم أعضاء متساوون.
        2. الدقة التاريخية: استخلص الحقائق من الأرشيف المرفق أدناه ولا تؤلف من خيالك.
        3. كشف السلوك: ادرس كيف يتفاعل كل شخص وما هو نمط ردوده.
        4. اللغة: العربية فقط، وبأسلوب أسطر قصيرة.

        الأدلة المستخرجة من الأرشيف:
        {historical_evidence}
        """

        response = ollama.chat(model='llama3', messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': question}
        ])
        
        return jsonify({'answer': response['message']['content']})

    except Exception as e:
        return jsonify({'answer': f"يا لؤي، تعذر معالجة البيانات داخل مجلد data: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)




    