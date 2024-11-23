# Blogging Platform Backend

This repository contains the backend implementation for a **Full-Stack Blogging Platform** built using **Django** and **Django REST Framework (DRF)**. The backend provides a robust, scalable, and secure API to power the platform's features, enabling seamless interaction between users and the frontend interface.

## Features

- **User Authentication and Authorization**:  
  - Registration, Login, Logout, and Password Reset.  
  - JWT-based authentication for secure API access.  

- **Blog Management**:  
  - Create, update, and delete blog posts with rich content support.  
  - Categorization and tagging of posts for better discoverability.  

- **Comment System**:  
  - Nested comment structure for threaded discussions.  
  - Moderation tools to manage user-generated content.  

- **User Profiles**:  
  - Customizable user profiles with bio, profile picture, and social links.  
  - Follow and unfollow functionality to track user activities.  

- **Like and Share**:  
  - Support for liking posts and sharing content via APIs.  

- **Search and Filtering**:  
  - Advanced search capabilities with filtering by tags, categories, and author.  

- **Analytics and Insights**:  
  - Track post views and user engagement metrics.  

## Tech Stack

- **Backend Framework**: Django  
- **API Layer**: Django REST Framework (DRF)  
- **Database**: PostgreSQL (or MySQL, customizable)  
- **Authentication**: djangorestframework-simplejwt  
- **Other Tools**:  
  - Celery with Redis for background tasks (e.g., sending email notifications).  
  - Django Signals for real-time actions (e.g., sending alerts on new comments).  
