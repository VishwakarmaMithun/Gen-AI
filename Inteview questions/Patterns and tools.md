# AI Agents & Patterns Cheat Sheet

## Quick mental model
- Tool = a structured capability the agent can call
- Tool schema = the contract for what arguments are valid
- Agent loop = reason -> choose tool -> act -> observe -> repeat
- Pattern = a strategy for decomposing or coordinating reasoning
- Error handling = what makes the system reliable, not just clever

---

## Part 2: Patterns and Tools

### 01. How would you decompose a travel-planning task across sub-agents?
**Answer:**
Decompose the task by responsibilities instead of by one giant prompt. One sub-agent can handle flight search, another hotel matching, another budget optimization, and a supervisor agent can merge the outputs into a final itinerary.

- **Flight agent:** searches flights, checks price and time constraints
- **Hotel agent:** finds matching stays and compares location/sleep quality
- **Budget agent:** ensures total trip fits constraints
- **Planner agent:** combines options and recommends the best overall plan

**Why it matters:**
Large tasks fail when one model tries to do everything alone. Decomposition reduces context overload and makes each agent more specialized and easier to debug.

**Example:**
A user asks for a 3-day trip to Paris under $900. The planner first asks about dates and budget, then assigns sub-tasks to the flight, hotel, and transport agents, and finally merges the best plan.

**Interview angle:**
Good decomposition is not about creating many agents for the sake of it. It is about dividing the problem into naturally separable decisions with clear ownership.

---

### 02. How does an agent prioritize competing goals or tasks?
**Answer:**
The agent needs an explicit priority model. It should rank goals by urgency, user preference, safety, and feasibility. A good system keeps a running objective function or priority list, then chooses the next step that maximizes success while respecting constraints.

Common priorities:
- user intent
- safety and policy
- time and cost constraints
- correctness and data freshness
- progress toward the final goal

**Why it matters:**
Without prioritization, an agent may spend time on low-value steps, loop endlessly, or ignore a critical constraint.

**Example:**
For a customer-support agent, answering a billing concern may outrank a low-priority feature question. For a travel planner, the shortest valid route may be less important than a safe, compliant booking.

**Interview angle:**
The agent is not just “thinking”; it is making trade-offs under constraints. Prioritization is one of the key skills that separates an assistant from a tool caller.

---

### 03. Compare ReAct, Plan-and-Execute, ToT, Reflexion and LLM Compiler.
**Answer:**
These are different ways to structure reasoning and action.

- **ReAct:** reason, act, observe, repeat. Simple and flexible.
- **Plan-and-Execute:** first create a plan, then execute it in stages.
- **ToT (Tree of Thought):** explore multiple reasoning branches before choosing a path.
- **Reflexion:** evaluate past work and improve based on feedback.
- **LLM Compiler:** treat tool calls and intermediate work as a compiled plan or structured execution flow.

**Why it matters:**
Each pattern is a trade-off between speed, quality, reliability, and cost.

**Example:**
- ReAct is strong for open-ended troubleshooting.
- Plan-and-Execute works well when the task is predictable but multi-step.
- ToT helps when there are several plausible solution paths.
- Reflexion helps when the system can learn from mistakes.
- LLM Compiler helps maintain structure in complex, multi-tool execution.

**Interview angle:**
The best answer is not “one is always better.” The real answer is which pattern best fits the failure modes of your task.

---

### 04. Plan-then-execute vs ReAct: which wins when?
**Answer:**
Plan-then-execute is better when the task is structured, the dependencies are known, and you want predictability. ReAct is better when the environment is dynamic and the next step depends on tool results.

- **Plan-first:** strong for travel booking, project workflows, code generation with clear steps
- **ReAct:** strong for research, debugging, tool-rich tasks, and uncertain execution paths

**Why it matters:**
A static plan can be brittle when the environment changes. ReAct adapts better, but it can also become noisy or loop.

**Example:**
Planning a wedding itinerary is better with a plan-first workflow. Investigating a failing deployment is better with ReAct because the cause is unknown at first.

