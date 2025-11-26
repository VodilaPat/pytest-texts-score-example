def generate_response(user_input):
    """
    Takes user input and returns it with the specific prefix.
    """
    return f"AI said: {user_input}"

def main():
    print("--- Fake GPT Initialized (Type 'exit' to quit) ---")
    
    while True:
        try:
            # Get input from the user
            user_text = input("You: ")
            
            # Check if user wants to quit
            if user_text.lower() in ["exit", "quit"]:
                break
            
            # Generate and print the 'fake' response
            response = generate_response(user_text)
            print(response)
            
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            break
    
    print("\nShutting down Fake GPT.")

if __name__ == "__main__":
    main()