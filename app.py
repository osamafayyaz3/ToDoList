from flask import Flask, render_template, request, redirect, url_for, jsonify

from model import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = 'postgres://bsrlhmynyfunyf:9e48e516537a7940762dadb66d6d15b17f2ac0b972d3468724dab1432d4a4e8f@ec2-107-21-214-222.compute-1.amazonaws.com:5432/du7dthddv5mf7'
app.config["SQLALCHEMY_TRACT_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form.get('content')
        if not task_content:
            return redirect('/')
        new_task = Taskes(action=task_content)
        db.session.add(new_task)
        db.session.commit()
        return redirect('/')
    else:
        tasks = Taskes.query.all()
        return render_template('index.html', taskes=tasks)


@app.route('/delete/<id>')
def delete(id):
    to_delete = Taskes.query.get(id)
    print(to_delete.id)
    db.session.delete(to_delete)
    db.session.commit()
    return redirect('/')

@app.route('/api/lists/<list_id>')
def list_api(list_id):
    task = Taskes.query.get(list_id)
    print(task)
    if task is None:
        return jsonify({"error": "Invalid list_id"}), 422
    actionList = task.action
    return jsonify(
        {
            "action": actionList
        }
    )

if __name__ == "__main__":
    app.run(debug=True)