**Interview angle:**
The common rule is: use plan-first for controllable tasks and ReAct for exploratory tasks.

---

### 05. Compare agent planning strategies: CoT, ToT, Go.
**Answer:**
These strategies differ in how deeply the model explores possibilities.

- **CoT (Chain-of-Thought):** linear reasoning trace, one path at a time
- **ToT (Tree of Thought):** branches into multiple candidate paths and evaluates them
- **Go (Graph of Thought):** represents reasoning as a graph of intermediate states, allowing more flexible reuse and composition

**Why it matters:**
The more branching you allow, the more compute and complexity you incur. That can improve performance on harder tasks but also increases cost and latency.

**Example:**
If you are solving a logic puzzle, ToT or Go might help. If you are summarizing a document, CoT is usually enough.

**Interview angle:**
Reasoning strategies are a cost-performance trade-off. A simple task does not need a large reasoning tree.

---

### 06. Why does Chain-of-Thought matter in agentic applications?
**Answer:**
CoT makes the model show step-by-step reasoning patterns that can improve problem solving on complex tasks. In agentic systems, it helps the agent break a larger goal into steps, decide which tool to use, and justify intermediate decisions.

**Why it matters:**
Without explicit reasoning steps, the model may jump to a plausible answer without checking the real state. In agent loops, this often leads to wrong tool calls, unsupported claims, or shallow completion.

**Example:**
For a customer issue, the model may reason: “I need user history, ticket status, and policy information before giving a refund decision.”

**Interview angle:**
CoT is useful when the task requires decomposition and multi-step reasoning. It is not a guarantee of correctness, but it often improves transparency and planning quality.

---

### 07. What are the trade-offs of CoT inside an agent loop?
**Answer:**
CoT can help the model reason more clearly, but it also increases token usage, latency, and sometimes hidden reasoning drift. In a loop, too much internal reasoning can become expensive and noisy.

**Pros:**
- better decomposition
- improved multi-step planning
- more explicit tool selection

**Cons:**
- higher latency
- more tokens consumed
- can reinforce wrong assumptions
- may produce verbose reasoning that is not useful for the final answer

**Why it matters:**
The agent has to spend compute on both reasoning and action. If reasoning becomes unbounded, the system becomes slower and more expensive.

**Interview angle:**
The best approach is often to use concise reasoning, strong prompts, and structured output instead of free-form long logs.

---

### 08. How does self-consistency prompting improve reasoning?
**Answer:**
Self-consistency asks the model to generate multiple reasoning paths or answers and then aggregate them. This is often more robust than taking the first answer because it reduces the risk of overfitting to one flawed reasoning chain.

**Why it matters:**
Many hard tasks have several plausible but incorrect intermediate paths. Sampling multiple responses helps identify the most consistent answer.

**Example:**
In a classification task, the model may produce three different reasoning traces for the same question. Choosing the answer that appears most often across them is often more reliable than trusting the first one.

**Interview angle:**
Self-consistency is essentially a voting scheme for reasoning quality. It is powerful, but it increases cost and latency.

---

### 09. When is tree-of-thought's extra cost justified?
**Answer:**
ToT is justified when the problem has branching uncertainty and the cost of a wrong first path is high. It is useful for difficult planning, puzzle-solving, and complex decision-making with several plausible directions.

**Why it matters:**
Normal linear reasoning may choose a path too early. ToT allows the agent to compare alternatives before committing.

**Example:**
A scheduling agent trying to optimize a 7-day team calendar may benefit from exploring multiple feasible schedules before choosing the best one.

**Interview angle:**
ToT is most valuable when the task is expensive to get wrong and a small amount of deeper search yields major gains.

---

### 10. When do reflection loops actually help, and what do they cost?
**Answer:**
Reflection helps when the task is difficult enough that the model can learn from its errors. A reflection loop asks: “What went wrong? What can I do better next time?”

**When it helps:**
- the task involves multiple steps
- early mistakes are detectable
- there is a clear success metric

