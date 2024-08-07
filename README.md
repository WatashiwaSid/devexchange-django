# Dev Exchange - A Tech Discussion Forum built with Django & Tailwind

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Microsoft Azure](https://img.shields.io/badge/Microsoft_Azure-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white)
![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

## Introduction

Dev Exchange is a dynamic and interactive platform designed for developers to connect, collaborate, and share knowledge. 
Dev Exchange is inspired by the popular Q&A platform Stack Overflow and aims to provide a vibrant community where developers can ask questions, provide answers, and share insights on a wide range of programming topics.

## Table of Content
  * [Introduction](#introduction)
  * [Technologies Used](#technologies-used)
  * [Features](#features)
  * [Installation](#installation)
  * [Tailwind Configuration](#tailwind-configuration)
  * [Media Configuration](#media-configuration)
  * [Website Screenshots](#website-screenshots)
  * [Admin Screenshots](#admin-screenshots)
  * [Security](#security)

## Technologies used

Dev Exchange is built with a powerful and modern technology stack to ensure performance, scalability, and security:

- **Backend:** *Django*, a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Frontend:** *Tailwind CSS* for modern and responsive UI, *Jinja2* for template rendering, and *JavaScript* for interactivity.
- **Database:** *PostgreSQL* for deployment environments and *SQLite3* for development, ensuring efficient data management.
- **Version Control:** *Git* and *GitHub* for source code management, enabling collaborative development.
- **Cloud Hosting:** *Microsoft Azure* Virtual Machine for cloud deployment, ensuring high availability and performance.
- **Image Processing:** Pillow for handling image uploads and processing.

## Features

- **Robust Authentication:** A secure and reliable authentication system that supports user **registration**, **login**, and **logout** processes. This ensures that user data is protected and access to the platform is controlled.

- **User Profiles:** Users can create and customize their profiles, providing a personalized experience. Features include the ability to update profile information and manage personal data.

- **Secure CRUD Functionality:** Dev Exchange offers a comprehensive CRUD (Create, Read, Update, Delete) system for questions and answers. The platform ensures that all operations are conducted securely, protecting against unauthorized access and data breaches.

- **Powerful Admin Panel:** An intuitive and powerful admin panel that allows administrators to manage the platform efficiently. Features include user management, content moderation, and analytics, providing full control over the platform's operations.

## Installation

1. Clone the repository:
```
https://github.com/WatashiwaSid/devexchange-django
```
2. Navigate to the project directory:
```
cd `devexchange-django`
```
3. Create and activate a new virtual environment:
```
python -m venv env
source env/bin/activate (Linux)
./env/Scripts/activate (Windows)
```
4. Install the project dependencies:
```
pip install -r requirements.txt
```
5. Create the database tables:
```python
python manage.py migrate
```
6. Run the development server:
```python
python manage.py runserver
```

## Tailwind Configuration
This version of the source code uses Tailwind CSS via the public CDN to render styles. The project also includes a pre-built CSS file, which can be utilized with the load static tag provided by the Jinja templating engine.

### Building Your Own Tailwind Files
If you wish to customize and build your own Tailwind CSS files, follow these steps:

1. **Modify settings.py:**

Make the necessary changes in the settings.py file located in the stackoverflow directory of the project. Ensure that all Tailwind configurations and paths are correctly set up according to your requirements.

2. **Node.js Requirement:**

Building Tailwind CSS requires Node.js. Ensure that Node.js is installed on your system. You can download it from the official Node.js website.

3. **Configure Node.js Path:**

In the settings.py file, configure the Node.js path appropriately to ensure the build process can locate the Node.js binary.

4. **Build Tailwind CSS:**

Once all necessary configurations are complete, run the following command to render Tailwind CSS:
```
python manage.py tailwind start
```
You can build the final css file with the following command:
```
python manage.py tailwind build
```

You can find a reference to setting up tailwind with django at [chaicode docs](https://docs.chaicode.com/tailwind-to-django/).

## Media Configurations
Put all media files in the */media* folder in the same structure as shown in the following screenshot:

![Imgur](https://imgur.com/xEswHNt).

## Website Screenshots



## Admin Screenshots

## Security
Dev Exchange prioritizes security and follows OWASP standards to protect against common vulnerabilities:

- **Path Traversal**
- **CSRF Attacks**
- **HTTP Host Header Injection**

Each vulnerability is manually tested and mitigated to ensure the safety and privacy of our users.
