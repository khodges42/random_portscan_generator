from scapy import data
import random
import string

TCP_REVERSE = dict((scapy.data.TCP_SERVICES[k], k) for k in scapy.data.TCP_SERVICES.keys())

def find_service(port):
    if int(port) in TCP_REVERSE:
        return TCP_REVERSE[int(port)]
    else:
        return None

def random_service():
    port = random.choice(list(TCP_REVERSE.keys()))
    return (port, TCP_REVERSE[port])

def generate_box(subnet=56, hostname="sensenet_"):
    VOWELS = "aeiou"
    CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))
    c_ports = [21,22,23,25,53,67,137,138,443]
    ports = []
    for i in range(random.randint(1,10)):
        if i % 2 == 0:
            hostname += random.choice(CONSONANTS)
        else:
            hostname += random.choice(VOWELS)
            
    for i in range(random.randint(1,10)):
        rc=random.choice(c_ports)
        ports.append((rc,find_service(rc)))
    ports = ports+ [random_service() for x in range(random.randint(1,15))]

    return {hostname:{"ports":ports}}
        
        
print({"scan":[generate_box() for x in range(random.randint(1,4))]})
