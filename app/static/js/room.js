// US-01 real-time pair programming client.
const socket = io();
const { code, name, role } = window.SESSION;

const editor = document.getElementById("editor");
const roleLabel = document.getElementById("role");
const usersList = document.getElementById("users");
const logList = document.getElementById("log");
const hint = document.getElementById("hint");
const swapBtn = document.getElementById("swap");

let myRole = role;

socket.on("connect", () => {
    socket.emit("join", { code, name, role: myRole });
});

// Driver sends edits; suppress echo while applying remote content.
let applyingRemote = false;
editor.addEventListener("input", () => {
    if (applyingRemote || myRole !== "Driver") return;
    socket.emit("edit", { code, content: editor.value });
});

socket.on("content", (data) => {
    if (document.activeElement === editor && myRole === "Driver") return;
    applyingRemote = true;
    editor.value = data.content;
    applyingRemote = false;
});

socket.on("roles", (data) => {
    // refresh my own role from the server's view
    const me = data.users.find((u) => u.name === name);
    if (me) {
        myRole = me.role;
        roleLabel.textContent = myRole;
        editor.readOnly = myRole !== "Driver";
        hint.textContent = myRole === "Driver"
            ? "You can edit. Changes stream to the Navigator."
            : "Read-only. Waiting for the Driver's changes.";
    }
    usersList.innerHTML = data.users
        .map((u) => `<li>${u.name} <span class="badge">${u.role}</span></li>`)
        .join("");
    logList.innerHTML = (data.log || [])
        .map((e) => `<li><b>${e.author}</b> ${e.description} <span class="hint">${e.time}</span></li>`)
        .join("");
});

swapBtn.addEventListener("click", () => socket.emit("swap", { code }));
