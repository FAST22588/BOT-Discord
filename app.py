from flask import Flask, render_template

# สร้างแอป Flask
app = Flask(__name__)

# การ route สำหรับหน้าแรก
@app.route('/')
def home():
    return render_template('index.html')

# รันแอปเมื่อไฟล์นี้ถูกเรียก
if __name__ == "__main__":
    app.run(debug=True)
