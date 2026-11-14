# AI Agents & Patterns Cheat Sheet

## Quick mental model
- Chain = fixed sequence
- Workflow = rule-based branching
- Agent = goal-driven decision-making
- Harness = runtime loop + tools + safety checks + memory + retries

---

## Part 1: Agent Fundamentals

### 01. How is an agent different from a chain and a workflow?
**Answer:**
A chain is a fixed sequence. It always follows the same order of operations and is ideal for deterministic tasks. A workflow adds decision points, but those decisions are still defined in advance by the developer. An agent goes one step further: it can interpret a task, decide what information it lacks, choose tools dynamically, and continue until it reaches a reasonable stopping point.

- **Chain:** predetermined sequence, usually no branching, same output every time
- **Workflow:** branching logic defined by rules, still pre-programmed
- **Agent:** goal-driven behavior, dynamic tool selection, flexible reasoning

**Why it matters:**
- A chain is best for repetitive tasks like sending a confirmation email.
- A workflow is best for rules-heavy processes like refund approval flows.
- An agent is best when the task requires judgment, context, and adaptation.

**Example:**
- Chain: send a standard confirmation email
- Workflow: if refund requested, route to billing; otherwise continue shipping
- Agent: customer says pizza is cold -> check order + kitchen queue -> decide refund or replacement

**Interview angle:**
An agent is useful when there is no fixed pipeline that always covers the real-world situation. It behaves more like a decision-maker than a script.

---

### 02. When should you NOT build an agent?
**Answer:**
You should not build an agent when the task can be solved reliably with regular software logic. If the decision path is clearly defined and does not require adapting to ambiguous situations, then using an LLM agent adds cost, latency, and unpredictability without real value.

- Use a script for arithmetic, validation, routing, data transforms, and repetitive automation.
- Use an agent only when there is uncertainty, context gathering, or dynamic decision-making.

**Example:**
- Do not build an autonomous agent for a 7% tax calculation; use code instead.
- Do not use an agent to check whether a number is even or odd; a simple branch is better.

**Interview angle:**
A good agent is not the most advanced solution; it is the simplest system that can solve the problem reliably.

---

### 03. What is the core agent loop?
**Answer:**
The agent loop is the repeated cycle of perceiving, deciding, acting, and learning. This is the heart of agentic systems.

1. **Input:** User gives a task or asks a question.
2. **Reason:** The model decides what it needs to do, what information is missing, and what tool might help.
3. **Act:** The agent calls a tool, executes code, or performs an action.
4. **Observe:** It reads the response from the tool or system.
5. **Repeat:** It continues until the task is complete or hits a guardrail.

**Stop conditions:**
- final answer produced
- max tool calls reached
- timeout
- repeated failure / no progress
- safety policy triggered

**Example:**
- User asks: "Where is order #405?"
- Agent decides: "I need the order status"
- Agent calls: get_order_status(405)
- Tool returns: "Out for delivery in 5 minutes"
- Agent responds with the final answer

**Interview angle:**
The loop is useful because it turns static prompting into interactive execution. The agent is not just answering once; it is actively working through the task.

---

### 04. What is the autonomy spectrum?
**Answer:**
The autonomy spectrum describes how much decision-making power the model gets. Low autonomy means the system is tightly controlled. High autonomy means the model can decide actions with less human oversight.

- **Zero autonomy:** fixed prompt, no dynamic action
- **Low autonomy:** simple tool usage with strong constraints
- **Medium autonomy:** handles multi-step work with guardrails
- **High autonomy:** acts more independently and can make its own next steps
- **Full autonomy:** near-complete control, risky and difficult to supervise

**Rule:**
Keep autonomy as low as possible while still solving the task. This reduces cost, risk, and unpredictable behavior.

**Interview angle:**
Good agent design is not maximum autonomy; it is controlled autonomy. You add freedom only where it improves reliability and value.

---

### 05. What is ReAct?
**Answer:**
ReAct stands for Reason + Act. It is a pattern where the model explicitly reasons, calls a tool or performs an action, and then observes the result before continuing.

- **Thought:** "I need to check the order status"
- **Action:** call get_order_status(405)
- **Observation:** the tool returns a status

This is more powerful than a single prompt-response because the agent can adapt based on real results instead of guessing.

**Failure modes:**
- infinite loops if the tool keeps failing
- repeated wrong tool calls because the model is confused
- memory bloat from storing too many failed attempts and logs

**Interview angle:**
ReAct is one of the foundational patterns because it combines step-by-step reasoning with real execution.

---

### 06. Tool call vs direct answer
**Answer:**
The model should answer directly only when it already has enough information or the answer is general knowledge. It should call a tool when the answer depends on fresh data, private business data, or calculations that cannot be inferred from memory alone.

**Use a tool when:**
- the task requires the current database state
- the answer depends on user-specific data
- the task needs external APIs or systems
- the response must be verified against a real system

**Example:**
- "What ingredients are in Margherita pizza?" -> answer from memory
- "Is order #405 out for delivery yet?" -> use tracking tool

**Interview angle:**
This is the central distinction between reasoning and execution. An agent should not pretend to know live data when it needs to query a system.

