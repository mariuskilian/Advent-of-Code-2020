input = open("Day14/input.txt").read().splitlines()

# Part 1
mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
memory = {}

def apply_mask_p1(val):
    global mask
    return ''.join([mask[i] if mask[i] in '01' else val[i] for i in range(len(val))])

def parse_mem_p1(line):
    global memory
    addr = int(line.split()[0].rstrip(']')[4:])
    val = apply_mask_p1(f'{int(line.split()[2]):036b}')
    memory[addr] = int(val, 2)

def parse_input_p1(input):
    global mask
    for line in input:
        if line.startswith('mask'): mask = line[7:]
        if line.startswith('mem'): parse_mem_p1(line)

parse_input_p1(input)
print(sum(memory.values()))

# Part 2
mask = '0000000000000000000000000000000000000'
memory = {}

def apply_mask_p2(mem):
    global mask
    addr = ''.join(mask[i] if mask[i] in '1X' else mem[i] for i in range(len(mem)))
    floating_idxs = []
    for i in range(len(addr)): floating_idxs.append(i) if addr[i] == 'X' else []
    addresses = []
    for float_val in range(pow(2, len(floating_idxs))):
        addresses.append(addr)
        for i in range(len(floating_idxs)):
            a = addresses[float_val]
            f_i = floating_idxs[i]
            addresses[float_val] = a[:f_i] + str((float_val >> i) & 1) + a[f_i+1:]
    return addresses

def parse_mem_p2(line):
    global memory
    addresses = apply_mask_p2(f'{int(line.split()[0].rstrip("]")[4:]):036b}')
    for addr in addresses: memory[addr] = int(line.split()[2])

def parse_input_p2(input):
    global mask
    for line in input:
        if line.startswith('mask'): mask = line[7:]
        if line.startswith('mem'): parse_mem_p2(line)

parse_input_p2(input)
print(sum(memory.values()))