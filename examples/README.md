# Bindu Examples

Welcome to the Bindu examples collection! This directory contains ready-to-run agents that demonstrate various capabilities of the Bindu framework, from simple echo bots to advanced payment-gated advisors with authentication.

## Quick Start

Ensure you have the dependencies installed:

```bash
uv sync --dev
```

Run any example using `uv run`:

```bash
uv run examples/<example_name>.py
```

## Available Examples

### 1. Basic Agents
These examples demonstrate the fundamental concepts of Bindu.

| File | Description | Key Features |
|------|-------------|--------------|
| `echo_agent.py` | A minimal agent that repeats what you say. | Basics of `bindufy`, minimal config |
| `echo_simple_agent.py` | An even simpler version of the echo agent. | Ultra-minimal config |
| `summarizer_agent.py` | Summarizes text into 2-3 sentences using GPT-4. | Agno integration, LLM usage |

### 2. Framework Integrations
Bindu works seamlessly with other agent frameworks like Agno.

| File | Description | Key Features |
|------|-------------|--------------|
| `agno_simple_example.py` | Simplified research assistant with DuckDuckGo search. | Agno integration, environment-based config |

### 3. Advanced Capabilities
Examples showcasing unique Bindu features like payments, webhooks, and security.

| File | Description | Key Features |
|------|-------------|--------------|
| `premium_advisor.py` | Market insights agent requiring crypto payment upfront. | **X402 Payments**, Payment gating |
| `echo_agent_with_webhooks.py` | Research agent with push notification support. | Webhooks, Push notifications |
| `zk_policy_agent.py` | Security agent demonstrating ZK-proof policy compliance. | Zero-knowledge proofs, Content filtering |

### 4. Utilities & Helpers
Helper scripts for testing and development.

| File | Description | Key Features |
|------|-------------|--------------|
| `webhook_client_example.py` | FastAPI webhook receiver for Bindu notifications. | Webhook handling, Event processing |

## Environment Setup

Most examples require environment variables for API keys and infrastructure configuration.

```bash
# Hydra authentication (default)
HYDRA__ADMIN_URL=https://hydra-admin.getbindu.com
HYDRA__PUBLIC_URL=https://hydra.getbindu.com

# Optional: For PostgreSQL storage
DATABASE_URL=postgresql+asyncpg://user:pass@host/db  # pragma: allowlist secret

# Optional: For Redis scheduler
REDIS_URL=rediss://default:pass@host:6379  # pragma: allowlist secret
```

## Spotlight: Premium Advisor Agent

The `premium_advisor.py` example demonstrates Bindu's unique **X402** payment protocol. This agent is configured to reject any interaction unless a micropayment is made.

**To run it:**
```bash
uv run examples/premium_advisor.py
```

**What happens:**
1. **Request**: You send a message to the agent.
2. **402 Payment Required**: The agent intercepts the request and demands payment (e.g., 0.01 USDC).
3. **Invoice**: The response contains the blockchain details needed to pay.
4. **Service**: Once paid (proved via signature), the agent releases the advice.

This powerful feature allows you to monetize your agents natively!

## Testing Your Agents

### Basic Request (No Auth)
```bash
curl -X POST http://localhost:3773/ \
     -H "Content-Type: application/json" \
     -d '{
           "jsonrpc": "2.0",
           "method": "message/send",
           "params": {"message": {"role": "user", "content": "Hello!"}},
           "id": 1
         }'
```

### Authenticated Request (Hydra)
Get a token using client credentials:
```bash
curl 'https://hydra.getbindu.com/oauth2/token' \
  --user 'YOUR_DID:YOUR_CLIENT_SECRET' \
  -d 'grant_type=client_credentials' \
  -d 'scope=openid agent:read agent:write'
```

### Public Endpoints (No Auth Required)
```bash
# Health check
curl http://localhost:3773/health

# Agent skills
curl http://localhost:3773/agent/skills

# DID resolution
curl -X POST http://localhost:3773/did/resolve \
  -H "Content-Type: application/json" \
  -d '{"did": "YOUR_AGENT_DID"}'
```

## Skills

The `skills/` directory contains reusable agent capabilities:
- `question-answering/` - Q&A skill with examples
- `pdf-processing/` - PDF extraction and analysis
- `zk-policy/` - Zero-knowledge policy verification

See individual skill directories for documentation.

## Next Steps

1. **Start Simple**: Run `echo_agent.py` to verify your setup
2. **Add Intelligence**: Try `summarizer_agent.py` with your OpenAI key
3. **Enable Payments**: Explore `premium_advisor.py` for monetization
4. **Add Authentication**: Use `agno_example.py` for production-ready security
5. **Build Custom**: Copy any example and modify for your use case

For more details, see the [main documentation](../README.md).
