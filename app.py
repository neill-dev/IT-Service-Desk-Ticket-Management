"""
IT Service Desk Ticket Management System

A Streamlit application for managing IT support tickets.
Demonstrates core service desk concepts including ticket management,
priority assignment, status tracking, and AI-assisted support.

This is an educational project built for interview demonstration.
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import database
import support_logic

# Page configuration
st.set_page_config(
    page_title="IT Service Desk",
    page_icon="🎫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize database
database.init_database()

# Custom CSS for professional styling
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .status-open {
        color: #ff6b6b;
    }
    .status-in-progress {
        color: #ffa500;
    }
    .status-resolved {
        color: #51cf66;
    }
    .status-closed {
        color: #6c757d;
    }
    .priority-high {
        color: #ff6b6b;
        font-weight: bold;
    }
    .priority-medium {
        color: #ffa500;
        font-weight: bold;
    }
    .priority-low {
        color: #51cf66;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

def format_datetime(dt_str):
    """Format datetime string for display."""
    if not dt_str:
        return ""
    try:
        dt = datetime.fromisoformat(dt_str)
        return dt.strftime("%Y-%m-%d %H:%M")
    except:
        return dt_str

# Sidebar Navigation
st.sidebar.title("🎫 IT Service Desk")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    ["📊 Dashboard", "➕ Create Ticket", "🔧 Manage Tickets", 
     "📖 Troubleshooting Guide", "🤖 AI Support Assistant"]
)

st.sidebar.markdown("---")
st.sidebar.info(
    """
    **IT Service Desk System**
    
    This system helps manage and track technical support requests from employees.
    
    **Version:** 1.0
    """
)

# PAGE 1: DASHBOARD
if page == "📊 Dashboard":
    st.title("📊 Service Desk Dashboard")
    st.markdown("---")
    
    # Get dashboard statistics
    stats = database.get_dashboard_stats()
    
    # Key Metrics Row
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Total Tickets", stats["total"])
    
    with col2:
        st.metric("Open Tickets", stats["open"])
    
    with col3:
        st.metric("In Progress", stats["in_progress"])
    
    with col4:
        st.metric("Resolved", stats["resolved"])
    
    with col5:
        st.metric("High Priority", stats["high_priority"])
    
    st.markdown("---")
    
    # Charts Row
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Tickets by Category")
        if stats["by_category"]:
            category_df = pd.DataFrame(
                list(stats["by_category"].items()),
                columns=["Category", "Count"]
            )
            st.bar_chart(category_df.set_index("Category"))
        else:
            st.info("No ticket data available")
    
    with col2:
        st.subheader("Tickets by Priority")
        if stats["by_priority"]:
            priority_df = pd.DataFrame(
                list(stats["by_priority"].items()),
                columns=["Priority", "Count"]
            )
            st.bar_chart(priority_df.set_index("Priority"))
        else:
            st.info("No ticket data available")
    
    st.markdown("---")
    
    # Status Distribution
    st.subheader("Ticket Status Distribution")
    if stats["by_status"]:
        status_df = pd.DataFrame(
            list(stats["by_status"].items()),
            columns=["Status", "Count"]
        )
        st.bar_chart(status_df.set_index("Status"))
    else:
        st.info("No ticket data available")
    
    st.markdown("---")
    
    # Recent Tickets
    st.subheader("Recent Tickets")
    recent = database.get_recent_tickets(limit=10)
    
    if recent:
        display_data = []
        for ticket in recent:
            display_data.append({
                "Ticket ID": ticket["ticket_id"],
                "Employee": ticket["employee_name"],
                "Category": ticket["category"],
                "Priority": ticket["priority"],
                "Status": ticket["status"],
                "Created": format_datetime(ticket["created_at"])
            })
        
        df = pd.DataFrame(display_data)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No tickets found")

# PAGE 2: CREATE TICKET
elif page == "➕ Create Ticket":
    st.title("➕ Create New Support Ticket")
    st.markdown("Fill out the form below to submit a new support request.")
    st.markdown("---")
    
    with st.form("ticket_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            employee_name = st.text_input("👤 Employee Name")
            employee_email = st.text_input("📧 Employee Email")
            department = st.selectbox(
                "🏢 Department",
                ["Finance", "HR", "IT", "Marketing", "Sales", "Operations", "Engineering", "Legal", "Other"]
            )
            device_type = st.selectbox(
                "💻 Device Type",
                ["Laptop", "Desktop", "Smartphone", "Tablet", "Printer", "Other"]
            )
        
        with col2:
            category = st.selectbox(
                "📂 Issue Category",
                ["Hardware", "Software", "Network", "Account & Access", "Microsoft 365", "Other"]
            )
            contact_method = st.selectbox(
                "📞 Preferred Contact Method",
                ["Email", "Phone", "Walk-in"]
            )
            issue_title = st.text_input("📝 Issue Title")
            description = st.text_area("📋 Issue Description", height=100)
        
        st.markdown("---")
        
        # AI Priority Suggestion
        col1, col2 = st.columns(2)
        
        with col1:
            if st.checkbox("💡 Use AI Priority Suggestion"):
                if issue_title and description:
                    suggested_priority = support_logic.suggest_priority(issue_title, description)
                    st.info(f"🤖 Suggested Priority: **{suggested_priority}**")
                    priority = st.selectbox(
                        "Priority (Override if needed)",
                        ["Low", "Medium", "High"],
                        index=["Low", "Medium", "High"].index(suggested_priority)
                    )
                else:
                    st.warning("Enter issue title and description to get priority suggestion")
                    priority = st.selectbox("Priority", ["Low", "Medium", "High"])
            else:
                priority = st.selectbox("Priority", ["Low", "Medium", "High"])
        
        st.markdown("---")
        submitted = st.form_submit_button("✅ Create Ticket", use_container_width=True)
    
    if submitted:
        # Validate form
        form_data = {
            "employee_name": employee_name,
            "employee_email": employee_email,
            "department": department,
            "device_type": device_type,
            "category": category,
            "issue_title": issue_title,
            "description": description,
            "priority": priority,
            "contact_method": contact_method
        }
        
        errors = support_logic.validate_ticket_form(form_data)
        
        if errors:
            st.error("❌ Please fix the following errors:")
            for error in errors:
                st.error(f"• {error}")
        else:
            # Create ticket
            ticket_id = database.create_ticket(
                employee_name=employee_name,
                employee_email=employee_email,
                department=department,
                device_type=device_type,
                category=category,
                issue_title=issue_title,
                description=description,
                priority=priority,
                contact_method=contact_method
            )
            
            st.success(f"✅ Ticket created successfully!")
            st.info(f"**Ticket ID:** {ticket_id}")
            st.balloons()

# PAGE 3: MANAGE TICKETS
elif page == "🔧 Manage Tickets":
    st.title("🔧 Manage Support Tickets")
    st.markdown("---")
    
    # Search and Filter Section
    col1, col2, col3 = st.columns(3)
    
    with col1:
        search_term = st.text_input("🔍 Search by Ticket ID or Employee", "")
    
    with col2:
        category_filter = st.selectbox(
            "📂 Filter by Category",
            ["All"] + ["Hardware", "Software", "Network", "Account & Access", "Microsoft 365", "Other"]
        )
    
    with col3:
        priority_filter = st.selectbox(
            "🎯 Filter by Priority",
            ["All", "High", "Medium", "Low"]
        )
    
    col1, col2 = st.columns(2)
    
    with col1:
        status_filter = st.selectbox(
            "📊 Filter by Status",
            ["All", "Open", "In Progress", "Resolved", "Closed"]
        )
    
    st.markdown("---")
    
    # Apply filters
    tickets = database.search_tickets(
        keyword=search_term if search_term else None,
        category=None if category_filter == "All" else category_filter,
        priority=None if priority_filter == "All" else priority_filter,
        status=None if status_filter == "All" else status_filter
    )
    
    if tickets:
        # Display tickets as expandable items
        for ticket in tickets:
            with st.expander(
                f"🎫 {ticket['ticket_id']} | {ticket['employee_name']} | {ticket['priority']} | {ticket['status']}"
            ):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"**Employee:** {ticket['employee_name']}")
                    st.write(f"**Email:** {ticket['employee_email']}")
                    st.write(f"**Department:** {ticket['department']}")
                    st.write(f"**Device:** {ticket['device_type']}")
                    st.write(f"**Category:** {ticket['category']}")
                    st.write(f"**Issue Title:** {ticket['issue_title']}")
                    st.write(f"**Description:** {ticket['description']}")
                
                with col2:
                    st.write(f"**Contact Method:** {ticket['contact_method']}")
                    st.write(f"**Created:** {format_datetime(ticket['created_at'])}")
                    st.write(f"**Updated:** {format_datetime(ticket['updated_at'])}")
                    st.write(f"**Assigned To:** {ticket['assigned_technician'] or 'Unassigned'}")
                    if ticket['resolution_notes']:
                        st.write(f"**Resolution Notes:** {ticket['resolution_notes']}")
                
                st.markdown("---")
                
                # Update ticket
                st.subheader("Update Ticket")
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    new_status = st.selectbox(
                        "Update Status",
                        ["Open", "In Progress", "Resolved", "Closed"],
                        index=["Open", "In Progress", "Resolved", "Closed"].index(ticket['status']),
                        key=f"status_{ticket['ticket_id']}"
                    )
                
                with col2:
                    new_priority = st.selectbox(
                        "Update Priority",
                        ["Low", "Medium", "High"],
                        index=["Low", "Medium", "High"].index(ticket['priority']),
                        key=f"priority_{ticket['ticket_id']}"
                    )
                
                with col3:
                    assigned_tech = st.text_input(
                        "Assigned Technician",
                        value=ticket['assigned_technician'] or "",
                        key=f"tech_{ticket['ticket_id']}"
                    )
                
                resolution_notes = st.text_area(
                    "Resolution Notes",
                    value=ticket['resolution_notes'] or "",
                    height=80,
                    key=f"notes_{ticket['ticket_id']}"
                )
                
                if st.button("💾 Save Changes", key=f"save_{ticket['ticket_id']}"):
                    database.update_ticket(
                        ticket['ticket_id'],
                        status=new_status,
                        priority=new_priority,
                        assigned_technician=assigned_tech if assigned_tech else None,
                        resolution_notes=resolution_notes if resolution_notes else None
                    )
                    st.success("✅ Ticket updated successfully!")
                    st.rerun()
    else:
        st.info("No tickets found matching your criteria.")

# PAGE 4: TROUBLESHOOTING GUIDE
elif page == "📖 Troubleshooting Guide":
    st.title("📖 Troubleshooting Guide")
    st.markdown(
        "This guide provides common troubleshooting steps for typical IT support issues. "
        "This is an educational guide. Follow your company's official procedures for any changes."
    )
    st.markdown("---")
    
    guides = {
        "🌐 Wi-Fi Not Working": {
            "symptoms": "Employee cannot connect to office Wi-Fi network",
            "steps": [
                "Check if Wi-Fi is enabled on the device",
                "Check if airplane mode is turned off",
                "Restart the Wi-Fi connection",
                "Restart the device",
                "Escalate to network team if issue persists"
            ]
        },
        "📧 Outlook Not Opening": {
            "symptoms": "Outlook application crashes or fails to launch",
            "steps": [
                "Check internet connection",
                "Restart Outlook application",
                "Restart the device",
                "Check Microsoft 365 service status",
                "Escalate to Microsoft 365 team if issue continues"
            ]
        },
        "🔐 Password/Account Issue": {
            "symptoms": "Cannot login or account is locked",
            "steps": [
                "Verify the username is correct",
                "Check if caps lock is accidentally on",
                "Check if account is locked after failed attempts",
                "Wait 15-30 minutes for locked account to unlock",
                "Use password reset portal if account is not locked",
                "Escalate to IT security for persistent issues"
            ]
        },
        "🖨️ Printer Not Working": {
            "symptoms": "Cannot print or printer is offline",
            "steps": [
                "Check if printer is powered on",
                "Check printer connection (USB/Network)",
                "Check printer status on device",
                "Set printer as default printer if needed",
                "Restart printer",
                "Escalate to IT if hardware failure suspected"
            ]
        },
        "💻 Laptop Running Slowly": {
            "symptoms": "Slow application loading, system freezing",
            "steps": [
                "Check available disk space",
                "Close unnecessary applications",
                "Restart the device",
                "Check for system updates",
                "Remove unnecessary startup programs",
                "Check Windows Task Manager for resource usage",
                "Escalate to IT if hardware upgrade needed"
            ]
        },
        "🌐 VPN Connection Failed": {
            "symptoms": "Cannot establish VPN connection when working remotely",
            "steps": [
                "Check internet connection",
                "Verify VPN credentials",
                "Restart VPN client",
                "Check VPN service status",
                "Restart device",
                "Escalate to network team for authentication issues"
            ]
        },
        "🎤 Microsoft Teams Audio Issues": {
            "symptoms": "Audio cutting out, echo, or no sound in Teams calls",
            "steps": [
                "Check microphone and speaker connections",
                "Check device volume levels",
                "Restart Microsoft Teams",
                "Check internet connection speed",
                "Test audio settings in Teams",
                "Escalate to Microsoft 365 team if issue persists"
            ]
        },
        "📱 Email Sync Issues": {
            "symptoms": "Mobile device not syncing emails",
            "steps": [
                "Check internet connection",
                "Check email account settings",
                "Restart email application",
                "Remove and re-add email account",
                "Restart device",
                "Escalate to mobile device management team"
            ]
        }
    }
    
    for guide_title, guide_content in guides.items():
        with st.expander(guide_title):
            st.write(f"**Symptoms:** {guide_content['symptoms']}")
            st.write("**Troubleshooting Steps:**")
            for i, step in enumerate(guide_content['steps'], 1):
                st.write(f"{i}. {step}")
    
    st.markdown("---")
    st.warning(
        "⚠️ **Important Disclaimer:** This is an educational troubleshooting guide. "
        "Always follow your organization's official procedures and policies. "
        "For sensitive operations like password resets or Active Directory changes, "
        "contact your IT administration team."
    )

# PAGE 5: AI SUPPORT ASSISTANT
elif page == "🤖 AI Support Assistant":
    st.title("🤖 AI-Assisted Support Demo")
    st.markdown(
        "This demonstrates how AI-assisted support could help service desk staff "
        "by analyzing issues and suggesting categories, priorities, and troubleshooting steps."
    )
    st.info(
        "**Note:** This is a demonstration using local rule-based logic. "
        "No external AI API is connected. In production, this would integrate with "
        "advanced AI/LLM services."
    )
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        user_issue = st.text_area(
            "Describe the employee's issue:",
            height=100,
            placeholder="Example: Outlook is not opening on my laptop..."
        )
    
    with col2:
        st.write("")
        st.write("")
        analyze_button = st.button("🔍 Analyze Issue", use_container_width=True)
    
    if analyze_button and user_issue:
        # Get AI support analysis
        analysis = support_logic.ai_support_demo(user_issue)
        
        st.markdown("---")
        st.subheader("📊 Analysis Results")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Detected Category", analysis["category"])
            st.metric("Suggested Priority", analysis["suggested_priority"])
        
        with col2:
            if analysis["should_escalate"]:
                st.warning("🚨 Escalation Recommended")
            else:
                st.success("✅ Can be handled by support staff")
        
        st.markdown("---")
        st.subheader("📋 Recommended Troubleshooting Steps")
        
        for i, step in enumerate(analysis["troubleshooting_steps"], 1):
            st.write(f"{i}. {step}")
        
        if analysis["escalation_note"]:
            st.markdown("---")
            st.info(f"📌 {analysis['escalation_note']}")
        
        # Provide option to create ticket
        st.markdown("---")
        if st.button("🎫 Create Ticket Based on Analysis"):
            # Pre-fill the ticket creation form with analysis data
            st.session_state.pre_filled_category = analysis["category"]
            st.session_state.pre_filled_priority = analysis["suggested_priority"]
            st.session_state.pre_filled_description = user_issue
            st.info("Navigate to 'Create Ticket' page - form will be pre-filled with analysis")
    
    elif analyze_button and not user_issue:
        st.error("❌ Please enter an issue description")
    
    # Demo examples
    st.markdown("---")
    st.subheader("💡 Try These Examples")
    
    examples = [
        "Cannot login to my account after incorrect password attempts",
        "Outlook crashes immediately when I try to open it",
        "My laptop is very slow and freezes frequently"
    ]
    
    for example in examples:
        if st.button(f"📌 {example}"):
            st.session_state.demo_issue = example
            st.rerun()
    
    if "demo_issue" in st.session_state:
        analysis = support_logic.ai_support_demo(st.session_state.demo_issue)
        
        st.markdown("---")
        st.subheader("📊 Analysis Results")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Detected Category", analysis["category"])
            st.metric("Suggested Priority", analysis["suggested_priority"])
        
        with col2:
            if analysis["should_escalate"]:
                st.warning("🚨 Escalation Recommended")
            else:
                st.success("✅ Can be handled by support staff")
        
        st.markdown("---")
        st.subheader("📋 Recommended Troubleshooting Steps")
        
        for i, step in enumerate(analysis["troubleshooting_steps"], 1):
            st.write(f"{i}. {step}")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray; font-size: 12px;'>"
    "IT Service Desk System v1.0 | Educational Project | "
    "<a href='https://github.com'>View Project</a>"
    "</div>",
    unsafe_allow_html=True
)
