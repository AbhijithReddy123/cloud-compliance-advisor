# ☁️ Cloud Compliance Advisor

A FastAPI-powered app that checks AWS EC2 instance compliance for security and regional policies. Designed to help cloud engineers validate infrastructure settings in real-time.

---

## 🔍 Project Purpose

This tool audits EC2 instances across two key compliance dimensions:
- **Encryption validation** of attached EBS volumes
- **Region enforcement** based on user-defined allowed regions

It supports YAML-based rule configuration and uses boto3 to fetch live AWS metadata.

---

## ⚙️ Features & Tech Stack

**Features:**
- ✅ Scans EC2 instances from live AWS environment
- 🔒 Verifies EBS volume encryption
- 📍 Checks instance regions against YAML-defined rules
- 🧾 Returns structured JSON showing compliance results

**Tech Stack:**
- Python
- FastAPI
- boto3
- YAML config (`config.yaml` rules)
- Swagger UI via `/docs` endpoint

---

## 💡 Setup Instructions

### Prerequisites
- Python 3.10+
- AWS credentials configured locally (`~/.aws/credentials`)
- Required packages:
  ```bash
  pip install fastapi uvicorn boto3 pyyaml
