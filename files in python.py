def manage_notes(filename="notes.txt"):
  """
  A function to perform various operations on a text file.

  Args:
      filename (str, optional): The name of the text file. Defaults to "notes.txt".

  Returns:
      None
  """

  def read_entire_text():
    """Reads the entire content of the text file."""
    try:
      with open(filename, 'r') as file:
        content = file.read()
      return content
    except FileNotFoundError:
      print(f"Error: File '{filename}' not found.")
      return None

  def insert_line(line_to_insert, position="end"):
    """Inserts a line into the text file at a specified position.

    Args:
        line_to_insert (str): The line to be inserted.
        position (str, optional): The position where to insert. Defaults to "end".
            Valid options are "beginning" or "end".
    """
    try:
      with open(filename, 'r+') as file:
        content = file.readlines()
        if position == "beginning":
          content.insert(0, line_to_insert + "\n")
        elif position == "end":
          content.append(line_to_insert + "\n")
        else:
          print(f"Invalid position: '{position}'. Valid options are 'beginning' or 'end'.")
          return
        file.seek(0)
        file.writelines(content)
    except FileNotFoundError:
      print(f"Error: File '{filename}' not found.")

  def count_lines():
    """Counts the number of lines in the text file."""
    try:
      with open(filename, 'r') as file:
        return sum(1 for _ in file)
    except FileNotFoundError:
      print(f"Error: File '{filename}' not found.")
      return 0

  def find_longest_words():
    """Finds the longest words in the text file and returns them as a list."""
    try:
      with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        longest_words = [max(words, key=len)]  # Find one longest initially
        for word in words:
          if len(word) == len(longest_words[0]):
            longest_words.append(word)
        return longest_words
    except FileNotFoundError:
      print(f"Error: File '{filename}' not found.")
      return []

  def append_text(text_to_append):
    """Appends text to the end of the text file."""
    try:
      with open(filename, 'a') as file:
        file.write(text_to_append)
    except FileNotFoundError:
      print(f"Error: File '{filename}' not found.")

  def display_text():
    """Reads and displays the entire content of the text file."""
    content = read_entire_text()
    if content:
      print(content)
    else:
      print(f"File '{filename}' is empty.")

  # Call the desired functions based on user input
  while True:
    print("\nMenu:")
    print("1. Read Entire Text")
    print("2. Insert Line")
    print("3. Count Lines")
    print("4. Find Longest Words")
    print("5. Append Text")
    print("6. Display Text")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
      text = read_entire_text()
      if text:
        print(text)
    elif choice == '2':
      line_to_insert = input("Enter the line to insert: ")
      position = input("Insert at (beginning/end)? ").lower()
      insert_line(line_to_insert, position)
    elif choice == '3':
      line_count = count_lines()
      print(f"Number of lines: {line_count}")
    elif choice == '4':
      longest_words = find_longest_words()
      if longest_words:
        print(f"Longest word(s): {', '.join(longest_words)}")
      else
