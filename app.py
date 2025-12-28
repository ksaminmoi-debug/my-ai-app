from flask import Flask, request, render_template_string
import google.generativeai as genai
import os

app = Flask(__name__)

# Gemini AI config
genai.configure(api_key="AIzaSyAkbmgH7QrnZV3fArvUzjxWK_FdsH89mqI")
model = genai.GenerativeModel('gemini-1.5-flash')

HTML_CODE = """
<!DOCTYPE html>
<html>
<head>
    <title>Saminmoi AI</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: sans-serif; background: #121212; color: white; text-align: center; padding: 20px; }
        .box { background: #1e1e1e; padding: 20px; border-radius: 10px; max-width: 400px; margin: auto; }
        input { width: 80%; padding: 10px; margin: 10px 0; border-radius: 5px; border: none; }
        button { padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; }
        .res { margin-top: 20px; text-align: left; background: #333; padding: 10px; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="box">
        <h1>Saminmoi AI 🤖</h1>
        <form method="POST">
            <input type="text" name="q" placeholder="প্ৰশ্ন সোধক..." required>
            <button type="submit">Ask</button>
        </form>
        {% if response %}<div class="res"><strong>উত্তৰ:</strong><p>{{ response }}</p></div>{% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    response = ""
    if request.method == 'POST':
        q = request.form.get('q')
        try:
            res = model.generate_content(q)
            response = res.text
        except:
            response = "দুঃখিত, কিবা ভুল হৈছে।"
    return render_template_string(HTML_CODE, response=response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
  
