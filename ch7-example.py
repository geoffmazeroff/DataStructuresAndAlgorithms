def find_needle(needle, haystack):
    needle_index = 0
    haystack_index = 0

    # The original code in the book didn't subtract out the length of the needle, meaning
    # find_needle("cd", "abc") would get an index out of range error.
    while haystack_index < len(haystack) - len(needle):
        if needle[needle_index] == haystack[haystack_index]:
            found_needle = True

            while needle_index < len(needle):
                if needle[needle_index] != haystack[haystack_index + needle_index]:
                    found_needle = False
                    break
                needle_index += 1
        
            if found_needle: return True

            needle_index = 0
        haystack_index += 1
    
    return False

print(find_needle("ghi", "abcdefgh"))