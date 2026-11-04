# DAY 26 – Multi-Agent Systems: Roles and Collaboration

## 1. What is a Multi-Agent System?

A Multi-Agent System is a system where multiple AI agents work together to complete a task.

Each agent has a different role and responsibility.

Instead of one agent doing everything, tasks are divided between specialized agents.

## 2. Why Do We Use Multiple Agents?

- To divide complex tasks into smaller tasks.
- To improve accuracy.
- To save time.
- To use specialized knowledge.
- To review and improve results.

## 3. Three Main Agent Roles

### Agent 1: Coordinator

**Role:** Manages the complete task and assigns work to other agents.

**Input:** User's request and task requirements.

**Output:** Task plan and instructions for the specialist agent.

### Agent 2: Specialist

**Role:** Performs the main task using its specialized knowledge.

**Input:** Task instructions from the coordinator.

**Output:** Completed work or solution.

### Agent 3: Reviewer

**Role:** Checks the specialist's work and finds mistakes.

**Input:** Completed work from the specialist.

**Output:** Feedback, corrections, and approved final result.

## 4. How Do Agents Collaborate?

Example: Creating a Python presentation.

1. Coordinator: Understands the task and divides the work.
2. Specialist: Creates the Python presentation content.
3. Reviewer: Checks the content for mistakes and accuracy.
4. Final Result: The corrected presentation is delivered.

## 5. Simple Multi-Agent Role Map

User Request
     |
     v
Coordinator Agent
     |
     v
Specialist Agent
     |
     v
Reviewer Agent
     |
     v
Final Output

## 6. Conclusion

Multi-Agent Systems allow multiple specialized agents to work together. Each agent has a specific responsibility, making complex tasks easier to manage and complete.