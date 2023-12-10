# Instagram Clone using Django

This Instagram Clone project is built using Django and provides users with a social media platform for posting images, following other users, liking posts, and managing user profiles.

## Table of Contents

1. [About](#about)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Demo Images](#demo-images)
   - [Register User](#register-user)
   - [Login User](#login-user)
   - [Form Validation | User Creadentails Validation](#validation-user)
   - [Home](#home)
   - [Upload Posts](#upload-posts)
   - [User Settings](#user-settings)
   - [Current User Profile](#my-profile)
   - [Other User Profile](#other-profile)
   - [Follow and Unfollow Profile](#follow-profile)
   - [All Following Users post](#following-users-post)
   - [Search Users](#search-users)
   - [Like Users](#like-users)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Technologies Used](#technologies-used)

## About <a name="about"></a>

This repository contains an Instagram Clone project developed using Django. The platform enables users to create profiles, upload images, follow other users, like posts, and update their settings. The application offers features similar to the popular social media platform Instagram.

## Features <a name="features"></a>

This Instagram Clone project boasts several features:

- **User Authentication:** Allows users to register, log in, and log out securely.
- **Profile Management:** Enables users to update their profiles, including profile images, bios, and locations.
- **Posting Images:** Users can upload images with captions to share with their followers.
- **Following Users:** Functionality to follow other users and view their posts.
- **Like Posts:** Users can like posts and see the number of likes on each post.
- **Search Functionality:** Provides a search feature to find users based on their usernames.

## Project Structure <a name="project-structure"></a>

The project directory structure is organized as follows:

```plaintext
instagram-clone/
├── core/                    # Django app for managing posts, profiles, likes, and followers
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── authentication/          # Django app for user authentication
│   ├── urls.py
│   └── views.py
├── templates/               # HTML templates (index.html, profile.html, setting.html, signin.html, signup.html)
├── static/                  # Static assets (assets, css, fonts, images, settings, js, video)
├── media/                   # Media files (posts, profile pictures)
├── manage.py                # Django's command-line utility
└── env/                     # Virtual environment folder
└── requirements.txt         # Required Python packages
```

## Demo Images <a name="demo-images"></a>

### Register User <a name="register-user"></a>

### Login User <a name="login-user"></a>

### Form Validation | User Creadentails Validation <a name="validation-user"></a>

### Home <a name="home"></a>

### Upload Posts <a name="upload-posts"></a>

### User Settings <a name="user-settings"></a>

### Current User Profile <a name="my-profile"></a>

### Other User Profile <a name="other-profile"></a>

### Follow and Unfollow Profile <a name="follow-profile"></a>

### All Following Users post <a name="following-users-post"></a>

### Search Users <a name="search-users"></a>

### Like Users <a name="admin-panel-user-list"></a>

## Installation <a name="like-users"></a>

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mustafa854/simpleInstagramClone.git
   ```

2. **Create and activate a virtual environment:**

   ```bash
   # Create a virtual environment
   python -m venv myenv

   # Activate the virtual environment
   source myenv/bin/activate  # For Linux or macOS
   .\myenv\Scripts\activate   # For Windows
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Django settings:**

   - Open `settings.py` and set up your database configurations.

5. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Start the Django server:**

   ```bash
   python manage.py runserver
   ```

## Usage <a name="usage"></a>

- Visit the homepage to view posts and profiles.
- Sign up or log in to access features like uploading posts, updating settings, following users, and liking posts.

## Technologies Used <a name="technologies-used"></a>

- Django
- Bootstrap 5
- Debug Toolbar
