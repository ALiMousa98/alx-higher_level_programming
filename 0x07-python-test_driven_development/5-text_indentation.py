def text_indentation(text):
    """Prints a text with 2 new lines after each occurrence of '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':', '\n', '']
    result = ""
    line = ""
    
    for char in text:
        line += char

        if char in punctuation:
            result += line.strip() + '\n' 
            line = ""

    if line:
        result += line.strip()

    print(result)
