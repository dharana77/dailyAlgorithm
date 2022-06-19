def solution(s):
    answer = ""
    for idx, target in enumerate(s):
        if target.isdigit():
            answer += target
        else:
            if s[idx:idx+4] == "zero":
                answer += "0"
            elif s[idx:idx+3] == "one":
                answer += "1"
            elif s[idx:idx+3] == "two":
                answer += "2"
            elif s[idx:idx+5] == "three":
                answer += "3"
            elif s[idx:idx+4] == "four":
                answer+="4"
            elif s[idx:idx+4] == "five":
                answer+="5"
            elif s[idx:idx+3] == "six":
                answer+="6"
            elif s[idx:idx+5] == "seven":
                answer+="7"
            elif s[idx:idx+5] == "eight":
                answer+="8"
            elif s[idx:idx+4] == "nine":
                answer+="9"
    return int(answer)