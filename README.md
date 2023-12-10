![5](https://github.com/mustafa854/simpleInstagramClone/assets/84233282/2ec50036-921b-4077-8eb2-afc8cbc70533)

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
   - [Search Users Result](#search-users)
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
![2](https://github.com/mustafa854/simpleInstagramClone/assets/84233282/edadb669-4f24-4063-ae29-3d56f4af32ad)

### Login User <a name="login-user"></a>
![1](https://github.com/mustafa854/simpleInstagramClone/assets/84233282/aa262852-3563-4e1b-87a1-0c03001a949b)

### Form Validation | User Creadentails Validation <a name="validation-user"></a>
![3 1](https://github.com/mustafa854/simpleInstagramClone/assets/84233282/92fc4c54-faa8-49f5-8fd1-2ccf91749449)

![3 2](https://github.com/mustafa854/simpleInstagramClone/assets/84233282/7e311510-6377-4e8d-912e-b36b8c789ce1)

![3 3](https://github.com/mustafa854/simpleInstagramClone/assets/84233282/ef80e123-c2ac-4dc8-91fb-33bf38446106)

### Home <a name="home"></a>
![4](https://github.com/mustafa854/simpleInstagramClone/assets/84233282/233973e0-00b2-464d-950f-ece10089a79b)

### Upload Posts <a name="upload-posts"></a>
![5](https://github.com/mustafa854/simpleInstagramClone/assets/84233282/e313d496-5a1f-4242-90ca-da2c87665951)

### User Settings <a name="user-settings"></a>
![6](https://github.com/mustafa854/simpleInstagramClone/assets/84233282/9fb6ac40-8a9f-471e-8364-411a00f5ddaa)

### Current User Profile <a name="my-profile"></a>
![7 1](https://github.com/mustafa854/simpleInstagramClone/assets/84233282/1f50a03f-a94e-466b-9c7a-b86ad9ceb987)


### Other User Profile <a name="other-profile"></a>
![8 1](https://github.com/mustafa854/simpleInstagramClone/assets/84233282/dc955e5b-2cf2-4c8f-895e-5ac6ac4ac5f0)

### Follow and Unfollow Profile <a name="follow-profile"></a>
![8 2](https://github.com/mustafa854/simpleInstagramClone/assets/84233282/4cce7ac1-e551-4f4a-a781-cee7b1848935)

### All Following Users post <a name="following-users-post"></a>
![8 3](https://github.com/mustafa854/simpleInstagramClone/assets/84233282/40585721-4e38-4540-8f6c-587ebe0e7254)

### Search Users Result <a name="search-users"></a>
![9](https://github.com/mustafa854/simpleInstagramClone/assets/84233282/2cf719d8-99e1-4232-8932-8aa4153f2b66)

### Like Users <a name="admin-panel-user-list"></a>
![10](https://github.com/mustafa854/simpleInstagramClone/assets/84233282/0139886a-c736-48be-952b-9c5fe826c054)

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
