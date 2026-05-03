Assessment Failure Recovery System
Overview

This project implements an Assessment Failure Recovery System designed to prevent data loss during online assessments. It uses a checkpoint-based mechanism to continuously save user progress and restore it in case of system or API failures. The system ensures that users can resume their assessment from the last saved state without losing previously entered data.

Features
Partial data recovery using checkpoints
Persistence of user progress in database
Recovery of last saved state after failure
RESTful API implementation using FastAPI
PostgreSQL integration for reliable storage
Health check endpoint for system monitoring
Technology Stack
Backend: FastAPI (Python)
Database: PostgreSQL
ORM: SQLAlchemy
Server: Uvicorn
Configuration: Python-dotenv
System Workflow
User submits answers during an assessment
System stores responses as checkpoints in the database
In case of failure, data remains محفوظ (safe)
Recovery API retrieves the latest checkpoint
User resumes from the last saved question
Project Setup
Clone the Repository
git clone https://github.com/pranjalik2004/assessment-recovery-system.git
cd assessment-recovery-system

Create Virtual Environment
python -m venv venv
venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt

Configure Environment Variables

Create a .env file in the root directory:

DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/recovery_db

Run the Application
python -m uvicorn app.main:app --reload

API Documentation

Once the server is running, access the API documentation at:

http://127.0.0.1:8000/docs

Key Endpoints
Save Checkpoint

POST /assessment/checkpoint
Stores user progress in the database.

Recover Assessment Data

GET /assessment/recover/{user_id}
Retrieves the last saved checkpoint for a user.

Health Check

GET /assessment/health
Verifies that the system is running.

Use Case

This system is suitable for platforms where maintaining user progress is critical, such as:

Online examinations
Coding assessments
Interview evaluation systems
Future Enhancements
Automated retry mechanisms for failed operations
Distributed fault tolerance using container orchestration
Integration with cloud-based storage and monitoring tools
Conclusion

This project demonstrates the implementation of a reliable backend system that ensures data persistence and recovery during failures. It highlights the importance of checkpoint-based mechanisms in maintaining system reliability and enhancing user experience.
