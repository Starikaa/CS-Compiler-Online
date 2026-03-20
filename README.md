# Compiler Online

**Nên tạo dự án cho riêng mình và ghi vào CV nha theo từng bước + mở rộng thêm**

## Mục lục

- [1. CS Compiler](#1--cs-compiler)
- [2. CS Compiler Backend API](#2--cs-compiler-backend-api)
- [3. Docker & CI/CD](#3--docker--cicd)
- [4. Deploy lên Azure](#4--deploy-lên-azure)
- [5. Hiện thực UI](#5--hiện-thực-ui)
- [6. Hiện thực Proxy và Cache dùng nginx](#6--hiện-thực-proxy-và-cache-dùng-nginx)

## 1. 🚀 CS Compiler

Dự án này triển khai một trình biên dịch (compiler) cho **ngôn ngữ CS**, được phát triển dựa trên bài tập lớn trong môn PPL1.

**Compiler sẽ:**
- 📥 Đọc file nguồn .cs
- ⚙️ Biên dịch thành bytecode .class
- ▶️ Chạy chương trình bằng Java Virtual Machine (JVM)

**🧱 Kiến trúc tổng quan**
```
.cs source code
      ↓
  Compiler (Python)
      ↓
 .class (Java bytecode)
      ↓
     JVM (java)
      ↓
   Output
```

**📝 Ví dụ chương trình CS**
```
// ------------ Program --------------
const a = 2;
const b = 3 + a;
print(a + b);
// ------------------------------------
```

**▶️ Cách chạy**
```
➜  compiler# python3 run.py main.cs 
/Backend/compiler/src/runtime
Compile success
➜  compiler# (cd src/runtime && java CS)            
7
```

---

## 2. 🚀 CS Compiler Backend API

**Backend cung cấp API để:**
- Quản lý file source code
- Biên dịch (build) chương trình
- Chạy chương trình
- Chỉnh sửa nội dung file

**📂 API Endpoints**
* `GET /files/` → Lấy danh sách file
* `POST /files/create` → Tạo file mới
* `GET /files/run` → Chạy chương trình
* `GET /files/{filename}` → Đọc file
* `DELETE /files/{filename}` → Xóa file
* `POST /files/edit/{filename}` → Sửa nội dung file
* `POST /files/build/{filename}` → Build (compile) file

![alt text](images/api.png)

Dưới đây là phiên bản README **ngắn gọn, rõ ràng** cho phần Docker + CI/CD:

---

## 3. 🚀 Docker & CI/CD

### 🐳 Docker

**Chạy bằng Docker Compose**

```bash
docker compose up --build test
```

---

### 📦 Dockerfile

* Base image: `python:3.11-slim`
* Cài thêm:

  * `openjdk-21`
  * `build-essential`
* Cài dependencies từ `requirements.txt`
* Run app bằng:

```bash
python run.py
```

---

### 🔄 CI/CD (GitHub Actions)

* Trigger khi push vào branch `main`
* Tự động:

  1. Checkout code
  2. Build Docker
  3. Run test (`pytest`)

```yaml
docker compose build
docker compose run --rm test
```

---

## 4. 🚀 Deploy lên Azure

### 🧾 Bước 1: Đăng ký

Đăng ký tài khoản Azure (có thể dùng mail trường để được free credits)

### 🖥️ Bước 2: Tạo server

- Tạo VM (Ubuntu) https://portal.azure.com/#create/canonical.ubuntu-24_04-lts
- Chọn `Ed25519 SSH Format` và Mở port 80 443 22
![alt text](images/azure.png)
- Tải về SSH key `cs-complier_key.pem` để truy cập
```
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjfAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtz
......................
-----END OPENSSH PRIVATE KEY-----
```

### 🔐 Bước 3: Kết nối server & Cài Docker & chạy project

- Truy cập VN mới tạo lấy ra `Public IP address`
- Dùng lệnh kết nôi `ssh -i <duong_dan_key.pem> <username>@<ip>`
```
➜  Backend git:(main) ✗ ssh -i cs-complier_key.pem azureuser@50.11.17.98
Welcome to Ubuntu 24.04.4 LTS (GNU/Linux 6.14.0-1017-azure x86_64)
azureuser@cs-compiler:~$ 
```
- Cài Docker & chạy project
```sh
sudo apt update
sudo apt install -y docker.io
sudo apt  install docker-compose 
azureuser@cs-compiler:~$ docker --version
Docker version 27.5.1, build 27.5.1-0ubuntu3~24.04.2
```

### 🐳 Bước 4: Clone code & chạy thử

- 🔑 Tạo SSH key trên server

```
ssh-keygen -t rsa -b 4096 -C "votinen10cham@gmail.com"
azureuser@cs-compiler:~$ cat ~/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCOgkJpWEwKlDq/Rjth1dSz8R20cMJN4NHZ2XHXK+9
```
![alt text](images/SHHKEY.png)

- Clone dự án về  
```
azureuser@cs-compiler:~$ git clone git@github.com:PPL-BK/Backend_Complier.git
Cloning into 'Backend_Complier'...
The authenticity of host 'github.com (20.205.243.166)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'github.com' (ED25519) to the list of known hosts.
remote: Enumerating objects: 57, done.
remote: Counting objects: 100% (57/57), done.
remote: Compressing objects: 100% (48/48), done.
remote: Total 57 (delta 1), reused 57 (delta 1), pack-reused 0 (from 0)
Receiving objects: 100% (57/57), 207.89 KiB | 321.00 KiB/s, done.
Resolving deltas: 100% (1/1), done.
azureuser@cs-compiler:~$ ls
Backend_Complier
azureuser@cs-compiler:~$ cd Backend_Complier/
azureuser@cs-compiler:~/Backend_Complier$ ls
Dockerfile  README.md  app  compiler  docker-compose.yml  images  requirements.txt  run.py  tests
```
- Chạy thử

```
azureuser@cs-compiler:~/Backend_Complier$ sudo docker-compose up --build production
Step 8/8 : CMD ["python", "run.py"]
 ---> Running in 1e04b4e36700
 ---> Removed intermediate container 1e04b4e36700
 ---> 1ade8e0b3ee6
Successfully built 1ade8e0b3ee6
Successfully tagged backend_complier_production:latest
Creating cs-api ... done
Attaching to cs-api
cs-api        | INFO:     Will watch for changes in these directories: ['/app']
cs-api        | INFO:     Uvicorn running on http://0.0.0.0:9000 (Press CTRL+C to quit)
cs-api        | INFO:     Started reloader process [1] using StatReload
cs-api        | INFO:     Started server process [8]
cs-api        | INFO:     Waiting for application startup.
cs-api        | INFO:     Application startup complete.
cs-api        | INFO:     1.54.5.34:15710 - "GET /docs HTTP/1.1" 200 OK
cs-api        | INFO:     1.54.5.34:15710 - "GET /openapi.json HTTP/1.1" 200 OK

```

- Truy cập http://50.11.17.98/docs#/


### 🔄 Bước 5: Cấu hình CD với GitHub Actions

- Cấu hình Secrets trên GitHub `Repo → Settings → Secrets → Actions`

| Tên               | Giá trị                |
| ----------------- | ---------------------- |
| `SERVER_IP`       | IP Azure VM            |
| `SERVER_USER`     | `azureuser`            |
| `SSH_PRIVATE_KEY` | nội dung file `id_rsa` |


## 5. 🚀 Hiện thực UI

---

## 6. 🚀 Hiện thực Proxy và Cache dùng nginx

--- 

<p align="center">
  <a href="https://www.facebook.com/Shiba.Vo.Tien">
    <img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white" alt="Facebook"/>
  </a>
  <a href="https://www.tiktok.com/@votien_shiba">
    <img src="https://img.shields.io/badge/TikTok-000000?style=for-the-badge&logo=tiktok&logoColor=white" alt="TikTok"/>
  </a>
  <a href="https://www.facebook.com/groups/khmt.ktmt.cse.bku?locale=vi_VN">
    <img src="https://img.shields.io/badge/Facebook%20Group-4267B2?style=for-the-badge&logo=facebook&logoColor=white" alt="Facebook Group"/>
  </a>
  <a href="https://www.facebook.com/CODE.MT.BK">
    <img src="https://img.shields.io/badge/Page%20CODE.MT.BK-0057FF?style=for-the-badge&logo=facebook&logoColor=white" alt="Facebook Page"/>
  </a>
  <a href="https://github.com/VoTienBKU">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>
</p>
