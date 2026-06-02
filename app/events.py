"""SocketIO handlers for US-01 real-time pair programming.

Each session is a room keyed by its code. Only the Driver may edit the shared
file; edits are broadcast to the Navigator. Roles can be swapped live.
"""
from flask import request
from flask_socketio import join_room, emit
from app import socketio, state


def _roles(session):
    return [{"name": u["name"], "role": u["role"]} for u in session["users"].values()]


@socketio.on("join")
def on_join(data):
    code = data.get("code")
    session = state.get_session(code)
    if not session:
        return
    join_room(code)
    session["users"][request.sid] = {"name": data.get("name"), "role": data.get("role")}
    emit("content", {"content": session["archivo"].get_content()})
    emit("roles", {"users": _roles(session), "log": _log(session)}, room=code)


@socketio.on("edit")
def on_edit(data):
    code = data.get("code")
    session = state.get_session(code)
    if not session:
        return
    user = session["users"].get(request.sid)
    if not user or user["role"] != "Driver":
        return  # only the Driver may edit
    content = data.get("content", "")
    session["archivo"].update_content(content)
    session["registro"].register(user["name"], "edited shared file (v%d)" % session["archivo"].version)
    emit("content", {"content": content}, room=code, include_self=False)
    emit("roles", {"users": _roles(session), "log": _log(session)}, room=code)


@socketio.on("swap")
def on_swap(data):
    code = data.get("code")
    session = state.get_session(code)
    if not session:
        return
    for user in session["users"].values():
        user["role"] = "Navigator" if user["role"] == "Driver" else "Driver"
    emit("roles", {"users": _roles(session), "log": _log(session)}, room=code)


@socketio.on("disconnect")
def on_disconnect():
    for session in state.sessions.values():
        if request.sid in session["users"]:
            del session["users"][request.sid]
            emit("roles", {"users": _roles(session), "log": _log(session)},
                 room=session["sesion"].codigo)
            break


def _log(session):
    return [
        {"author": e["author"], "description": e["description"],
         "time": e["timestamp"].strftime("%H:%M:%S")}
        for e in session["registro"].get_history()
    ]
