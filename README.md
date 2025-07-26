# MAMA (Multi-Agent Modular Assistant)

## Project Overview
MAMA is a sophisticated AI assistant system that combines multiple capabilities including speech processing, browser automation, chatbot functionality, and system automation.

## Core Components

### 1. Backend Services

#### Speech Processing
- **TextToSpeech.py**
  - Handles text-to-speech conversion
  - Supports both online and offline modes
  - Uses Azure TTS with fallback to offline TTS
  - Configurable voice settings
  - Handles audio file generation and playback

- **SpeechToText.py**
  - Provides speech recognition capabilities
  - Includes language detection and translation
  - Supports offline recognition mode
  - Universal translator functionality
  - Status monitoring and query modification

#### Browser Automation
- **simple_browser_test.py**
  - Browser automation using Playwright
  - Supports headless/visible browser modes
  - Handles page navigation and interactions
  - Error handling and status logging

#### System Automation
- **Automation.py**
  - System command processing
  - Volume control functionality
  - Power management commands
  - String similarity comparison
  - Integration with Groq API

### 2. Frontend
- **GUI.py** in Frontend/Graphics/
  - Graphical user interface implementation
  - User interaction handling

### 3. Data Management
- **Data/** directory
  - Stores chat logs
  - Generated images
  - Voice recordings
  - User configurations
  - Email templates

### 4. Configuration
- **personas.json**
  - Chatbot personality configurations
  - System prompts
  - Behavior settings

## Prerequisites

### System Requirements
- Python 3.10 or higher
- Windows 10/11 (for full system automation support)
- Microphone (for voice interaction)
- Speakers or headphones
- Stable internet connection (for online features)

### Required API Keys
1. **Azure Cognitive Services**
   - Speech Service API key for TTS/STT
   - Set in environment variable: `AZURE_SPEECH_KEY`
   - Region: Set in `AZURE_SPEECH_REGION`

2. **Groq API**
   - Required for advanced language processing
   - Set in environment variable: `GROQ_API_KEY`

### Environment Setup

### Virtual Environments Setup
1. **Create main environment**:
   ```powershell
   python -m venv mama
   .\mama\Scripts\activate
   pip install -r Requirements.txt
   ```

2. **Create browser environment**:
   ```powershell
   python -m venv browser-env
   .\browser-env\Scripts\activate
   pip install playwright
   playwright install chromium
   ```

### Dependencies
Key dependencies include:
- Playwright for browser automation
- Speech recognition libraries
- Azure Cognitive Services SDK
- Groq API client
- PyQt6 for GUI
- TensorFlow for offline processing

## Project Structure
```
mama/
├── Backend/
│   ├── Automation.py
│   ├── TextToSpeech.py
│   ├── SpeechToText.py
│   ├── simple_browser_test.py
│   └── ...
├── Frontend/
│   └── Graphics/
│       └── GUI.py
├── Data/
│   ├── ChatLog.json
│   ├── Voice.html
│   └── ...
└── browser-env/
    └── Scripts/
        └── activate.bat
```

## Testing
Multiple test files are included:
- test_automation.py
- test_system_function.py
- test_parse_function.py
- combined_test.py

## Initial Setup
1. Clone the repository:
   ```powershell
   git clone [repository-url]
   cd mama
   ```

2. Set up environment variables (create a .env file):
   ```plaintext
   AZURE_SPEECH_KEY=your_azure_key
   AZURE_SPEECH_REGION=your_region
   GROQ_API_KEY=your_groq_key
   ASSISTANT_VOICE=en-US-AriaNeural
   ```

3. Initialize the data directories:
   ```powershell
   mkdir Data/email_templates
   mkdir logs
   ```

## Usage

### Starting the Application
1. Activate the main environment:
   ```powershell
   .\mama\Scripts\activate
   ```

2. Run the main application:
   ```powershell
   python main.py
   ```

### Using Browser Automation Features
1. Activate the browser environment:
   ```powershell
   .\browser-env\Scripts\activate
   ```

2. Run browser automation:
   ```powershell
   python Backend/simple_browser_test.py
   ```

### Voice Commands
- Say "Hey MAMA" to activate voice recognition
- Use "Stop listening" to deactivate
- Common commands:
  - "Open browser"
  - "Check email"
  - "System status"
  - "Generate image [description]"

## Features
- Voice interaction (Text-to-Speech and Speech-to-Text)
- Browser automation
- System command execution
- Multi-language support
- Online/Offline operation modes
- Image generation capabilities
- Email automation
- Chat logging and history

## Logging
The system maintains several log files:
- chatbot.log
- image_generation.log
- model.log
- mama_status_log.txt

## Directory Structure
- **Backend/**: Core functionality implementations
- **Frontend/**: User interface components
- **Data/**: Storage for generated content and logs
- **MessageQueue/**: Message handling system
- **browser-env/**: Browser automation environment
- **mama/**: Main virtual environment

## Notes
- Supports both online and offline operations
- Includes fallback mechanisms for core functionalities
- Modular design for easy extension
- Comprehensive error handling and logging
