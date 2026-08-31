"""
Support Logic Module

This module contains rule-based logic for:
1. Automatic priority suggestion
2. AI-Assisted Support Demo (local rule-based, no external API)

These are educational demonstrations of AI-assisted support concepts.
"""

PRIORITY_HIGH_KEYWORDS = [
    "cannot login", "can't login", "login failed", "login error",
    "account locked", "locked out", "account access",
    "vpn not working", "vpn failed", "vpn error", "vpn down",
    "internet down", "internet not working", "no internet",
    "system down", "server down", "network down",
    "password reset", "password expired"
]

PRIORITY_MEDIUM_KEYWORDS = [
    "outlook", "teams", "microsoft 365", "email",
    "software", "application", "installer",
    "printer", "print", "printing",
    "slow", "freezing", "crash", "error",
    "installation", "update", "upgrade"
]

CATEGORY_KEYWORDS = {
    "Hardware": ["printer", "monitor", "keyboard", "mouse", "device", "laptop", "desktop", "hardware", "screen"],
    "Software": ["application", "software", "install", "crash", "outlook", "teams", "error", "program"],
    "Network": ["wifi", "internet", "vpn", "connection", "network", "ethernet", "wireless"],
    "Account & Access": ["login", "password", "account", "access", "locked", "authentication"],
    "Microsoft 365": ["outlook", "teams", "sharepoint", "onedrive", "excel", "word", "microsoft 365"],
}

TROUBLESHOOTING_STEPS = {
    "Hardware": [
        "Check if the device is powered on and properly connected.",
        "Check cable connections and power supply.",
        "Restart the device.",
        "Check Device Manager for driver issues.",
        "Contact IT for hardware replacement or repair."
    ],
    "Software": [
        "Check internet connection.",
        "Restart the application.",
        "Restart the device.",
        "Check if the application is up to date.",
        "Reinstall the application if the issue persists."
    ],
    "Network": [
        "Check if Wi-Fi/network is enabled.",
        "Check airplane mode setting.",
        "Restart the router/modem.",
        "Restart your device's network connection.",
        "Escalate to network team if issue persists."
    ],
    "Account & Access": [
        "Verify your username is correct.",
        "Check if your account is locked.",
        "Attempt password reset through the portal.",
        "Wait 15-30 minutes if account is locked.",
        "Contact IT for account unlock or password reset."
    ],
    "Microsoft 365": [
        "Check internet connection.",
        "Check Microsoft 365 service status.",
        "Restart the Microsoft 365 application.",
        "Restart your device.",
        "Sign out and sign back into Microsoft 365.",
        "Escalate if issue continues."
    ],
    "Other": [
        "Describe the issue in detail.",
        "Take screenshots if possible.",
        "Note any error messages.",
        "Contact IT support for assistance."
    ]
}

def suggest_priority(issue_title, description):
    """
    Suggest a priority level based on issue content.
    
    This is a simple rule-based system, NOT machine learning.
    
    Returns: "High", "Medium", or "Low"
    """
    combined_text = (issue_title + " " + description).lower()
    
    # Check for high priority keywords
    for keyword in PRIORITY_HIGH_KEYWORDS:
        if keyword in combined_text:
            return "High"
    
    # Check for medium priority keywords
    for keyword in PRIORITY_MEDIUM_KEYWORDS:
        if keyword in combined_text:
            return "Medium"
    
    # Default to low priority
    return "Low"

def detect_category(issue_description):
    """
    Detect the issue category based on keywords.
    
    Returns: Detected category string
    """
    description_lower = issue_description.lower()
    
    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in description_lower:
                return category
    
    return "Other"

def get_troubleshooting_steps(category):
    """
    Get standard troubleshooting steps for a category.
    
    Returns: List of troubleshooting steps
    """
    return TROUBLESHOOTING_STEPS.get(category, TROUBLESHOOTING_STEPS["Other"])

def ai_support_demo(issue_description):
    """
    AI-Assisted Support Demo Function
    
    This demonstrates how an AI support assistant could help by:
    1. Detecting the issue category
    2. Suggesting priority
    3. Providing troubleshooting steps
    4. Recommending escalation if needed
    
    This is a LOCAL RULE-BASED SYSTEM. No external AI API is used.
    
    Args:
        issue_description (str): Description of the issue
    
    Returns:
        dict: Contains category, priority, steps, and escalation recommendation
    """
    
    detected_category = detect_category(issue_description)
    suggested_priority = suggest_priority(issue_description, issue_description)
    troubleshooting_steps = get_troubleshooting_steps(detected_category)
    
    # Determine if escalation is recommended
    escalation_keywords = [
        "hardware", "physical", "repair", "replacement",
        "network", "vpn", "server", "system",
        "account", "locked", "active directory"
    ]
    
    should_escalate = any(keyword in issue_description.lower() for keyword in escalation_keywords)
    
    return {
        "category": detected_category,
        "suggested_priority": suggested_priority,
        "troubleshooting_steps": troubleshooting_steps,
        "should_escalate": should_escalate,
        "escalation_note": "This issue may require specialized team support." if should_escalate else None
    }

def validate_email(email):
    """Simple email validation."""
    return "@" in email and "." in email

def validate_ticket_form(data):
    """Validate ticket form data."""
    errors = []
    
    if not data.get("employee_name"):
        errors.append("Employee name is required")
    
    if not data.get("employee_email"):
        errors.append("Employee email is required")
    elif not validate_email(data["employee_email"]):
        errors.append("Please enter a valid email address")
    
    if not data.get("department"):
        errors.append("Department is required")
    
    if not data.get("device_type"):
        errors.append("Device type is required")
    
    if not data.get("category"):
        errors.append("Issue category is required")
    
    if not data.get("issue_title"):
        errors.append("Issue title is required")
    
    if not data.get("description"):
        errors.append("Issue description is required")
    
    if not data.get("priority"):
        errors.append("Priority is required")
    
    if not data.get("contact_method"):
        errors.append("Preferred contact method is required")
    
    return errors
