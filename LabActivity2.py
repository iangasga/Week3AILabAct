students_in_line = [
    {"name": "Marco", "minutes_left": 8, "items": 2, "teacher_pass": False},
    {"name": "Diane", "minutes_left": 15, "items": 1, "teacher_pass": False},
    {"name": "Kyle", "minutes_left": 5, "items": 6, "teacher_pass": False},
    {"name": "Ella", "minutes_left": 20, "items": 5, "teacher_pass": True},
]

def check_fast_lane(minutes_left, items, teacher_pass):
    if teacher_pass:
        return "Fast lane approved"
    elif minutes_left < 10 and items <= 3:
        return "Fast lane approved"
    else:
        return "Use regular line"

approved = 0

for student in students_in_line:
    result = check_fast_lane(
        student["minutes_left"],
        student["items"],
        student["teacher_pass"]
    )

    print(student["name"], "-", result)

    if result == "Fast lane approved":
        approved += 1
    else:
        print("Minutes left:", student["minutes_left"])
        print("Suggestion: Use regular line.")

print("Total approved:", approved)

print("\nExplanation:")
print("Rule-based systems need override rules for special cases.")
print("Ella is approved because she has a teacher's pass.")
print("If the program checks time and items first, she may be rejected.")
print("The teacher's pass should be checked before the normal rules.")
print("This helps the program give the correct result.")
print("If the cafeteria is closed for cleaning, that rule should come first.")
print("In that case, nobody can use the fast lane.")
print("The highest priority rule should always be checked first.")
