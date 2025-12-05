# 🚀 Multi-Agent Fraud Detection System

> An intelligent AI system for detecting and analyzing fraudulent insurance claims using multi-agent architecture, rule-based detection, and RAG-powered analytics.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![License](https://img.shields.io/badge/License-Apache%202.0-green)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Technology Stack](#-technology-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [License](#-license)

---

## 🎯 Overview

The **Multi-Agent Fraud Detection System** is a comprehensive solution designed to identify, investigate, and explain fraudulent insurance claims. Built for the Abacus Insights Hackathon, this system combines traditional rule-based detection with modern AI techniques to provide accurate, explainable fraud detection.

### **What Makes It Unique?**

- **Four Specialized AI Agents** working in orchestration
- **Hybrid Detection**: Rule-based algorithms + LLM-powered intelligence
- **RAG-Powered Chatbot** for natural language queries
- **Explainable AI**: Technical findings translated to business-friendly language
- **Interactive Dashboard**: Visual exploration of fraud patterns
- **End-to-End Pipeline**: From data generation to actionable insights

---

## ✨ Features

### 🔍 **Fraud Detection**
- **6 Rule-Based Detection Algorithms**:
  - Duplicate claim detection
  - Amount anomaly detection (Z-score analysis)
  - Procedure-diagnosis code mismatch
  - Velocity fraud (multiple claims in short timeframes)
  - Provider outlier detection
  - Impossible scenario detection

### 🤖 **Multi-Agent System**
- **Detection Agent**: Rule-based fraud identification
- **Investigation Agent**: LLM-powered deep analysis
- **Explanation Agent**: Business-friendly reporting
- **Query Agent**: RAG-based natural language interface

### 📊 **Interactive Dashboard**
- Real-time fraud statistics
- Visual analytics with Plotly
- Claim-by-claim exploration
- AI-powered chatbot assistant

### 💾 **Data Pipeline**
- Synthetic data generation (2,500+ claims)
- ETL processing with feature engineering
- Vector embeddings for semantic search
- SQLite database for persistence

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interface (Streamlit)                │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │  Dashboard   │  │    Claim     │  │  AI Assistant    │  │
│  │  Analytics   │  │   Explorer   │  │    Chatbot       │  │
│  └──────────────┘  └──────────────┘  └──────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Orchestrator Layer                        │
│            (Coordinates Multi-Agent Workflow)                │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
┌──────────────┐    ┌──────────────────┐    ┌─────────────┐
│  Detection   │───▶│  Investigation   │───▶│ Explanation │
│    Agent     │    │     Agent        │    │    Agent    │
│ (Rule-Based) │    │  (LLM-Powered)   │    │ (Business)  │
└──────────────┘    └──────────────────┘    └─────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │   Query Agent    │
                    │  (RAG + FAISS)   │
                    └──────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                     Data Layer                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │    SQLite    │  │    FAISS     │  │   Embeddings     │  │
│  │   Database   │  │  Vector DB   │  │   (Sentence-     │  │
│  │              │  │              │  │  Transformers)   │  │
│  └──────────────┘  └──────────────┘  └──────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### **Workflow:**

1. **Data Generation** → Synthetic claims with injected fraud patterns
2. **ETL Pipeline** → Feature engineering and database storage
3. **Detection Agent** → Apply 6 fraud detection rules
4. **Investigation Agent** → Deep LLM-powered analysis of suspicious claims
5. **Explanation Agent** → Generate business-friendly reports
6. **Query Agent** → Answer natural language questions via RAG

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.8+ |
| **UI Framework** | Streamlit |
| **Database** | SQLite |
| **LLM API** | OpenAI (via OpenRouter) |
| **Vector Database** | FAISS |
| **Embeddings** | SentenceTransformers |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Plotly |
| **Environment Management** | python-dotenv |

---

## 📦 Installation

### **Prerequisites**
- Python 3.8 or higher
- pip package manager
- OpenRouter API key (for LLM features)

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/yourusername/Abacus-Insights-Hackathon.git
cd Abacus-Insights-Hackathon
```

### **Step 2: Create Virtual Environment (Recommended)**
```bash
python -m venv .venv

# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 4: Configure Environment Variables**
Create a `.env` file in the root directory:
```env
OPENROUTER_API_KEY=your_api_key_here
OPENROUTER_MODEL=openai/gpt-4
```

> **Note**: Get your API key from [OpenRouter](https://openrouter.ai/)

---

## 🚀 Usage

### **Quick Start: Run the Complete Pipeline**

```bash
python setup_data_pipeline.py
```

This will:
1. ✅ Generate 2,500+ synthetic insurance claims
2. ✅ Run ETL pipeline with feature engineering
3. ✅ Execute fraud detection (6 rules)
4. ✅ Generate vector embeddings for RAG

**Expected Output:**
- `data/raw/claims_data.csv` - Raw synthetic claims
- `data/processed/fraud_detection.db` - SQLite database
- `data/embeddings/` - Vector embeddings for RAG

---

### **Option 1: Web Interface (Recommended)**

```bash
streamlit run src/app/app.py
```

Then open your browser to `http://localhost:8501`

**Features:**
- 📊 **Dashboard Tab**: View fraud statistics and analytics
- 🔍 **Claim Explorer Tab**: Investigate individual claims
- 💬 **AI Assistant Tab**: Chat with RAG-powered fraud analyst

---

### **Option 2: Command Line Interface**

```bash
python src/orchestrator.py
```

**Interactive Menu:**
```
1. 🚀 Run Full Fraud Detection Pipeline
2. 🔍 Investigate Single Claim
3. 💬 Ask a Question (Query Agent)
4. 🚪 Exit
```

---

### **Option 3: Individual Components**

**Generate Data Only:**
```bash
python -c "from src.data.generator import ClaimsGenerator; ClaimsGenerator().generate_claims(2500)"
```

**Run Fraud Detection:**
```bash
python src/fraud/rules.py
```

**Test Query Agent:**
```bash
python src/agents/query_agent.py
```

---

## 📁 Project Structure

```
Abacus-Insights-Hackathon/
│
├── src/                          # Source code
│   ├── agents/                   # AI Agents
│   │   ├── investigation_agent.py    # LLM-powered investigator
│   │   ├── explanation_agent.py      # Business report generator
│   │   ├── query_agent.py            # RAG chatbot
│   │   └── sql_agent.py              # SQL query helper
│   │
│   ├── app/                      # Streamlit UI
│   │   ├── app.py                    # Main dashboard
│   │   └── ui_utils.py               # UI utilities
│   │
│   ├── data/                     # Data processing
│   │   ├── generator.py              # Synthetic data generator
│   │   └── etl.py                    # ETL pipeline
│   │
│   ├── fraud/                    # Fraud detection
│   │   └── rules.py                  # 6 fraud detection rules
│   │
│   ├── rag/                      # RAG components
│   │   └── embeddings.py             # Vector embedding generator
│   │
│   ├── utils/                    # Utilities
│   │   └── llm.py                    # LLM client wrapper
│   │
│   └── orchestrator.py           # Multi-agent coordinator
│
├── data/                         # Data storage
│   ├── raw/                          # Raw synthetic data
│   ├── processed/                    # SQLite database
│   └── embeddings/                   # Vector embeddings
│
├── guide/                        # Hackathon documentation
│   ├── Hackathon.docx
│   └── Hackathon Template.pptx
│
├── requirements.txt              # Python dependencies
├── setup_data_pipeline.py        # One-click pipeline setup
├── .env.example                  # Environment template
└── README.md                     # This file
```

---

## 🔬 How It Works

### **1. Data Generation**
The system generates realistic insurance claims with intentionally injected fraud patterns:
- **Duplicate claims** (75 cases)
- **Abnormal amounts** (40 cases)
- **Code mismatches** (50 cases)
- **Impossible scenarios** (25 cases)
- **Provider outliers** (35 cases)
- **Velocity fraud** (25 cases)

### **2. Fraud Detection Rules**

#### **Rule 1: Duplicate Claims**
Identifies claims with identical claim IDs

#### **Rule 2: Amount Anomaly**
Uses Z-score analysis to detect abnormally high claim amounts
```python
z_score = (amount - mean) / std_dev
if z_score > 3: flag as fraud
```

#### **Rule 3: Code Mismatch**
Detects procedure codes that don't match diagnosis codes

#### **Rule 4: Velocity Fraud**
Flags multiple claims from same patient within short timeframe

#### **Rule 5: Provider Outlier**
Identifies providers billing significantly more than peers

#### **Rule 6: Impossible Scenarios**
Detects physically impossible situations (e.g., duplicate surgeries)

### **3. Multi-Agent Investigation**

When fraud is detected:
1. **Detection Agent** assigns fraud score (0-100)
2. **Investigation Agent** (LLM) analyzes patterns and context
3. **Explanation Agent** translates findings to business language
4. **Query Agent** enables natural language exploration

### **4. RAG-Powered Queries**

The system uses **Retrieval Augmented Generation**:
1. User asks question in natural language
2. Question is embedded using SentenceTransformers
3. FAISS retrieves relevant fraud cases
4. LLM generates answer with citations

---

## 📊 Expected Results

After running the pipeline:
- **Total Claims**: ~2,575
- **Fraud Cases Detected**: ~250 (10% fraud rate)
- **Database Tables**: 4 (claims, providers, patients, fraud_flags)
- **Vector Embeddings**: Generated for all fraud cases
- **Detection Accuracy**: High recall for injected fraud patterns

---

## 🧪 Testing & Validation

**Verify Database:**
```bash
python check_db.py
```

**Test RAG System:**
```bash
python check_rag.py
```

**Find Duplicates:**
```bash
python find_duplicates.py
```

**Diagnose Fraud Cases:**
```bash
python diagnose_fraud.py
```

---

## 🎓 Key Learning Outcomes

This project demonstrates:
- ✅ Building multi-agent AI systems
- ✅ Combining rule-based and LLM approaches
- ✅ Implementing RAG for domain-specific queries
- ✅ Creating explainable AI systems
- ✅ Designing production-ready data pipelines
- ✅ Building interactive dashboards with Streamlit

---

## 🙏 Acknowledgments

- **Abacus Insights** for hosting the hackathon
- **OpenRouter** for LLM API access
- **Streamlit** for the amazing UI framework
- **FAISS** for efficient vector search

---
