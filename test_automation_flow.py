# Test script for Automation command flow
import sys
import os
import asyncio

# Add the Backend directory to the path if needed
if not os.path.exists("Backend"):
    print("Make sure you're running this from the root directory where Backend folder exists")
    sys.exit(1)

sys.path.append("Backend")

try:
    print("Importing Automation module...")
    from Backend.Automation import parse_natural_language, TranslateAndExecute
    print("Successfully imported Automation functions")
    
    # Test the command execution flow
    async def test_command_flow():
        test_commands = [
            "play afsoos",
            "volume up",
            "open notepad",
            "search for python tutorials"
        ]
        
        print("\nTesting command execution flow:")
        for command in test_commands:
            parsed_cmd = parse_natural_language(command)
            print(f"Input: '{command}' -> Parsed as: '{parsed_cmd}'")
            
            # Test TranslateAndExecute with a single command
            print(f"Executing command: '{parsed_cmd}'")
            try:
                result = await TranslateAndExecute([parsed_cmd])
                print(f"Execution result: {result}")
            except Exception as e:
                print(f"Error executing command: {e}")
                import traceback
                traceback.print_exc()
            
            print("-" * 50)
    
    # Run the async test function
    asyncio.run(test_command_flow())
    
    print("\nAll tests completed!")
    
except ImportError as e:
    print(f"Error importing from Automation module: {e}")
except Exception as e:
    print(f"Error during testing: {e}")
    import traceback
    traceback.print_exc()