---

### 07. Reactive vs proactive agent
**Answer:**
A reactive agent waits for an input event. A proactive agent watches for state changes or background triggers and acts without a direct user request.

- **Reactive agent:** user messages, bot replies
- **Proactive agent:** detects issue, sends follow-up, suggests intervention

**Example:**
- Reactive: answers "Where is my pizza?"
- Proactive: notices a driver has a flat tire and texts the customer automatically with a discount and updated ETA

**Interview angle:**
Proactive systems are more complex because they require event detection, state monitoring, and safe trigger logic. They are powerful, but higher risk if poorly designed.

---

### 08. Stateless vs stateful agent
**Answer:**
A stateless agent does not retain context across conversations. Every new request must include the entire prior history. A stateful agent stores relevant information and can continue from where it left off.

- **Stateless:** simpler, but weak continuity
- **Stateful:** better for customer support and long-running workflows

**Example:**
- Stateless: each message starts from scratch
- Stateful: customer asks about an order, comes back later, and the agent still knows the order ID and complaint

**Key point:**
For support bots, statefulness is generally required because customers expect continuity.

---

### 09. Agent state vs memory
**Answer:**
Agent state is the temporary context needed to complete the current task. Memory is persistent information retained across tasks or sessions.

- **Agent state:** what the agent needs right now
- **Memory:** what it should remember over time

**Example:**
- State: "I verified this customer’s phone number in this chat"
- Memory: "This customer is allergic to mushrooms and always orders extra garlic"

**Interview angle:**
State helps with short-term coherence. Memory enables personalization and continuity across repeated interactions.

---

### 10. How do you set termination conditions?
**Answer:**
Termination conditions define when an agent must stop. Without them, an agent may loop forever, waste tokens, or take dangerous actions.

Common termination rules:
- maximum tool-call limit
- wall-clock timeout
- no-progress threshold
- repeated tool-call guard
- human approval for high-risk actions

**Example:**
- stop after 5 tool calls
- stop if the same API call repeats twice with the same error
- stop if the system has not reached a sensible answer after 30 seconds

**Interview angle:**
Termination conditions are the safety mechanism that keeps the autonomous system bounded.

---

### 11. Why do agent errors compound?
**Answer:**
Agent systems are multi-step. If each step is 90% reliable, the probability of success for the whole task drops quickly as the number of steps increases.

If each step succeeds with probability 0.90:

$$0.90^5 \approx 59\%$$

and

$$0.90^{10} \approx 35\%$$

This means small mistakes are amplified across long chains. A single wrong tool call or misread result can derail the whole task.

**Takeaway:**
- errors compound fast
- tools should be validated
- the agent should retry carefully
- verification steps matter a lot

**Interview angle:**
This is why real-world agent systems need guardrails, retries, and confidence checks.

---

### 12. What makes a good system prompt?
**Answer:**
A good system prompt does not just say "be helpful." It defines the role, boundaries, decision process, and expected output format. This reduces ambiguity and keeps the agent aligned with business rules.

A strong prompt includes:
- role: who the agent is
- rules: what it can and cannot do
- constraints: risk boundaries and approval requirements
- context: current date, order details, environment
- output format: short response, structured JSON, or escalation workflow

**Example:**
- "You are a pizza support agent. Never approve a refund above $50 without manager approval. Use a calm tone and keep responses under 3 sentences unless the customer is angry."

**Interview angle:**
The prompt is not magic. It is a control layer that shapes behavior, just like software constraints shape program logic.

---

### 13. Tool call vs function call
**Answer:**
In a workflow, the developer explicitly writes the function call. In an agent, the model chooses which tool to call and what arguments to pass based on the current task.

- **Workflow:** "Run function X now"
- **Agent:** "I think I need order status, so I will call get_order_status(order_id)"

This flexibility is why agents are useful, but it also creates risk if the tool list is too vague or the system prompt is weak.

**Interview angle:**
A tool call is the bridge between reasoning and external execution. It is where a language model becomes operational.

---

### 14. Three anti-patterns
**Answer:**
These are common mistakes when building agents.

1. **Too many tools:** too many choices confuse the model and lower precision.
2. **Using an agent for trivial logic:** if a rule-based system can do it, use that instead.
3. **No stop conditions or guardrails:** the system may loop, overdraw, or call the wrong API repeatedly.

**Risk:**
- wrong actions
- runaway loops
- risky or costly decisions

**Interview angle:**
Good agent design is not about giving the model maximum freedom; it is about giving it just enough structure to succeed safely.

---

## Part 2: Harness & Patterns

### 15. Model vs harness
**Answer:**
The model is the reasoning engine. The harness is the software around it that makes the model useful in production.

- **Model:** language understanding, reasoning, planning, tool selection
- **Harness:** execution loop, tool wrappers, context management, retries, monitoring, and sandboxing

**Why this matters:**
A strong harness can make an average model perform much better in a real environment. In production systems, the harness often determines success more than the model alone.

---

### 16. Which matters more: model or harness?
**Answer:**
For most production systems, the harness matters more than the raw model quality. A weaker model can still be effective if the system is carefully designed with strong context, evals, and deterministic guardrails.

