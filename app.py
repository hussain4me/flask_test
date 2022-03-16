from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_projects():
    return render_template("index.html")

@app.route('/project/<project_id>')
def show_task(project_id):
    return render_template("project-tasks.html", project_id=project_id)
 
if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=3000)
