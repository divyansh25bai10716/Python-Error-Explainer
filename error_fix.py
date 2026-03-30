import pandas as pd

csv_file = "error_messages_explained.csv"

data = pd.read_csv(csv_file)

error_list = data["error_message"].astype(str).tolist()
explanation_list = data["explanation"].astype(str).tolist()


def explain_error(user_error):

    for i in range(len(error_list)):
        if error_list[i].lower() in user_error.lower():
            return explanation_list[i]

    print("\nNew error detected!")
    user_explanation = input("Please enter explanation for this error: ")

    new_data = pd.DataFrame({
        "error_message": [user_error],
        "explanation": [user_explanation]
    })

    new_data.to_csv(csv_file, mode='a', header=False, index=False)

    error_list.append(user_error)
    explanation_list.append(user_explanation)

    return "New error saved successfully!"


print("Python Error Explainer")
print("Type QUIT if no error")

while True:

    error = input("\nEnter error: ")

    if error.lower() == "quit":
        break

    print("\nExplanation:")
    print(explain_error(error))
