# Test script for Automation.py
import sys
import os

# Add the Backend directory to the path if needed
if not os.path.exists("Backend"):
    print("Make sure you're running this from the root directory where Backend folder exists")
    sys.exit(1)

sys.path.append("Backend")

try:
    print("Importing Automation module...")
    from Backend import Automation
    print("Successfully imported Automation module")
    
    # Test some basic functions
    print("\nTesting basic functions:")
    
    # Test string_similarity function
    print("\n1. Testing string_similarity function:")
    similarity = Automation.string_similarity("hello world", "hello there")
    print(f"Similarity between 'hello world' and 'hello there': {similarity}%")
    
    # Test Content function (this will use the Groq API, so it might fail if API key is not set)
    print("\n2. Testing Content function (will be skipped if API key is not set):")
    if Automation.GroqAPIKey:
        print("API key found, but we'll skip actual content generation to avoid API usage")
    else:
        print("No API key found, skipping Content function test")
    
    # Test system functions that don't require external resources
    print("\n3. Testing parse_time_expression function:")
    seconds = Automation.parse_time_expression("wait for 5 minutes and 30 seconds")
    print(f"'wait for 5 minutes and 30 seconds' parsed as {seconds} seconds")
    
    print("\nAll tests completed successfully!")
    
except ImportError as e:
    print(f"Error importing Automation module: {e}")
except Exception as e:
    print(f"Error during testing: {e}")
