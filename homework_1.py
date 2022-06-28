import ipaddress
import itertools
import math


def domain_name(url):
    clean_url = url.replace('http://', '').replace('https://', '').replace('www.', '')  # Get rid of protocol and prefix
    dot_idx = clean_url.index('.')  # Find first dot in clean URL
    return clean_url[:dot_idx]


def int32_to_ip(int32):
    result = str(ipaddress.IPv4Address(int32))  # Since ipaddress is a built-in module starting 3.3, I think we are fine
    return result


def zeros(n):
    x = n // 5  # Since each 5! adds 1 trailing zero to result, divide by 5
    trailing_zeros = x
    while x > 0:  # Continue dividing while you can
        x /= 5
        trailing_zeros += int(x)
    return trailing_zeros


def bananas(s) -> set:
    result = set()
    pattern = 'banana'
    enumerated_characters = list(enumerate(s))
    for iteration in itertools.combinations(enumerated_characters, len(pattern)):  # itertools you say?
        characters_list = list(s)  # Convert original string to list for further character replacing
        if ''.join(item[1] for item in iteration) == pattern:
            for idx, character in enumerate(s):  # Compare enumerated characters from original string
                if (idx, character) not in iteration:
                    characters_list[idx] = '-'  # And replace character with '-'
            result.add(''.join(characters_list))
    return result


def count_find_num(primes_list, limit):  # Change argument name according to PEP 8
    result = []
    length = len(primes_list)
    go_on = True
    # Expand length of primes_list and evaluate the product of primes combinations while you can
    while go_on:
        go_on = False
        for item in itertools.combinations_with_replacement(primes_list, length):
            product = math.prod(item)  # Built-in module, once again
            if product <= limit and len(set(item)) >= len(primes_list):
                result.append(product)
                go_on = True
        length += 1
    return [len(result), max(result)] if result else result
