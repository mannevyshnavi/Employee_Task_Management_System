📌 Employee Task Management System

A full-stack web application that allows users to manage Employees and Tasks, featuring authentication, CRUD operations, and database integration.

This project is built as part of:

Track 2 – Backend Development (API + Database)
using FastAPI and a connected frontend.


🌐 Live Demo Links

| Component              | URL                                                                                                                              |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Frontend**           | [https://employee-task-management-system-1-h91k.onrender.com](https://employee-task-management-system-1-h91k.onrender.com)       |
| **Backend (API)**      | [https://employee-task-management-system-6jvu.onrender.com](https://employee-task-management-system-6jvu.onrender.com)           |
| **API Docs (Swagger)** | [https://employee-task-management-system-6jvu.onrender.com/docs](https://employee-task-management-system-6jvu.onrender.com/docs) |


🧰 Tech Stack Used

  BACKEND
  
| Technology            | Purpose                           |
| --------------------- | --------------------------------- |
| **FastAPI**           | Backend API framework             |
| **Python**            | Programming language              |
| **SQLAlchemy ORM**    | Database ORM layer                |
| **Pydantic**          | Data validation and schemas       |
| **SQLite**            | Local database storage            |
| **JWT (python-jose)** | Authentication & token generation |
| **Uvicorn**           | ASGI server for FastAPI           |
| **Passlib (bcrypt)**  | Password hashing                  |

FRONTEND

| Technology                 | Purpose                                 |
| -------------------------- | --------------------------------------- |
| **HTML5**                  | Structure of the UI                     |
| **CSS3**                   | Styling and layout                      |
| **JavaScript (Fetch API)** | API integration & dynamic functionality |

DEPLOYMENT
| Platform                         | Purpose                      |
| -------------------------------- | ---------------------------- |
| **Render (Web Service)**         | Backend deployment           |
| **Render (Static Site Hosting)** | Frontend deployment          |
| **GitHub**                       | Version control & repository |

📁 Project Structure

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/8e2dde74-6d7f-49e6-adb3-8abf62962093" />



🚀 Setup Steps
 1. Clone the Repository

 Step             | Command                                                                          |
| ---------------- | -------------------------------------------------------------------------------- |
| Clone project    | `git clone https://github.com/mannevyshnavi/Employee_Task_Management_System.git` |
| Move into folder | `cd Employee_Task_Management_System`                                             |

2. Backend Setup (FastAPI)

| Step                                   | Command                             |
| -------------------------------------- | ----------------------------------- |
| Create virtual environment             | `python -m venv venv`               |
| Activate virtual environment (Windows) | `venv\Scripts\activate`             |
| Install dependencies                   | `pip install -r requirements.txt`   |
| Start backend server                   | `uvicorn backend.main:app --reload` |
| Default backend URL                    | `http://127.0.0.1:8000`             

3. Frontend Setup
 | Step                                  | Description             |
| ------------------------------------- | ----------------------- |
| Open `frontend/index.html`            | Start login UI          |
| Open `frontend/dashboard.html`        | Task management UI      |
| Update `API_URL` in `frontend/app.js` | Point it to backend URL |

4.Deployment Setup
| Component | Platform             | Status    |
| --------- | -------------------- | --------- |
| Backend   | Render - Web Service | Deployed  |
| Frontend  | Render - Static Site | Deployed  |
| GitHub    | Public Repository    | Completed |

5.Run the Application
| Action               | URL                                                              |
| -------------------- | ---------------------------------------------------------------- |
| Open Frontend (Live) | `https://employee-task-management-system-1-h91k.onrender.com`    |
| Backend API Docs     | `https://employee-task-management-system-6jvu.onrender.com/docs` |

 LOGIN PAGE && DASHBOARD
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/8acd55c4-c92c-407c-bff6-1c4082c10271" />
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/72683249-eee8-4d06-a7f4-33a0f8cf9259" />
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/84f6f6a4-f1eb-424a-b83b-f2b21f772cfa" />
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/02c5f569-c37a-4ac6-ac85-13854fb633db" />
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/0ebe2ec8-e57c-42a5-966c-14700fd1324b" />
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/e636e7cb-955b-42e7-8319-deeb0e3e0b60" />

 FASTAPI SWAGGER UI
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/961e04e8-0dce-4655-822f-c71e9166329c" />
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/077035ce-446c-41fb-b86f-6d87b1ef9c7d" />

📝 Assumptions

-> Every logged-in user is allowed to manage all employees/tasks.
-> SQLite is used for simplicity; can be upgraded to PostgreSQL.
-> Frontend is lightweight and uses only vanilla JavaScript.
-> All task/employee relations follow a 1-to-many structure.


BONUS FEATURES IMPLEMENTED

✔ Full JWT Authentication (Login + Protected Routes)
✔ Complete CRUD for Employees & Tasks
✔ Extra API Endpoints:
  > Get all tasks of an employee
  > Get employee assigned to a task
  > Get only the employee name
  > Get only task titles
✔ Clean UI with edit modals
✔ Fully deployed Frontend + Backend
✔ Well-structured FastAPI modular architecture


👩‍💻 Author

Manne Vyshnavi
CSE – VIT-AP






