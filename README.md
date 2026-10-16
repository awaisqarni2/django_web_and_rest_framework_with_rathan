# 🚀 Django & Django REST Framework Notes + Source Code (Beginner Friendly)

> **Free Django notes (PDF + HTML), complete source code, and DRF examples, built while learning from the _Complete Django & Django REST Framework Course for Beginners_ by Tech With Rathan.**

⭐ **Find this useful? Star the repo** so other Django learners can find it too!

---

## 👋 Why This Repo Exists

I spent my last week learning Django, and this course helped me a lot. **Rathan explains everything clearly**, so I coded along, wrote detailed notes, and packed everything into this single repo.

The goal: **new learners watch the course, grab the code and notes here, learn faster, and spend more time building real projects.** Use it for quick revision, syntax checking, and interview prep.

---

## 🎥 The Course

**[▶️ Complete Django & Django REST Framework Course for Beginners (2026) | Tech With Rathan](https://youtu.be/1dlLxeri-Pg)**

⏱️ 14+ hours · Beginner friendly · Python required (basics)

| Timestamp | Topic                                        |
| --------- | -------------------------------------------- |
| 00:03:22  | Getting Started with Django                  |
| 00:18:00  | Creating a Test Django Project               |
| 00:53:23  | Fundamentals of Django                       |
| 02:55:08  | Working with Django Framework                |
| 05:28:55  | Django Forms & CRUD Operations               |
| 07:52:26  | Authentication, Permissions & Groups         |
| 10:09:14  | Django REST Framework: Creating Backend APIs |
| 12:15:26  | DRF Class-Based Views, Search & Filtering    |

> 📌 All credit for the course goes to [Tech With Rathan](https://www.youtube.com/channel/UCYesptHRU1QZ2pHZkAqdQTw). This repo is an independent student resource with my own notes and code-along files. Rathan's official project repo: [django_employee_records](https://github.com/dev-rathankumar/django_employee_records).

---

## 📦 What You Get

| Resource            | Details                                                         |
| ------------------- | --------------------------------------------------------------- |
| 📝 **Notes (PDF)**  | Clean, printable revision notes for the whole course            |
| 🌐 **Notes (HTML)** | Browser-friendly version, easy to search and read on any device |
| 💻 **Source Code**  | Code-along files to **check your syntax** when you get stuck    |
| 🔌 **DRF Examples** | REST API with viewsets, filtering and search                    |
| 👥 **Employee App** | Full web app with CRUD, authentication and image uploads        |

---

## 🗂️ Repository Structure

```
.
├── Notes/                      # Course notes (PDF + HTML)
├── part_1_code/                # Django basics project
└── part_2_3_code/
    ├── django_rest_framework/  # Django REST Framework (DRF) API examples
    └── employees/              # Employee management web app
```

---

## 🎯 What You'll Learn

- ✅ Django fundamentals: project structure, apps, URLs, views, templates
- ✅ Models & Django ORM
- ✅ Forms & CRUD operations
- ✅ Authentication, permissions & groups
- ✅ Building REST APIs with Django REST Framework
- ✅ Class-based views, search & filtering

**Perfect for:** Python beginners, students, aspiring backend developers, and anyone preparing for Django interviews.

---

## ⚡ Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/awaisqarni2/django_web_and_rest_framework_by_rathan.git
cd django_web_and_rest_framework_by_rathan

# 2. Pick a project
cd part_2_3_code/employees        # or django_rest_framework

# 3. Create & activate a virtual environment
python -m venv venv
source venv/bin/activate          # Windows: .\venv\Scripts\Activate.ps1

# 4. Install dependencies
python -m pip install -r requirements.txt
python -m pip install djangorestframework

# 5. Run it
python manage.py migrate
python manage.py runserver
```

Open **http://127.0.0.1:8000/** 🎉

**Requirements:** Python 3.12+, Django, Django REST Framework, django-filter, Pillow (for image uploads).

### 🔗 Useful Routes

| Route        | What it does                                                         |
| ------------ | -------------------------------------------------------------------- |
| `/admin/`    | Django admin (create a user with `python manage.py createsuperuser`) |
| `/students/` | Student views                                                        |
| `/api/v1/`   | REST API routes (employee viewset)                                   |

---

## 🧭 How to Study With This Repo

1. 🎬 Watch a section of the [course](https://youtu.be/1dlLxeri-Pg)
2. ⌨️ Code along yourself (don't just copy!)
3. 🔍 Compare with the code here if you get errors
4. 📝 Revise using the PDF/HTML notes
5. 🛠️ **Build your own project.** That's where real learning happens

---

## ⚠️ Notes

- Projects use SQLite for local development.
- Run tests with `python manage.py test` inside each project folder.
- Do **not** use the included secret keys or `DEBUG = True` in production.

---

## 🤝 Contribute

Found a typo or have a better explanation? Open an [issue](https://github.com/awaisqarni2/django_web_and_rest_framework_by_rathan/issues) or send a pull request. Improvements are welcome!

---

## 🔎 Keywords

`django` · `django notes` · `django tutorial` · `django for beginners` · `django rest framework` · `drf` · `drf tutorial` · `django rest api` · `python backend` · `python web development` · `django crud` · `django authentication` · `django course notes` · `django source code` · `django interview preparation` · `tech with rathan`

---

⭐ **If this repo saved you time, give it a star and share it with a friend who's learning Django!**

Made with ❤️ by [Awais Qarni](https://github.com/awaisqarni2)
