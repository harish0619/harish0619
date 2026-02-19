from typing import Any

user_prompt = ""

todos: list[Any] = []

# As long as the condition is true, the statements inside while will be executed.
# This is called a loop.

while True:
    user_action: str = input("Type add, show or exit:").strip()

    # If nothing matches the condition below, loop will continue
    match user_action:
        case "add":
            todo = input("Enter a todo: ").strip()
            todos.append(todo)
        # Alternative to shows can be added like this. BITWISE OR operator
        # case "show" | "display":
        case "show":
            for item in todos:
                print(item)
        case "exit":
            break
        # case _: # This is to match anything else a user types by mistake
        #     print("You entered an unknown action!")
        #     continue

print("Goodbye!")



