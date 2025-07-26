# Test script for System function in Automation.py
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
    
    # Test the System function
    print("\nTesting System function:")
    
    # Test with a simple command
    print("\n1. Testing with a simple command:")
    result = Automation.System("volume up")
    print(f"Result of 'volume up' command: {result}")
    
    # Test with a command that includes time expressions
    print("\n2. Testing with a command that includes time expressions:")
    result = Automation.System("volume down in 2 seconds")
    print(f"Result of 'volume down in 2 seconds' command: {result}")
    
    # Test with a power command
    print("\n3. Testing with a power command (simulated, won't actually execute):")
    # We'll use the process_power_commands function directly to avoid actual shutdown
    power_cmd = Automation.process_power_commands("shutdown in 5 minutes")
    print(f"Processed power command 'shutdown in 5 minutes' to: {power_cmd}")
    
    print("\nAll System function tests completed!")
    
except ImportError as e:
    print(f"Error importing Automation module: {e}")
except Exception as e:
    print(f"Error during testing: {e}")
    import traceback
    traceback.print_exc()
