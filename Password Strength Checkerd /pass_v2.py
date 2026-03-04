from zxcvbn import zxcvbn

password = input("Enter your password: ")

result = zxcvbn(password)

score = result["score"]
feedback = result["feedback"]

print("\nPassword Strength Score:", score, "/ 4")

if score == 0:
    print("Strength: Very Weak ❌")
elif score == 1:
    print("Strength: Weak ⚠️")
elif score == 2:
    print("Strength: Fair ⚠️")
elif score == 3:
    print("Strength: Good ✅")
elif score == 4:
    print("Strength: Strong 🔒")

# Suggestions
if feedback["warning"]:
    print("\nWarning:", feedback["warning"])

if feedback["suggestions"]:
    print("\nSuggestions:")
    for suggestion in feedback["suggestions"]:
        print("-", suggestion)
