from mcp.server.fastmcp import FastMCP
from datetime import datetime

import os
import base64
from email.message import EmailMessage

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


mcp = FastMCP("Genese Business Assistant")


leads = {
    "ABC Technologies": {
        "company": "ABC Technologies",
        "contact": "John Sharma",
        "email": "john@abc.example",
        "industry": "Software",
        "interest": "Cloud migration"
    },
    "Himalayan Solutions": {
        "company": "Himalayan Solutions",
        "contact": "Aarav Thapa",
        "email": "aarav@himalayan.example",
        "industry": "Fintech",
        "interest": "AI automation"
    },
    "Everest Retail": {
        "company": "Everest Retail",
        "contact": "Priya Karki",
        "email": "priya@everestretail.example",
        "industry": "Retail",
        "interest": "E-commerce platform"
    },
    "Mountain Logistics": {
        "company": "Mountain Logistics",
        "contact": "Suman Rai",
        "email": "suman@mountainlogistics.example",
        "industry": "Logistics",
        "interest": "Fleet management software"
    },
    "Nepal Data Systems": {
        "company": "Nepal Data Systems",
        "contact": "Anisha Gurung",
        "email": "anisha@nepaldatasystems.example",
        "industry": "Data Analytics",
        "interest": "Business intelligence"
    }
}


@mcp.tool()
def get_lead_details(lead_name: str) -> dict:
    """Retrieve company and contact information for a lead."""

    lead = leads.get(lead_name)

    if not lead:
        return {
            "found": False,
            "message": f"No lead found for {lead_name}."
        }

    return {
        "found": True,
        **lead
    }


# ============================================================
# EVENTS
# ============================================================

events = {
    "ABC Technologies": {
        "event_id": "EVT-001",
        "title": "Cloud Migration Follow-up",
        "date": "2026-10-15",
        "time": "11:00"
    },
    "Himalayan Solutions": {
        "event_id": "EVT-002",
        "title": "AI Automation Discussion",
        "date": "2026-10-17",
        "time": "14:00"
    },
    "Everest Retail": {
        "event_id": "EVT-003",
        "title": "E-commerce Platform Demo",
        "date": "2026-10-20",
        "time": "10:30"
    },
    "Mountain Logistics": {
        "event_id": "EVT-004",
        "title": "Fleet Management Proposal",
        "date": "2026-10-22",
        "time": "15:00"
    },
    "Nepal Data Systems": {
        "event_id": "EVT-005",
        "title": "Business Intelligence Consultation",
        "date": "2026-10-25",
        "time": "11:30"
    }
}


@mcp.tool()
def get_upcoming_event(lead_name: str) -> dict:
    """Retrieve the upcoming event for a business lead."""

    event = events.get(lead_name)

    if not event:
        return {
            "found": False,
            "message": f"No upcoming event for {lead_name}."
        }

    return {
        "found": True,
        **event
    }


# ============================================================
# FOLLOW-UP TASKS
# ============================================================

tasks = []


@mcp.tool()
def create_followup_task(
    company: str,
    task: str,
    due_date: str
) -> dict:
    """Create a follow-up task for a business lead."""

    task_id = f"TASK-{len(tasks) + 1:03d}"

    item = {
        "task_id": task_id,
        "company": company,
        "task": task,
        "due_date": due_date,
        "status": "open"
    }

    tasks.append(item)

    return item


# ============================================================
# START MCP SERVER
# ============================================================

if __name__ == "__main__":
    mcp.run()
