# 📚 Library Management System using Python and Streamlit

A **full-featured, role-based Library Management System** built using **Python** and **Streamlit**, designed to digitize and automate library operations such as book issuing, returns, viewing, recommendations, and more.  
The system supports both **Students** and **Librarians**, offering secure login, detailed book previews, personalized recommendations, real-time notifications, chatbot assistance, and data stored in **JSON** format.

---
## Screenshots  

<p align="center">
  <img src="Screenshot/Screenshot.gif" width="500"/>
</p>

## 🚀 Features

### 🔐 User Authentication
- Signup/Login with **Name**, **Mobile Number**, **Email**, **Password**, and **Role** (Student/Librarian/Others).  
- Secure password validation and role-based access.  
- Librarian-exclusive features for managing the system.  

### 📖 Book Management
- **View All Books** with:
  - Book ID, Title, Author
  - Cover image, Description
  - Availability Status
- **Book Overview with Index Page**  
- JSON-based book storage for portability and flexibility.  
- **Add New Book** *(Librarian only)*  
- **Delete Book** *(Librarian only)*  

### 📋 Student Utilities
- **Add to Book List** (Wishlist/Favorites before issuing)  
- **Issue Book** with:
  - Due date tracking  
  - Countdown on days remaining  
- **Return Book** to mark availability  
- **View Issued Books** and manage reading activity  

### 🤖 Book Recommendation System
- Suggests books based on:
  - Favorite Books
  - Past borrowing history  
  - Book categories & keywords  
- Enhances discovery of related books  

### 🔔 Notifications & Fines
- Due date reminders  
- Fine calculation for overdue books  
- Notifications displayed inside the app  

### 📊 Librarian Dashboard
- Track issued books with due dates & fines  
- Monitor user activity  
- View analytics of most issued & most favorited books  

### 💬 Chatbot Assistant
- Integrated **AI-based chatbot**  
- Helps students find books and get recommendations instantly  
- Provides guidance on library usage  

---

## 🛠️ Tech Stack

| Technology      | Usage                                |
|-----------------|--------------------------------------|
| `Python`        | Backend & Logic                      |
| `Streamlit`     | Frontend UI                          |
| `JSON`          | Data storage for books and users     |
| `Pandas`        | Data processing and management       |
| `Streamlit Cloud` | Deployment platform                |
| `GitHub`        | Version Control & Hosting            |
| `hashlib`       | Password hashing & authentication    |
| `datetime`      | Due dates, fines, reminders          |

---

## 📂 Folder Structure

```
📁 Library-Management-System/
│
├── 📄 app.py                  # Main Streamlit application
├── 📁 assets/                 # Book cover images
├── 📄 books.json              # Book data with descriptions & availability
├── 📄 users.json              # User data (students/librarians)
├── 📄 issued_books.json       # Issued book records
├── 📄 requirements.txt        # Python dependencies
└── 📄 README.md               # Project documentation
```

---

## 🖥️ Live Demo

🌐 **Try the app now**:  
[🔗 Live Streamlit App](https://library-management-system-9wooqes876lppnvdb7nzpq.streamlit.app/#welcome-to-library-management-system)  

---

## 📌 How to Run Locally

1. Clone this repo:
```bash
git clone https://github.com/thisisdhritiman1439/Library-Management-System.git
cd Library-Management-System
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

---

## 📂 Demo Credentials

Use these demo accounts for testing:

- **Librarian**
  - Email: `librarian@example.com`
  - Password: `admin123`

- **User**
  - Email: `user@example.com`
  - Password: `user123`

---

## 📷 Screenshots

> Add screenshots in the `assets/` folder and embed them here:

* ✅ Login & Sign Up  
* 📚 View All Books  
* 📘 Book Description + Index  
* ➕ Add/Delete Book  
* 📥 Issue/Return Book  
* ⭐ Favorites  
* 🤖 Recommendation Panel  
* 💬 Chatbot Assistant  
* 📊 Analytics Dashboard  

---

## 📈 Future Enhancements

* 📧 Email/OTP-based authentication  
* 🔍 Advanced search & filter system  
* 🧾 Export issued book reports to CSV/Excel  
* 📊 More detailed analytics dashboard for librarians  
* ☁️ Database integration (SQLite/PostgreSQL)  
* 📱 Mobile-friendly responsive design  

---

## 👨‍💻 Developers

| Name                     | Role                          |
| ------------------------ | ----------------------------- |
| Khandakar Nafees Hossain | Project Lead & Developer      |
| Dhritiman Bera           | Developer & Designer          |
| Parthib Mahapatra        | Tester & Deployment           |
| Mr. Subhabrata Sengupta  | Faculty Guide                 |
| Dr. Rupayan Das          | Faculty Guide                 |

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Acknowledgments

* Built with ❤️ using Python and Streamlit  
* Inspired by the real-world challenges of manual library systems  
* Enhanced with modern features like recommendations, chatbot, and analytics  
