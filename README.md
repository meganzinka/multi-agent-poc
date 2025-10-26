# AI Campaign Strategist

<div align="center">

![AI Campaign](https://img.shields.io/badge/AI-Campaign%20Strategist-blue?style=for-the-badge&logo=robot)
![Google ADK](https://img.shields.io/badge/Google-ADK-4285F4?style=for-the-badge&logo=google)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active%20Development-green?style=for-the-badge)

*A multi-agent AI system built with the Google Agent Development Kit (ADK) to help turn a simple idea into a complete, actionable campaign plan.*

**🎯 Solving the "blank page" problem for marketers, accelerating the creative and strategic process for new campaigns.**

</div>

---

## 🔍 Problem & Solution

### 🚫 The Problem
Marketers often start with a high-level goal (e.g., *"launch a new feature"*) but must manually and sequentially develop the strategy, content ideas, and copy drafts. This process is:

- ⏰ **Time-consuming**
- 🏢 **Creates creative silos**
- 🔄 **Inefficient sequential workflow**

### ✅ The Solution
This project uses a **team of specialized AI agents** that work in parallel to develop a comprehensive campaign plan from a single, simple brief. It acts as an **"AI brainstorming partner"**.

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🤖 Multi-Agent Workflow
Orchestrates a team of specialist agents for comprehensive output

### ⚡ Parallel Processing
Strategist, Content Idea, and Email Drafter agents work simultaneously for maximum speed

</td>
<td width="50%">

### 📝 Simple Input
Requires only a simple brief:
- Goal
- Audience  
- Key Message

### 🎯 Actionable Output
Generates a clean, structured `campaign_plan.md` file ready for implementation

</td>
</tr>
</table>

## 🏗️ Architecture

> Built with **Google Agent Development Kit (ADK)**

This project uses Google's ADK to define and orchestrate a hierarchy of specialized agents:

### 🎭 Agent Roles

<div align="center">

```mermaid
graph TD
    A[🎯 RootAgent<br/>The Conductor] --> B[🧠 StrategistAgent<br/>The "Why"]
    A --> C[💡 ContentIdeaAgent<br/>The "What"]
    A --> D[📧 EmailDrafterAgent<br/>The "How"]
    
    B --> E[📄 campaign_plan.md]
    C --> E
    D --> E
    
    style A fill:#4285F4,stroke:#333,stroke-width:3px,color:#fff
    style B fill:#34A853,stroke:#333,stroke-width:2px,color:#fff
    style C fill:#FBBC04,stroke:#333,stroke-width:2px,color:#000
    style D fill:#EA4335,stroke:#333,stroke-width:2px,color:#fff
    style E fill:#9AA0A6,stroke:#333,stroke-width:2px,color:#fff
```

</div>

#### 🎯 **RootAgent** (The Conductor)
- 📥 Receives the high-level brief from the user
- 🚀 Passes the brief to three specialist agents, triggering parallel execution
- ⏳ Waits for all agents to complete their work
- 📊 Gathers all text outputs
- 📝 Uses built-in `write_to_markdown` tool to format and save the final `campaign_plan.md`

#### 🧠 **StrategistAgent** (The "Why")
- 🎯 Defines 3-5 key strategic pillars for the campaign
- 📺 Identifies primary and secondary target channels (Blog, LinkedIn, Email, etc.)

#### 💡 **ContentIdeaAgent** (The "What")
- 🧠 Brainstorms 3-5 specific, creative content ideas and angles
- 📝 Generates blog titles, video concepts that align with strategic pillars

#### 📧 **EmailDrafterAgent** (The "How")
- ✍️ Writes a draft 3-part email nurture sequence:
  - 🔍 **Awareness**
  - 🤔 **Consideration** 
  - 🎯 **Conversion**

---

## 🛠️ Tech Stack

<div align="center">

| Component | Technology | Description |
|-----------|------------|-------------|
| 🎭 **Orchestration** | Google Agent Development Kit (ADK) | Multi-agent workflow management |
| 🐍 **Language** | Python 3.10+ | Core development language |
| 🤖 **LLMs** | Google Gemini (Vertex AI) | AI model providers |
| ☁️ **Deployment** | GCP Cloud Run | Container-based cloud deployment |

</div>


