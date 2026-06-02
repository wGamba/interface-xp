from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import state
from app.models.funcionalidad import Funcionalidad

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


# --- US-01: Pair Programming ---------------------------------------------
@bp.route("/pair", methods=["GET", "POST"])
def pair():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        action = request.form.get("action")
        if not name:
            flash("Enter your name.")
            return redirect(url_for("main.pair"))
        if action == "create":
            code = state.create_session(name)
            return redirect(url_for("main.room", code=code, name=name, role="Driver"))
        code = request.form.get("code", "").strip().upper()
        if not state.get_session(code):
            flash("Session not found.")
            return redirect(url_for("main.pair"))
        return redirect(url_for("main.room", code=code, name=name, role="Navigator"))
    return render_template("pair.html")


@bp.route("/pair/<code>")
def room(code):
    s = state.get_session(code)
    if not s:
        flash("Session not found.")
        return redirect(url_for("main.pair"))
    name = request.args.get("name", "Anonymous")
    role = request.args.get("role", "Navigator")
    return render_template(
        "room.html",
        code=code,
        name=name,
        role=role,
        content=s["archivo"].get_content(),
    )


# --- US-02: Client Feedback ----------------------------------------------
@bp.route("/feedback")
def feedback():
    fb = state.feedback
    it = fb["iteracion"]
    section = fb["comentarios"]
    funcs = list(enumerate(it.get_functionalities()))
    comments = section.get_comments() if section.is_active() else []
    return render_template(
        "feedback.html",
        funcs=funcs,
        status=it.get_status(),
        active=section.is_active(),
        comments=comments,
        cambios=list(enumerate(fb["cambios"])),
    )


@bp.route("/feedback/add", methods=["POST"])
def feedback_add():
    description = request.form.get("description", "").strip()
    try:
        state.feedback["iteracion"].add_functionality(Funcionalidad(description))
    except (ValueError, Exception) as e:
        flash(str(e))
    return redirect(url_for("main.feedback"))


@bp.route("/feedback/finish", methods=["POST"])
def feedback_finish():
    try:
        state.feedback["iteracion"].finish(state.feedback["comentarios"])
    except Exception as e:
        flash(str(e))
    return redirect(url_for("main.feedback"))


@bp.route("/feedback/evaluate", methods=["POST"])
def feedback_evaluate():
    fb = state.feedback
    funcs = fb["iteracion"].get_functionalities()
    try:
        index = int(request.form.get("index"))
        decision = request.form.get("decision")
        justification = request.form.get("justification", "").strip()
        func = funcs[index]
        if decision == "approve":
            fb["cliente"].approve(func, justification)
        else:
            fb["cliente"].reject(func, justification)
    except (ValueError, IndexError, Exception) as e:
        flash(str(e))
    return redirect(url_for("main.feedback"))


@bp.route("/feedback/propose", methods=["POST"])
def feedback_propose():
    fb = state.feedback
    description = request.form.get("description", "").strip()
    priority = request.form.get("priority", "")
    try:
        change = fb["cliente"].propose_change(description, priority)
        fb["cambios"].append(change)
    except (ValueError, Exception) as e:
        flash(str(e))
    return redirect(url_for("main.feedback"))


@bp.route("/feedback/comment", methods=["POST"])
def feedback_comment():
    comment = request.form.get("comment", "").strip()
    try:
        state.feedback["comentarios"].add_comment(comment)
    except (ValueError, Exception) as e:
        flash(str(e))
    return redirect(url_for("main.feedback"))


@bp.route("/feedback/prioritize", methods=["POST"])
def feedback_prioritize():
    fb = state.feedback
    try:
        index = int(request.form.get("index"))
        priority = request.form.get("priority", "")
        fb["programador"].prioritize_change(fb["cambios"][index], priority)
    except (ValueError, IndexError, Exception) as e:
        flash(str(e))
    return redirect(url_for("main.feedback"))


@bp.route("/feedback/reset", methods=["POST"])
def feedback_reset():
    state.reset_feedback()
    return redirect(url_for("main.feedback"))
