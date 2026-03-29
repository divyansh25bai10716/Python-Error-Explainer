import pandas as pd

data = pd.read_csv("error_messages_explained.csv")
error_list = data["error_message"].astype(str).tolist()
explanation_list = data["explanation"].astype(str).tolist()

def explain_error(user_error):

    for i in range(len(error_list)):
        
        if error_list[i].lower() in user_error.lower():
            return explanation_list[i]

    return "New error detected — explanation not available."

print("Python Error Explainer")
print("type QUIT if no error")

while True:
    
    error = input("\nEnter error: ")

    if error.lower() == "quit":
        break

    print("\nExplanation:")
    print(explain_error(error))