**When it hurts:**
- trivial or low-risk tasks
- repeated failures with no new information
- cases where the model keeps “rethinking” without learning

**Why it matters:**
Reflection adds a second-order loop: the model reviews its previous path and tries to improve. This improves quality, but adds time and token cost.

**Interview angle:**
Reflection is valuable only when it creates actionable corrections, not just more verbosity.

---

### 11. A sub-agent is wrong and reflection can't fix it. What now?
**Answer:**
When reflection fails, the real fix is often to improve the task contract or the control structure, not to ask the same model to “think harder.” You may need narrower scope, better tools, stronger verification, or a different sub-agent responsibility.

Possible fixes:
- give the sub-agent a clearer objective
- add a validator or critic agent
- constrain the tool usage
- split the problem into smaller units
- replace the failing agent with a deterministic function when appropriate

**Why it matters:**
A poorly scoped sub-agent can keep producing low-quality outputs even under reflection. In such cases, system architecture matters more than prompt quality.

**Interview angle:**
When the underlying task definition is flawed, more reflection usually just produces more confident nonsense.

---

### 12. Reasoning model vs fast model inside an agent loop: when each?
**Answer:**
Use a strong reasoning model for planning, hard judgment, or high-risk decisions. Use a fast model for low-cost steps like routing, summarization, or simple classification.

**Why it matters:**
A large reasoning model can be expensive. The system should use it only where deeper reasoning yields value.

**Example:**
- fast model: decide which tool to call among a few obvious options
- reasoning model: decide whether the user should receive a refund or escalation

**Interview angle:**
The best agent loop is not always one model. A common pattern is a hybrid system: cheap models do structure and routing, expensive models do decisive reasoning.

---

### 13. How should an agent allocate reasoning effort across steps?
**Answer:**
Reasoning effort should match impact. Spend more on steps that affect the final outcome, and spend less on routine steps. The agent should focus its compute where uncertainty is high or where decision quality matters most.

**Why it matters:**
A model does not need deep reasoning for every action. It should reason more before critical tool calls and less before low-risk actions.

**Example:**
Before making a payment or approving a refund, the model should do careful reasoning. Before a simple retrieval call or context lookup, a lighter step is enough.

**Interview angle:**
This is the “thinking budget” problem. Efficient agents ration reasoning like a system designer, not a casual user.

---

### 14. What do you do with the model's reasoning between tool calls?
**Answer:**
Reasoning between tool calls should be concise, structured, and directly useful for the next decision. It should not be treated as a long free-form monologue unless the task truly needs it.

Good practices:
- summarize the current state
- note what information is still missing
- state the next action clearly
- avoid huge reasoning traces in the conversation history

**Why it matters:**
Tool-call loops accumulate context quickly. Too much reasoning history can waste tokens and confuse the model.

**Example:**
Instead of a huge thought dump, the agent should say: “I have the order ID and current status. I still need payment history to decide whether to refund or escalate.”

**Interview angle:**
The reasoning should be operational, not ornamental. It should help the next tool call, not just impress a human reader.

---

### 15. How does inference-time compute scaling change agent design?
**Answer:**
More inference-time compute allows the agent to spend more effort on planning, self-checking, search, or multiple candidate reasoning paths. This changes architecture because the system can become more careful and more deliberate.

**Why it matters:**
The same model can behave very differently depending on how much compute is allocated per step. More compute often improves performance on hard tasks without changing the underlying model.

**Example:**
A coding agent that explores several implementation options before patching may outperform a single-pass agent on a tricky bug fix, but at a higher cost.

**Interview angle:**
Inference-time scaling turns reasoning into a resource management problem: scale the compute to the complexity of the task.

---

### 16. Your long-running agent drifts onto the wrong task. Fix it.
**Answer:**
Task drift happens when the agent loses track of the original objective or gets distracted by irrelevant tool results. The fix is to enforce a clear objective, provide bounded memory, and add progress checks.

