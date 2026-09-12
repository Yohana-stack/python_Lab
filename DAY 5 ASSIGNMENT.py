# DAY 5 ASSIGNMENT

## A) User Manual Procedure

### How to Set Up a GitHub Repository and Make a First Commit

#### Introduction

GitHub is a platform used to store and manage software projects online. A GitHub repository is a place where project files and their history are stored. This procedure explains how a beginner can create a repository, add a project file, and make the first commit.

### Prerequisites

Before starting, the reader needs:

* A computer with internet access.
* A web browser such as Chrome, Edge, or Firefox.
* A GitHub account.
* A project file ready to upload.
* Basic knowledge of creating and locating files on a computer.

### Procedure

#### Step 1: Open GitHub

Open a web browser and go to GitHub.

**Expected result:** The GitHub website opens.

#### Step 2: Sign in to GitHub

Sign in using your GitHub account.

**Expected result:** Your GitHub account homepage is displayed.

#### Step 3: Open the new repository page

Select the option to create a new repository.

**Expected result:** The new repository creation form appears.

#### Step 4: Enter the repository name

Enter `python-week-1-assignment` as the repository name.

**Expected result:** The repository name appears in the repository-name field.

#### Step 5: Enter the repository description

Enter `My Week 1 Python assignment demonstrating variables, comments, and print statements.` as the description.

**Expected result:** The description appears in the description field.

#### Step 6: Set the repository visibility

Select **Public** as the repository visibility.

**Expected result:** The Public option is selected.

#### Step 7: Create the repository

Select **Create repository**.

**Expected result:** The new repository page opens.

#### Step 8: Open the file-upload option

Select **Add file** and choose **Upload files**.

**Expected result:** The file-upload page opens.

#### Step 9: Select the Python file

Select the `all_about_me.py` file from your computer.

**Expected result:** The Python file appears in the list of files waiting to be uploaded.

#### Step 10: Upload the file

Select **Commit changes**.

**Expected result:** GitHub saves the file and creates the first commit.

#### Step 11: Verify the repository

'Open the repository's main page.

**Expected result:** The `all_about_me.py` file is visible in the repository.

### Screenshot Description

A screenshot should show the completed GitHub repository page. The screenshot should clearly display the repository name `python-week-1-assignment`, the uploaded `all_about_me.py` file, and the commit information. The screenshot should be clear enough for an instructor to verify that the repository was created successfully and that the Python file was uploaded.

### Troubleshooting

**Problem: The uploaded file does not appear in the repository.**

The most common beginner error is forgetting to complete the commit after selecting the file. Return to the upload page, make sure the file is selected, and select **Commit changes**. Then refresh the repository page and check whether the file appears.

---

# B) API Reference Entry

## Create a New Task

### Endpoint

**HTTP Method:** `POST`

**Endpoint Path:**

`/api/v1/projects/{projectId}/tasks`

### Description

Creates a new task inside a specified project in a project management application.

The request must be made by an authenticated user. The new task contains a title, an optional description, an assignee, a due date, and a priority level.

### Authentication

The endpoint requires a valid bearer access token.

### Request Headers

| Header          | Required | Type   | Description                                        |
| --------------- | -------- | ------ | -------------------------------------------------- |
| `Authorization` | Yes      | String | Bearer access token used to authenticate the user. |
| `Content-Type`  | Yes      | String | Must be `application/json`.                        |
| `Accept`        | Optional | String | Specifies that the client expects a JSON response. |

### Path Parameters

| Parameter   | Type   | Required | Description                                                      |
| ----------- | ------ | -------- | ---------------------------------------------------------------- |
| `projectId` | String | Yes      | Unique identifier of the project where the task will be created. |

### Query Parameters

This endpoint does not require any query parameters.

### Request Body

The request body must be formatted as JSON.

| Field         | Type   | Required | Description                                                           |
| ------------- | ------ | -------- | --------------------------------------------------------------------- |
| `title`       | String | Yes      | Name or short title of the task.                                      |
| `description` | String | No       | Additional information about the task.                                |
| `assigneeId`  | String | Yes      | Unique ID of the user assigned to the task.                           |
| `dueDate`     | String | Yes      | Date when the task is due, using the `YYYY-MM-DD` format.             |
| `priority`    | String | Yes      | Priority of the task. Allowed values are `low`, `medium`, and `high`. |

### Example Request

```http
POST /api/v1/projects/proj_1025/tasks HTTP/1.1
Host: api.example.com
Authorization: Bearer eyJhbGciOi...
Content-Type: application/json
Accept: application/json
```

```json
{
  "title": "Prepare project presentation",
  "description": "Create the slides and review the presentation before the team meeting.",
  "assigneeId": "usr_2048",
  "dueDate": "2026-09-20",
  "priority": "high"
}
```

### HTTP Response Codes

| Status Code                 | Meaning                                                                                    |
| --------------------------- | ------------------------------------------------------------------------------------------ |
| `201 Created`               | The task was successfully created.                                                         |
| `400 Bad Request`           | The request contains invalid or missing data.                                              |
| `401 Unauthorized`          | Authentication is missing or the access token is invalid or expired.                       |
| `403 Forbidden`             | The authenticated user does not have permission to create a task in the project.           |
| `404 Not Found`             | The specified project or assignee does not exist.                                          |
| `409 Conflict`              | The task cannot be created because it conflicts with an existing resource or project rule. |
| `422 Unprocessable Entity`  | The request format is valid, but one or more supplied values fail validation.              |
| `500 Internal Server Error` | An unexpected error occurred on the server.                                                |

### Successful Response

**Status:** `201 Created`

json
{
  "id": "task_78421",
  "projectId": "proj_1025",
  "title": "Prepare project presentation",
  "description": "Create the slides and review the presentation before the team meeting.",
  "assigneeId": "usr_2048",
  "dueDate": "2026-09-20",
  "priority": "high",
  "status": "todo",
  "createdAt": "2026-09-11T22:30:00Z",
  "updatedAt": "2026-09-11T22:30:00Z"
}


### Response Field Description

| Field         | Type   | Description                                                   |
| ------------- | ------ | ------------------------------------------------------------- |
| `id`          | String | Unique identifier assigned to the new task.                   |
| `projectId`   | String | Identifier of the project containing the task.                |
| `title`       | String | Title of the newly created task.                              |
| `description` | String | Optional detailed description of the task.                    |
| `assigneeId`  | String | ID of the user assigned to the task.                          |
| `dueDate`     | String | Task deadline in `YYYY-MM-DD` format.                         |
| `priority`    | String | Task priority: `low`, `medium`, or `high`.                    |
| `status`      | String | Current task status. A newly created task starts with `todo`. |
| `createdAt`   | String | Date and time when the task was created.                      |
| `updatedAt`   | String | Date and time when the task was last updated.                 |

### Summary

The `POST /api/v1/projects/{projectId}/tasks` endpoint allows an authenticated user to create a task in a project. The request must contain the task title, assignee, due date, and priority. A description can optionally be included. When successful, the API returns HTTP `201 Created` together with the newly created task and its details.
