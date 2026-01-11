import gradio as gr
import joblib
import numpy as np
import os

# 1.التحقق من وجود ملف الموديل 
MODEL_PATH = 'linear_regression_model.pkl'
model = None

if os.path.exists(MODEL_PATH):
    try:
        model = joblib.load(MODEL_PATH)
        print("✅ تم تحميل الموديل بنجاح")
    except Exception as e:
        print(f"❌ خطأ أثناء تحميل الموديل: {e}")
else:
    print(f"⚠️ تحذير: لم يتم العثور على الملف {MODEL_PATH} في المجلد الحالي")

# دالة تنظيف الأرقام
def clean_num(val):
    if val is None or val == "": return 0.0
    # تحويل الأرقام العربية لإنجليزية
    arabic_digits = "٠١٢٣٤٥٦٧٨٩"
    english_digits = "0123456789"
    table = str.maketrans(arabic_digits, english_digits)
    try:
        return float(str(val).translate(table))
    except:
        return 0.0

def predict_spending(app_time, web_time, membership):
    # 1. التأكد من تحميل الموديل
    if model is None:
        return "⚠️ خطأ: ملف الموديل غير موجود", "لا يمكن الحساب"
    
    # 2. معالجة المدخلات
    t_app = clean_num(app_time)
    t_web = clean_num(web_time)
    m_years = clean_num(membership)

    # التحقق من المدخلات
    if t_app == 0 and t_web == 0:
        return "⚠️ فضلاً أدخل أرقاماً صحيحة", "0"

    try:
        # 3. الحسابات الداخلية
        # الموديل يحتاج 4 قيم: [Avg. Session Length, Time on App, Time on Website, Length of Membership]
        avg_session = (t_app + t_web) / 2
        # لجعل الواجهه اسهل استخداما قمت بحساب المتوسط 
        # تحضير المصفوفة للموديل
        features = np.array([[avg_session, t_app, t_web, m_years]])
        
        # التنبؤ
        prediction = model.predict(features)[0]
        final_val = max(0, round(prediction, 2))
        
        return f"{final_val} دولار سنويًا", f"{round(avg_session, 2)} دقيقة"
    
    except Exception as e:
        return f"❌ خطأ تقني: {str(e)}", "خطأ في الحساب"

# 4. تنسيق الواجهة (CSS) لحل مشكلة تداخل النصوص العربية والانجليزية
css = """
.gradio-container {
    direction: rtl !important;
    text-align: right !important;
}
.md, .label, .input-label {
    text-align: right !important;
    direction: rtl !important;
}
"""

with gr.Blocks(theme=gr.themes.Soft(), css=css) as demo:
    gr.Markdown("""
    # 🛍️ نظام التنبؤ بإنفاق العملاء
    هذا التطبيق يحلل سلوك العميل الرقمي للتنبؤ بالقيمة المالية لإنفاقه.
    [كود المشروع على GitHub](https://github.com/Loai-Alrazi/Python/tree/0a75521653c817a1f271cf080a5e2c685858d58c/Data-Science-Projects/Ecommerce_Project)
    """)
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("### 📥 البيانات المطلوبة")
            in_app = gr.Number(label="وقت استخدام التطبيق (App Time)", value=None)
            in_web = gr.Number(label="وقت استخدام الموقع (Web Time)", value=None)
            in_mem = gr.Number(label="سنوات العضوية (Membership)", value=None)
            btn = gr.Button("🚀 احسب النتائج الآن", variant="primary")

        with gr.Column():
            gr.Markdown("### 📈 النتائج")
            out_money = gr.Textbox(label="المبلغ المتوقع إنفاقه", interactive=False)
            out_avg = gr.Textbox(label="متوسط طول الجلسة (محسوب آليًا)", interactive=False)

    btn.click(
        fn=predict_spending,
        inputs=[in_app, in_web, in_mem],
        outputs=[out_money, out_avg]
    )

    gr.Markdown("---")
    gr.Markdown(" تطوير: **م. لؤي الرازي (Data Scientist)**")

if __name__ == "__main__":
    demo.launch()