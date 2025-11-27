const API_URL = "http://127.0.0.1:8000";

let editingEmployeeId = null;
let editingTaskId = null;

// ------------------- SWITCH TABS ---------------------
function showTab(name) {
    document.querySelectorAll(".tab").forEach(t => t.classList.remove("active"));
    document.querySelector(`[onclick="showTab('${name}')"]`).classList.add("active");

    document.querySelectorAll(".tab-content").forEach(c => c.classList.add("hidden"));
    document.getElementById(name).classList.remove("hidden");
}

// ------------------- REGISTER ---------------------
async function registerUser() {
    const name = document.getElementById("reg-name").value;
    const email = document.getElementById("reg-email").value;
    const password = document.getElementById("reg-password").value;

    const res = await fetch(`${API_URL}/auth/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, password })
    });

    alert(res.ok ? "Registration successful!" : "Registration failed");
}

// ------------------- LOGIN ---------------------
async function login() {
    const email = document.getElementById("log-email").value;
    const password = document.getElementById("log-password").value;

    const form = new URLSearchParams();
    form.append("username", email);
    form.append("password", password);

    const res = await fetch(`${API_URL}/auth/login`, {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: form
    });

    if (!res.ok) {
        alert("Invalid login");
        return;
    }

    const data = await res.json();
    localStorage.setItem("token", data.access_token);

    window.location.href = "dashboard.html";
}

// ------------------- LOGOUT ---------------------
function logout() {
    localStorage.clear();
    window.location.href = "index.html";
}

// =============================================================
// ===================== EMPLOYEE CRUD =========================
// =============================================================

async function createEmployee() {
    const token = localStorage.getItem("token");

    const body = {
        name: document.getElementById("emp-name").value,
        email: document.getElementById("emp-email").value,
        role: document.getElementById("emp-role").value,
        status: document.getElementById("emp-status").value
    };

    const res = await fetch(`${API_URL}/employees`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify(body)
    });

    alert(res.ok ? "Employee created successfully!" : "Failed to create employee");
}

async function loadEmployees() {
    const token = localStorage.getItem("token");

    const res = await fetch(`${API_URL}/employees`, {
        headers: { "Authorization": `Bearer ${token}` }
    });

    const list = document.getElementById("employee-list");
    list.innerHTML = "";

    if (!res.ok) return alert("Failed to load employees");

    const employees = await res.json();

    employees.forEach(emp => {
        const li = document.createElement("li");
        li.innerHTML = `
            ${emp.id} — ${emp.name} — ${emp.email}
            <button class="edit-btn" onclick="openEmployeeEdit(${emp.id}, '${emp.name}', '${emp.email}', '${emp.role}', '${emp.status}')">Edit</button>
            <button class="delete-btn" onclick="deleteEmployee(${emp.id})">Delete</button>
        `;
        list.appendChild(li);
    });
}

async function deleteEmployee(id) {
    const token = localStorage.getItem("token");

    const res = await fetch(`${API_URL}/employees/${id}`, {
        method: "DELETE",
        headers: { "Authorization": `Bearer ${token}` }
    });

    alert(res.ok ? "Employee deleted!" : "Delete failed");
    loadEmployees();
}

// ------------------- EDIT EMPLOYEE (MODAL) ---------------------

function openEmployeeEdit(id, name, email, role, status) {
    editingEmployeeId = id;

    document.getElementById("edit-emp-name").value = name;
    document.getElementById("edit-emp-email").value = email;
    document.getElementById("edit-emp-role").value = role;
    document.getElementById("edit-emp-status").value = status;

    document.getElementById("employee-edit-section").classList.remove("hidden");
}

function closeEmployeeEdit() {
    document.getElementById("employee-edit-section").classList.add("hidden");
}

async function updateEmployee() {
    const token = localStorage.getItem("token");

    const updated = {
        name: document.getElementById("edit-emp-name").value,
        email: document.getElementById("edit-emp-email").value,
        role: document.getElementById("edit-emp-role").value,
        status: document.getElementById("edit-emp-status").value
    };

    const res = await fetch(`${API_URL}/employees/${editingEmployeeId}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify(updated)
    });

    alert(res.ok ? "Employee updated!" : "Update failed");
    closeEmployeeEdit();
    loadEmployees();
}

// =============================================================
// ========================= TASK CRUD ==========================
// =============================================================

async function createTask() {
    const token = localStorage.getItem("token");

    const body = {
        title: document.getElementById("task-title").value,
        description: document.getElementById("task-desc").value,
        status: document.getElementById("task-status").value,
        due_date: document.getElementById("task-date").value,
        employee_id: document.getElementById("task-emp-id").value
    };

    const res = await fetch(`${API_URL}/tasks`, {
        method: "POST",
        headers: {
            "Authorization": `Bearer ${token}`,
            "Content-Type": "application/json"
        },
        body: JSON.stringify(body)
    });

    alert(res.ok ? "Task created!" : "Failed to create");
}

