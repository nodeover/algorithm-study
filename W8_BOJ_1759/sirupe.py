def test():
    import re
    from itertools import combinations
    password_count, str_count = map(int, input().split())
    chars = sorted(input().split())
    vowel_re = re.compile("[aeiou]")
    for comb in combinations(chars, password_count):
        comb = ''.join(comb)
        vowel_count = len(vowel_re.findall(comb))
        if vowel_count == 0 or password_count - vowel_count < 2:
            continue
        print(comb)
