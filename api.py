from flask import Flask, render_template, request
import os
from androguard.core.bytecodes import apk

app = Flask(__name__)


@app.route('/', methods=['POST'])
def home():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        a = apk.APK(f.filename)
        os.remove(f.filename)
        return a.get_details_permissions()


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
