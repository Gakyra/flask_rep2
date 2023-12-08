from . import app
from flask import request, redirect, render_template
from .models.database import session
from .models.group import Group

@app.route("/")
@app.route("/group_management", methods=["POST", "GET"])
def group_manager():
    all_groups = session.query(Group).all()
    all_groups = [x.group_name for x in all_groups]

    if request.method == "POST":
        group_name = request.form["group_name"]
        group = Group(
            group_name=group_name
        )
        try:
            session.add(group)
            session.commit()
            session.close()
        except Exception as exc:
            return f"Виникла проблемка: {exc}"
        return redirect("/group_management")
    return render_template("group_management.html", group_names=all_groups)