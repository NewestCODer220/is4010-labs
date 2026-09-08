# Lab 02 CLI comparison journal

Do not include passwords, tokens, API keys, or complete authentication output.

## Tool check

### GitHub Copilot CLI

State that you installed and authenticated the tool, then record only its version or another non-sensitive verification detail. Yes

### Antigravity CLI

State that you installed and authenticated the tool, then record only its version or another non-sensitive verification detail. Yes

## Shared task

### Shared prompt

```text
Do not create or edit any files. Suggest a Python implementation for the function below and briefly explain your approach.

def count_vowels(text: str) -> int:
    """Count a, e, i, o, and u without regard to case; do not count y."""
```

### Copilot CLI observations

Copilot suggested checking each character after converting it to lowercase. It used a generator expression with `sum()` to count the characters found in `"aeiou"`. This approach handles uppercase and lowercase vowels while excluding y. I questioned whether the generator expression might be difficult for a beginner to understand at first. I would verify its accuracy using lowercase, uppercase, mixed-case, empty-string, and no-vowel test cases.


### Antigravity CLI observations

Antigravity suggested creating a set containing both lowercase and uppercase vowels, `"aeiouAEIOU"`, and then using a generator expression with `sum()` to count every matching character. I questioned whether listing both cases was necessary because each character could instead be converted to lowercase. I would verify that the function correctly handles lowercase vowels, uppercase vowels, mixed-case words, empty strings, consonants, spaces, numbers, punctuation, and the letter y. I would also run the provided automated tests before selecting this implementation.


### Comparison

Copilot suggested converting each character to lowercase and checking whether it appears in `"aeiou"`. It used `sum()` with a generator expression to count the vowels. Antigravity created a set containing lowercase and uppercase vowels with `set("aeiouAEIOU")` and counted the matching characters. Both approaches appear correct because they count uppercase and lowercase vowels without including y. Copilot’s response was shorter and easier for me to understand. Antigravity provided more technical detail by explaining set lookups and efficiency. Neither approach made assumptions about the input beyond the required string type. I selected Copilot’s approach because converting each character to lowercase clearly shows how case is handled and avoids listing every vowel twice. Overall, Copilot was more useful for this small beginner-level function, although both suggestions should produce the required result.


## Test-guided implementation

Before finalizing the implementation, I manually inspected each function against its written contract and considered several possible inputs. For `make_greeting`, I checked that the result would include the supplied name and follow the exact `"Hello, NAME!"` format, including capitalization, the comma, space, and exclamation point. For `is_even`, I verified that using the remainder operator would return `True` when a number is divisible by two and `False` otherwise. For `count_vowels`, I checked lowercase vowels, uppercase vowels, consonants, the letter y, an empty string, and text containing spaces or punctuation. This inspection influenced me to use Copilot’s lowercase approach because it handles both uppercase and lowercase text clearly. No revision was necessary during the manual inspection because the selected logic matched all three function contracts. I would confirm this conclusion by running the provided pytest grader.


## Preferred tool combination

Each tool fits a different part of my workflow. A browser chat is most helpful when I need a concept explained step by step or want to ask follow-up questions without changing repository files. GitHub Copilot in VS Code is useful for receiving suggestions while I am actively writing code. Copilot CLI helps when I want an agent to examine the repository and answer questions without leaving the terminal. Antigravity CLI serves a similar purpose, but during this comparison it provided a more detailed technical explanation. I currently prefer using browser chat to understand the assignment and Copilot CLI or Copilot in VS Code to work with the repository. My choice could change if Antigravity consistently finds mistakes that the other tools overlook or gives clearer suggestions for more complex programming tasks.

