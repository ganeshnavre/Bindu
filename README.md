<div align="center" id="top">
  <a href="https://getbindu.com">
    <picture>
      <img src="assets/bindu.png" alt="Bindu" width="300">
    </picture>
  </a>
</div>

<p align="center">
  <em>The identity, communication & payments layer for AI agents</em>
</p>

<p align="center">
  <a href="README.md">🇬🇧 English</a> •
  <a href="README.de.md">🇩🇪 Deutsch</a> •
  <a href="README.es.md">🇪🇸 Español</a> •
  <a href="README.fr.md">🇫🇷 Français</a> •
  <a href="README.hi.md">🇮🇳 हिंदी</a> •
  <a href="README.bn.md">🇮🇳 বাংলা</a> •
  <a href="README.zh.md">🇨🇳 中文</a> •
  <a href="README.nl.md">🇳🇱 Nederlands</a> •
  <a href="README.ta.md">🇮🇳 தமிழ்</a>
</p>

<p align="center">
  <a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/license-Apache%202.0-blue.svg" alt="License"></a>
  <a href="https://hits.sh/github.com/Saptha-me/Bindu.svg"><img src="https://hits.sh/github.com/Saptha-me/Bindu.svg" alt="Hits"></a>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.12+-blue.svg" alt="Python Version"></a>
  <a href="https://pepy.tech/projects/bindu"><img src="https://static.pepy.tech/personalized-badge/bindu?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads" alt="PyPI Downloads"></a>
  <a href="https://pypi.org/project/bindu/"><img src="https://img.shields.io/pypi/v/bindu.svg" alt="PyPI version"></a>
  <a href="https://pypi.org/project/bindu/"><img src="https://img.shields.io/pypi/dm/bindu" alt="PyPI Downloads"></a>
  <a href="https://coveralls.io/github/Saptha-me/Bindu?branch=v0.3.18"><img src="https://coveralls.io/repos/github/Saptha-me/Bindu/badge.svg?branch=v0.3.18" alt="Coverage"></a>
  <a href="https://github.com/getbindu/Bindu/actions/workflows/release.yml"><img src="https://github.com/getbindu/Bindu/actions/workflows/release.yml/badge.svg" alt="Tests"></a>
  <a href="https://discord.gg/3w5zuYUuwt"><img src="https://img.shields.io/badge/Join%20Discord-7289DA?logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://github.com/getbindu/Bindu/graphs/contributors"><img src="https://img.shields.io/github/contributors/getbindu/Bindu" alt="Contributors"></a>
</p>

---

**Bindu** (read: _binduu_) is an operating layer for AI agents that provides identity, communication, and payment capabilities. It delivers a production-ready service with a convenient API to connect, authenticate, and orchestrate agents across distributed systems using open protocols: **A2A**, **AP2**, and **X402**.

Built with a distributed architecture (Task Manager, scheduler, storage), Bindu makes it fast to develop and easy to integrate with any AI framework. Transform any agent framework into a fully interoperable service for communication, collaboration, and commerce in the Internet of Agents.

<p align="center">
  <strong>🌟 <a href="https://bindus.directory">Register your agent</a> • 🌻 <a href="https://docs.getbindu.com">Documentation</a> • 💬 <a href="https://discord.gg/3w5zuYUuwt">Discord Community</a></strong>
</p>


---

<br/>

## 🎥 Watch Bindu in Action

<div align="center">
  <a href="https://www.youtube.com/watch?v=qppafMuw_KI" target="_blank">
    <img src="https://img.youtube.com/vi/qppafMuw_KI/maxresdefault.jpg" alt="Bindu Demo" width="640" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" />
  </a>
</div>


## 📋 Prerequisites

Before installing Bindu, ensure you have:

