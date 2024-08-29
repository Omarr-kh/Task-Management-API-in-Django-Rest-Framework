# API Endpoints Documentation

## 1. Get All Tasks
- **URL:** `/api/tasks/`
- **Method:** `GET`
- **Description:** Retrieves a list of all tasks.
- **Response:**
  - **Status Code:** `200 OK`
  - **Body:**
    ```json
    [
        {
            "id": 1,
            "title": "Task 1",
            "description": "Description of Task 1",
            "completed": false,
            "user": 1
        },
        ...
    ]
    ```

## 2. View a Single Task
- **URL:** `/api/tasks/<int:pk>/`
- **Method:** `GET`
- **Description:** Retrieves the details of a single task by its ID.
- **URL Parameters:**
  - `pk` (int): The ID of the task to be retrieved.
- **Response:**
  - **Status Code:** `200 OK`
  - **Body:**
    ```json
    {
        "id": 1,
        "title": "Task 1",
        "description": "Description of Task 1",
        "completed": false,
        "user": 1
    }
    ```
    
## 3. Create a New Task
- **URL:** `/api/tasks/`
- **Method:** `POST`
- **Description:** Creates a new task.
- **Request Body:**
  - **Example:**
    ```json
    {
        "title": "New Task",
        "description": "Details of the new task",
        "completed": false,
        "user": 1
    }
    ```
- **Response:**
  - **Status Code:** `201 Created`
  - **Body:**
    ```json
    {
        "id": 1,
        "title": "New Task",
        "description": "Details of the new task",
        "completed": false,
        "user": 1
    }
    ```

## 4. Update an Existing Task
- **URL:** `/api/tasks/<int:pk>/`
- **Method:** `POST`
- **Description:** Updates an existing task by its ID. Supports partial updates.
- **URL Parameters:**
  - `pk` (int): The ID of the task to be updated.
- **Request Body:**
  - **Example:**
    ```json
    {
        "title": "Updated Task"
    }
    ```
- **Response:**
  - **Status Code:** `200 OK`
  - **Body:**
    ```json
    {
        "id": 1,
        "title": "Updated Task",
        "description": "Description of Task 1",
        "completed": false,
        "user": 1
    }
    ```
  - **Error Response:**
    - **Status Code:** `404 Not Found`
    - **Body:**
      ```json
      {
          "error": "Task not found"
      }
      ```

## 5. Delete a Task
- **URL:** `/api/tasks/<int:pk>/`
- **Method:** `DELETE`
- **Description:** Deletes a task by its ID.
- **URL Parameters:**
  - `pk` (int): The ID of the task to be deleted.
- **Response:**
  - **Status Code:** `204 No Content`
  - **Body:** `"Item successfully deleted!"`

