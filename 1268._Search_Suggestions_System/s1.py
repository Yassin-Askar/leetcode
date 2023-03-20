class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()
        res = []
        l, r = 0, len(products) - 1
        for i in range(len(searchWord)):
            prods = []
            char = searchWord[i]
            while l <= r and (len(products[l]) <= i or products[l][i] != char):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != char):
                r -= 1
            res.append([])
            remain = r - l + 1
            for j in range(min(3, remain)):
                res[-1].append(products[l+j])
        return res


products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"
print(Solution(). suggestedProducts(products=products, searchWord=searchWord, ))
