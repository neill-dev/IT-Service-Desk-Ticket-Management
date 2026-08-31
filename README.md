# IT Service Desk Ticket Management System

## Project Overview

This is a **professional Service Desk management application** built with Python and Streamlit. It demonstrates core IT support concepts including ticket creation, prioritization, assignment, status tracking, and AI-assisted support workflows.

**Important Disclaimer:** This is an educational portfolio project designed for interview demonstration. It is **NOT** an official OpenText system or product. It simulates typical service desk workflows to demonstrate practical problem-solving and technical support skills.

## Problem Statement

Modern organizations require a structured approach to manage employee technical support requests. Without proper ticketing systems, issues become:

- **Disorganized** (no single tracking mechanism)
- **Inconsistent** (no prioritization or assignment)
- **Inefficient** (no historical record or SLA tracking)
- **Difficult to escalate** (no clear escalation path)

## Solution

This Service Desk application provides:

- **Centralized ticket management** (single source of truth)
- **Automatic categorization and prioritization** (using rule-based logic)
- **Assignment and status tracking** (from creation to resolution)
- **Troubleshooting assistance** (built-in knowledge base)
- **AI-assisted support demo** (local rule-based, educational)

## Core Features

### 1. Dashboard

- **Key Metrics:** Total tickets, Open, In Progress, Resolved, High Priority counts
- **Visual Charts:** Tickets by category, priority, and status
- **Recent Activity:** Latest tickets for quick overview

### 2. Create Ticket

- **Employee-facing form** with mandatory fields:
  - Name, Email, Department, Device Type
  - Issue Category, Title, Description
  - Priority, Contact Method
- **Automatic Ticket ID generation** (unique identifier)
- **AI Priority Suggestion** (optional, user can override)
- **Form validation** (error messages for incomplete fields)

### 3. Automatic Priority Suggestion

- **Rule-based system** (NOT machine learning)
- **High Priority keywords:** "cannot login", "account locked", "VPN down", "system down"
- **Medium Priority keywords:** "Outlook", "Teams", "software", "printer", "slow"
- **Low Priority:** Everything else
- **User override:** Support staff can change suggested priority

### 4. Ticket Management

- **Search functionality:** By Ticket ID or Employee name
- **Advanced filtering:** By Category, Priority, Status
- **Ticket view:** Expandable details for each ticket
- **In-place updates:**
  - Status (Open → In Progress → Resolved → Closed)
  - Priority reassignment
  - Technician assignment
  - Resolution notes

### 5. Ticket Details Page

Each ticket displays:

- Ticket ID, Employee info (name, email, department)
- Device type and issue category
- Issue title and description
- Current priority and status
- Assigned technician
- Creation and update timestamps
- Resolution notes (if applicable)

### 6. Troubleshooting Guide

Educational reference for common issues:

- **Wi-Fi Not Working** (8 steps)
- **Outlook Not Opening** (5 steps)
- **Password/Account Issues** (6 steps)
- **Printer Not Working** (6 steps)
- **Laptop Running Slowly** (7 steps)
- **VPN Connection Failed** (6 steps)
- **Teams Audio Issues** (7 steps)
- **Email Sync Issues** (6 steps)

**Important:** This is educational. Always follow official company procedures.

### 7. AI-Assisted Support (Demo)

- **Local rule-based analysis** (no external API required)
- **Analyzes issue description** and provides:
  - Detected category
  - Suggested priority
  - Troubleshooting steps
  - Escalation recommendation
- **Example-driven interface** with pre-populated examples
- **Ticket creation shortcut** (creates ticket with analysis)
- **Disclaimer:** Clearly labeled as demonstration

### 8. Database (SQLite)

- **Automatic initialization** on application start
- **Tickets table** with comprehensive fields:
  - IDs, employee info, device details, issue info
  - Priority, status, assignment, resolution tracking
  - Timestamps for audit trail
- **10 sample tickets** pre-loaded for demonstration
- **Parameterized queries** for SQL injection protection

### 9. Sample Data

