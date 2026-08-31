import sqlite3
import os
from datetime import datetime
import uuid

DB_FILE = "service_desk.db"

def get_connection():
    """Get a database connection."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    """Initialize the database with the tickets table."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            ticket_id TEXT PRIMARY KEY,
            employee_name TEXT NOT NULL,
            employee_email TEXT NOT NULL,
            department TEXT NOT NULL,
            device_type TEXT NOT NULL,
            category TEXT NOT NULL,
            issue_title TEXT NOT NULL,
            description TEXT NOT NULL,
            priority TEXT NOT NULL,
            status TEXT NOT NULL,
            assigned_technician TEXT,
            contact_method TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            resolution_notes TEXT
        )
    """)
    
    conn.commit()
    
    # Check if sample data already exists
    cursor.execute("SELECT COUNT(*) as count FROM tickets")
    count = cursor.fetchone()['count']
    
    if count == 0:
        insert_sample_data(conn)
    
    conn.close()

def insert_sample_data(conn):
    """Insert sample tickets into the database."""
    sample_tickets = [
        {
            "employee_name": "John Smith",
            "employee_email": "john.smith@company.com",
            "department": "Finance",
            "device_type": "Laptop",
            "category": "Network",
            "issue_title": "Cannot connect to Wi-Fi",
            "description": "Employee reports that their laptop cannot connect to the office Wi-Fi network. They can see the network but connection fails.",
            "priority": "High",
            "status": "Open",
            "assigned_technician": None,
            "contact_method": "Email"
        },
        {
            "employee_name": "Sarah Johnson",
            "employee_email": "sarah.johnson@company.com",
            "department": "Marketing",
            "device_type": "Desktop",
            "category": "Microsoft 365",
            "issue_title": "Outlook not opening",
            "description": "Outlook application crashes immediately upon opening on Windows desktop. No error message is displayed.",
            "priority": "High",
            "status": "In Progress",
            "assigned_technician": "Tom Wilson",
            "contact_method": "Walk-in"
        },
        {
            "employee_name": "Mike Chen",
            "employee_email": "mike.chen@company.com",
            "department": "IT",
            "device_type": "Laptop",
            "category": "Account & Access",
            "issue_title": "Account locked after password attempt",
            "description": "Employee is locked out of their account after multiple failed login attempts. They cannot access any company resources.",
            "priority": "High",
            "status": "In Progress",
            "assigned_technician": "Lisa Garcia",
            "contact_method": "Phone"
        },
        {
            "employee_name": "Emma Davis",
            "employee_email": "emma.davis@company.com",
            "department": "HR",
            "device_type": "Printer",
            "category": "Hardware",
            "issue_title": "Printer not responding",
            "description": "The office printer on the 3rd floor is not responding to print jobs. Print queue is backed up.",
            "priority": "Medium",
            "status": "Open",
            "assigned_technician": None,
            "contact_method": "Email"
        },
        {
            "employee_name": "Robert Martinez",
            "employee_email": "robert.martinez@company.com",
            "department": "Sales",
            "device_type": "Laptop",
            "category": "Software",
            "issue_title": "Microsoft Teams audio issues",
            "description": "During Teams meetings, audio is cutting out frequently. Video works fine but audio is choppy.",
            "priority": "Medium",
            "status": "Open",
            "assigned_technician": None,
            "contact_method": "Email"
        },
        {
            "employee_name": "Jessica Lee",
            "employee_email": "jessica.lee@company.com",
            "department": "Operations",
            "device_type": "Laptop",
            "category": "Software",
            "issue_title": "Laptop running very slowly",
            "description": "Employee reports that their laptop is extremely slow when opening applications. System is freezing occasionally.",
            "priority": "Medium",
            "status": "Resolved",
            "assigned_technician": "Tom Wilson",
            "contact_method": "Walk-in",
            "resolution_notes": "Removed unnecessary startup programs and cleared cache. Laptop performance improved significantly."
        },
        {
            "employee_name": "David Wilson",
            "employee_email": "david.wilson@company.com",
            "department": "Engineering",
            "device_type": "Laptop",
            "category": "Network",
            "issue_title": "VPN connection fails",
            "description": "Employee cannot establish VPN connection when working from home. Error message indicates authentication failure.",
            "priority": "High",
            "status": "Open",
            "assigned_technician": None,
            "contact_method": "Email"
        },
        {
            "employee_name": "Amanda Brown",
            "employee_email": "amanda.brown@company.com",
            "department": "Finance",
            "device_type": "Desktop",
            "category": "Software",
            "issue_title": "Software installation request",
            "description": "Employee requests installation of statistical analysis software for data processing tasks.",
            "priority": "Low",
            "status": "Open",
            "assigned_technician": None,
            "contact_method": "Email"
        },
        {
            "employee_name": "Christopher Taylor",
            "employee_email": "christopher.taylor@company.com",
            "department": "Marketing",
            "device_type": "Smartphone",
            "category": "Account & Access",
            "issue_title": "Mobile device not syncing email",
            "description": "Company mobile device is not syncing emails. Last sync was 2 days ago.",
            "priority": "Low",
            "status": "Open",
            "assigned_technician": None,
            "contact_method": "Email"
        },
        {
            "employee_name": "Patricia Anderson",
            "employee_email": "patricia.anderson@company.com",
            "department": "Legal",
            "device_type": "Laptop",
            "category": "Hardware",
            "issue_title": "Monitor not displaying correctly",
            "description": "External monitor is showing distorted colors and flickering. Graphics may be failing.",
            "priority": "Medium",
            "status": "Resolved",
            "assigned_technician": "Lisa Garcia",
            "contact_method": "Walk-in",
            "resolution_notes": "Replaced faulty monitor with spare. Employee's setup working correctly now."
        },
    ]
    
    cursor = conn.cursor()
    now = datetime.now().isoformat()
    
    for ticket in sample_tickets:
        ticket_id = f"TK-{uuid.uuid4().hex[:8].upper()}"
        cursor.execute("""
            INSERT INTO tickets (
                ticket_id, employee_name, employee_email, department,
                device_type, category, issue_title, description, priority,
                status, assigned_technician, contact_method, created_at,
                updated_at, resolution_notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            ticket_id,
            ticket["employee_name"],
            ticket["employee_email"],
            ticket["department"],
            ticket["device_type"],
            ticket["category"],
            ticket["issue_title"],
            ticket["description"],
            ticket["priority"],
            ticket["status"],
            ticket["assigned_technician"],
            ticket["contact_method"],
            now,
            now,
            ticket.get("resolution_notes")
        ))
    
    conn.commit()

