input = open("Day7/input.txt").read().splitlines()

# Divides rules into a list of tuples where the first value is the bag name and the second
#   is a dictionary with bags allowed in that bag as key, and number of those bags as value
rules = {}
for rule in input:
    r = rule.rstrip('.').split(" contain ")
    sub_bag_list = [] if r[1] == "no other bags" else r[1].split(", ")
    s = {(bs := bag.split(' ', 1))[1].rstrip('s') : bs[0] for bag in sub_bag_list}
    rules[r[0].rstrip('s')] = s

# Part 1
# Returns a set of bags (string) that can contain input bag (string) in any way
def can_contain(bag):
    bags = set()
    for b_r in rules:
        if bag in rules[b_r]:
            bags.add(b_r)
            for b in can_contain(b_r): bags.add(b)
    return bags
print(len(can_contain("shiny gold bag")))

# Part 2
def count_bags_in(bag):
    count = 0
    for b in (s_bags := rules[bag]):
        count += int(s_bags[b]) * (1 + count_bags_in(b))
    return count
print(count_bags_in("shiny gold bag"))

# Combined solution
part1 = len(can_contain("shiny gold bag"))
part2 = count_bags_in("shiny gold bag")
print("Part 1 solution: " + str(part1))
print("Part 2 solution: " + str(part2))
