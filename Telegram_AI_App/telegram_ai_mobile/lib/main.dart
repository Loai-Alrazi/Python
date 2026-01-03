import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(const MaterialApp(
    debugShowCheckedModeBanner: false,
    home: TelegramAIChat(),
  ));
}

class TelegramAIChat extends StatefulWidget {
  const TelegramAIChat({Key? key}) : super(key: key);

  @override
  _TelegramAIChatState createState() => _TelegramAIChatState();
}

class _TelegramAIChatState extends State<TelegramAIChat> {
  final TextEditingController _controller = TextEditingController();
  final List<Map<String, String>> _messages = [];
  bool _isLoading = false;

  // تم تعديل الدالة لتقبل الإرسال عبر زر الإنتر أو الأيقونة
  Future<void> _sendMessage([String? text]) async {
    final messageText = text ?? _controller.text;
    if (messageText.trim().isEmpty) return;

    setState(() {
      _messages.add({"role": "user", "text": messageText});
      _isLoading = true;
    });

    _controller.clear();

    try {
      final response = await http.post(
        Uri.parse('http://192.168.8.174:5000/chat'),
        //Uri.parse('http://192.168.103.192:5000/chat'),
        headers: {"Content-Type": "application/json"},
        body: jsonEncode({"question": messageText}),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(utf8.decode(response.bodyBytes));
        setState(() {
          _messages.add({"role": "bot", "text": data['answer']});
        });
      } else {
        setState(() {
          _messages.add({
            "role": "bot",
            "text": "⚠️ خطأ في السيرفر: ${response.statusCode}"
          });
        });
      }
    } catch (e) {
      setState(() {
        _messages.add({
          "role": "bot",
          "text": "❌ تأكد من تشغيل السيرفر ومن اتصالك بنفس الشبكة"
        });
      });
    } finally {
      setState(() => _isLoading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        // الحل لظهور الاسم كاملاً
        title: const FittedBox(
          fit: BoxFit.scaleDown,
          child: Text("ذكريات مجموعة الحسام "),
        ),
        backgroundColor: Colors.blueAccent,
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              padding: const EdgeInsets.all(10),
              itemCount: _messages.length,
              itemBuilder: (context, index) {
                final msg = _messages[index];
                final isUser = msg["role"] == "user";
                return Align(
                  alignment:
                      isUser ? Alignment.centerRight : Alignment.centerLeft,
                  child: Container(
                    margin: const EdgeInsets.symmetric(vertical: 5),
                    padding: const EdgeInsets.all(12),
                    decoration: BoxDecoration(
                      color: isUser ? Colors.blue[100] : Colors.green[100],
                      borderRadius: BorderRadius.circular(15),
                    ),
                    // الحل لتمكين نسخ الرسائل
                    child: SelectableText(
                      msg["text"]!,
                      style: const TextStyle(fontSize: 16),
                      textDirection: TextDirection.rtl,
                    ),
                  ),
                );
              },
            ),
          ),
          if (_isLoading) const LinearProgressIndicator(),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _controller,
                    // الحل لتفعيل زر الإرسال (Enter) من الكيبورد
                    onSubmitted: (value) => _sendMessage(value),
                    decoration: const InputDecoration(
                      hintText: "اسأل عن ذكرياتكم...",
                      border: OutlineInputBorder(),
                    ),
                    textDirection: TextDirection.rtl,
                  ),
                ),
                IconButton(
                  icon: const Icon(Icons.send, color: Colors.blueAccent),
                  onPressed: () => _sendMessage(),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}



