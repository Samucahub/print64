# Print64

A Python library that automatically converts all output from `print()` to Base64.
For people who enjoy a good challenge.

## Installation

```bash
pip install print64
```
---

## How To Use

### Example 1:

```python
import print64

print("Hello World!")
```

Output:

```bash
SGVsbG8gV29ybGQh
```

### Example 2 with `Disable`:

```python
import print64

print64.disable()
print("Hello World!")
```

Output:

```bash
Hello World!
```
