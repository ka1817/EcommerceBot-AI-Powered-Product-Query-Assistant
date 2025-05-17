# 🏍️ 🛍️ Ecommerce AI Product Insight Assistant

> 🤖 Empowering smarter shopping experiences through AI-driven insights.

🔍 Introduction

Ecommerce AI Product Insight Assistant is an intelligent chatbot that helps users make smarter shopping choices by extracting insights from customer feedback. It processes Flipkart product data and uses advanced AI technologies like LangChain, Groq's LLaMA model, and FAISS vector search to answer user queries in a helpful, context-aware way.
The system combines a clean frontend with a powerful FastAPI backend, CI/CD automation via GitHub Actions, and Dockerized deployment — making it easy to scale, maintain, and deploy on platforms like AWS EC2.

---

## 🔧 Features

* ✨ Analyze Flipkart product reviews using LLMs
* 🌎 FastAPI backend for real-time queries
* 🚀 Dockerized for seamless deployment
* ⚙️ CI/CD pipeline with GitHub Actions
* 🌐 Frontend with HTML/CSS (Jinja2 templates)
* 🤝 Simple question submission and response display

---

## 📁 Project Structure

```bash
EcommerceBot-AI-Powered-Product-Query-Assistant/
├── .github/workflows/ci-cd.yml       # GitHub Actions CI/CD pipeline
├── data/
│   └── flipkart_product_review.csv  # Product review data
├── src/
│   ├── __pycache__/
│   ├── data_converter.py            # Converts CSV into LangChain docs
│   ├── ingest.py                    # Embeds data into FAISS vector store
│   └── retrival_genaration.py      # QA chain with LLM and retriever
├── static/
│   └── style.css                    # Frontend styling
├── templates/
│   └── index.html                  # Frontend form template
├── venv/                            # Virtual environment (excluded in Docker)
├── .dockerignore
├── .env                             # Environment variables (GROQ_API_KEY)
├── .gitignore
├── Dockerfile                       # Build and run container
├── main.py                          # FastAPI application
├── requirements.txt                # Project dependencies
```

---

## 🎓 Technologies Used

* **Python 3.10**
* **FastAPI**
* **LangChain** + **FAISS** + **HuggingFaceEmbeddings**
* **ChatGroq (LLM)**
* **Pandas**, **dotenv**
* **Docker** + **Docker Hub**
* **GitHub Actions** (CI/CD)

---

## 🚀 Setup & Usage

### ⚖️ Prerequisites

* Docker installed
* GROQ API Key ([get one](https://console.groq.com))
* EC2 instance (optional for deployment)

### 🔀 Clone & Setup

```bash
git clone https://github.com/ka1817/EcommerceBot-AI-Powered-Product-Query-Assistant.git
cd EcommerceBot-AI-Powered-Product-Query-Assistant
```

### 🗖️ Create `.env` file

```env
GROQ_API_KEY=your_groq_api_key_here
# Create your API key at: https://console.groq.com
```

### 🪖 Build and Run with Docker

```bash
docker build -t pranavreddy123/ecommercebot .
docker run -d -p 8000:8000 --env-file .env pranavreddy123/ecommercebot
```

### 💻 Local Development (Optional)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

### 🌐 Access Web App

Open in browser:

```
http://localhost:8000
```

---

## 🗕️ CI/CD with GitHub Actions

GitHub Actions workflow at `.github/workflows/ci-cd.yml`:

* Validates syntax
* Runs tests
* Builds Docker image
* Pushes image to Docker Hub

**Docker Hub Repo**:

```
docker pull pranavreddy123/ecommercebot
```

---

## 🤖 How it Works

1. `data_converter.py`: Loads and processes product reviews.
2. `ingest.py`: Embeds the processed data using HuggingFace embeddings into a FAISS vector store.
3. `retrival_genaration.py`: Sets up a RetrievalQA chain with Groq LLM.
4. `main.py`: FastAPI web app for frontend interaction.

---

## 📄 Example Query

> **Q:** "Which product has the highest rating?"
>
> **A:** AI-generated response based on semantic search of reviews.

---

## ✨ Future Improvements

* Add authentication for secured access
* Integrate real-time Flipkart scraping or API
* Use a database for persistent vector store
* Expand frontend to show product cards with reviews

---

## 🌟 Contributors

* [@ka1817](https://github.com/ka1817) — Developer

---

## 📦 Deployment on AWS EC2

1. SSH into your EC2 instance:

   ```bash
   ssh -i your-key.pem ec2-user@<your-ec2-public-ip>
   ```

2. Install Docker:

   ```bash
   sudo yum update -y
   sudo yum install docker -y
   sudo service docker start
   sudo usermod -a -G docker ec2-user
   ```

   Log out and log back in to apply Docker permissions.

3. Pull and run Docker image:

   ```bash
   docker pull pranavreddy123/ecommercebot
   echo "GROQ_API_KEY=your_groq_api_key" > .env
   docker run -d -p 8000:8000 --env-file .env pranavreddy123/ecommercebot
   ```

4. Access the app:

   ```
   http://<your-ec2-public-ip>:8000/
   ```

---

## 🛆 License

This project is open source under the [MIT License](LICENSE).

---

Developed By Pranav Reddy

