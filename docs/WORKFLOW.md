# Automated LeetCode Daily Solver Workflow

## System Architecture

```
┌─────────────────────┐    Daily Problem     ┌──────────────────────────────────────────┐
│   LeetCode API      │ ─────────────────────► │        leetcode Repository               │
│ (leetcode-api-pied  │                       │  ┌─────────────────────────────────────┐ │
│  .vercel.app)       │                       │  │      GitHub Actions Workflow       │ │
└─────────────────────┘                       │  │      (Scheduled Daily @ 00:05)     │ │
                                              │  └─────────────────────────────────────┘ │
                      Multi-Agent API Call    │                   │                       │
┌─────────────────────┐ ◄─────────────────────┼───────────────────▼─────────────────────┐ │
│   opticodegen       │                       │  ┌─────────────────────────────────────┐ │ │
│   FastAPI Service   │ ─────────────────────► │  │    Problem Fetcher & Processor     │ │ │
│   (Railway Deploy) │   AI Solutions        │  │  • Fetch daily challenge via API   │ │ │
│                     │                       │  │  • Parse problem data & metadata   │ │ │
│  ┌───────────────┐  │                       │  └─────────────────────────────────────┘ │ │
│  │ Reasoning LLM │  │                       │                   │                       │ │
│  │ Coding LLM    │  │                       │                   ▼                       │ │
│  │ QC LLM        │  │                       │  ┌─────────────────────────────────────┐ │ │
│  │ Testing LLM   │  │                       │  │      Multi-Agent Solver            │ │ │
│  │ Context LLM   │  │                       │  │  • Call opticodegen API endpoints  │ │ │
│  └───────────────┘  │                       │  │  • Coordinate specialized agents   │ │ │
│  ┌───────────────┐  │                       │  │  • Generate optimized solution     │ │ │
│  │ Rust Compiler │  │                       │  └─────────────────────────────────────┘ │ │
│  │ WASM Runtime  │  │                       │                   │                       │ │
│  │ E2B Sandbox   │  │                       │                   ▼                       │ │
│  └───────────────┘  │                       │  ┌─────────────────────────────────────┐ │ │
└─────────────────────┘                       │  │      Solution Processor            │ │ │
                                              │  │  • Format markdown documentation   │ │ │
                                              │  │  • Update statistics (stats.json)  │ │ │
┌─────────────────────┐                       │  │  • Validate code quality           │ │ │
│   Mailgun SMTP      │ ◄─────────────────────┼──└─────────────────────────────────────┘ │ │
│   Email Service     │   Success/Failure     │                   │                       │ │
└─────────────────────┘   Notifications       │                   ▼                       │ │
                                              │  ┌─────────────────────────────────────┐ │ │
                                              │  │      Git Operations Manager        │ │ │
                                              │  │  • Commit new solution files       │ │ │
                                              │  │  • Push to main branch             │ │ │
                                              │  │  • Send notification email         │ │ │
                                              │  └─────────────────────────────────────┘ │ │
                                              └──────────────────────────────────────────┘ │
                                                                                          │
                                              ┌──────────────────────────────────────────┘
                                              │
                                              ▼
                                    ┌─────────────────────┐
                                    │   Repository Files  │
                                    │                     │
                                    │ • /solves/*.md      │
                                    │ • stats.json        │
                                    │ • README.md         │
                                    └─────────────────────┘
```

## Workflow Components

### 1. **Trigger System**
- **Schedule**: Daily execution at 00:05 UTC via GitHub Actions cron
- **Manual**: On-demand execution via `workflow_dispatch`
- **Reliability**: Timeout protection and error handling

### 2. **Problem Acquisition**
- **Source**: [LeetCode API](https://leetcode-api-pied.vercel.app/daily)
- **Method**: RESTful GET request to `/daily` endpoint
- **Data**: Complete problem metadata including description, constraints, examples

### 3. **AI Solution Generation**
- **Service**: opticodegen FastAPI deployment on Railway
- **Architecture**: Multi-agent system with specialized LLMs
- **Process**: 
  - Problem analysis and approach selection
  - Code generation with multiple language support
  - Quality control and optimization
  - Test case generation and validation

### 4. **Infrastructure Stack**

#### opticodegen Service (Railway)
- **Framework**: FastAPI with async/await support
- **Runtime**: Python 3.11+ with Rust extensions
- **Code Execution**: 
  - Primary: Rust compiler with WASM runtime
  - Fallback: E2B Code Interpreter sandbox
- **LLM Integration**: OpenAI, Anthropic, Google, and open-source models

#### Supporting Libraries
- **API & HTTP**: FastAPI, HTTPX, Uvicorn
- **Data Validation**: Pydantic v2, OrJSON
- **Code Quality**: Ruff, Black, MyPy, isort
- **Reliability**: Tenacity retry logic
- **Testing**: Pytest with asyncio and coverage

### 5. **Solution Processing**
- **Format**: Markdown with embedded code blocks
- **Metadata**: Problem details, complexity analysis, approach explanation
- **Storage**: `/solves` directory with systematic naming
- **Statistics**: Dynamic tracking in `stats.json`

### 6. **Quality Assurance**
- **Code Validation**: Syntax and runtime verification
- **Test Coverage**: Comprehensive edge case testing
- **Performance**: Time/space complexity analysis
- **Documentation**: Detailed approach explanations

### 7. **Notification System**
- **Service**: Mailgun SMTP integration
- **Content**: Solution summary with copy-paste ready code
- **Fallback**: GitHub Actions status notifications
- **Format**: HTML and plain text email variants

## Benefits

### **Automation Excellence**
- Zero-touch daily operation
- Consistent quality and formatting
- Automatic error recovery and notifications

### **AI Capability Demonstration**
- Real-world multi-agent coordination
- Continuous model performance evaluation
- Transparent AI decision-making process

### **Portfolio Development**
- Daily commit streak maintenance
- High-quality solution documentation
- Public demonstration of AI integration skills

### **System Reliability**
- Decoupled architecture for maintainability
- Comprehensive error handling and logging
- Multiple fallback mechanisms for code execution

## Configuration

### Required Secrets
- `OPTICODEGEN_API_URL`: Railway deployment endpoint
- `MAILGUN_API_KEY`: Email service authentication
- `MAILGUN_DOMAIN`: Configured sending domain
- `MAILGUN_SMTP_*`: SMTP configuration parameters
- `EMAIL_RECIPIENT`: Notification destination

### Environment Variables
- Model configurations and fallback settings
- API timeouts and retry parameters
- Feature flags for testing and debugging