async function loadTasks() {
    const token = localStorage.getItem("token");

    const res = await fetch(`${API_URL}/tasks`, {
        headers: { "Authorization": `Bearer ${token}` }
    });

    const list = document.getElementById("task-list");
    list.innerHTML = "";

    if (!res.ok) return alert("Failed to load tasks");

    const tasks = await res.json();

    tasks.forEach(task => {
        const li = document.createElement("li");
        li.innerHTML = `
            ${task.id} — ${task.title} — ${task.status}
            <button class="edit-btn" onclick="openTaskEdit(${task.id}, '${task.title}', '${task.description}', '${task.status}', '${task.due_date}', '${task.employee_id}')">Edit</button>
            <button class="delete-btn" onclick="deleteTask(${task.id})">Delete</button>
        `;
        list.appendChild(li);
    });
}

async function deleteTask(id) {
    const token = localStorage.getItem("token");

    const res = await fetch(`${API_URL}/tasks/${id}`, {
        method: "DELETE",
        headers: { "Authorization": `Bearer ${token}` }
    });

    alert(res.ok ? "Task deleted!" : "Delete failed");
    loadTasks();
}

// ------------------- EDIT TASK (MODAL) ---------------------

function openTaskEdit(id, title, desc, status, due, emp) {
    editingTaskId = id;

    document.getElementById("edit-task-title").value = title;
    document.getElementById("edit-task-desc").value = desc;
    document.getElementById("edit-task-status").value = status;
    document.getElementById("edit-task-date").value = due;
    document.getElementById("edit-task-emp-id").value = emp;

    document.getElementById("task-edit-section").classList.remove("hidden");
}

function closeTaskEdit() {
    document.getElementById("task-edit-section").classList.add("hidden");
}

async function updateTask() {
    const token = localStorage.getItem("token");

    const updated = {
        title: document.getElementById("edit-task-title").value,
        description: document.getElementById("edit-task-desc").value,
        status: document.getElementById("edit-task-status").value,
        due_date: document.getElementById("edit-task-date").value,
        employee_id: document.getElementById("edit-task-emp-id").value
    };

    const res = await fetch(`${API_URL}/tasks/${editingTaskId}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify(updated)
    });

    alert(res.ok ? "Task updated!" : "Update failed");
    closeTaskEdit();
    loadTasks();
}


// ========================= EXTRA QUERY FUNCTIONS ===============================

async function getTasksOfEmployee() {
    const token = localStorage.getItem("token");
    const id = document.getElementById("query-emp-id").value;

    const res = await fetch(`${API_URL}/employees/${id}/tasks`, {
        headers: { "Authorization": `Bearer ${token}` }
    });

    const list = document.getElementById("emp-task-results");
    list.innerHTML = "";

    if (!res.ok) return alert("Employee not found");

    const tasks = await res.json();

    tasks.forEach(t => {
        const li = document.createElement("li");
        li.textContent = `${t.id} — ${t.title} — ${t.status}`;
        list.appendChild(li);
    });
}

async function getEmployeeOfTask() {
    const token = localStorage.getItem("token");
    const id = document.getElementById("query-task-id").value;

    const res = await fetch(`${API_URL}/tasks/${id}/employee`, {
        headers: { "Authorization": `Bearer ${token}` }
    });

    const list = document.getElementById("task-emp-results");
    list.innerHTML = "";

    if (!res.ok) return alert("Task or employee not found");

    const emp = await res.json();

    const li = document.createElement("li");
    li.textContent = `${emp.id} — ${emp.name} — ${emp.email}`;
    list.appendChild(li);
}

async function getEmployeeNameOfTask() {
    const token = localStorage.getItem("token");
    const id = document.getElementById("query-task-id-name").value;

    const res = await fetch(`${API_URL}/tasks/${id}/employee/name`, {
        headers: { "Authorization": `Bearer ${token}` }
    });

    if (!res.ok) {
        document.getElementById("task-emp-name-result").textContent = "Not Found";
        return;
    }

    const data = await res.json();
    document.getElementById("task-emp-name-result").textContent = data.employee_name;
}

async function getTaskTitlesOfEmployee() {
    const token = localStorage.getItem("token");
    const id = document.getElementById("query-emp-id-titles").value;

    const res = await fetch(`${API_URL}/employees/${id}/task-titles`, {
        headers: { "Authorization": `Bearer ${token}` }
    });

    const list = document.getElementById("emp-task-titles-results");
    list.innerHTML = "";

    if (!res.ok) return alert("Employee not found");

    const data = await res.json();

    data.task_titles.forEach(title => {
        const li = document.createElement("li");
        li.textContent = title;
        list.appendChild(li);
    });
}
