# Novatech E-Commerce 🛒

A complete, modern e-commerce web application built using Django. The platform is designed specifically for selling electronics and mobile devices, featuring a sleek, dark-themed neumorphic user interface that provides a premium aesthetic and engaging user experience.

## 🌟 Features
- **Neumorphic Dark Theme UI**: A stunning, custom-designed interface utilizing soft shadows, glassmorphism, and modern aesthetics.
- **User Authentication**: Secure and fully functional Login and User Registration systems.
- **Product Management**: Powerful admin dashboard (via standard Django Admin) to entirely manage inventory (Add, Update, Delete electronics).
- **Contact Form**: An integrated contact form that securely stores customer inquiries in the backend database.
- **Product Details**: Detailed view pages for individual items showcasing product specifications and images.
- **Responsive Design**: Designed to work and look great on desktops, tablets, and mobile phones alike.

## 🛠️ Technology Stack
- **Backend:** Python, Django
- **Frontend:** HTML5, Vanilla CSS3 (Custom Neumorphism), crispy-bootstrap5
- **Database:** SQLite3 (Configured default)
- **Image Processing:** Pillow (for dynamic product image uploads)

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sujeet05-dev/Novatech-E-commerce-.git
   cd Novatech-E-commerce-
   ```

2. **Create a Virtual Environment (Optional but highly recommended):**
   ```bash
   python -m venv myenv
   myenv\Scripts\activate  # On Windows
   # source myenv/bin/activate # On macOS/Linux
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create an admin account (To access the admin dashboard):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

7. Open your preferred web browser and navigate to `http://127.0.0.1:8000/`. 
To access the administrator panel to add products, go to `http://127.0.0.1:8000/admin/`.

## 📸 Screenshots
*(Coming soon: Consider adding screenshot images of your homepage, login page, and shop interface inside a `media` or `docs` folder and linking them here!)*

---
*Developed by Sujeet*
