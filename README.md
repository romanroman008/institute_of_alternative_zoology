# 🦎 Alternative Zoology (Django App)

**Alternative Zoology** is a simple web application built to practice the **Django** framework and learn how to deploy a project on **Render**.  
It presents a fictional “Institute of Alternative Zoology” with absurd information about animals.


---

## 🧩 Features
- Basic Django views and routing  
- HTML templates using Django Templates  
- Simple MVC (Model–View–Template) structure  
- Deployment on Render using Gunicorn  
- Static files and environment variables configuration  

---

## ⚙️ Tech Stack
- **Python**
- **Django**  
- **HTML**
- **Tailwind**  

---

## 🐳 **Docker Setup**

### 1️⃣ Change .env.example name to .env

### 2️⃣ Build and start the containers
```bash
docker compose up --build
```
This will:
- Launch the PostgreSQL database
- Run the Django application
- Load fixtures to database
- Launch the app at:
http://localhost:8010
  
