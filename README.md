# GimiBot

A Streamlit-based AI chatbot powered by Google Gemini.

## Features

- Natural language conversations powered by Gemini AI
- Clean and responsive Streamlit interface
- Real-time responses
- Easy to deploy

## Tech Stack

- **Python 3.11+** - Programming language
- **Streamlit** - Web interface framework
- **Google Gemini API** - AI model
- **python-dotenv** - Environment variable management

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        GimiBot Architecture                   │
└─────────────────────────────────────────────────────────────┘

  ┌──────────────┐    1. User Input    ┌──────────────┐
  │   Streamlit   │ ──────────────────► │   app.py     │
  │   Frontend    │                     │  (Handler)   │
  └──────────────┘                      └──────┬───────┘
       ▲                                       │
       │                                       ▼
       │ 6. Display Response           ┌──────────────┐
       │                              │   Gemini     │
       │                              │   API        │
       └───────────────────────────── │  (Google)   │
                                       └──────────────┘
                                               ▲
                                               │ 5. AI Response
                                               │
                                       ┌───────┴───────┐
                                       │  Chat Session │
                                       │  (Context)   │
                                       └───────────────┘
```

### How It Works

1. **User Input** - User types message in Streamlit text input field
2. **Form Submission** - Message sent via Streamlit form submission
3. **API Request** - `app.py` sends message to Gemini API with API key
4. **AI Processing** - Gemini processes the message
5. **Response** - Generated text response returned to handler
6. **Display** - Response rendered in Streamlit markdown

### Component Details

| Component | File | Purpose |
|-----------|------|---------|
| Frontend | Streamlit UI | User interaction interface |
| Handler | `app.py` | Request routing and API calls |
| AI Model | Gemini 2.5 Flash | Natural language processing |
| Config | `.env` | API key storage |

## Prerequisites

- Python 3.11 or higher
- Google Gemini API key

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/gimibot.git
cd GimiBot
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Get API Key

Get your Google Gemini API key from [Google AI Studio](https://aistudio.google.com/)

### 5. Configure Environment

Create a `.env` file in the project root:

```bash
cp example.env .env
```

Edit `.env` and add your API key:

```
GOOGLE_API_KEY=your_actual_api_key_here
```

## Running the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Project Structure

```
GimiBot/
├── app.py              # Main application handler
├── .env                # Environment variables (API key)
├── .gitignore          # Git ignore rules
├── example.env         # Environment template
├── example.gitignore   # Gitignore template with explanations
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Included Templates

This repo includes template files to help beginners understand the project structure:

### example.env

The template for environment variables. Beginners should:
1. Copy `example.env` to `.env`
2. Replace `your_api_key_here` with actual Google Gemini API key

```env
GOOGLE_API_KEY=your_api_key_here
```

### example.gitignore

Comprehensive gitignore template with explanations for each rule:

| Rule | Purpose |
|------|---------|
| `*.pyc`, `__pycache__/` | Python compiled cache files |
| `venv/`, `.venv/` | Virtual environment folders |
| `.env` | **Important:** API keys and secrets |
| `.vscode/`, `.idea/` | IDE settings |
| `Thumbs.db`, `.DS_Store` | OS-specific files |

Copy the rules you need or use this file as-is by renaming to `.gitignore`.

## How to Learn from This Repo

### Step 1: Understand the Flow

Study `app.py` line by line:
```
Line 1-2: Load environment variables from .env
Line 4-8: Configure Gemini API with your key
Line 13-16: Handle user input → API call → response
Line 18-35: Streamlit UI components
```

### Step 2: Key Concepts to Learn

| Concept | File | What You'll Learn |
|---------|------|-------------------|
| API Configuration | `app.py:8` | How to securely use API keys |
| Environment Variables | `.env` | Separating config from code |
| Streamlit Basics | `app.py:18-35` | Forms, input, markdown display |
| Git Safety | `.gitignore` | Protecting sensitive files |

### Step 3: Customization Ideas

1. **Change the Model** - Modify `model` in `app.py:11`
2. **Add Chat History** - Store conversation in `st.session_state`
3. **Custom UI** - Edit Streamlit components in `app.py:18-35`
4. **Add Features** - Integrate file upload, image generation, etc.

### Step 4: Deployment

When ready to deploy:
1. Set `GOOGLE_API_KEY` in production environment
2. Use `requirements.txt` for dependencies
3. Run `streamlit run app.py` or deploy to Streamlit Cloud

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GOOGLE_API_KEY` | Yes | Google Gemini API key from AI Studio |

## Security Notes

- Never commit `.env` file to version control
- Always use environment variables for API keys
- The `.gitignore` file excludes `.env` by default

## License

MIT License