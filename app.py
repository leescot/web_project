from flask import Flask, render_template, request, jsonify
import PyPDF2
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # 檢查是否收到 PDF 文件
    if 'pdf' not in request.files:
        return 'No file found', 400

    pdf_file = request.files['pdf']
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # 提取 PDF 中的文本
    text = ''
    for page_num in range(pdf_reader.numPages):
        text += pdf_reader.getPage(page_num).extractText()

    # TODO: 在此處添加對提取文本的分類邏輯

    # 返回提取的文本
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)
