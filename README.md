# LLM Hub

A scalable Python framework for integrating and interacting with multiple Large Language Models (LLMs) through a unified interface. This platform supports seamless switching between different AI providers (OpenAI, Anthropic, Google) and allows for customizable chat personalities.

## Features

- 🤖 Multi-model support (GPT-4, GPT-3.5, Claude-3, PaLM)
- 🎯 Pre-configured chat personalities
- ⚙️ Custom system prompt creation
- 🔄 Real-time streaming responses
- 🎨 Clean and intuitive Gradio interface
- 📝 Comprehensive logging system

## Installation

1. Clone the repository:
```bash
git clone https://github.com/priyakannu238/llm-hub.git
cd llm-hub
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your API keys:
```env
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GOOGLE_API_KEY=your_google_key
```

## Usage

1. Run the application:
```bash
python main.py
```

2. Access the interface at `http://localhost:7860`

3. Select your preferred:
   - AI Model
   - Chat Personality
   - Custom system message (optional)

## Acknowledgments

- Built with [Gradio](https://gradio.app/)
- Integrates with OpenAI, Anthropic, and Google AI