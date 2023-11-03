def unencrypted(input_message = ""):
  if not input_message:
    return ""

  message = ""
  counter = {}

  for word in input_message.split(" "):
    counter[word] = counter.get(word, 0) + 1

  for key, value in counter.items():
    message += key + str(value)

  return message

if __name__ == "__main__":
  enter = input("Insert the message: ")

  print("Message: ", unencrypted(enter))