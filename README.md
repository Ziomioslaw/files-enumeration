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

Require editing main file.

Use main class:

```python
renamer = EnumerationAdder()
renamer.convertFilesNameFromPath('/home/ziomioslaw/filestobeenumare', 'txt')
```

Then run:

```bash
$ python files-enumeration.py
```

## Removing logging

You can add logger class in constructor,

```python
EnumerationAdder(NonLogger())
```
