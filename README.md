# TO DO TASK MANAGER


# Flask Task Manager Application

This is a **Task Manager** web application built with Flask. It allows users to register, log in, and manage their tasks. The application includes user authentication, task creation, editing, and deletion functionalities.

## Features

1. **User Authentication**:
   - User registration.
   - User login and logout.
   - Passwords are securely hashed using `werkzeug.security`.

2. **Task Management**:
   - Add new tasks.
   - View a list of tasks.
   - Edit existing tasks.
   - Delete tasks.

3. **Database Integration**:
   - SQLite database is used to store user credentials and task data.
   - Models are defined using SQLAlchemy ORM.

4. **Session Management**:
   - User sessions are managed to persist login status.

## Requirements

- Python 3.7 or higher
- Flask
- Flask-SQLAlchemy
- Werkzeug




## File Structure

├── app.py              # Main Flask application\
├── templates          # HTML templates\
│   ├── index.html      # Home page\
│   ├── tasks.html      # Task management dashboard\
│   ├── edit.html       # Edit task page\
├── static             # Static files (CSS, JS, etc.)\
├── database.db         # SQLite database file\
├── requirements.txt    # Python dependencies\


## Security

Passwords are hashed using generate_password_hash and validated with check_password_hash.
User sessions are protected with a secret key stored in app.secret_key.



# HTML Overview
# Welcome Page - index.html

This HTML template defines the **Welcome Page** for the Flask Task Manager application. It serves as the entry point for users, allowing them to log in or register to access their To-Do tasks.

## Structure Overview

- **Base Template Extension**:
  The file extends `base.html` to inherit common styles and layout.

- **Body Content**:
  - A full-screen background (`height: 100vh`).
  - A centered container with a welcome message and login/register form.

- **Form Handling**:
  - A form for logging in or registering users.
  - A JavaScript function to dynamically set the form's action and submit it based on user interaction.

---

## HTML Elements and Attributes

### Background
- **Class**: `ppimage`
- **Style**: `height: 100vh` ensures the background occupies the full screen.

---

### Welcome Message
- **Container**:
  - Aligned centrally using `align=center` and `margin-top` styles for proper positioning.
- **Heading**:
  - `<h1>` displays "Welcome!" in white text.
- **Paragraph**:
  - `<p>` provides an additional message: "Log in/Register to see your To Do's."

---

### Login/Register Form
- **Form**:
  - ID: `auth-form`
  - `action`: Dynamically set using JavaScript to either the `login` or `register` route.
  - `method`: Defaults to `POST`.

- **Input Fields**:
  - `username` (text input).
  - `password` (password input).

- **Buttons**:
  - **Login**: Submits the form with the `login` route.
  - **Register**: Submits the form with the `register` route.

---


# Task Manager Dashboard - tasks.html

This HTML template defines the task manager dashboard for the Flask Task Manager application. It provides a user-friendly interface for managing tasks, including the ability to add, edit, and delete tasks.

---

## Structure Overview

### Base Template
- **Extension**:
  The template extends `base.html` to inherit shared layout and styles.

---

### Head Section
- **Title**:
  - Sets the page title to **Task Manager** using the `{% block head %}` block.

---

### Body Content
The main body is wrapped in `{% block body %}` and consists of the following sections:

#### Logout Button
- Positioned in the top-right corner of the page.
- Provides a logout option that redirects to the `logout` route.

#### Welcome Message
- Displays a personalized greeting: **Welcome, {{username}}!**


---

### Task Management
#### Displaying Tasks
- If no tasks exist, displays a message: *"There are no tasks..Create one here!"*
- Otherwise, tasks are presented in a responsive table with the following columns:
  1. **Task**: Task content.
  2. **Added**: The date the task was created (formatted as `YYYY-MM-DD`).
  3. **Actions**:
     - **Delete**: Deletes the task using the `/delete/{{task.id}}` route.
     - **Edit**: Redirects to the edit page using the `/edit/{{task.id}}` route.

#### Adding a New Task
- A form allows users to input a task and submit it to the `task` route using the `POST` method.

---

## HTML Elements and Attributes

### Table
- **Class**: `table table-hover m-5` for a styled, hoverable table.
- **Columns**:
  - **Task**: Displays the task description.
  - **Added**: Displays the task creation date, formatted using `strftime`.
  - **Actions**:
    - **Delete**: A small button styled for removing tasks.
    - **Edit**: A small button styled for editing tasks.

### Forms
- **Task Input Form**:
  - **Input**: A text field for entering task content.
  - **Submit Button**: Adds the new task by submitting the form to the `task` route.

### Buttons
- **Logout Button**:
  - **Class**: `btn btn-outline-secondary` for a styled, bordered button.
- **Action Buttons (Delete/Edit)**:
  - Small, light-styled buttons with custom padding and font sizes.

---

## Flask Integration

### Jinja Placeholders
- **Dynamic Content**:
  - `{{username}}`: Displays the logged-in user's username.
  - `{{task.content}}`: Displays the content of each task.
  - `{{task.created.strftime("%Y-%m-%d")}}`: Formats the task creation date.
- **Conditional Rendering**:
  - Checks if tasks exist using `{% if tasks | length < 1 %}`.
- **Routes**:
  - `{{url_for('logout')}}`: URL for logging out.
  - `/delete/{{task.id}}`: URL for deleting a task.
  - `/edit/{{task.id}}`: URL for editing a task.
  - `{{url_for('task')}}`: URL for submitting new tasks.


## Styling
- **Alignment**:
  - Containers are centered or right-aligned using `align=center` and `align=right`.
- **Table**:
  - Styled with Bootstrap classes (`table table-hover`).
  - Compact action buttons with custom padding and font sizes.
- **Form**:
  - Simple, centered task submission form with a primary button.








