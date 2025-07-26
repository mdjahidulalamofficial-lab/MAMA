import os
import sys
import logging
from datetime import datetime
from pathlib import Path

# Add Backend directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'Backend'))

# Import backend components
try:
    from Backend.TextToSpeech import text_to_speech
    from Backend.SpeechToText import SpeechRecognition, SetAssistantStatus
    from Backend.Automation import System
    from Backend.ImageGeneration import generate_image
    from Backend.Chatbot import process_message
except ImportError as e:
    print(f"Error importing backend components: {e}")
    sys.exit(1)

# Configure logging
def setup_logging():
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_dir / "mama_status_log.txt"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

class MAMA:
    def __init__(self):
        self.logger = setup_logging()
        self.active = True
        self.logger.info("Initializing MAMA system...")
        
        # Initialize status
        SetAssistantStatus("Initializing...")
        
        # Verify environment variables
        self._check_environment()
        
        self.logger.info("MAMA system initialized successfully")
        SetAssistantStatus("Ready")

    def _check_environment(self):
        """Check required environment variables"""
        required_vars = [
            "AZURE_SPEECH_KEY",
            "AZURE_SPEECH_REGION",
            "GROQ_API_KEY"
        ]
        
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        if missing_vars:
            self.logger.error(f"Missing environment variables: {', '.join(missing_vars)}")
            text_to_speech("Missing required environment variables. Please check configuration.")
            sys.exit(1)

    def process_command(self, command: str) -> None:
        """Process user commands"""
        try:
            self.logger.info(f"Processing command: {command}")
            
            # System commands
            if command.startswith(("system", "volume", "shutdown", "restart")):
                response = System(command)
                text_to_speech(response)
                
            # Image generation
            elif "generate image" in command.lower():
                image_prompt = command.replace("generate image", "").strip()
                generate_image(image_prompt)
                text_to_speech("Image generation complete")
                
            # Chat interaction
            else:
                response = process_message(command)
                text_to_speech(response)
                
        except Exception as e:
            self.logger.error(f"Error processing command: {e}")
            text_to_speech("I encountered an error processing your request")

    def run(self):
        """Main execution loop"""
        text_to_speech("MAMA system is ready")
        
        try:
            while self.active:
                # Get speech input
                command = SpeechRecognition(None)  # None for default driver
                
                # Check for exit command
                if command.lower() in ["exit", "quit", "stop"]:
                    self.active = False
                    text_to_speech("Shutting down MAMA system")
                    continue
                
                # Process the command
                self.process_command(command)
                
        except KeyboardInterrupt:
            self.logger.info("Received shutdown signal")
            text_to_speech("Shutting down MAMA system")
        except Exception as e:
            self.logger.error(f"Critical error: {e}")
            text_to_speech("A critical error occurred. Please check the logs.")
        finally:
            SetAssistantStatus("Offline")
            self.logger.info("MAMA system shutdown complete")

def main():
    try:
        assistant = MAMA()
        assistant.run()
    except Exception as e:
        print(f"Failed to start MAMA: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
