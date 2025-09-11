from flask import Flask, request, redirect, render_template
import random
import string
from models import (
    init_db, 
    insert_url,
    get_all_urls,
    get_url,
    increment_visit_count,
    delete_url_by_code
)

app = Flask(__name__)
init_db()

def generate_short_code(length=7):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        short_code = generate_short_code()
        insert_url(original_url, short_code)

        return redirect('/')
    else:
        all_urls = get_all_urls()
        print(all_urls)
        return render_template('index.html', all_urls=all_urls)

@app.route("/about")
def about():
    return f"This is me, Flask. Hello!"



if __name__ == '__main__':
    app.run(debug=True)