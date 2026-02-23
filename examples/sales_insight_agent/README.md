# Sales Insight Agent

This example shows how basic business analytics logic can be wrapped into a Bindu-powered agent.

The idea is simple: take structured sales data, compute useful metrics, and expose the results through an agent interface.

---

## What This Agent Does

The Sales Insight Agent:

- Reads a structured sales CSV file  
- Calculates total revenue  
- Identifies the top-performing products  
- Counts total transactions  
- Returns structured JSON insights  

Even though the logic is straightforward, the structure makes it agent-ready and easy to extend.

---

## Why This Example

Bindu is about turning AI capabilities into interoperable microservices.

With this example, the goal is to explore how traditional data processing tasks can:

- Be structured as reusable tools  
- Be exposed via an agent  
- Be extended into paid or orchestrated workflows  

It’s a small step toward building data-aware agents inside the Bindu ecosystem.

---

## Running the Agent

From the root of the repository:

```bash
uv run examples/sales_insight_agent/sales_agent.py
