import json
import requests
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from datetime import datetime

class TelegramAIBackend:
    def __init__(self):
        # 1. المحرك الإحصائي
        self.all_messages = []
        self.users_stats = {}
        self.my_accounts = ["لؤي الرازي", "الُحـ๛ـــــآمٌ", "قناة الُحـ๛ـــــآمٌ الرئيسية"]
        
        # 2. المحرك الدلالي (سيتم تحميله محلياً)
        print("⏳ جاري تحميل نموذج اللغة المحلي...")
        # self.semantic_model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
        # أضف local_files_only=True ليعمل بدون إنترنت
        self.semantic_model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2', device='cpu')
        self.index = None
        self.rich_texts = []

    def load_data(self, file_paths):
        """تحميل ودمج الرسائل من عدة ملفات JSON"""
        self.all_messages = []
        for path in file_paths:
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # دمج الرسائل من كل ملف في القائمة الرئيسية
                    self.all_messages.extend(data.get('messages', []))
                print(f"✅ تم تحميل ودمج: {path}")
            except Exception as e:
                print(f"❌ خطأ في تحميل {path}: {e}")
        
        # ترتيب الرسائل زمنياً لضمان دقة التحليل
        self.all_messages.sort(key=lambda x: x.get('date', ''))
        print(f"📊 إجمالي الرسائل بعد الدمج: {len(self.all_messages)}")

    def build_semantic_index(self):
        """بناء ذاكرة البحث بالمعنى"""
        print("🧠 بناء الفهرس الدلالي... (برجاء الانتظار)")
        self.rich_texts = [self._get_text(m) for m in self.all_messages if len(self._get_text(m)) > 20]
        embeddings = self.semantic_model.encode(self.rich_texts, show_progress_bar=True)
        
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(np.array(embeddings).astype('float32'))
        print("✅ الذاكرة الدلالية جاهزة للعمل.")

    def _get_text(self, msg):
        text = msg.get('text', '')
        if isinstance(text, list):
            return "".join([t if isinstance(t, str) else t.get('text', '') for t in text])
        return str(text)

    def ask_ai(self, question):
        """الوظيفة الكبرى: ابحث في FAISS ثم اسأل Llama"""
        # البحث عن السياق
        query_vec = self.semantic_model.encode([question]).astype('float32')
        _, indices = self.index.search(query_vec, k=5)
        context = "\n".join([self.rich_texts[i] for i in indices[0]])
        
        # إرسال لـ Ollama
        prompt = f"سياق المحادثات:\n{context}\n\nسؤال المستخدم: {question}\nأجب بناءً على السياق فقط."
        
        try:
            r = requests.post('http://localhost:11434/api/generate', 
                            json={"model": "llama3.2:1b", "prompt": prompt, "stream": False})
            return r.json().get('response', "لا يوجد رد.")
        except:
            return "❌ خطأ: تأكد من تشغيل Ollama."

                    