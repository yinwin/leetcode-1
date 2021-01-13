'''
给定一个较长字符串big和一个包含较短字符串的数组smalls，设计一个方法，根据smalls中的每一个较短字符串，对big进行搜索。输出smalls中的字符串在big里出现的所有位置positions，其中positions[i]为smalls[i]出现的所有位置。

示例：

输入：
big = "mississippi"
smalls = ["is","ppi","hi","sis","i","ssippi"]
输出： [[1,4],[8],[],[3],[1,4,7,10],[5]]
提示：

0 <= len(big) <= 1000
0 <= len(smalls[i]) <= 1000
smalls的总字符数不会超过 100000。
你可以认为smalls中没有重复字符串。
所有出现的字符均为英文小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/multi-search-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        
        bi = big
        if len(smalls) == 0:
            positions = [[]]
        else:
            positions=[[] for j in range(len(smalls))]
        for i in range(len(smalls)):
            big = bi
            a = -1
            c = smalls[i]
            b = big.find(c)
            while smalls[i]!= '' and b != -1:
                a += b + 1
                positions[i].append(a)
                big = big[b+1:]
                b= big.find(c)
        return positions