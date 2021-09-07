# Covert Channel #2 - /tmp file

This covert channel is based on the following rules:
1. Create a file `touch /tmp/tmp_cc`
2. Modify permission masks on the file to encode covert message:
- `644` : An acknowledgement flag placed to indicate bit read / write
- `766` : An acknowledgement flag to indicate a transmission of complete ASCII message
- `664` : Bit 1 
- `666` : Bit 0

## Usage
### Prerequisites
Ensure a file is first created on `/tmp/tmp_cc`
```commandline
touch /tmp/tmp_cc
```
### Receiver
```commandline
python3 tmp_receiver.py
```
### Sender
```commandline
python3 tmp_sender.py
```

## Output
```commandline
rajeev@rajeev-laptop:/mnt/d/rit/PycharmProjects/CSEC.750.Covert.Comm/tmp_cc$ python3 tmp_sender.py
Enter your message: Hello World, this is Rajeev Karuvath
Enter your message: Four score and seven years ago our fathers brought forth upon this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this. But, in a larger sense, we can not dedicate, we can not consecrate, we can not hallow, this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us, that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion,that we here highly resolve that these dead shall not have died in vain, that this nation, under God, shall have a new birth of freedom,and that government of the people, by the people, for the people, shall not perish from the earth.
```
```json
rajeev@rajeev-laptop:/mnt/d/rit/PycharmProjects/CSEC.750.Covert.Comm/tmp_cc$ python3 tmp_reciever.py
{   'calculated_throughput': '7.261625 kbits/sec',
    'received_bits': 288,
    'received_message': 'Hello World, this is Rajeev Karuvath',
    'time_taken': '0.038731 secs'}
{   'calculated_throughput': '8.391428 kbits/sec',
    'received_bits': 11672,
    'received_message': 'Four score and seven years ago our fathers brought '
                        'forth upon this continent, a new nation, conceived in '
                        'Liberty, and dedicated to the proposition that all '
                        'men are created equal. Now we are engaged in a great '
                        'civil war, testing whether that nation, or any nation '
                        'so conceived and so dedicated, can long endure. We '
                        'are met on a great battle-field of that war. We have '
                        'come to dedicate a portion of that field, as a final '
                        'resting place for those who here gave their lives '
                        'that that nation might live. It is altogether fitting '
                        'and proper that we should do this. But, in a larger '
                        'sense, we can not dedicate, we can not consecrate, we '
                        'can not hallow, this ground. The brave men, living '
                        'and dead, who struggled here, have consecrated it, '
                        'far above our poor power to add or detract. The world '
                        'will little note, nor long remember what we say here, '
                        'but it can never forget what they did here. It is for '
                        'us the living, rather, to be dedicated here to the '
                        'unfinished work which they who fought here have thus '
                        'far so nobly advanced. It is rather for us to be here '
                        'dedicated to the great task remaining before us, that '
                        'from these honored dead we take increased devotion to '
                        'that cause for which they gave the last full measure '
                        'of devotion,that we here highly resolve that these '
                        'dead shall not have died in vain, that this nation, '
                        'under God, shall have a new birth of freedom,and that '
                        'government of the people, by the people, for the '
                        'people, shall not perish from the earth.',
    'time_taken': '1.358343 secs'}
```

## Performance Evaluation
Throughput metrics were captured by :
- Calculating number of bits transferred over the covert channel
- A timer was started when the first bit was received
- The timer was closed when the `MESSAGE` flag was placed, and the time difference was calculated
- Throughput was calculated by the following formula : `number_of_bits` / `time_difference`
- Messages of varying lengths were sent

### Results
On an average, a throughput of `8 kbps` was achieved