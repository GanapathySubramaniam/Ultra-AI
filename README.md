# Ultra AI

> Your All-in-One AI Assistant Powered by Cutting-Edge Technology



[Key Features](#key-features) • [Demo](#demo) • [Quick Start](#quick-start) • [Installation](#installation) • [Usage](#usage) • [Tech Stack](#tech-stack) 
## Key Features

- 💬 **AI-Powered Chat**: Engage in intelligent conversations
- 🎨 **Image Generation**: Create stunning visuals with DALL-E 3
- 🗣️ **Voice Interaction**: Talk to your AI assistant
- ✨ **Prompt Engineering**: Craft perfect prompts for any task
- 🔐 **Secure Access**: Keep your AI safe with built-in authentication
- 🌐 **Multi-Language**: Communicate in your preferred language
- 📊 **Analytics Dashboard**: Track your AI usage and insights
- 🔄 **Model Switching**: Choose the best AI for each task
- 📱 **Responsive Design**: Use on desktop, tablet, or mobile

## Demo

Check out our Ultra AI in action:

[![Ultra AI Demo](https://img.youtube.com/vi/-YeUZHr1w6E/0.jpg)](https://www.youtube.com/watch?v=-YeUZHr1w6E "Ultra AI Demo")

## Quick Start

```bash
# Clone repository
git clone https://github.com/yourusername/ultra-ai.git

# Navigate to directory
cd ultra-ai

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run 1_Chat_👽.py
```

**Prerequisites:**
- Python 3.7+
- pip
- Virtual environment (recommended)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ultra-ai.git
   cd ultra-ai
   ```

2. **Set up virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configuration**
   - Create `.env` in `models/` directory:
     ```ini
     OPENAI=your_openai_api_key_here
     ANTHROPIC=your_anthropic_api_key_here
     ```
   - Set password in `pwd.txt`:
     ```
     your_chosen_password_here
     ```
     > ⚠️ Use a strong, unique password. Never share or commit this file.

5. **Run the application**
   ```bash
   streamlit run 1_Chat_👽.py
   ```

## Usage

1. **Login**: Enter your password to access the app.
2. **Chat**: Start conversations with the AI.
3. **Image Generation**: Describe and create images.
4. **Voice Interaction**: Speak with the AI assistant.
5. **Prompt Engineering**: Craft custom AI prompts.

## Tech Stack

- **Frontend**: Streamlit
- **AI Models**: 
  - Claude (Anthropic) for advanced language processing
  - GPT-3.5 (OpenAI) for quick responses
  - DALL-E 3 (OpenAI) for image generation
  - Whisper (OpenAI) for speech recognition
- **Text-to-Speech**: OpenAI's TTS model
- **Backend**: Python 3.7+
- **Authentication**: Custom implementation with password hashing
- **Version Control**: Git




---
you can reach out to me [here] (https://ganapathysubramaniam.github.io/)
Built with ❤️ by [Ganapathy Subramaniam Sundar ([https://github.com/yourusername](https://github.com/GanapathySubramaniam))****
