# 🎓 EduManage — Django Course Management System
An intuitive, instructor-first course management web app built with Django and deployed on Render.


🔗 **Live Demo:** [https://edumanage-project.onrender.com/](https://edumanage-project.onrender.com/)  
📂 **Source Code:** [GitHub Repository](https://github.com/Prabhanshiyadav/edumanage_project)

---

## 📌 Features

✅ Instructor Dashboard to:
- 🔍 List all courses  
- 📄 View course details  
- ✏️ Create new courses  
- 🛠️ Edit course information  
- ❌ Delete outdated courses

---

## 🧠 Tech Stack

- **Backend**: Django 4.x  
- **Frontend**: HTML, Django Templating  
- **Database**: SQLite3 (default)  
- **Deployment**: Render  
- **Hosting**: GitHub, Render Web Service  

---


## ⚙️ Installation

```bash
# Clone the project
git clone https://github.com/Prabhanshiyadav/edumanage_project.git
cd edumanage_project

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # for Git Bash / Linux
venv\Scripts\activate     # for Windows CMD/PowerShell

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create a superuser for admin access
python manage.py createsuperuser

# Start the development server
python manage.py runserver

🗃️ Project Structure


edumanage_project/
│
├── courses/            # Core course app
│   ├── models.py       # Course model
│   ├── views.py        # CBVs for course CRUD
│   ├── urls.py         # URL patterns
│   └── templates/      # HTML templates
│
├── edumanage/          # Django config
│   └── settings.py     # Project settings
│
├── db.sqlite3          # SQLite database
├── requirements.txt    # Python dependencies
├── Procfile            # Render deployment config
└── render.yaml         # Render service definition

🙋‍♀️ Author
Prabhanshi Yadav
🔗 GitHub 