- **Python 3.12 or higher** - [Download here](https://www.python.org/downloads/)
- **UV package manager** - [Installation guide](https://github.com/astral-sh/uv)
- **Note**: You will need an OPENROUTER_API_KEY (or OpenAI key) set in your environment variables to run the agent successfully.You can use free open router models for testing.


### Verify Your Setup

```bash
# Check Python version
uv run python --version  # Should show 3.12 or higher

# Check UV installation
uv --version
```

---

<br/>

## 📦 Installation
<details>
<summary><b>Users note (Git & GitHub Desktop)</b></summary>

On some Windows systems, git may not be recognized in Command Prompt even after installation due to PATH configuration issues.

If you face this issue, you can use *GitHub Desktop* as an alternative:

1. Install GitHub Desktop from https://desktop.github.com/
2. Sign in with your GitHub account
3. Clone the repository using the repository URL:
   https://github.com/getbindu/Bindu.git

GitHub Desktop allows you to clone, manage branches, commit changes, and open pull requests without using the command line.

</details>

```bash
# Install Bindu
uv add bindu

# For development (if contributing to Bindu)
# Create and activate virtual environment
uv venv --python 3.12.9
source .venv/bin/activate  # On macOS/Linux
# .venv\Scripts\activate  # On Windows

uv sync --dev
```

<details>
<summary><b>Common Installation Issues</b> (click to expand)</summary>

<br/>

| Issue | Solution |
|-------|----------|
| `uv: command not found` | Restart your terminal after installing UV. On Windows, use PowerShell |
| `Python version not supported` | Install Python 3.12+ from [python.org](https://www.python.org/downloads/) |
| Virtual environment not activating (Windows) | Use PowerShell and run `.venv\Scripts\activate` |
| `Microsoft Visual C++ required` | Download [Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) |
| `ModuleNotFoundError` | Activate venv and run `uv sync --dev` |

</details>

---

<br/>

## 🚀 Quick Start

### Option 1: Using Cookiecutter (Recommended)

**Time to first agent: ~2 minutes ⏱️**

```bash
# Install cookiecutter
uv add cookiecutter

# Create your Bindu agent
uvx cookiecutter https://github.com/getbindu/create-bindu-agent.git
```

## 🎥 Create Production Ready Agent in Minutes

<div align="center">
  <a href="https://youtu.be/obY1bGOoWG8?si=uEeDb0XWrtYOQTL7" target="_blank">
    <img src="https://img.youtube.com/vi/obY1bGOoWG8/maxresdefault.jpg" alt="Bindu Demo" width="640" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" />
  </a>
</div>

That's it! Your local agent becomes a live, secure, discoverable service. [Learn more →](https://docs.getbindu.com/bindu/create-bindu-agent/overview)

> **💡 Pro Tip:** Agents created with cookiecutter include GitHub Actions that automatically register your agent in the [Bindu Directory](https://bindus.directory) when you push to your repository. No manual registration needed!

### Option 2: Manual Setup

Create your agent script `my_agent.py`:

```python
from bindu.penguin.bindufy import bindufy
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.openai import OpenAIChat

# Define your agent
agent = Agent(
    instructions="You are a research assistant that finds and summarizes information.",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
)

# Configuration
config = {
    "author": "your.email@example.com",
    "name": "research_agent",
    "description": "A research assistant agent",
    "deployment": {"url": "http://localhost:3773", "expose": True},
    "skills": ["skills/question-answering", "skills/pdf-processing"]
}

# Handler function
def handler(messages: list[dict[str, str]]):
    """Process messages and return agent response.

    Args:
        messages: List of message dictionaries containing conversation history

    Returns:
        Agent response result
    """
    result = agent.run(input=messages)
    return result

# Bindu-fy it
bindufy(config, handler)

# if you want to use tunnel to expose your agent to the internet, use the following command
#bindufy(config, handler, launch=True)
```

![Sample Agent](assets/agno-simple.png)

Your agent is now live at `http://localhost:3773` and ready to communicate with other agents.

---
### Beginner: Zero-Config Local Agent (Recommended for First-Time Users)

If you want to try Bindu without setting up Postgres, Redis, or any cloud services,
this zero-config example is the fastest way to get started.

It runs entirely locally using in-memory storage and scheduler.

```bash
python examples/beginner_zero_config_agent.py
```


### Option 3: Minimal Echo Agent (Testing)

<details>
<summary><b>View minimal example</b> (click to expand)</summary>

Smallest possible working agent:

```python
from bindu.penguin.bindufy import bindufy

def handler(messages):
    return [{"role": "assistant", "content": messages[-1]["content"]}]

config = {
    "author": "your.email@example.com",
    "name": "echo_agent",
    "description": "A basic echo agent for quick testing.",
    "deployment": {"url": "http://localhost:3773", "expose": True},
    "skills": []
}

bindufy(config, handler)

# if you want to use tunnel to expose your agent to the internet, use the following command
#bindufy(config, handler, launch=True)
```

**Run and test:**

```bash
# Start the agent
python examples/echo_agent.py
```

</details>

<details>
<summary><b>Test the agent with curl</b> (click to expand)</summary>

<br/>

Input:
```bash
curl --location 'http://localhost:3773/' \
--header 'Content-Type: application/json' \
--data '{
    "jsonrpc": "2.0",
    "method": "message/send",
    "params": {
        "message": {
            "role": "user",
            "parts": [
                {
                    "kind": "text",
                    "text": "Quote"
                }
            ],
            "kind": "message",
            "messageId": "550e8400-e29b-41d4-a716-446655440038",
            "contextId": "550e8400-e29b-41d4-a716-446655440038",
            "taskId": "550e8400-e29b-41d4-a716-446655440300"
        },
        "configuration": {
            "acceptedOutputModes": [
                "application/json"
            ]
        }
    },
    "id": "550e8400-e29b-41d4-a716-446655440024"
}'
```

Output:
```bash
{
    "jsonrpc": "2.0",
    "id": "550e8400-e29b-41d4-a716-446655440024",
    "result": {
        "id": "550e8400-e29b-41d4-a716-446655440301",
        "context_id": "550e8400-e29b-41d4-a716-446655440038",
        "kind": "task",
        "status": {
            "state": "submitted",
            "timestamp": "2025-12-16T17:10:32.116980+00:00"
        },
        "history": [
            {
                "message_id": "550e8400-e29b-41d4-a716-446655440038",
                "context_id": "550e8400-e29b-41d4-a716-446655440038",
                "task_id": "550e8400-e29b-41d4-a716-446655440301",
                "kind": "message",
                "parts": [
                    {
                        "kind": "text",
                        "text": "Quote"
                    }
                ],
                "role": "user"
            }
        ]
    }
}
```

Check the status of the task
```bash
curl --location 'http://localhost:3773/' \
--header 'Content-Type: application/json' \
--data '{
    "jsonrpc": "2.0",
    "method": "tasks/get",
    "params": {
        "taskId": "550e8400-e29b-41d4-a716-446655440301"
    },
    "id": "550e8400-e29b-41d4-a716-446655440025"
}'
```

Output:
```bash
{
    "jsonrpc": "2.0",
    "id": "550e8400-e29b-41d4-a716-446655440025",
    "result": {
        "id": "550e8400-e29b-41d4-a716-446655440301",
        "context_id": "550e8400-e29b-41d4-a716-446655440038",
        "kind": "task",
        "status": {
            "state": "completed",
            "timestamp": "2025-12-16T17:10:32.122360+00:00"
        },
        "history": [
            {
                "message_id": "550e8400-e29b-41d4-a716-446655440038",
                "context_id": "550e8400-e29b-41d4-a716-446655440038",
                "task_id": "550e8400-e29b-41d4-a716-446655440301",
                "kind": "message",
                "parts": [
                    {
                        "kind": "text",
                        "text": "Quote"
                    }
                ],
                "role": "user"
            },
            {
                "role": "assistant",
                "parts": [
                    {
                        "kind": "text",
                        "text": "Quote"
                    }
                ],
                "kind": "message",
                "message_id": "2f2c1a8e-68fa-4bb7-91c2-eac223e6650b",
                "task_id": "550e8400-e29b-41d4-a716-446655440301",
                "context_id": "550e8400-e29b-41d4-a716-446655440038"
            }
        ],
        "artifacts": [
            {
                "artifact_id": "22ac0080-804e-4ff6-b01c-77e6b5aea7e8",
                "name": "result",
                "parts": [
                    {
                        "kind": "text",
                        "text": "Quote",
                        "metadata": {
                            "did.message.signature": "5opJuKrBDW4woezujm88FzTqRDWAB62qD3wxKz96Bt2izfuzsneo3zY7yqHnV77cq3BDKepdcro2puiGTVAB52qf"  # pragma: allowlist secret
                        }
                    }
                ]
            }
        ]
    }
}
```

</details>

---

<br/>

## 🔐 Authentication

Bindu uses **Ory Hydra** OAuth2 for secure API access. Authentication is **optional** - perfect for development without auth.

**Quick Setup:**
```bash
AUTH__ENABLED=true
AUTH__PROVIDER=hydra
HYDRA__ADMIN_URL=https://hydra-admin.getbindu.com
HYDRA__PUBLIC_URL=https://hydra.getbindu.com
```

**Get Access Token:**
```bash
curl -X POST https://hydra.getbindu.com/oauth2/token \
  -d "grant_type=client_credentials" \
  -d "client_id=did:bindu:<YOUR_AGENT_DID>" \
  -d "client_secret=<YOUR_CLIENT_SECRET>"
```

📖 **[Full Authentication Guide →](docs/AUTHENTICATION.md)**

---

<br/>

## 💰 Payment Integration (X402)

Monetize your AI agents with **X402 payment protocol** - accept USDC payments on Base blockchain before executing protected methods.

**Quick Setup:**
```python
config = {
    "execution_cost": {
        "amount": "$0.0001",
        "token": "USDC",
        "network": "base-sepolia",  # or "base" for production
        "pay_to_address": "0xYourWalletAddress",
        "protected_methods": ["message/send"]
    }
}
```

**Payment Flow:**
1. User initiates payment session → Gets browser URL
2. User pays with MetaMask/Coinbase Wallet → Blockchain verification
3. User receives payment token → Can call protected methods

<img src="assets/payment-required-base.png" alt="Payment Screen" width="400" />

📖 **[Full Payment Guide →](docs/PAYMENT.md)** - Wallet setup, testing, production deployment

---

<br/>

## 💾 PostgreSQL Storage

Persistent storage for production deployments. **Optional** - InMemoryStorage used by default.

**Quick Setup:**
```bash
STORAGE_TYPE=postgres
DATABASE_URL=postgresql+asyncpg://<user>:<password>@<host>:<port>/<database>?ssl=require
```

**Features:**
- Task history with JSONB
- Context management
- Automatic migrations
- Task-first pattern support

📖 **[Full Storage Guide →](docs/STORAGE.md)** - Setup, cloud providers, migrations

---

<br/>

## 📋 Redis Scheduler

Distributed task scheduling for multi-worker deployments. **Optional** - InMemoryScheduler used by default.

**Quick Setup:**
```bash
SCHEDULER_TYPE=redis
REDIS_URL=rediss://default:<password>@<host>:<port>
```

**Features:**
- Distributed queuing
- Blocking operations (no polling)
- Multi-worker support
- High throughput

📖 **[Full Scheduler Guide →](docs/SCHEDULER.md)** - Multi-worker setup, cloud Redis, monitoring

---

<br/>

## [Retry Mechanism](https://docs.getbindu.com/bindu/learn/retry/overview)

> Automatic retry logic with exponential backoff for resilient Bindu agents

Bindu includes a built-in Tenacity-based retry mechanism to handle transient failures gracefully across workers, storage, schedulers, and API calls. This ensures your agents remain resilient in production environments.


### ⚙️ Default Settings

If not configured, Bindu uses these defaults:

| Operation Type | Max Attempts | Min Wait | Max Wait |
| -------------- | ------------ | -------- | -------- |
| Worker         | 3            | 1.0s     | 10.0s    |
| Storage        | 5            | 0.5s     | 5.0s     |
| Scheduler      | 3            | 1.0s     | 8.0s     |
| API            | 4            | 1.0s     | 15.0s    |

---

<br/>

## [Sentry Integration](https://docs.getbindu.com/bindu/learn/sentry/overview)

> Real-time error tracking and performance monitoring for Bindu agents

Sentry is a real-time error tracking and performance monitoring platform that helps you identify, diagnose, and fix issues in production. Bindu includes built-in Sentry integration to provide comprehensive observability for your AI agents.

### ⚙️ Configuration

<details>
<summary><b>View configuration example</b> (click to expand)</summary>

```bash
#You can find in the env.example file
# Sentry Error Tracking (Optional)
# Enable error tracking and performance monitoring
SENTRY_ENABLED=true
SENTRY_DSN=https://<key>@<org-id>.ingest.sentry.io/<project-id>
```

Configure Sentry directly in your `bindufy()` config:

```python
config = {
    "author": "gaurikasethi88@gmail.com",
    "name": "echo_agent",
    "description": "A basic echo agent for quick testing.",
    "deployment": {"url": "http://localhost:3773", "expose": True},
    "skills": []
}

def handler(messages):
    # Your agent logic
    pass

bindufy(config, handler)
```

</details>

### 🚀 Getting Started

1. **Create Sentry Account**: Sign up at [sentry.io](https://sentry.io)
2. **Get Your DSN**: Copy from project settings
3. **Configure Bindu**: Add `sentry` config (see above)
4. **Run Your Agent**: Sentry initializes automatically

> 📚 See the [full Sentry documentation](https://docs.getbindu.com/bindu/learn/sentry/overview) for complete details.

---

<br/>

## 🎯 Skills

Reusable capabilities that agents advertise and execute. Enable intelligent task routing and orchestration.

**API Endpoints:**
```bash
GET /agent/skills                      # List all skills
GET /agent/skills/{skill_id}           # Get details
GET /agent/skills/{skill_id}/documentation  # Get docs
```

📖 **[Full Skills Guide →](docs/SKILLS.md)** - Creating skills, metadata, examples

---

<br/>

## 🤝 Negotiation

Capability-based agent selection for intelligent orchestration. Query multiple agents and select the best one.

**How It Works:**
1. Orchestrator broadcasts → Multiple agents
2. Agents self-assess → Capability scoring
3. Orchestrator ranks → Multi-factor scoring
4. Best agent selected → Task executed

**API:**
```bash
POST /agent/negotiation
```

📖 **[Full Negotiation Guide →](docs/NEGOTIATION.md)** - Scoring, orchestration, examples

---

<br/>

## 📬 Push Notifications

Real-time webhook notifications for task updates. No polling required.

**Quick Setup:**
```bash
GLOBAL_WEBHOOK_URL=https://your-server.com/webhooks
GLOBAL_WEBHOOK_TOKEN=your_secret_token
```

**Event Types:**
- `status-update` - Task state changes
- `artifact-update` - Output generation

📖 **[Full Notifications Guide →](docs/NOTIFICATIONS.md)** - Webhook setup, security, examples

---

<br/>

## 🔄 Retry Mechanism

Automatic retry with exponential backoff for resilient agents. Handles transient failures gracefully.

📖 **[Retry Documentation →](https://docs.getbindu.com/bindu/learn/retry/overview)**

---

<br/>

## 📊 Observability & Monitoring

Track performance, debug issues, and monitor your agents with **OpenTelemetry** and **Sentry**.

**OpenTelemetry (Langfuse, Arize):**
```bash
TELEMETRY_ENABLED=true
OLTP_ENDPOINT=https://cloud.langfuse.com/api/public/otel/v1/traces
OLTP_SERVICE_NAME=your-agent-name
OLTP_HEADERS={"Authorization":"Basic <base64-credentials>"}
```

**Sentry Error Tracking:**
```bash
SENTRY_ENABLED=true
SENTRY_DSN=https://<key>@<org>.ingest.sentry.io/<project>
SENTRY_ENVIRONMENT=production
```

**Features:**
- Distributed tracing
- LLM call monitoring
- Error tracking
- Performance metrics

📖 **[Full Observability Guide →](docs/OBSERVABILITY.md)** - Platform setup, custom instrumentation, troubleshooting

---

<br/>

## 📬 Push Notifications

Bindu supports **real-time webhook notifications** for long-running tasks, following the [A2A Protocol specification](https://a2a-protocol.org/latest/specification/). This enables clients to receive push notifications about task state changes and artifact generation without polling.

### Quick Start

1. **Start webhook receiver:** `python examples/webhook_client_example.py`
2. **Configure agent** in `examples/echo_agent_with_webhooks.py`:
   ```python
   manifest = {
       "capabilities": {"push_notifications": True},
       "global_webhook_url": "http://localhost:8000/webhooks/task-updates",
       "global_webhook_token": "secret_abc123",
   }
   ```
3. **Run agent:** `python examples/echo_agent_with_webhooks.py`
4. **Send tasks** - webhook notifications arrive automatically

<details>
<summary><b>View webhook receiver implementation</b> (click to expand)</summary>

```python
from fastapi import FastAPI, Request, Header, HTTPException

@app.post("/webhooks/task-updates")
async def handle_task_update(request: Request, authorization: str = Header(None)):
    if authorization != "Bearer secret_abc123":
        raise HTTPException(status_code=401)

    event = await request.json()

    if event["kind"] == "status-update":
        print(f"Task {event['task_id']} state: {event['status']['state']}")
    elif event["kind"] == "artifact-update":
        print(f"Artifact generated: {event['artifact']['name']}")

    return {"status": "received"}
```

</details>

<details>
<summary><b>View notification event types</b> (click to expand)</summary>

<br/>

**Status Update Event** - Sent when task state changes:
```json
{
  "kind": "status-update",
  "task_id": "123e4567-...",
  "status": {"state": "working"},
  "final": false
}
```

**Artifact Update Event** - Sent when artifacts are generated:
```json
{
  "kind": "artifact-update",
  "task_id": "123e4567-...",
  "artifact": {
    "artifact_id": "456e7890-...",
    "name": "results.json",
    "parts": [...]
  }
}
```

</details>

### ⚙️ Configuration

<details>
<summary><b>View configuration example</b> (click to expand)</summary>

**Using `bindufy`:**

```python
from bindu.penguin.bindufy import bindufy

def handler(messages):
    return [{"role": "assistant", "content": messages[-1]["content"]}]

config = {
    "author": "you@example.com",
    "name": "my_agent",
    "description": "Agent with push notifications",
    "deployment": {"url": "http://localhost:3773"},
    "capabilities": {"push_notifications": True},
    # Global webhook configuration is now set via environment variables:
    # GLOBAL_WEBHOOK_URL and GLOBAL_WEBHOOK_TOKEN
}

bindufy(config, handler)
```

**Per-Task Webhook Override:**

```python
"configuration": {
    "long_running": True,  # Persist webhook in database
    "push_notification_config": {
        "id": str(uuid4()),
        "url": "https://custom-endpoint.com/webhooks",
        "token": "custom_token_123"
    }
}
```

**Long-Running Tasks:**

For tasks that run longer than typical request timeouts (minutes, hours, or days), set `long_running=True` to persist webhook configurations across server restarts. The webhook config will be stored in the database (`webhook_configs` table).

</details>

📖 **[Complete Documentation](docs/long-running-task-notifications.md)** - Detailed guide with architecture, security, examples, and troubleshooting.

---

<br/>

## 🎨 Chat UI

Please go to frontend folder and run `npm run dev` to start the frontend server.
Bindu includes a beautiful chat interface at `http://localhost:5173`

<p align="center">
  <img src="assets/agent-ui.png" alt="Bindu Agent UI" width="640" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" />
</p>

---

<br/>

## 🌐 Bindu Directory

The [**Bindu Directory**](https://bindus.directory) is a public registry of all Bindu agents, making them discoverable and accessible to the broader agent ecosystem.

### ✨ Automatic Registration with Cookiecutter

When you create an agent using the cookiecutter template, it includes a pre-configured GitHub Action that automatically registers your agent in the directory:

1. **Create your agent** using cookiecutter
2. **Push to GitHub** - The GitHub Action triggers automatically
3. **Your agent appears** in the [Bindu Directory](https://bindus.directory)

> **🔑 Note**: You need to collect the BINDU_PAT_TOKEN from bindus.directory and use it to register your agent.

### 📝 Manual Registration

We are working on a manual registration process.

---

<br/>

## 🌌 The Vision

```
a peek into the night sky
}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
{{            +             +                  +   @          {{
}}   |                *           o     +                .    }}
{{  -O-    o               .               .          +       {{
}}   |                    _,.-----.,_         o    |          }}
{{           +    *    .-'.         .'-.          -O-         {{
}}      *            .'.-'   .---.   `'.'.         |     *    }}
{{ .                /_.-'   /     \   .'-.\.                   {{
}}         ' -=*<  |-._.-  |   @   |   '-._|  >*=-    .     + }}
{{ -- )--           \`-.    \     /    .-'/                   }}
}}       *     +     `.'.    '---'    .'.'    +       o       }}
{{                  .  '-._         _.-'  .                   }}
}}         |               `~~~~~~~`       - --===D       @   }}
{{   o    -O-      *   .                  *        +          {{
}}         |                      +         .            +    }}
{{ jgs          .     @      o                        *       {{
}}       o                          *          o           .  }}
{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{
```

_Each symbol is an agent — a spark of intelligence. The tiny dot is Bindu, the origin point in the Internet of Agents._

### NightSky Connection [In Progress]

NightSky enables swarms of agents. Each Bindu is a dot annotating agents with the shared language of A2A, AP2, and X402. Agents can be hosted anywhere—laptops, clouds, or clusters—yet speak the same protocol, trust each other by design, and work together as a single, distributed mind.

> **💭 A Goal Without a Plan Is Just a Wish.**

---


<br/>

## 🛠️ Supported Agent Frameworks

Bindu is **framework-agnostic** and tested with:

- **Agno**
- **CrewAI**
- **LangChain**
- **LlamaIndex**
- **FastAgent**

Want integration with your favorite framework? [Let us know on Discord](https://discord.gg/3w5zuYUuwt)!

---

<br/>

## 🧪 Testing

Bindu maintains **64%+ test coverage**:

```bash
uv run pytest -n auto --cov=bindu --cov-report= && coverage report --skip-covered --fail-under=64
```

---

<br/>

## Troubleshooting
<details>
<summary>Common Issues</summary>

<br/>

| Issue | Solution |
|-------|----------|
| `Python 3.12 not found` | Install Python 3.12+ and set in PATH, or use `pyenv` |
| `bindu: command not found` | Activate virtual environment: `source .venv/bin/activate` |
| `Port 3773 already in use` | Change port in config: `"url": "http://localhost:4000"` |
| Pre-commit fails | Run `pre-commit run --all-files` |
| Tests fail | Install dev dependencies: `uv sync --dev` |
| `Permission denied` (macOS) | Run `xattr -cr .` to clear extended attributes |

**Reset environment:**
```bash
rm -rf .venv
uv venv --python 3.12.9
uv sync --dev
```

**Windows PowerShell:**
```bash
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

</details>

<br/>

## 🤝 Contributing

We welcome contributions! Join us on [Discord](https://discord.gg/3w5zuYUuwt). Pick the channel that best matches your contribution.

```bash
git clone https://github.com/getbindu/Bindu.git
cd Bindu
uv venv --python 3.12.9
source .venv/bin/activate
uv sync --dev
pre-commit run --all-files
```

> 📖 [Contributing Guidelines](.github/contributing.md)

---

<br/>

## 📜 License

Bindu is open-source under the [Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/).

---

<br/>

## 💬 Community

We 💛 contributions! Whether you're fixing bugs, improving documentation, or building demos—your contributions make Bindu better.

- 💬 [Join Discord](https://discord.gg/3w5zuYUuwt) for discussions and support
- ⭐ [Star the repository](https://github.com/getbindu/Bindu) if you find it useful!

---

<br/>

## 👥 Active Moderators

Our dedicated moderators help maintain a welcoming and productive community:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/raahulrahl">
        <img src="https://avatars.githubusercontent.com/u/157174139?v=4" width="100px;" alt="Raahul Dutta"/>
        <br />
        <sub><b>Raahul Dutta</b></sub>
      </a>
      <br />
    </td>
    <td align="center">
      <a href="https://github.com/Paraschamoli">
        <img src="https://avatars.githubusercontent.com/u/157124537?v=4" width="100px;" alt="Paras Chamoli"/>
        <br />
        <sub><b>Paras Chamoli</b></sub>
      </a>
      <br />
    </td>
    <td align="center">
      <a href="https://github.com/Gaurika-Sethi">
        <img src="https://avatars.githubusercontent.com/u/178935569?v=4" width="100px;" alt="Gaurika Sethi"/>
        <br />
        <sub><b>Gaurika Sethi</b></sub>
      </a>
      <br />
    </td>
    <td align="center">
      <a href="https://github.com/Avngrstark62">
        <img src="https://avatars.githubusercontent.com/u/133889196?v=4" width="100px;" alt="Abhijeet Singh Thakur"/>
        <br />
        <sub><b>Abhijeet Singh Thakur</b></sub>
      </a>
      <br />
    </td>
  </tr>
</table>

> Want to become a moderator? Reach out on [Discord](https://discord.gg/3w5zuYUuwt)!

---

<br/>

## �� Acknowledgements

Grateful to these projects:

- [FastA2A](https://github.com/pydantic/fasta2a)
- [12 Factor Agents](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-11-trigger-from-anywhere.md)
- [A2A](https://github.com/a2aproject/A2A)
- [AP2](https://github.com/google-agentic-commerce/AP2)
- [Huggingface chatui](https://github.com/huggingface/chat-ui)
- [X402](https://github.com/coinbase/x402)
- [Bindu Logo](https://openmoji.org/library/emoji-1F33B/)
- [ASCII Space Art](https://www.asciiart.eu/space/other)

---

<br/>

## 🗺️ Roadmap

- [ ] GRPC transport support
- [ ] Increase test coverage to 80% - In progress
- [ ] AP2 end-to-end support
- [ ] DSPy integration - In progress
- [ ] MLTS support
- [ ] X402 support with other facilitators

> 💡 [Suggest features on Discord](https://discord.gg/3w5zuYUuwt)!

---

<br/>

## 🎓 Workshops

- [AI Native in Action: Agent Symphony](https://www.meetup.com/ai-native-amsterdam/events/311066899/) - [Slides](https://docs.google.com/presentation/d/1SqGXI0Gv_KCWZ1Mw2SOx_kI0u-LLxwZq7lMSONdl8oQ/edit)

---

<br/>

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=getbindu/Bindu&type=Date)](https://www.star-history.com/#getbindu/Bindu&Date)

---

<p align="center">
  <strong>Built with 💛 by the team from Amsterdam </strong><br/>
  <em>Happy Bindu! 🌻🚀✨</em>
</p>

<p align="center">
  <strong>From idea to Internet of Agents in 2 minutes.</strong><br/>
  <em>Your agent. Your framework. Universal protocols.</em>
</p>

<p align="center">
  <a href="https://github.com/getbindu/Bindu">⭐ Star us on GitHub</a> •
  <a href="https://discord.gg/3w5zuYUuwt">💬 Join Discord</a> •
  <a href="https://docs.getbindu.com">🌻 Read the Docs</a>
</p>
