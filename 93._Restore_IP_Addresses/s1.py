class Solution:
    def restoreIpAddresses(self,s):



        res = []
        str_length = len(s)
        if str_length > 12:
            return res
        def generate_ip(i,dots,data):
            if dots == 4 and i == str_length:
                res.append(data[:-1])
                return res
            if dots > 4:
                return
            ip_length = min(i+3,str_length)
            for j in range(i,ip_length):
                if int(s[i:j+1]) <256 and (i ==j or s[i] !="0"):
                    generate_ip(j+1,dots+1,data+s[i:j+1 ]+".")
        generate_ip(0,0,"")
        return res




s = "25525511135"
print(Solution(). restoreIpAddresses(s))