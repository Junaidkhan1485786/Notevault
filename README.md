# Notevault
NoteVault is secure your all notes

# **NoteVault**

**NoteVault** is a note-taking application built with **FastAPI** and **MongoDB**, designed to store and manage notes with a title, date, and detailed description. This project provides a backend API for creating, retrieving, updating, and deleting notes.

## Features
- **Create a new note** with title, date, and detailed description.
- **Retrieve** notes by title or date.
- **Update** existing notes.
- **Delete** notes by ID.
- **MongoDB** as the primary database for efficient and scalable storage.
- Fast and lightweight API with **FastAPI**.

---

## Tech Stack
- **Backend Framework**: FastAPI
- **Database**: MongoDB
- **Language**: Python
- **Environment Management**: Virtualenv or Conda (recommended)
- **Tools**: PyMongo for MongoDB interaction, Uvicorn for running the FastAPI app

---

## Table of Contents
1. [Installation](#installation)
2. [Environment Variables](#environment-variables)
3. [Running the Application](#running-the-application)
4. [API Endpoints](#api-endpoints)
5. [Contributing](#contributing)
6. [License](#license)

---

## Installation

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.8 or higher
- MongoDB (locally or through a cloud provider like MongoDB Atlas)
- Virtual Environment (optional but recommended)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/NoteVault.git
    cd NoteVault
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\\Scripts\\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up MongoDB. Make sure MongoDB is running locally or configure a MongoDB Atlas cluster.

---

## Environment Variables

Before running the application, you need to set the following environment variables:

| Variable | Description | Example |
| -------- | ----------- | ------- |
| `MONGODB_URI` | MongoDB connection string | `mongodb://localhost:27017` or your MongoDB Atlas connection string |
| `DATABASE_NAME` | Name of the MongoDB database | `notevault_db` |

Example (for Linux/macOS):
```bash
export MONGODB_URI="your-mongodb-connection-string"
export DATABASE_NAME="notevault_db"
```

Example (windows):
```bash
set MONGODB_URI="your-mongodb-connection-string"
set DATABASE_NAME="notevault_db"
```

Running the Application
After setting up the environment variables, run the FastAPI server using Uvicorn:
```bash
uvicorn app.main:app --reload --port 8000
```
By default, the API will be available at http://127.0.0.1:8000.

## API Endpoints

Here is the list of main endpoints provided by the **NoteVault** API:

### 1. **Create a Note**
- **Endpoint**: `/notes`
- **Method**: POST
- **Request Body**:
    ```json
    {
      "title": "Note Title",
      "date": "2024-10-01",
      "description": "Detailed note description here."
    }
    ```
- **Response**: 
    ```json
    {
      "id": "64bf1d7f45d6a",
      "title": "Note Title",
      "date": "2024-10-01",
      "description": "Detailed note description here."
    }
    ```

### 2. **Get All Notes**
- **Endpoint**: `/notes`
- **Method**: GET
- **Response**:
    ```json
    [
      {
        "id": "64bf1d7f45d6a",
        "title": "Note Title",
        "date": "2024-10-01",
        "description": "Detailed note description here."
      }
    ]
    ```

### 3. **Update a Note**
- **Endpoint**: `/notes/{id}`
- **Method**: PUT
- **Request Body**:
    ```json
    {
      "title": "Updated Title",
      "date": "2024-10-01",
      "description": "Updated description."
    }
    ```
- **Response**:
    ```json
    {
      "message": "Note updated successfully."
    }
    ```

### 4. **Delete a Note**
- **Endpoint**: `/notes/{id}`
- **Method**: DELETE
- **Response**:
    ```json
    {
      "message": "Note deleted successfully."
    }
    ```

---

## Contributing

If you would like to contribute to **NoteVault**, feel free to open a pull request or submit issues. Please ensure all tests pass before submitting your PR.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
"""
