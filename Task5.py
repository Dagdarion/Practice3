text = "1 2 3 4"
count = 0

for i in text.split():
        if i.isalpha():
            count += 1
        else:
            count = 0

print("True" if count == 3 else
      "False")