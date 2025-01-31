# 📅 Assignment Assistant  

## Overview  

**Assignment Assistant** is an automated daily reminder system that fetches assignments from **Notion** and sends a message about upcoming deadlines. It runs every day at **9 AM**, ensuring that you stay on top of your coursework without manually checking your Notion database.  

The system:  
- Retrieves **assignments and due dates** from Notion.  
- **Formats** the data into an easy-to-read message.  
- **Sends notifications** about assignments due today and the rest of the week.  

## Key Features  

✅ **Automated Daily Run** – Executes every morning at **9 AM** to send reminders.  
✅ **Notion Integration** – Pulls assignments from your **Notion database**.  
✅ **Custom Message Formatting** – Organizes tasks into a structured report.  
✅ **Status Tracking** – Ignores completed assignments based on **Notion checkbox**.  
✅ **Multi-Database Support** – Handles multiple Notion databases for different users.  

## Technologies Used  

- **Notion API** – Fetches assignment details  
- **Python** – Core scripting language  
- **JSON** – Data storage and processing  
- **Messaging API** – Sends reminders  

## Installation  

### Clone the Repository  

```bash
git clone https://github.com/Th1sJustIn/Assignment-Assistant.git
cd Assignment-Assistant
