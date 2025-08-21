# Automatic Daily Leetcode Solves: An AI Evolution Experiment

[![Deployed on Railway](https://img.shields.io/badge/Deployed%20on-Railway-black?logo=railway)](https://railway.app)
[![FastAPI](https://img.shields.io/badge/Powered%20By-FastAPI-%2300C7B7?logo=fastapi)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)](https://python.org)
[![Rust](https://img.shields.io/badge/Rust-Code%20Execution-orange?logo=rust)](https://rust-lang.org)

## The Autonomous Revolution

As AI increasingly demonstrates proficiency in solving coding tasks, the key differentiator becomes the ability to effectively orchestrate, tune, and maintain AI systems for real-world applications. This repository provides full transparency about AI's role in automated LeetCode solving while highlighting the critical human expertise (that's me) required in system design, cloud architecture, multi-agent orchestration, prompt engineering, and quality assurance.

In this new age of AI-powered autonomous revolution, the workforce isn’t disappearing, but the old ways of working are. To quote Steve Jobs, “Innovation distinguishes between a leader and a follower.”

## Implementation

Powered by **OptiCodeGen** - my proprietary multi-agent API system deployed on Railway serverless infrastructure - this experiment demonstrates advanced AI orchestration from problem to multi-language solutions with built-in code testing and quality assurance measures. The OptiCodeGen engine is the backbone that makes this possible, featuring:

### Core Infrastructure
- **FastAPI** backend with high-performance async endpoints
- **Rust** integration for secure code compilation and execution
- **E2B Code Interpreter** as fallback sandbox for code testing
- **WebAssembly (WASM)** runtime for isolated code execution
- **Multi-agent orchestration** with specialized task-specific models

### Key Libraries & Technologies
- **Model Orchestration**: Pydantic V2 and Instructor for multi-model coordination
- **LLM Integration**: OpenAI, Google, and custom system prompting
- **Data Validation**: Structured type validation and schema enforcement
- **HTTP & API**: High-performance async endpoint management
- **Code Quality**: Automated formatting and linting pipelines
- **Reliability**: Robust error handling and retry mechanisms
- **Testing**: Comprehensive test coverage with async support

## Multi-Agent System Architecture

Solutions are generated through a specialized three-agent system powered by world-class LLMs. This architecture emphasizes clear role boundaries and iterative improvement:

### 🎭 Core Agents

- **Orchestrator**
  - Manages workflow coordination
  - Facilitates inter-agent communication
  - Documents optimization journey
  - Maintains context across iterations
  - Powered by large-context-window LLM

- **Coder**
  - Handles code generation
  - Implements optimizations
  - Maintains code quality
  - Ensures best practices
  - Uses advanced code-specialized models

- **Reasoner**
  - Analyzes solution approaches
  - Evaluates performance implications
  - Identifies optimization opportunities
  - Validates implementation choices
  - Leverages reasoning-optimized LLMs

### 🔄 Solution Workflow

The system follows a recursive optimization pattern:

1. **Problem Analysis**: Orchestrator evaluates the challenge
2. **Solution Generation**: Coder implements approach
3. **Validation**: Code is compiled and executed
4. **Analysis**: Reasoner evaluates results
5. **Iteration**: Process repeats if improvements needed

### 💡 Core Philosophy

You'll notice that all solutions in the [`/solves`](./solves) directory, includes not just the "what" but also the crucial "why" behind implementation decisions. Think of these robotic code comments as a glimpse inside the mind of the machine or receipts for code decisions (whether for better or worse). It'll be facinating to see how AI improves over time with more advanced models released on the regular!

## Solution Statistics

[![Total Solutions](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/yourusername/leetcode-daily/main/stats.json&label=Total&query=$.total&color=blue)](./solves)
[![Easy Problems](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/yourusername/leetcode-daily/main/stats.json&label=Easy&query=$.easy&color=green)](./solves)
[![Medium Problems](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/yourusername/leetcode-daily/main/stats.json&label=Medium&query=$.medium&color=yellow)](./solves)
[![Hard Problems](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/yourusername/leetcode-daily/main/stats.json&label=Hard&query=$.hard&color=red)](./solves)
[![Build Status](https://github.com/yourusername/leetcode-daily/workflows/Daily%20Solve/badge.svg)](https://github.com/yourusername/leetcode-daily/actions)

## Technical Details

### Solution Architecture
- **Problem Fetching:** LeetCode GraphQL API with smart caching
- **Solution Generation:** Multi-agent AI system via my OptiCodeGen API engine
- **Deployment:** Railway-hosted infrastructure
- **Automation:** GitHub Actions with intelligent scheduling
- **Monitoring:** Metrics and notifications

## License

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

*Powered by OptiCodeGen - My proprietary multi-agent code intelligence system, leveraging world-class LLMs for automated problem-solving*

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