Includes 10 realistic, clearly fictional tickets covering:

- Network issues (Wi-Fi, VPN)
- Software problems (Outlook, Teams)
- Account issues (locked accounts, password)
- Hardware issues (printer, monitor)
- Performance issues

### 10. UI/UX Design

- **Professional appearance** (corporate style, not flashy)
- **Sidebar navigation** (5 main sections)
- **Responsive layout** (works on different screen sizes)
- **Color-coded status and priority** (visual indicators)
- **Expandable sections** (clean interface, details on demand)
- **Clear buttons and forms** (intuitive workflow)
- **Interview-ready** (professional demo experience)

### 11. Error Handling

- **Form validation** (required fields, email format)
- **Database error handling** (graceful failure)
- **User-friendly messages** (no Python tracebacks)
- **Missing data handling** (displays "Unassigned", etc.)
- **Input sanitization** (parameterized SQL queries)

### 12. Code Quality

- **Modular structure** (database.py, support_logic.py, app.py)
- **Meaningful variable names** (employee_name, not emp_nm)
- **Beginner-friendly Python** (no advanced techniques)
- **Comments where helpful** (not over-commented)
- **Clean code principles** (single responsibility)

## Technology Stack

| Technology     | Purpose           | Why?                                                        |
| -------------- | ----------------- | ----------------------------------------------------------- |
| **Python**     | Backend logic     | Widely used, great for beginners, versatile                 |
| **Streamlit**  | Web UI framework  | Quick UI development, perfect for demos, no frontend needed |
| **SQLite**     | Database          | Lightweight, file-based, perfect for standalone apps        |
| **Pandas**     | Data manipulation | Simple data operations and analysis                         |
| **Git/GitHub** | Version control   | Industry standard practice                                  |

## Project Structure

```
IT-Service-Desk/
├── app.py                 # Main Streamlit application
├── database.py            # SQLite database operations
├── support_logic.py       # Rule-based priority & AI logic
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── .gitignore             # Git ignore rules
└── service_desk.db        # SQLite database (auto-created)
```

### File Descriptions

**app.py** (350 lines)

- Main Streamlit application
- Five pages: Dashboard, Create Ticket, Manage Tickets, Troubleshooting, AI Assistant
- UI components, form handling, data display

**database.py** (250 lines)

- SQLite database initialization
- CRUD operations (Create, Read, Update, Delete)
- Search and filter functions
- Dashboard statistics aggregation
- Parameterized SQL queries for security

**support_logic.py** (200 lines)

- Rule-based priority suggestion
- Category detection from issue text
- Troubleshooting step lookup
- AI-Assisted Support demo function
- Form validation logic

**requirements.txt**

- Streamlit 1.35.0
- Pandas 2.1.3

## How It Works

### Ticket Lifecycle

```
Employee submits issue
        ↓
System auto-generates Ticket ID (TK-XXXXXXXX)
        ↓
System suggests Priority (High/Medium/Low)
        ↓
Employee can override priority if needed
        ↓
Ticket saved to SQLite database with status: "Open"
        ↓
Support staff reviews on Dashboard
        ↓
Staff assigns Technician, updates status to "In Progress"
        ↓
Staff reviews Troubleshooting Guide
        ↓
Staff investigates or escalates issue
        ↓
Staff adds Resolution Notes
        ↓
Staff updates status to "Resolved"
        ↓
Ticket marked as "Closed" (optional final step)
```

### Rule-Based Priority System

The system suggests priorities based on keywords in the issue description:

**High Priority Triggers:**

- "cannot login", "can't login", "login failed"
- "account locked", "locked out"
- "vpn not working", "vpn down"
- "internet down", "no internet"
- "system down", "server down"

**Medium Priority Triggers:**

- "outlook", "teams", "microsoft 365", "email"
- "software", "application", "installer"
- "printer", "printing"
- "slow", "freezing", "crash"

**Default: Low Priority**

- Everything else gets low priority unless human review changes it

## Database Design

### Tickets Table

