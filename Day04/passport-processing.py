import string

input = open("Day4/input.txt").read()

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional_fields = ["cid"]

# Part 1
def has_all_req_fields(passport):
    fields = [field.split(':')[0] for field in passport.split()]
    for req in required_fields:
        if req not in fields:
            return False
    return True
    
num_valid_passports = 0
passports = input.split("\n\n")
for passport in passports:
    if has_all_req_fields(passport): num_valid_passports += 1
print(num_valid_passports)

# Part 2
def is_field_valid(field_type, field_input):
    if field_type in optional_fields: return True
    if field_type not in required_fields: return False
    # Birth Year, Issue Year, Expiration Year
    elif field_type in ["byr", "iyr", "eyr"]:
        if not field_input.isdigit() or len(field_input) != 4: return False
        if field_type == "byr": return 1920 <= int(field_input) <= 2002
        if field_type == "iyr": return 2010 <= int(field_input) <= 2020
        if field_type == "eyr": return 2020 <= int(field_input) <= 2030
    # Height
    elif field_type == "hgt":
        # Check for valid format
        if len(field_input) <= 2: return False
        hgt_unit = field_input[-2:]
        hgt_value = field_input[:-2]
        if not hgt_value.isdigit(): return False
        # Check for valid input
        if hgt_unit == "cm" and 150 <= int(hgt_value) <= 193: return True
        if hgt_unit == "in" and 59 <= int(hgt_value) <= 76: return True
        return False
    # Hair Color
    elif field_type == "hcl":
        if len(field_input) != 7 or field_input[0] != '#': return False
        return all(c in string.hexdigits for c in field_input[1:])
    # Eye Color
    elif field_type == "ecl":
        return field_input in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    # Passport ID
    elif field_type == "pid":
        return len(field_input) == 9 and all(c in string.digits for c in field_input)

def all_fields_valid(passport):
    for field in [fields.split(':') for fields in passport.split()]:
        if not is_field_valid(field[0], field[1]): return False
    return True

num_valid_passports = 0
passports = input.split("\n\n")
for passport in passports:
    if has_all_req_fields(passport) and all_fields_valid(passport): num_valid_passports += 1
print(num_valid_passports)

# Combined solution
part1 = 0
part2 = 0
passports = input.split("\n\n")
for passport in passports:
    if has_all_req_fields(passport):
        part1 += 1
        if all_fields_valid(passport): part2 += 1
print("Part 1 solution: " + str(part1))
print("Part 2 solution: " + str(part2))