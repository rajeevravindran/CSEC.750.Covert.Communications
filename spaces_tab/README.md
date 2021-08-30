# Covert Channel #1

This covert channel is based on the following rules:
1. `\t` or a tab represents a `1`
2. ` `or a space represents a `0`
3. Each character is encoding by above scheme using its 8-bit ASCII code.

## Usage
### Generating covert message encoded channel 
Syntax
```commandline
python3 "OVERT_TEXT_FILE_NAME" "COVERT_MESSAGE"
```
Example
```commandline
D:\apps\python\37\python.exe D:/rit/PycharmProjects/CSEC.750.Covert.Comm/spaces_tab/write_comm.py overt_text.txt "Covert message by alphanerd"
[*] 'Covert message by alphanerd' embedded inside 'overt_text.txt_out.txt' !
```
### Reading covert message encoded channel 
Syntax
```commandline
python3 read_comm.py "COVERT_TEXT_FILENAME" 
```
Example
```commandline
D:\apps\python\37\python.exe D:/rit/PycharmProjects/CSEC.750.Covert.Comm/spaces_tab/write_comm.py overt_text.txt "Covert message by alphanerd"
[*] 'Covert message by alphanerd' embedded inside 'overt_text.txt_out.txt' !
```

## Limitations
1. `write_comm.py` requires `OVERT_TEXT_FILE_NAME` contain same or more number of overt lines as compared to number of characters in `COVERT_MESSAGE`