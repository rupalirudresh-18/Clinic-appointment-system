# 🏥 Smart Clinic Queue & Appointment System

A full-stack **Django-based web application** designed to streamline clinic operations by managing appointments, doctor schedules, and real-time patient queue flow efficiently.

---

## 🚀 Live Demo

🔗 https://clinic-appointment-system-2-hjou.onrender.com
---

## ✨ Overview

This system provides a smooth workflow for **patients, doctors, and admins** to interact within a clinic environment.

From booking appointments to managing queues and recording visit notes — everything is handled in one place.

---

## 🌟 Key Features

- 👤 **Patient Authentication**
  - Secure registration & login
  - Book and cancel appointments
  - View real-time queue status

- 🩺 **Doctor Dashboard**
  - Manage available time slots
  - Track patient queue
  - Update visit status
  - Add notes / prescriptions

- 🛠 **Admin Control Panel**
  - Manage users & doctors
  - Monitor appointments
  - Track daily clinic activity

- 🔄 **Queue Management System**
  - Organized patient flow
  - Status updates (Waiting / In Progress / Completed)

---

---

## 🛠 Tech Stack

| Technology | Usage |
|----------|------|
| Python | Backend logic |
| Django | Web framework |
| SQLite  | Database |
| HTML, CSS, Bootstrap | Frontend |
| Render | Deployment |

---

## 👥 User Roles

### 👤 Patient
- Register & login  
- Book appointments  
- Cancel bookings  
- View queue status  

### 🩺 Doctor
- Manage time slots  
- View patient queue  
- Update appointment status  
- Add prescriptions / notes  

### 🛠 Admin
- Manage users & doctors  
- Monitor appointments  
- Track clinic workflow  

---

## 📁 Project Structure (Simplified)

```
smart-clinic/
│── appointments/
|── accounts/
│── dashboard/
|── doctors/
│── templates/
│── static/
│── db.sqlite3
│── manage.py
```

---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/rupalirudresh-18/Clinic-appointment-system.git
# Navigate into project
cd Clinic-appointment-system

# Create virtual environment
python -m venv venv

# Activate environment
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

---

## 🔮 Future Enhancements

- 📱 Mobile responsiveness improvements  
- 🔔 Notification system (SMS/Email)  
- 📊 Analytics dashboard  
- 🤖 AI-based appointment prioritization  

---

