# Test script for parse_natural_language function
import sys
import os

# Add the Backend directory to the path if needed
if not os.path.exists("Backend"):
    print("Make sure you're running this from the root directory where Backend folder exists")
    sys.exit(1)

sys.path.append("Backend")

try:
    print("Importing parse_natural_language function from Automation module...")
    from Backend.Automation import parse_natural_language
    print("Successfully imported parse_natural_language function")
    
    # Test the function with various inputs
    test_inputs = [
        "play afsoos",
        "volume up",
        "open notepad",
        "close chrome",
        "search for python tutorials",
        "brightness 50",
        "shutdown in 5 minutes"
    ]
    
    print("\nTesting parse_natural_language function:")
    for input_text in test_inputs:
        result = parse_natural_language(input_text)
        print(f"Input: '{input_text}' -> Output: '{result}'")
    
    print("\nAll tests completed successfully!")
    
except ImportError as e:
    print(f"Error importing from Automation module: {e}")
except Exception as e:
    print(f"Error during testing: {e}")
    import traceback
    traceback.print_exc()