def create_ticket(employee_name, employee_email, department, device_type, category,
                  issue_title, description, priority, contact_method):
    """Create a new ticket."""
    conn = get_connection()
    cursor = conn.cursor()
    
    ticket_id = f"TK-{uuid.uuid4().hex[:8].upper()}"
    now = datetime.now().isoformat()
    
    cursor.execute("""
        INSERT INTO tickets (
            ticket_id, employee_name, employee_email, department,
            device_type, category, issue_title, description, priority,
            status, assigned_technician, contact_method, created_at,
            updated_at, resolution_notes
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        ticket_id, employee_name, employee_email, department,
        device_type, category, issue_title, description, priority,
        "Open", None, contact_method, now, now, None
    ))
    
    conn.commit()
    conn.close()
    
    return ticket_id

def get_all_tickets():
    """Get all tickets."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM tickets ORDER BY created_at DESC")
    tickets = cursor.fetchall()
    
    conn.close()
    
    return [dict(ticket) for ticket in tickets]

def get_ticket(ticket_id):
    """Get a specific ticket by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM tickets WHERE ticket_id = ?", (ticket_id,))
    ticket = cursor.fetchone()
    
    conn.close()
    
    return dict(ticket) if ticket else None

def update_ticket(ticket_id, status=None, priority=None, assigned_technician=None, 
                  resolution_notes=None):
    """Update ticket information."""
    conn = get_connection()
    cursor = conn.cursor()
    
    now = datetime.now().isoformat()
    updates = []
    params = []
    
    if status is not None:
        updates.append("status = ?")
        params.append(status)
    
    if priority is not None:
        updates.append("priority = ?")
        params.append(priority)
    
    if assigned_technician is not None:
        updates.append("assigned_technician = ?")
        params.append(assigned_technician)
    
    if resolution_notes is not None:
        updates.append("resolution_notes = ?")
        params.append(resolution_notes)
    
    if updates:
        updates.append("updated_at = ?")
        params.append(now)
        params.append(ticket_id)
        
        query = f"UPDATE tickets SET {', '.join(updates)} WHERE ticket_id = ?"
        cursor.execute(query, params)
        conn.commit()
    
    conn.close()

def search_tickets(keyword=None, category=None, priority=None, status=None):
    """Search and filter tickets."""
    conn = get_connection()
    cursor = conn.cursor()
    
    query = "SELECT * FROM tickets WHERE 1=1"
    params = []
    
    if keyword:
        query += " AND (ticket_id LIKE ? OR employee_name LIKE ? OR employee_email LIKE ? OR issue_title LIKE ? OR description LIKE ?)"
        search_term = f"%{keyword}%"
        params.extend([search_term] * 5)
    
    if category:
        query += " AND category = ?"
        params.append(category)
    
    if priority:
        query += " AND priority = ?"
        params.append(priority)
    
    if status:
        query += " AND status = ?"
        params.append(status)
    
    query += " ORDER BY created_at DESC"
    
    cursor.execute(query, params)
    tickets = cursor.fetchall()
    
    conn.close()
    
    return [dict(ticket) for ticket in tickets]

def get_dashboard_stats():
    """Get dashboard statistics."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Total tickets
    cursor.execute("SELECT COUNT(*) as count FROM tickets")
    total = cursor.fetchone()['count']
    
    # Open tickets
    cursor.execute("SELECT COUNT(*) as count FROM tickets WHERE status = 'Open'")
    open_count = cursor.fetchone()['count']
    
    # In Progress tickets
    cursor.execute("SELECT COUNT(*) as count FROM tickets WHERE status = 'In Progress'")
    in_progress = cursor.fetchone()['count']
    
    # Resolved tickets
    cursor.execute("SELECT COUNT(*) as count FROM tickets WHERE status = 'Resolved'")
    resolved = cursor.fetchone()['count']
    
    # High priority tickets
    cursor.execute("SELECT COUNT(*) as count FROM tickets WHERE priority = 'High'")
    high_priority = cursor.fetchone()['count']
    
    # Tickets by category
    cursor.execute("SELECT category, COUNT(*) as count FROM tickets GROUP BY category")
    by_category = {row['category']: row['count'] for row in cursor.fetchall()}
    
    # Tickets by priority
    cursor.execute("SELECT priority, COUNT(*) as count FROM tickets GROUP BY priority")
    by_priority = {row['priority']: row['count'] for row in cursor.fetchall()}
    
    # Tickets by status
    cursor.execute("SELECT status, COUNT(*) as count FROM tickets GROUP BY status")
    by_status = {row['status']: row['count'] for row in cursor.fetchall()}
    
    conn.close()
    
    return {
        "total": total,
        "open": open_count,
        "in_progress": in_progress,
        "resolved": resolved,
        "high_priority": high_priority,
        "by_category": by_category,
        "by_priority": by_priority,
        "by_status": by_status
    }

def get_recent_tickets(limit=10):
    """Get recent tickets."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM tickets ORDER BY created_at DESC LIMIT ?", (limit,))
    tickets = cursor.fetchall()
    
    conn.close()
    
    return [dict(ticket) for ticket in tickets]
