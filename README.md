# EventHive

EventHive is a modern, full-featured event management platform built with Django. It enables users to discover, organize, and manage events with ease, offering a seamless experience for both attendees and organizers.

## Technologies Used
- **Backend:** Django (Python)
- **Frontend:** HTML, Tailwind CSS
- **Database:** SQLite (default, can be changed)
- **Hosting:** PythonAnywhere

## Live Demo
Visit the live site: [EventHive on PythonAnywhere](http://talhaameeroffical.pythonanywhere.com)

## Features
- **Event Listings:** Browse upcoming events with detailed information.
- **User Authentication:** Secure signup, login, and profile management.
- **Dashboard:** Personalized dashboard for users and organizers.
- **Admin Panel:** Manage events, users, and site content.
- **Responsive UI:** Built with Tailwind CSS for a clean, modern look.
- **Contact & About Pages:** Easy access to information and support.

## Getting Started
1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd <project-folder>
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv env
   env\Scripts\activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```
5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```
6. **Access the site:**
   Open [http://localhost:8000](http://localhost:8000) in your browser.

## Configuration
- Update `.env` with your secret keys and email settings.
- Static and media files are managed via Django settings.

## Folder Structure
- `event_system/` - Main Django project
- `events/` - Event app (models, views, forms)
- `templates/` - HTML templates
- `static/` - Static files (CSS, images)
- `env/` - Python virtual environment

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---
**EventHive** – Your gateway to seamless event management and discovery.