Useful controls:
- store the original user goal in state
- summarize progress every few steps
- inject a “return to goal” instruction when drift is detected
- block unrelated tool calls unless they directly support the goal

**Why it matters:**
Long-running agents often accumulate too much context. Without constraints, they can wander into unrelated topics or low-value branches.

**Example:**
A trip planner begins researching restaurants when the user asked for a flight-only itinerary. A task guard should redirect it back to the original objective.

**Interview angle:**
Goal anchoring is a fundamental requirement for resilient agents. Without it, the system behaves like a confused generalist.

---

### 17. Your agent loops or gives up too early. Diagnose both.
**Answer:**
Looping happens when the agent keeps retrying the same action, revisiting dead ends, or failing to observe the result correctly. Giving up too early happens when the system treats ambiguity as failure and stops before a useful tool or alternative path is explored.

**How to diagnose:**
- inspect the tool-call pattern
- check whether the same action repeats without new information
- review if the failure signal is too strict or too weak
- measure whether the system is getting fresh observations or repeating stale context

**Why it matters:**
Both failure modes are common in agent loops. They often stem from poor stopping criteria, weak tool definitions, or insufficient state tracking.

**Example:**
An agent that retries the same API call after a 401 error without refreshing credentials is looping. An agent that stops after one failed search without trying synonyms is giving up too early.

**Interview angle:**
Good agent systems are highly observable. If you cannot inspect loops and stop conditions, you cannot fix them reliably.

---

### 18. How does tool calling work mechanically, end to end?
**Answer:**
Tool calling is a structured execution path between the model and the system. The model decides which tool to call, passes valid arguments, receives a result, and incorporates that result into the next reasoning step.

End-to-end flow:
1. model reads user request and current context
2. model identifies relevant tool and arguments
3. tool schema validates the request
4. runtime executes the tool
5. result is returned as structured output
6. model reasons about the result and decides next step

**Why it matters:**
Tool calling is where the model stops being a text generator and becomes a decision-maker that interacts with software systems.

**Example:**
A weather assistant calls get_weather(city="Paris", date="2026-11-15"). The tool returns structured data like temperature and precipitation. The model uses that to answer the user.

**Interview angle:**
The mechanics matter because they determine reliability. If the interface is weak, the model’s reasoning quality becomes irrelevant.

---

### 19. “The model executes the tool.” What is wrong with that?
**Answer:**
This statement is misleading. The model does not directly execute the tool in the runtime sense. The application layer, orchestrator, or function runner executes the tool. The model only produces a tool call request, which the system validates and invokes.

**Why it matters:**
This distinction is critical for safety, observability, and debugging. In real systems, the runtime enforces permissions, schema validation, and execution boundaries.

**Example:**
The model says “call refund_customer(id=123)”, but a backend service actually invokes the refund API. The model never reaches the internal payment system directly.

**Interview angle:**
This is a key architectural truth: the model is a planner and decision-maker, while the runtime is the executor.

---

### 20. Parallel tool calls vs tool-choice forcing: when each?
**Answer:**
Parallel tool calls let the agent fetch multiple independent pieces of information at once. Tool-choice forcing restricts the model to a specific tool or a specific set of tools for a step.

Use parallel calls when:
- inputs are independent
- the task benefits from a wider information search
- the context can be merged cleanly

Use tool-choice forcing when:
- you need deterministic routing
- only one tool is valid at that step
- you want to reduce model uncertainty and costs

**Why it matters:**
Parallelization improves throughput but increases complexity in aggregation. Forced tool choice improves reliability but reduces flexibility.

**Example:**
An agent checking a customer issue may call get_order_status and get_recent_tickets in parallel. A refund approval flow may force the tool choice to approval_service once the policy check is complete.

**Interview angle:**
This is a classic trade-off between flexibility and control. Use the more constrained option when correctness matters more than autonomy.

---

### 21. What makes a good tool definition? Give concrete rules.
**Answer:**
A good tool definition is clear, narrow, and expressive. It tells the model exactly what the tool does, what arguments it expects, and what kind of output it returns.

