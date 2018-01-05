#变位词检测  某个单词是另一个单词的重新排列组合
#假设字符串相同且由26个小写字母组成
def anagram_solution1(s1, s2):
    a_list = list(s2)
    pos1 = 0
    still_ok = True
    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(a_list) and not found:
            if s1[pos1] == a_list[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        if found:
            a_list[pos2] = None
        else:
            still_ok = False
        pos1 = pos1 + 1
    return still_ok

#解法2：排序后比较字符串
#解法3：暴力匹配，穷举可能的字符串 性能最差
#解法4：统计两个单词字符出现次数
def anagram_solution4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord("a")
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1
    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False
    return still_ok

print(anagram_solution1("abcd", 'dcba'))
print(anagram_solution4("abcd", 'dcba'))