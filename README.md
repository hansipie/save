# Save

## Overview


`save` is a "tee-like" utility to pipeline saving of content, while keeping the output stream intact.

`SAVE_OUTPUT_PATH` environment variable needs to be set to define where you save.

## Packaging

Use pyinstaller to create a standalone executable.

```bash
$ pip install pyinstaller
$ pyinstaller --onefile save.py
```

## Usage

```bash
Usage: save [--help] [--silent] [filename]

save: a "tee-like" utility to pipeline saving of content, while keeping the output stream intact.

positional arguments:
  filename            filename to save the input. Use quotes if you have spaces. Resulting format is filename.txt by default

options:
  --ext           Custom file extension.
  --silent        Don't use STDOUT for output, only save to the file.
  --help          show this help message and exit.
```

## Examples

```bash
$ echo test | save output_file
test

$ cat {SAVE_OUTPUT_PATH}/output_file.txt
test
```

```bash
$ echo test | save --ext md output_file
test

$ cat {SAVE_OUTPUT_PATH}/output_file.md
test
```
