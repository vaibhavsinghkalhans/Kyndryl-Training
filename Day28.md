# DAY 28 – Human-in-the-Loop + Cyclic Workflows

## 1. What is Human-in-the-Loop?

Human-in-the-Loop means involving a human in an automated process when approval or verification is required.

The AI agent does not complete every task automatically. Sometimes it stops and waits for human approval.

### Why do we need it?

- To avoid mistakes.
- To improve safety.
- To get human approval for important actions.
- To maintain control over automation.

### Example:

Suppose an AI agent prepares an important email.

1. AI creates the email.
2. Human reviews the email.
3. Human approves it.
4. Only then the email is sent.

## 2. Approval Gate

An Approval Gate is a checkpoint where the workflow stops until a human gives approval.

**Input:** Completed email draft.

**Decision:** Approved or Rejected.

**Output:**
- Approved → Continue the workflow.
- Rejected → Send back for correction.

**Exit Condition:** Workflow continues only after approval. If rejected, it returns for correction instead of sending the email.

## 3. What is a Cyclic Workflow?

A Cyclic Workflow is a process where an agent repeats a task until the result meets the required conditions or the retry limit is reached.

It is also called a Retry Loop.

### Why do we use it?

- To correct mistakes.
- To improve output quality.
- To handle temporary failures.
- To achieve the required result.

### Example:

An AI agent writes a Python program.

1. Agent writes the code.
2. Reviewer checks the code.
3. If errors are found, the code goes back for correction.
4. Agent corrects the code.
5. Reviewer checks it again.

## 4. Retry Loop with Exit Condition

**Maximum retries: 3**

- If the output is correct → Stop and accept the result.
- If errors are found → Send back for correction.
- If 3 retries are completed and errors remain → Stop and escalate to a human.

**Exit Condition:** Successful review or maximum retry limit reached.

## 5. Updated Workflow Design

User Request
     |
     v
Supervisor / Router
     |
     v
Specialist Agent
     |
     v
Reviewer Agent
     |
     v
Are there errors?
   /       
 Yes        No
  |          |
  v          v
Retry      Approval Gate
  |          |
  v          v
Correction  Human Review
  |          |
  v          v
Review     Approved?
Again      /     
          Yes     No
           |       |
           v       v
        Final    Correction /
        Output   Escalation

## 6. Two Important Safety Rules

1. Never perform important actions without required human approval.
2. Never allow unlimited retries. Always define a maximum retry limit.

## 7. Conclusion

Human-in-the-Loop provides human control and approval in automated workflows.

Cyclic Workflows allow agents to repeat tasks and correct mistakes.

Both concepts make multi-agent systems safer and more reliable.