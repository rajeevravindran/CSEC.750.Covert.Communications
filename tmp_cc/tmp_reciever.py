import os
from datetime import datetime
from pprint import pprint

mask_mapping = {
    "FLAG": 0o644,
    "1": 0o664,
    "0": 0o666,
    "MESSAGE": 0o766
}  # Unix permission masks used for decoding the message, and to indicate state of reception / transmission

TMP_CC_FILE_LOCATION = "/tmp/tmp_cc"  # Location of file used to encode the permission bits on
buffer_message = []  # Start a buffer to store received message bits
current_time = datetime.now()  # start initial timer
first_bit = True  # A flag indicate reception of first bit of the message


def bit_array_to_string(bit_array):
    """
    This function converts an array of bits to corresponding ASCII representation
    :param bit_array: An array of bits representing a ASCII string (e.g HI => [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1])
    :return: str
    """
    return "".join(chr(int("".join(map(str, bit_array[i:i + 8])), 2)) for i in range(0, len(bit_array), 8))


while True:
    tmp_cc_stat = os.stat(TMP_CC_FILE_LOCATION)  # Read file properties
    permission_mask = oct(tmp_cc_stat.st_mode)[-3:]  # Extract file permissions
    if permission_mask == "766":  # Check if new message received
        time_taken = (datetime.now() - current_time).total_seconds()  # Calculate time taken to receive all bits since first bit
        decoded_message = bit_array_to_string(buffer_message)  # Convert buffer to string
        if len(decoded_message) > 0:
            pprint({
                "received_message": decoded_message,
                "received_bits": len(buffer_message),  # Calculate number of bits of received message
                "time_taken": "%s secs" % time_taken,
                "calculated_throughput": "%f kbits/sec" % ((len(buffer_message) / time_taken) / 1024)  # Calc throughput
            }, indent=4)  # Print transmission stats
        buffer_message = []
        first_bit = True
    elif permission_mask != "644":  # Check if ready to read a bit
        if permission_mask == "664":  # Check if Bit 1 encoding
            # print(1)
            buffer_message.append(1)
        if permission_mask == "666":  # Check if Bit 0 encoding
            # print(0)
            buffer_message.append(0)
        if first_bit:
            current_time = datetime.now()  # If this is the first bit since MESSAGE flag is set, start timer
            first_bit = False
        os.chmod(TMP_CC_FILE_LOCATION, mask_mapping["FLAG"])  # Set flag to indicate successful reception
    # print(permission_mask)
