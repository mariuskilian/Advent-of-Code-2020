input = open("Day6/input.txt").read()
forms = input.split('\n\n')

# Naive solution
# Part 1
count = 0
for form_g in forms:
    yes = set([''.join(list(form)) for form in form_g.replace('\n', '')])
    count += len(yes)
print(count)

# Part 2
count = 0
for form_g in forms:
    form_g = sorted(form_g.split(), key=len)
    for c in form_g[0]:
        if all([c in form for form in form_g[1:]]):
            count += 1
print(count)

# Combined solution
part1 = 0
part2 = 0
for form_g in forms:
    part1 += len(set([''.join(list(form)) for form in form_g.replace('\n', '')]))
    sorted_form_g = sorted(form_g.split(), key=len)
    for c in sorted_form_g[0]:
        if all([c in form for form in sorted_form_g[1:]]): part2 += 1
print("Part 1 solution: " + str(part1))
print("Part 2 solution: " + str(part2))

# Advanced solution
# Part 1
print(sum([len(set([''.join(list(form)) for form in form_g.replace('\n','')])) for form_g in forms]))

#Part 2
forms_s = [sorted(forms_g.split(), key=len) for forms_g in forms]
print(sum([[all ([c in form for form in form_g[1:]]) for c in form_g[0]].count(True) for form_g in forms_s]))

# Combined solution
part1 = 0
part2 = 0
for form_g in forms:
    part1 += len(set([''.join(list(form)) for form in form_g.replace('\n','')]))
    form_g = sorted(form_g.split(), key=len)
    part2 += [all ([c in form for form in form_g[1:]]) for c in form_g[0]].count(True)
print("Part 1 solution: " + str(part1))
print("Part 2 solution: " + str(part2))