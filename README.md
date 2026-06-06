# docker-two-tier-application
Built a two-tier application using Docker, Flask, and MySQL. Created Docker images and containers, configured a custom bridge network for communication between application and database containers, and implemented message storage and retrieval using MySQL. Gained hands-on experience with Docker networking and multi-container deployments.

# Step 1: Create Project Structure

```bash
mkdir two-tier-app
cd two-tier-app

mkdir templates

touch app.py
touch requirements.txt
touch Dockerfile

touch templates/index.html
```

---

# Step 2: Flask Application (app.py)
----> You can get the code from repository.

# Step 3: HTML Page
-----> You can get it from templates folder.

# Step 5: Dockerfile
------>----> You can get the code from repository.

# Step 6: Create Custom Bridge Network

```bash
docker network create my-network
```

Verify:

```bash
docker network ls
```

---

# Step 7: Run MySQL Container

```bash
docker run -d \
--name mysql-db \
--network my-network \
-e MYSQL_ROOT_PASSWORD=root123 \
-e MYSQL_DATABASE=messagesdb \
mysql:8.0
```

Check:

```bash
docker ps
```

---

# Step 8: Create Table

Enter MySQL container:

```bash
docker exec -it mysql-db bash
```

Login:

```bash
mysql -u root -p
```

Password:

```text
root123
```

Select database:

```sql
USE messagesdb;
```

Create table:

```sql
CREATE TABLE messages(
id INT AUTO_INCREMENT PRIMARY KEY,
message VARCHAR(255)
);
```

Verify:

```sql
SHOW TABLES;
```

Exit:

```sql
exit
```

---

# Step 9: Build Flask Image

Inside project directory:

```bash
docker build -t flask-mysql-app .
```

---

# Step 10: Run Flask Container

```bash
docker run -d \
--name flask-app \
--network my-network \
-p 5000:5000 \
flask-mysql-app
```

---

# Step 11: Verify Networking

Inspect network:

```bash
docker network inspect my-network
```

You should see:

```text
mysql-db
flask-app
```

attached to the same bridge network.

---

# Step 12: Test Connectivity

From Flask container:

```bash
docker exec -it flask-app sh
```

Install ping:

```bash
apt update
apt install iputils-ping -y
```

Ping MySQL container:

```bash
ping mysql-db
```

You should get replies.

This proves Docker DNS resolution is working through the custom bridge network.

---

# Step 13: Access Application

Open:

```text
http://localhost:5000
```

Enter:

```text
Hello Docker Networking
```

Click Submit.

The message will be stored in MySQL and displayed on the page.

# Step 14: To Check if the messages are stored in sql-db

Enter the container:

docker exec -it mysql-db bash

Login to MySQL:

mysql -u root -p

Enter password:

root123

Select the database:

USE messagesdb;

View all records:

SELECT * FROM messages;

Example output:

+----+--------------------------+
| id | message                  |
+----+--------------------------+
|  1 | Hello Docker             |
|  2 | Docker Networking Test   |
|  3 | Flask MySQL Connection   |
+----+--------------------------+

