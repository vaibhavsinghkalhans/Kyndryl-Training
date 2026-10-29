# Day 24 - Reasoning Decomposition

## Scenario
User cannot access a company application.

## Step-by-Step Agent Workflow

### Step 1: Receive Incident
- Collect username, application name, and error message.
- Decision:
  - Information complete → Step 2
  - Information missing → Request details

### Step 2: Verify User Account
- Check account status.
- Decision:
  - Active account → Step 3
  - Locked/Disabled account → Fix and notify user

### Step 3: Check Authentication Services
- Verify AD, Azure AD, LDAP, or SSO services.
- Decision:
  - Service healthy → Step 4
  - Service issue → Escalate to Identity Team

### Step 4: Check Application Health
- Verify server and application status.
- Decision:
  - Application available → Step 5
  - Application unavailable → Open incident

### Step 5: Check Network Connectivity
- Verify DNS, VPN, firewall, and proxy.
- Decision:
  - Network issue found → Escalate to Network Team
  - No issue found → Step 6

### Step 6: Perform Remediation
- Reset password/session.
- Clear cache or update permissions.
- Decision:
  - Issue resolved → Step 7
  - Not resolved → Escalate

### Step 7: Confirm Resolution
- User verifies access.
- Update and close ticket.

## Workflow

Incident Received
↓
Gather Details
↓
Check User Account
↓
Check Authentication Service
↓
Check Application Health
↓
Check Network Connectivity
↓
Apply Fix
↓
Resolved?
├─ Yes → Close Ticket
└─ No → Escalate