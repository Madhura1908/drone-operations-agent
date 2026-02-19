---

# 🚁 Skylark Drone Services – AI Operations Coordinator

An AI-powered Drone Operations Coordinator built using **Streamlit + Google Sheets + Python**, designed to automate pilot assignments, drone inventory management, and mission coordination through a conversational interface.

This project demonstrates how an AI agent can replace manual coordination by intelligently managing resources across multiple drone missions.

---

## ✨ Features

### 🧠 Conversational AI Agent

Interact with the system using natural commands such as:

* `hi`
* `show pilots`
* `show drones`
* `show missions`
* `available pilots`
* `available drones`
* `assign mission PRJ001`
* `complete mission PRJ001`
* `add pilot P005 Rahul Mapping DGCA Pune Available 3000`
* `remove pilot P005`
* `add drone D010 DJI RGB Mumbai Available 2026-04-01`
* `remove drone D010`

---

### 👨‍✈ Pilot Management

* View all pilots
* Check availability
* Add / remove pilots
* Assign pilots to missions
* Automatically release pilots after mission completion

---

### 🚁 Drone Fleet Management

* View all drones
* Track deployment status
* Add / remove drones
* Automatically assign drones based on pilot location
* Release drones after mission completion

---

### 📍 Mission Coordination

* View active missions
* Assign pilots + drones to missions
* Complete missions and free resources
* Conflict-aware assignment logic

---

### 📊 Real-Time Dashboard

* KPI cards (Pilots, Available Pilots, Available Drones, Missions)
* Live cards for Pilots, Drones, and Missions
* Auto-refresh after every chatbot interaction

---

### ☁️ Google Sheets Integration (2-Way Sync)

The system uses Google Sheets as the live database:

* PilotRoster
* DroneFleet
* Missions

All updates made through the AI agent are synced back to Google Sheets instantly.

---

## 🛠 Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **Database:** Google Sheets (via gspread)
* **Authentication:** Google Service Account
* **Deployment:** HuggingFace Spaces
* **Data Handling:** Pandas

---

## 🏗 Architecture Overview

```
User (Chat Interface)
        ↓
Streamlit UI
        ↓
AI Agent Logic
        ↓
Assignment / Validation Engine
        ↓
Google Sheets (Live Database)
```

---

## 🚀 How It Works

1. User enters a command in the chat.
2. AI Agent interprets intent.
3. Backend validates pilots, drones, and missions.
4. Assignments or updates are executed.
5. Google Sheets are updated.
6. Dashboard refreshes automatically.

---

## 🔐 Environment Setup

Create a Google Service Account and store credentials as:

```
GOOGLE_CREDENTIALS
```

inside HuggingFace Secrets.

---

## 🧪 Sample Commands

```
show pilots
available drones
assign mission PRJ001
complete mission PRJ001
add pilot P007 Aman Mapping DGCA Delhi Available 2500
remove drone D010
```

---

## 🌟 Key Highlights

* Fully conversational operations agent
* Real-time resource coordination
* Automatic conflict handling
* Cloud deployed
* No local setup required
* Production-style dashboard

---

## 📌 Future Improvements

* Budget-based pilot selection
* Weather-aware drone assignment
* Location mismatch alerts
* Role-based access
* Analytics dashboard

---

## 👩‍💻 Author

**Madhura Bedekar**
B.Tech AIML – Ramaiah University of Applied Sciences
Drone + AI Enthusiast

---


Just tell me 💙
