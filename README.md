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

### Example 3 with `Variables` and `Conditions`:

```python
import print64

x = 0
while x < 10:
      print(x)
      x += 1
```

Output:

```bash
MA==
MQ==
Mg==
Mw==
NA==
NQ==
Ng==
Nw==
OA==
OQ==
```

### Example 4 with `Variables`/`Conditions` and `Disable`/`Enable`:

```python
import print64

x = 0
while x < 10:
      if x % 2 == 0:
          print64.disable()
          print(x)
          print64.enable()
      else:
          print(x)
      x += 1
```

Output:

```bash
0
MQ==
2
Mw==
4
NQ==
6
Nw==
8
OQ==
```
