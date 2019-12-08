"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template
import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')
    first, last, github = hackbright.get_student_by_github(github)
    grade_title = hackbright.get_grades_by_github(github)
    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github,
                            grade_title=grade_title)


    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student-add")
def student_add():
    """Add a student"""

    return render_template("add_student.html")


@app.route("/project")
def project_details():
    """Lists project title, description, max grade"""
    project_info = hackbright.get_project_by_title(title)
    return render_template("student_info.html",
                            project_info=project_info)


@app.route("/student-confirmation", methods=['POST'])
def student_confirmation():
    
    first = request.form.get('first')
    last = request.form.get('last')
    github = request.form.get('github')

    hackbright.make_new_student(first, last, github)

    return render_template("student_confirmation.html",
                            github=github)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
