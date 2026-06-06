# Docker Two-Tier Flask & MySQL Application

## Overview

This project demonstrates a simple two-tier application using Docker, Flask, and MySQL. The application allows users to submit messages through a web interface, which are then stored in a MySQL database and displayed on the webpage.

The project focuses on Docker networking concepts such as custom bridge networks, container-to-container communication, and Docker DNS-based service discovery.

---

## Architecture

```text
+-------------------+
|   User Browser    |
+---------+---------+
          |
          v
+-------------------+
| Flask Container   |
| Port: 5000        |
+---------+---------+
          |
          | Custom Bridge Network
          |
          v
+-------------------+
| MySQL Container   |
| messages table    |
+-------------------+
```

---

## Technologies Used

* Docker
* Python
* Flask
* MySQL
* Linux

---

## Key Concepts Demonstrated

* Docker image creation using Dockerfile
* Container deployment and management
* Custom bridge network creation
* Container-to-container communication
* Docker DNS-based service discovery
* Flask and MySQL integration
* Port mapping and application exposure
* Multi-container application deployment

---

## Project Structure

```text
two-tier-app/
│
├── app.py
├── Dockerfile
├── requirements.txt
│
└── templates/
    └── index.html
```

---

## Create Docker Network

```bash
docker network create my-network
```

Verify:

```bash
docker network ls
```

---

## Run MySQL Container

```bash
docker run -d \
--name mysql-db \
--network my-network \
-e MYSQL_ROOT_PASSWORD=root123 \
-e MYSQL_DATABASE=messagesdb \
mysql:8.0
```

---

## Create Database Table

Enter the container:

```bash
docker exec -it mysql-db bash
```

Login to MySQL:

```bash
mysql -u root -p
```

Select the database:

```sql
USE messagesdb;
```

Create table:

```sql
CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(255)
);
```

---

## Build Flask Image

```bash
docker build -t flask-mysql-app .
```

---

## Run Flask Container

```bash
docker run -d \
--name flask-app \
--network my-network \
-p 5000:5000 \
flask-mysql-app
```

---

## Verify Container Networking

Check network details:

```bash
docker network inspect my-network
```

Both containers should appear under the network:

```text
mysql-db
flask-app
```

---

## Test Connectivity

Access Flask container:

```bash
docker exec -it flask-app sh
```

Ping MySQL container:

```bash
ping mysql-db
```

Successful replies confirm Docker DNS resolution and network connectivity.

---

## Access the Application

Open a browser and visit:

```text
http://localhost:5000
```

Enter a message and click **Submit**.

The message will be stored in the MySQL database and displayed on the webpage.

---

## Verify Stored Messages

Connect to MySQL:

```bash
docker exec -it mysql-db mysql -u root -p
```

Run:

```sql
USE messagesdb;
SELECT * FROM messages;
```

Example output:

```text
+----+--------------------------+
| id | message                  |
+----+--------------------------+
|  1 | Hello Docker             |
|  2 | Docker Networking Test   |
+----+--------------------------+
```

---

## Learning Outcomes

* Built a two-tier application using Docker, Flask, and MySQL.
* Configured a custom Docker bridge network for container communication.
* Used Docker DNS to connect containers using container names.
* Implemented database integration between application and database containers.
* Gained hands-on experience with Docker networking and multi-container deployments.

## Verifying Data Stored in the MySQL Container

After submitting messages through the Flask web application, verify that the data has been successfully stored in the MySQL database by following these steps:

### Step 1: Access the MySQL Container

Open an interactive shell inside the running MySQL container:

```bash
docker exec -it mysql-db bash
```

### Step 2: Log in to the MySQL Server

Connect to MySQL using the root user:

```bash
mysql -u root -p
```

When prompted, enter the root password:

```text
root123
```

### Step 3: Select the Application Database

Switch to the database created for the application:

```sql
USE messagesdb;
```

### Step 4: View Stored Records

Retrieve all records from the `messages` table:

```sql
SELECT * FROM messages;
```

### Example Output

```text
+----+--------------------------+
| id | message                  |
+----+--------------------------+
|  1 | Hello Docker             |
|  2 | Docker Networking Test   |
|  3 | Flask MySQL Connection   |
+----+--------------------------+
```

## Author

V. Naga Sai Prahallada Reddy

Aspiring Linux & DevOps Engineer | Docker | Linux | Networking | Cybersecurity
