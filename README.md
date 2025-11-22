

# 📘 URL Shortener

A lightweight and fast URL shortener built using **Flask**, styled with
**HTML/CSS**, and powered by **AJAX** for instant short-link generation
--- similar to Bit.ly.

## 🚀 Features

-   🔗 Shorten any long URL instantly\
-   ⚡ No page reload --- uses AJAX\
-   🎨 Clean, modern UI\
-   📋 One-click copy button\
-   🔄 Auto-redirect using short keys\
-   🧩 Simple and beginner-friendly codebase

## 🛠️ Tech Stack

-   **Backend:** Python (Flask)\
-   **Frontend:** HTML, CSS, JavaScript (Fetch API)\
-   **Data Storage:** In-memory dictionary\
-   **Architecture:** MVC-like with manager utilities

## 📁 Project Structure

    project/
    │
    ├── app.py
    ├── manager/
    │     ├── urlStrGenerator.py
    │     ├── global_urls.py
    │
    └── templates/
          └── index.html

## 🔧 Setup & Installation

``` bash
pip install flask
python app.py
```

Open in browser:

    http://localhost:8000/get_small_url

## 🧠 How It Works

1.  User enters a long URL\
2.  Flask generates a **unique short key**\
3.  The key is stored with its original URL\
4.  User gets a short link like:

```{=html}
<!-- -->
```
    http://localhost:8000/AbC123

5.  Visiting this redirects to the original URL.

## 🌱 Future Enhancements

-   🔐 User accounts\
-   📊 Link analytics\
-   📅 URL expiry\
-   📱 Mobile UI improvements

## ⭐ Author

**Sudama Kumar Sharma**\
Python Developer • Full Stack Learner
