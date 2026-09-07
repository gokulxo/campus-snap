# CampusSnap 🎓📸

A dynamic Flask web application for college students to share photo posts filtered by department, deployed on AWS EC2 with production-grade DevOps practices.

## Live Demo
http://campussnap.duckdns.org

## Tech Stack
- **Backend:** Flask, SQLAlchemy, SQLite
- **Web Server:** Nginx (reverse proxy)
- **App Server:** Gunicorn (WSGI)
- **Cloud:** AWS EC2 (Amazon Linux)
- **CI/CD:** GitHub Actions
- **Domain:** DuckDNS

## Architecture
User → Nginx (port 80) → Gunicorn (socket) → Flask App → SQLite DB
GitHub push → GitHub Actions → SSH to EC2 → Auto-deploy

## Features
- Department-wise photo filter
- Like system
- Dynamic post feed from database

## Screenshots
(idhula unga screenshots insert பண்ணலாம்)

## Deployment Steps
1. EC2 instance setup (Amazon Linux)
2. Gunicorn systemd service configuration
3. Nginx reverse proxy setup
4. CI/CD pipeline with GitHub Actions
5. Custom domain via DuckDNSs

