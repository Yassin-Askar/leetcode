class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


address = "255.100.50.0"
print(Solution(). defangIPaddr(address=address, ))
