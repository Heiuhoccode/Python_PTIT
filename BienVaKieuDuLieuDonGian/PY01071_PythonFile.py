nameFile = input().lower()
print("yes") if nameFile[len(nameFile)-3::] == ".py" else print("no")
