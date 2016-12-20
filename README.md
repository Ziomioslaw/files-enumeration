# Files enumeration

Script for adding enumeration in filenames. Including with padding zeros. Written in Python 3.

# Example of work

It will turn files from

```bash
aaaa.txt
bbbb.txt
cccc.txt
```

into:

```bash
01.txt
02.txt
03.txt
```

# Usage:

```bash
$ python files-enumeration.py
Usage: <directory with files> <extension files>
```

Example:

```bash
$ python files-enumeration.py /home/ziomioslaw/filestobeenumare txt
```

## Removing logging

You can add logger class in constructor,

```python
EnumerationAdder(NonLogger())
```
