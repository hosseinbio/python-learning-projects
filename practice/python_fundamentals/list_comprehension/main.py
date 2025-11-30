numbers = list(range(1, 51))
seleted_nums = [i for i in numbers if (i**2)%2 == 0]

sentence = "Python makes bioinformatics easier"
letters = [len(word) for word in sentence.split()]

items = [12, "ATG", 3.5, "Gene", True, "DNA"]
strs = [i for i in items if isinstance(i, str)]

print(seleted_nums)
print(letters)
print(strs)
