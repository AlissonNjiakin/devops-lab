# DevOps Lab

A Python/FastAPI application built as a learning project for DevOps fundamentals.

## What This Project Covers

- FastAPI REST API with health and version endpoints
- Automated testing with pytest
- CI pipeline with GitHub Actions (runs on every push and PR)
- Containerization with Docker and docker-compose
- CD pipeline via Coolify (deploys automatically when tests pass)
- PostgreSQL database with automated S3 backups
- CloudWatch monitoring on AWS EC2

## Running Locally

### Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) — install with `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Docker Desktop

### Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/devops-lab.git
cd devops-lab
