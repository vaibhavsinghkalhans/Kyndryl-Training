# DAY 27 – Supervisor/Router + Explicit State

## 1. What is a Supervisor/Router?

A Supervisor or Router is an agent that decides which specialized agent should handle a particular user request.

It receives the request, understands it, and sends it to the correct agent.

Example:
If a user asks a Python question, the router sends it to the Python Agent.

## 2. Why Do We Use a Router?

- To send tasks to the correct agent.
- To manage multiple agents.
- To avoid unnecessary work.
- To make task handling organized.
- To maintain the flow of information.

## 3. Router Table

| Request Type | Destination |
|---|---|
| Python Questions | Python Agent |
| Network Issues | Networking Agent |
| GitHub Questions | GitHub Agent |
| General Questions | General Agent |

## 4. What is Explicit State?

Explicit State means storing important information about a task so that agents can use it in the next steps.

It helps agents remember the current task, previous results, and task progress.

## 5. Five State Fields

| State Field | Description |
|---|---|
| user_request | Original request from the user |
| selected_agent | Agent selected by the router |
| task_status | Current status of the task |
| previous_result | Output received from the previous agent |
| final_response | Final answer given to the user |

## 6. How Router and State Work Together

1. User sends a request.
2. Router understands the request.
3. Router selects the correct agent.
4. State stores the request and selected agent.
5. The agent completes the task.
6. State gets updated with the result.
7. Final response is delivered to the user.

## 7. Simple Flow Diagram

User Request
     |
     v
Supervisor / Router
     |
     v
Select Correct Agent
     |
     v
Update State
     |
     v
Selected Agent Works
     |
     v
Save Result in State
     |
     v
Final Response

## 8. Conclusion

A Router decides which agent should handle a task, while Explicit State stores important information between steps.

Together, they help multi-agent systems work in an organized and controlled way.