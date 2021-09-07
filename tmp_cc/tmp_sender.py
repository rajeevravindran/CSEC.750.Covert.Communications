import os

mask_mapping = {
    "FLAG": 0o644,
    "1": 0o664,
    "0": 0o666,
    "MESSAGE": 0o766
}  # Unix permission masks used for encoding the message, and to indicate state of reception / transmission

TMP_CC_FILE_LOCATION = "/tmp/tmp_cc"  # Location of file used to encode the permission bits on

while True:
    tmp_cc_stat = os.stat(TMP_CC_FILE_LOCATION)  # Read file properties
    permission_mask = oct(tmp_cc_stat.st_mode)[-3:]  # Extract file permissions
    covert_message = input("Enter your message: ")  # Read covert text from user input
    for each_bit in "".join([format(ord(c), '08b') for c in covert_message]):  # convert covert text to stream of 8 bit ASCII
        os.chmod(TMP_CC_FILE_LOCATION,mask_mapping[str(each_bit)])  # Apply permission mask based on bit, i.e 1 => 664, 0 => 666
        while True:
            new_permission_mask = oct(os.stat(TMP_CC_FILE_LOCATION).st_mode)[-3:]
            if new_permission_mask == "644":  # Wait for receiver to acknowledge if reading is complete
                break
    os.chmod(TMP_CC_FILE_LOCATION,mask_mapping["MESSAGE"])  # Apply permission mask to indicate entire message has been sent
