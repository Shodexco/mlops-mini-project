#  MLOps Mini Project  
![Build Status](https://github.com/Shodexco/mlops-mini-project/actions/workflows/ci-cd.yml/badge.svg)

A lightweight **MLOps pipeline** that demonstrates how to build, containerize, and deploy a Machine Learning model using **FastAPI** for backend inference and **Streamlit** for frontend visualization — all orchestrated with **Docker** and **GitHub Actions CI/CD**.  

---

##  Project Overview  

This project shows a full end-to-end MLOps workflow including:  
- Model training, saving, and loading  
- REST API for model inference using FastAPI  
- Interactive dashboard using Streamlit  
- Dockerized microservices (API + Dashboard)  
- Continuous Integration/Deployment with GitHub Actions  

---

##  Project Structure  

##  Tech Stack  

| Component       | Technology Used |
|-----------------|-----------------|
| **Backend API** | FastAPI |
| **Frontend** | Streamlit |
| **Modeling** | scikit-learn, pandas, numpy, joblib |
| **Containerization** | Docker & Docker Compose |
| **CI/CD** | GitHub Actions |
| **Language** | Python 3.12 |

---

##  Setup Instructions  

### 1. Clone the Repository
```bash
git clone https://github.com/Shodexco/mlops-mini-project.git
cd mlops-mini-project
2. Create a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate     # On macOS/Linux
venv\Scripts\activate        # On Windows
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Train the Model
bash
Copy code
python src/train.py
This script will generate and save a model file into the /models directory.

 Running the Project Locally
Option 1: Run with Docker Compose
Build and start both FastAPI + Streamlit containers:

bash
Copy code
docker-compose up --build
Then visit:

FastAPI → http://localhost:8000/docs

Streamlit Dashboard → http://localhost:8501

Option 2: Run manually (without Docker)
Run the backend:

bash
Copy code
cd app
uvicorn main:app --reload --host 0.0.0.0 --port 8000
Run the frontend:

bash
Copy code
cd frontend
streamlit run dashboard.py
 Continuous Integration / Deployment
This repo includes a GitHub Actions workflow that:

Triggers on push or pull request to main

Builds both Docker images

Ensures the build passes without errors

Workflow file: .github/workflows/ci-cd.yml

 Dockerfile Summary
Backend: Dockerfile.fa
dockerfile
Copy code
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
Frontend: frontend/Dockerfile.dashboard
dockerfile
Copy code
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir streamlit requests joblib numpy pandas
CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
🧾 License
This project is licensed under the MIT License — see the LICENSE file for details.

 Author
Jonathan Sodeke
Aspiring AI/ML Developer and Scientist
 Email: sodekejonathan@gmail.com
 GitHub: https://github.com/Shodexco

 Future Improvements
Add monitoring and logging via Prometheus/Grafana

Deploy using Kubernetes (GKE / EKS)

Integrate CI/CD with DockerHub or AWS ECR

Include unit and integration tests

 CI/CD Build Status:








