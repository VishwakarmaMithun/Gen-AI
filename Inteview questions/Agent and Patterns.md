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
- **Chain:** Always runs the same path: A -> B -> C.
- **Workflow:** Follows developer-defined branches and rules.
- **Agent:** Chooses tools, gathers missing info, and decides when the task is done.

**Example:**
- Chain: send a standard confirmation email
- Workflow: if refund requested, route to billing; otherwise continue shipping
- Agent: customer says pizza is cold -> check order + kitchen queue -> decide refund or replacement

---

### 02. When should you NOT build an agent?
**Answer:**
- Use a normal script when the task is predictable, cheap, and deterministic.
- Agents are slower, more expensive, and less reliable for simple logic.

**Example:**
- Do not build an autonomous agent for a 7% tax calculation; use code instead.

---

### 03. What is the core agent loop?
**Answer:**
1. Input
2. Reason
3. Act
4. Observe
5. Repeat until done or limited

**Stop conditions:**
- final answer produced
- max tool calls reached
- timeout
- repeated failure / no progress

**Example:**
- User asks: "Where is order #405?"
- Agent calls: get_order_status(405)
- Result: "Out for delivery in 5 minutes"

---

### 04. What is the autonomy spectrum?
**Answer:**
- Zero autonomy: single fixed prompt
- Low autonomy: small tool usage
- Medium autonomy: multi-step decisions
- High autonomy: acts independently with guardrails
- Full autonomy: near-complete control, high risk

**Rule:**
- Keep autonomy as low as possible while still solving the task.

---

### 05. What is ReAct?
**Answer:**
- Reason -> Act -> Observe
- The model thinks before calling a tool and then reads the result.

**Failure modes:**
- infinite loops
- repeated wrong tool calls
- memory bloat

---

### 06. Tool call vs direct answer
**Answer:**
- Use a tool when the answer needs real-time data, private info, or a live calculation.
- Use knowledge when the answer is static and already known.

**Example:**
- "What ingredients are in Margherita pizza?" -> answer from memory
- "Is order #405 out for delivery?" -> use tool

---

### 07. Reactive vs proactive agent
**Answer:**
- Reactive: waits for a prompt
- Proactive: monitors events and acts without being asked

**Example:**
- Reactive: answers customer question
- Proactive: notices a driver issue and sends a discount before the customer complains

---

### 08. Stateless vs stateful agent
**Answer:**
- Stateless: loses context between turns
- Stateful: remembers chat history, preferences, and ticket state

**Key point:**
- For support bots, statefulness is usually required.

---

### 09. Agent state vs memory
**Answer:**
- Agent state = current session data
- Memory = long-term retention across sessions

**Example:**
- State: "I verified this customer’s phone number in this chat"
- Memory: "This customer is allergic to mushrooms"

---

### 10. How do you set termination conditions?
**Answer:**
- max tool calls
- max time limit
- stop when repeated action adds no value
- require human approval for high-risk actions

---

### 11. Why do agent errors compound?
**Answer:**
If each step succeeds with probability 0.90, then 5 steps succeed with:

$$0.90^5 \approx 59\%$$

and 10 steps succeed with:

$$0.90^{10} \approx 35\%$$

**Takeaway:**
- errors compound fast
- verification and retries matter

---

### 12. What makes a good system prompt?
**Answer:**
- role
- rules
- constraints
- context
- response format

**Example:**
- "You are a pizza support agent. Never approve a refund above $50 without manager approval."

---

### 13. Tool call vs function call
**Answer:**
- Workflow: code explicitly calls function X
- Agent: LLM decides which tool and parameters to use based on context

---

### 14. Three anti-patterns
**Answer:**
1. Too many tools
2. Using an agent for trivial logic
3. No stop conditions or guardrails

**Risk:**
- wrong actions
- runaway loops
- risky or costly decisions

---

## Part 2: Harness & Patterns

### 15. Model vs harness
**Model:** reasoning + language

**Harness:** loop + tools + retries + memory + sandbox + security + monitoring

---

### 16. Which matters more: model or harness?
**Answer:**
- For production coding agents, the harness often matters more.
- Good scaffolding makes a weaker model usable.

---

### 17. Six canonical single-agent patterns
1. ReAct: think -> act -> observe
2. Plan-and-Execute: plan first, then execute
3. Reflection: self-review before final answer
4. ReWOO: plan tool usage in one pass, then execute
5. Tree Search: explore multiple reasoning branches
6. Code-Act: write and run small scripts to solve problems

---

### 18. Router pattern
**Answer:**
- A classifier routes requests to the right specialist flow.
- Rule-based routing: simple keyword logic
- LLM-based routing: better for nuanced tasks

---

### 19. Subagents
**Answer:**
- A manager agent delegates complex work to smaller specialized agents.
- Useful when a task is too large for one context window.

**Example:**
- main support agent spawns a delivery-log subagent to summarize old complaints

---

### 20. Prompt vs context vs harness engineering
**Answer:**
- Prompt engineering: static instructions
- Context engineering: dynamic memory and retrieval
- Harness engineering: runtime loop, tool execution, safety

---

### 21. Agent Skills
**Answer:**
- Small reusable instruction modules loaded only when needed
- Better than dumping huge context into every agent run

---

### 22. What changes when a new model ships?
**Answer:**
- simplify prompt hand-holding
- update context strategy
- re-run evaluations
- tighten / simplify tool routing

---

### 23. Critic pattern
**Answer:**
- One agent writes
- Another checks tone, facts, and policy compliance
- Great for customer-facing outputs

---

### 24. Map-Reduce pattern
**Answer:**
- Map: split a large task across worker agents
- Reduce: combine findings into one final answer

**Example:**
- analyze 20 store feedback reports in parallel, then summarize in one report

---

### 25. Hierarchical agent pattern
**Answer:**
- manager agent breaks work into sub-tasks
- specialists handle domain-specific work
- manager reviews final output

**Example:**
- billing agent + kitchen agent + manager review

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