```sql
CREATE TABLE tickets (
    ticket_id TEXT PRIMARY KEY,              -- TK-XXXXXXXX
    employee_name TEXT NOT NULL,             -- Full name
    employee_email TEXT NOT NULL,            -- Corporate email
    department TEXT NOT NULL,                -- Finance, HR, IT, etc.
    device_type TEXT NOT NULL,               -- Laptop, Desktop, etc.
    category TEXT NOT NULL,                  -- Hardware, Software, etc.
    issue_title TEXT NOT NULL,               -- Brief title
    description TEXT NOT NULL,               -- Detailed description
    priority TEXT NOT NULL,                  -- High, Medium, Low
    status TEXT NOT NULL,                    -- Open, In Progress, Resolved, Closed
    assigned_technician TEXT,                -- Name of assigned staff
    contact_method TEXT NOT NULL,            -- Email, Phone, Walk-in
    created_at TEXT NOT NULL,                -- ISO timestamp
    updated_at TEXT NOT NULL,                -- ISO timestamp
    resolution_notes TEXT                    -- Technician notes
)
```

**Indexes:** Optimized for common queries (status, priority, category)
**Constraints:** Primary key on ticket_id, NOT NULL on mandatory fields

## How to Run

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation & Execution

```bash
# Navigate to project directory
cd "IT Service Desk Ticket Management System"

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit application
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### Database

- SQLite database (`service_desk.db`) is created automatically on first run
- Sample data (10 tickets) is inserted automatically
- Database file persists between sessions

## Sample Screens

### Dashboard

- 5 key metrics (Total, Open, In Progress, Resolved, High Priority)
- Bar charts for Category distribution
- Bar chart for Priority distribution
- Status distribution chart
- Recent tickets table

### Create Ticket

- Form with 9 fields
- AI Priority Suggestion checkbox
- Form validation with error messages
- Success notification with Ticket ID

### Manage Tickets

- Search bar for Ticket ID/Employee
- Filter dropdowns (Category, Priority, Status)
- Expandable ticket list
- Edit Status, Priority, Technician, Resolution Notes
- Save button with success confirmation

### Troubleshooting Guide

- 8 expandable sections (Wi-Fi, Outlook, Password, Printer, Slow Laptop, VPN, Teams, Email)
- Each section shows symptoms and step-by-step troubleshooting
- Educational disclaimer

### AI Support Assistant

- Text area for issue description
- "Analyze Issue" button
- Results showing: Category, Priority, Steps, Escalation recommendation
- Pre-populated example buttons
- "Create Ticket" shortcut button

## Future Improvements

These features are **NOT implemented**. They represent production enhancements:

1. **ServiceNow/Jira Integration**
   - Real enterprise ticketing system integration
   - API connectivity for ticket sync

2. **Real Authentication**
   - Employee login system
   - Role-based access control (Employee, Technician, Manager)
   - LDAP/Azure AD integration

3. **Microsoft 365 Integration**
   - Outlook integration for automated emails
   - Teams integration for notifications
   - SharePoint for knowledge base

4. **Active Directory/Entra ID**
   - Real account unlock functionality
   - Password reset workflows
   - Real device management

5. **Real AI/LLM Integration**
   - OpenAI GPT integration for intelligent analysis
   - Natural language understanding
   - Contextual recommendations
   - Sentiment analysis

6. **Email Notifications**
   - Automated emails to employees on status updates
   - Email notifications to assigned technicians
   - Email summaries for management

7. **SLA Monitoring**
   - Service Level Agreement tracking
   - Response time calculations
   - Escalation alerts for overdue tickets

8. **Remote Support Integration**
   - TeamViewer or ConnectWise integration
   - Remote screen sharing capabilities
   - Remote device diagnostics

9. **Analytics & Reporting**
   - Custom report generation
   - Technician performance metrics
   - Department-specific trends
   - MTTR (Mean Time To Resolve) calculations

10. **Mobile Application**
    - Mobile app for employee ticket submission
    - Mobile dashboard for technicians
    - Push notifications

## Interview Explanation

### 60-Second Elevator Pitch

_"This is a Service Desk ticket management system built with Python and Streamlit. The problem it solves is that without a centralized system, technical support requests become disorganized and hard to track. The solution provides ticket creation with automatic categorization and priority suggestion, a management dashboard for support staff, and a troubleshooting guide. It uses SQLite for persistence and includes a demonstration of AI-assisted support using local rule-based logic. The entire workflow goes from ticket creation to resolution, and it's designed to be simple enough to explain in an interview while demonstrating practical understanding of service desk operations."_

### 2-Minute Detailed Explanation

**Problem:**

- Employees submit technical support requests
- Without a system, requests get lost in emails
- Support staff don't know which issues are urgent
- There's no history of what was tried before
- Escalation paths are unclear

**Solution:**
I built a Service Desk application that:

1. **Accepts ticket submissions** from employees with all relevant information (device type, issue category, description)

2. **Suggests priorities** automatically using a rule-based system. For example, if the description contains "cannot login" or "account locked", it suggests High priority. If it mentions "Outlook" or "Teams", it suggests Medium. This helps prioritize urgent issues.

3. **Creates unique ticket IDs** so every issue can be tracked individually

4. **Provides a management interface** where support staff can:
   - Search and filter tickets
   - Assign tickets to technicians
   - Update status (Open → In Progress → Resolved)
   - Add resolution notes

5. **Includes a troubleshooting guide** with step-by-step solutions for common issues like Wi-Fi problems, Outlook crashes, account lockouts, printer issues, etc.

6. **Demonstrates AI-assisted support** by analyzing issue descriptions and suggesting:
   - The likely category
   - Appropriate priority
   - Troubleshooting steps
   - Whether escalation is needed

The entire system is built with:

- **Python** for the backend logic
- **Streamlit** for the web interface (no complex frontend framework needed)
- **SQLite** as the database
- Clean, modular code that's easy to understand and modify

It includes 10 sample tickets so you can see it working immediately, and all the data is stored locally without needing external APIs or services.

## Important Concepts to Explain

Be prepared to discuss these interview topics:

1. **What is a Service Desk?**
   - Central point of contact for IT support
   - Receives, categorizes, prioritizes, and tracks requests
   - Escalates to specialized teams when needed

2. **What is a Support Ticket?**
   - Formal record of a support request
   - Contains issue details, employee info, priority, status
   - Used to track resolution

3. **Why use Ticket IDs?**
   - Unique identifier for tracking
   - Reference in communications
   - Audit trail

4. **Why categorize tickets?**
   - Route to correct team (Hardware, Software, Network, etc.)
   - Identify trends
   - Improve knowledge base

5. **Why prioritize?**
   - Focus on most critical issues first
   - Manage SLAs (response times)
   - Improve employee satisfaction
   - "Cannot login" blocks all work → High priority

6. **Ticket Status Workflow:**
   - **Open:** Newly created, not yet reviewed
   - **In Progress:** Technician assigned, actively working
   - **Resolved:** Issue fixed, awaiting confirmation
   - **Closed:** Confirmed fixed, closed by employee

7. **Why SQLite?**
   - No server needed (file-based)
   - Perfect for portfolio/demo projects
   - Easy to understand
   - Sufficient for small-to-medium workloads

8. **Why Streamlit?**
   - Rapid UI development
   - No separate frontend framework needed
   - Perfect for data applications
   - Great for portfolio demonstrations

9. **CRUD Operations:**
   - **Create:** New ticket submission
   - **Read:** View ticket details, search tickets
   - **Update:** Change status, priority, assignment
   - **Delete:** Not implemented (audit trail requirement)

10. **Rule-Based Priority System:**
    - NOT machine learning (no training data, no models)
    - Simple keyword matching
    - Human-overridable
    - Production systems would use ML or AI

11. **Escalation:**
    - When issue exceeds support staff capability
    - Database issues → Database team
    - Hardware failures → Hardware team
    - Example: Printer hardware failure → escalate to maintenance

12. **Why AI-Assisted Support?**
    - Reduce human effort
    - Consistent categorization
    - Faster issue resolution
    - Learning aid for new staff

## Security Considerations

### Current Implementation

- **NO authentication** (educational project)
- **SQL parameterization** (prevents SQL injection)
- **NO password storage** (not implemented)
- **Local database only** (no network exposure)

### Production Improvements

- Enterprise authentication (LDAP, Azure AD)
- Role-based access control (Employee, Technician, Manager, Admin)
- Encryption for sensitive data
- Audit logging for compliance
- API security (if exposed externally)

## Code Quality Features

### Modularity

- `database.py`: All database operations
- `support_logic.py`: All business logic
- `app.py`: All UI/presentation logic
- Clean separation of concerns

### Validation

- Email format validation
- Required field checking
- Database constraint enforcement
- User-friendly error messages

### Error Handling

- Try-catch for database operations
- Validation before database writes
- Graceful failure with user messages
- No Python tracebacks in UI

### Naming Conventions

- Clear, descriptive names (employee_name, not emp_nm)
- Consistent casing (snake_case for functions/variables)
- No single-letter variables (except loop counters)

## Common Interview Questions & Answers

### 1. What problem does this project solve?

**Answer:** It demonstrates understanding of IT service desk operations by creating a system to manage support tickets from submission to resolution. It addresses the real problem of disorganized support requests by providing centralized tracking, prioritization, and assignment.

### 2. Why did you choose these technologies?

**Answer:** Python is widely used and accessible, Streamlit allows rapid development without complex frontend skills, SQLite is perfect for standalone applications, and this stack is common for internal tools in many organizations.

### 3. How does the priority suggestion work?

**Answer:** It's a simple rule-based system that looks for keywords in the issue description. If it finds "cannot login" or "account locked", it suggests high priority. If it finds "Outlook" or "printer", it suggests medium. The technician can override it. This is NOT machine learning - it's basic pattern matching.

### 4. How is the data stored?

**Answer:** SQLite database with a single Tickets table. Each field corresponds to ticket information (employee name, email, device type, issue, priority, status, etc.). It's a local file-based database with no external dependencies.

### 5. What happens when an employee creates a ticket?

**Answer:** The system validates the form, generates a unique Ticket ID, optionally suggests a priority, saves all data to the database with timestamps, and returns the Ticket ID. The ticket starts with status "Open".

### 6. How would you extend this to a real production system?

**Answer:** Add authentication and role-based access, integrate with ServiceNow or Jira, connect to Active Directory for real account operations, add email notifications, implement SLA monitoring, and potentially integrate with real AI/LLM services for smarter analysis.

### 7. What is the AI-assisted support feature?

**Answer:** It's a demonstration of how AI could help. It analyzes issue descriptions locally and suggests: the category, priority level, step-by-step troubleshooting, and whether escalation is needed. No external API is required for this demo version.

### 8. How does escalation work?

**Answer:** The system suggests escalation based on keywords in the issue. For example, hardware failures, network issues, account lockouts, and system-wide problems are flagged for escalation to specialized teams. The technician reviews this recommendation.

### 9. How many tickets can this system handle?

**Answer:** Locally, it can handle hundreds of thousands of tickets since SQLite is quite efficient. For millions, you'd migrate to PostgreSQL or MySQL. Performance is typically limited by the UI (Streamlit) more than the database for this use case.

### 10. What validation does the system perform?

**Answer:** It validates required fields, checks email format, prevents SQL injection through parameterized queries, and provides user-friendly error messages instead of technical errors. The database enforces NOT NULL constraints and primary key uniqueness.

### 11. Why no real authentication?

**Answer:** This is an educational portfolio project. Real authentication would require enterprise directory integration (LDAP, Azure AD), password hashing, and complex role management. For a demonstration, it's not necessary and would complicate the code without adding interview value.

### 12. What would you change if you built this again?

**Answer:** I'd consider using a microservices architecture for scalability, implement real authentication from the start, add comprehensive logging, create a REST API for potential mobile apps, and integrate with enterprise systems (ServiceNow, Microsoft 365, Active Directory). I'd also add more sophisticated analytics and SLA tracking.

## Limitations to Mention Honestly

1. **No Real Authentication**
   - Educational project assumption: anyone can access any ticket
   - Production would require role-based access

2. **Rule-Based Prioritization Only**
   - Uses keyword matching, not machine learning
   - Cannot handle nuanced edge cases
   - Explicitly labeled as demonstration

3. **Local Database Only**
   - SQLite is not suitable for multiple concurrent users
   - No backup/disaster recovery
   - Production would use distributed databases

4. **No Integration**
   - No Microsoft 365, ServiceNow, Active Directory, or Jira integration
   - Cannot perform real account operations
   - Troubleshooting guide is informational only

5. **No Email/Notifications**
   - No automated communication with employees or staff
   - No SLA monitoring or escalation alerts

6. **Limited Analytics**
   - Only basic dashboard metrics
   - No MTTR (Mean Time To Resolve) calculations
   - No technician performance metrics

7. **No Mobile Support**
   - Streamlit not optimized for mobile devices
   - No native mobile application

## Running Locally & Demonstration

### Start Application

```bash
streamlit run app.py
```

### First-Time Experience

1. Application initializes database automatically
2. 10 sample tickets are loaded
3. Dashboard shows ticket statistics immediately
4. Explore each page to understand workflow

### Demo Sequence for Video/Recording

1. **Show Dashboard** (5 seconds)
   - Highlight metrics and charts
   - Explain ticket overview

2. **Create a Test Ticket** (20 seconds)
   - Navigate to "Create Ticket"
   - Fill form with sample employee info
   - Show AI Priority Suggestion
   - Submit and note Ticket ID

3. **Manage Tickets** (30 seconds)
   - Navigate to "Manage Tickets"
   - Search for newly created ticket
   - Show filtering by category/priority
   - Expand ticket details
   - Update status to "In Progress"
   - Assign a technician
   - Save and refresh
   - Note updated timestamp

4. **Troubleshooting Guide** (15 seconds)
   - Navigate to "Troubleshooting Guide"
   - Expand one example (e.g., "Wi-Fi Not Working")
   - Show step-by-step guide
   - Explain it's educational only

5. **AI Support Assistant** (25 seconds)
   - Navigate to "AI Support Assistant"
   - Use example button or type custom issue
   - Show analysis results (category, priority, steps)
   - Demonstrate "Create Ticket" shortcut

6. **Return to Dashboard** (10 seconds)
   - Show updated metrics reflecting new ticket
   - Explain full workflow completion

**Total Demo Time: ~2-3 minutes**

## Interview Talking Points

### Technical Competency

- ✅ Python programming (clean, modular code)
- ✅ Database design (SQL, SQLite, normalization)
- ✅ Web application development (Streamlit)
- ✅ CRUD operations (Create, Read, Update)
- ✅ Form validation and error handling

### Business Understanding

- ✅ IT service desk operations
- ✅ Ticket lifecycle and status workflows
- ✅ Prioritization logic
- ✅ Category and escalation concepts
- ✅ User needs (employee vs. support staff)

### Problem Solving

- ✅ Identified real service desk problems
- ✅ Designed appropriate solution
- ✅ Chose suitable technologies
- ✅ Implemented validation and error handling
- ✅ Considered future enhancements

### Communication

- ✅ Professional README with detailed explanations
- ✅ Clean, understandable code
- ✅ Helpful error messages to users
- ✅ Clear system design documentation
- ✅ Honest about limitations

## Contact & Support

This is an educational portfolio project. For questions during your interview preparation, review the code comments and README.

---

**Project Built:** August 2024
**Version:** 1.0
**Status:** Complete and Interview-Ready
**License:** Educational Use Only

**Good luck with your interview! Remember to explain WHY you made each choice, not just WHAT you built.**