**Example:**
A good coding agent may be built from a mid-tier model backed by a robust repo navigator, test runner, and sandbox. That often outperforms a powerful model without the proper harness.

---

### 17. Six canonical single-agent patterns
**Answer:**
These are important design patterns used in agentic systems.

1. **ReAct:** think -> act -> observe
2. **Plan-and-Execute:** plan steps first, then perform them
3. **Reflection:** self-check before sending a final answer
4. **ReWOO:** pre-plan tool usage and variable dependencies before execution
5. **Tree Search:** explore multiple reasoning paths and choose the best one
6. **Code-Act:** write or execute small code snippets to solve a task

**Interview angle:**
The best architecture depends on the problem. A simple task may only need ReAct, while a more complex task may need planning, reflection, or branching.

---

### 18. Router pattern
**Answer:**
A router is a front-door classifier. It decides which downstream workflow or specialized model should handle an incoming request.

- **Rule-based routing:** keywords or fixed conditions
- **LLM-based routing:** uses the model to classify intent

**Example:**
- message contains "refund" -> billing workflow
- message contains "delivery delay" -> support workflow
- message is vague -> general assistant

**Why it matters:**
Routing makes systems modular and reduces prompt complexity. It also improves reliability by sending the request to the most relevant subsystem.

---

### 19. Subagents
**Answer:**
A subagent is a specialized helper agent created to handle a narrow task. The parent agent delegates work to the subagent, reviews the result, and keeps the main context clean.

**Example:**
- main support agent spawns a subagent to inspect historical deliveries and summarize the issue
- parent then uses that summary to craft a final answer

**Benefit:**
- cleaner context
- better specialization
- lower chance of task contamination

**Interview angle:**
Subagents are useful when a task is big enough that one agent would get overloaded or distracted.

---

### 20. Prompt vs context vs harness engineering
**Answer:**
These are three layers of agent design.

- **Prompt engineering:** writing the instructions the model follows
- **Context engineering:** deciding what information enters the model window at runtime
- **Harness engineering:** the surrounding software system that executes the loop safely and consistently

**Example:**
- prompt: "You are a pizza support bot"
- context: order history, previous complaint, retrieved customer notes
- harness: tool wrappers, retries, logging, timeouts, guardrails

**Interview angle:**
Most people focus on prompts, but the real production quality often comes from context and harness engineering.

---

### 21. Agent Skills
**Answer:**
Agent skills are small reusable instruction modules or guides that can be loaded only when needed. They are useful because they reduce prompt bloat while improving task-specific performance.

**Example:**
A customer support agent may load a refund-handling skill only when the user asks about billing, instead of always injecting a long refund policy into every conversation.

**Why it matters:**
- better context management
- more modular design
- less unnecessary token use

---

### 22. What changes when a new model ships?
**Answer:**
When a stronger model is released, an engineering team usually revisits the harness rather than blindly adding more prompts. Better models often need fewer rigid instructions and can handle larger context windows, but they still need evaluation and routing refinement.

Typical changes:
- remove old prompt hand-holding
- update context window strategy
- re-run evals
- simplify tool routing
- revisit safety/verification rules

**Interview angle:**
Agent systems evolve continuously. The model changes, but the operating system around it also changes.

---

### 23. Critic pattern
**Answer:**
The Critic pattern adds a second model or reviewer that checks the first agent's output before it is sent. This is especially useful for customer-facing content, where tone, factual correctness, and policy compliance matter.

**Example:**
- Agent A drafts a refund message
- Critic agent checks if the message is empathetic, compliant, and accurate
- If needed, Agent A rewrites it

**Why it matters:**
This helps catch mistakes that a single model might miss.

---

### 24. Map-Reduce pattern
**Answer:**
The Map-Reduce pattern is a distributed pattern for large-scale analysis. It breaks a task into small subproblems, solves them in parallel, and then combines the results into a final answer.

- **Map:** multiple agents handle distinct sub-tasks
- **Reduce:** one agent combines the output into a final synthesis

**Example:**
- analyze 20 store feedback reports in parallel
- reduce into one summary of issues and trends

**Interview angle:**
This pattern scales well when a task can be split into independent units.

---

### 25. Hierarchical agent pattern
**Answer:**
A hierarchical pattern uses a manager agent to divide a large problem into smaller tasks, assign them to specialized workers, and then review the results before sending a final output.

**Example:**
- manager: "Handle this delivery issue"
- billing worker: checks refund policy
- kitchen worker: checks order status and prep queue
- manager: combines both findings and replies to the customer

**Why it matters:**
This mirrors how real organizations work and helps reduce the cognitive load on one single agent.

---

## Final interview takeaway
**Use an agent when:**
- the work is dynamic
- tools are required
- the system needs reasoning and planning

**Do not use an agent when:**
- logic is obvious and deterministic
- a simple pipeline or script is enough
- correctness and cost are more important than flexibility

**Best practice:**
- start with the simplest viable architecture
- add autonomy only when the task truly needs it
- keep guardrails, evals, and verification in place