Concrete rules:
- use clear names and verbs
- describe the purpose in one sentence
- specify required vs optional arguments
- define schema types precisely
- document output shape clearly
- keep the tool narrowly scoped
- avoid overloading one tool with too many jobs

**Why it matters:**
A bad tool definition makes the model guess. A good one makes the model less likely to misuse the tool and more likely to call it correctly.

**Example:**
Instead of a vague tool called “manage_order,” use tools like get_order_status(order_id), update_shipping_address(order_id, address), and cancel_order(order_id, reason).

**Interview angle:**
Tool design is a product design problem. The interface is the model’s operating system.

---

### 22. What does strict mode on a tool schema guarantee, and not?
**Answer:**
Strict mode guarantees that the tool call follows the defined schema and types. It reduces malformed arguments and makes calls more predictable. It does not guarantee that the model chooses the correct tool, that the business logic is sound, or that the tool result is semantically correct.

**What it guarantees:**
- correct argument types
- required fields are present
- invalid tool calls are rejected early

**What it does not guarantee:**
- correctness of the user’s intention
- safety of the chosen action
- soundness of the returned business data

**Why it matters:**
Schema validation is a safety net, not a replacement for reasoning or business rules.

**Interview angle:**
Strict mode is necessary but not sufficient. Good tool design also needs policy checks and validation logic.

---

### 23. How should tool errors be surfaced back to the model?
**Answer:**
Tool errors should be surfaced as structured, actionable feedback, not as a vague “something failed.” The model needs enough information to decide whether to retry, switch tools, ask for clarification, or escalate.

Good error format:
- error type
- tool name
- argument summary
- status code or reason
- suggested next action

**Why it matters:**
If errors are hidden or cryptic, the model will guess and may continue down a bad path. Good error propagation makes the loop resilient.

**Example:**
Instead of “Failed,” return: “Authentication failed for get_customer_profile: token expired; retry after refresh or request re-authentication.”

**Interview angle:**
The agent needs feedback loops, not silence. Error handling is part of the intelligence.

---

### 24. Consolidated vs granular tools: how do you decide?
**Answer:**
A consolidated tool is broad and convenient; a granular tool is specialized and precise. Consolidation reduces decision overhead but can hide complexity and increase misuse risk. Granularity increases control but may make the agent do more routing work.

Choose granular tools when:
- the tool does a well-defined action
- you need controlled permissions or validation
- different branches require different behavior

Choose consolidated tools when:
- the task is simple and the tool is low-risk
- the model benefits from fewer tool choices
- you want less orchestration complexity

**Why it matters:**
The tool interface shapes the model’s behavior. Too much power in one tool creates mistakes; too much fragmentation creates overhead.

**Interview angle:**
The correct trade-off depends on the real risk and complexity of the operation.

---

### 25. How do you make tool outputs token-efficient?
**Answer:**
A tool output should be compact, structured, and relevant. Do not return everything; return only the fields the model needs to continue. Use short summaries, structured JSON, and filtering around the actual decision point.

Good practices:
- return only essential fields
- truncate large data blocks
- summarize log-heavy outputs
- use nested structured objects instead of raw text dumps
- include useful metadata like IDs and error codes

**Why it matters:**
Model context is costly. If every tool call returns huge blobs, the agent spends too much time and money on context handling instead of decision-making.

**Example:**
Instead of returning an entire 50KB API response, return only the fields needed for the next action: order status, ETA, and failure reason.

**Interview angle:**
Efficient tools are part of efficient agents. The best tool output is the smallest result that still preserves the decision signal.

---

## Final takeaways
- The most important part of agent design is not the model alone; it is the interaction pattern.
- A strong tool layer makes an agent reliable, cheap, and controllable.
- Good orchestration depends on clear goals, structured outputs, and exit conditions.
- Agents fail most often from poor architecture, not from a single bad prompt.

This is the core lesson: an agent is not “just a model with tools.” It is a control system with memory, tools, feedback loops, and safety boundaries.
