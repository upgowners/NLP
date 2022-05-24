def FA(s):
    if len(s) < 3:
        return "Rejected"
    if s[0] == '1':
        if s[1] == '0':
            if s[2] == '1':
                for i in range(3, len(s)):
                    if s[i] != '1':
                        return "Rejected"
                    return "Accepted"  # if all 4 nested if true
                return "Rejected"  # else of 3rd if
            return "Rejected"  # else of 2nd if
        return "Rejected"  # else of 1st if


inputs = ['1', '10101', '101', '10111',
          '01010', '100', '', '10111101', '1011111']
for i in inputs:
    print(FA(i))
