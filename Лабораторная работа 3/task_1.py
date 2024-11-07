# bijN2g6W/06q+q1HhgujbwEiXA0kqiOQ5b4RugC0yG6opWy9w6dEOR9FxkZPUdePH7Usv05z8W4R1lQJdQo9IIVeN33NOLWbURDZUK8s8yqyCA6+IDbLvLz4R9nhXGIIw7FiTtaavidvw3Dr6VCF9mhNV/eqe3oBsypDOi/+aptMq+2JjgY8u8VxJJIKg//iSv1Ec+we7IOK8u5QEK3nPkxjPbC7q6Y0G8WfQSzFSCsHrRZLtvclSjlFY2RMctHZTCee9NeP2huShMFNDqJzEiwCLy66LWGXxpoqAnLdjne7Qa2vuiQRTUQ0+JDLfhiKIx8DeRQ7NbF/V93KScbGV71j0xUGS5EA9zI9XgfgmkAtCkaMdvSi8HSQMUfhV4ACs8Ro50sct0enoeCZgDZN9paLdjtIkKlKyc/DAdnOQCpMdBOjST9sYzVMYsWx97/uhRx28XWzsSdUM8HUKtmk9NxWOfdyYKRT6mFOLTVB8XcvpjydC6GHdFEeAB8RnvYBsotxj25mD1jp6UkthWBdSMDtW3TuvVM/GCfMfy71cMfuSuha6aEH+WOkXcslNdXb7v7JCi4Rl9zAbkJd6KbeGMxKPt/B7u4hzKV3Kb1cubYbqkCoM9WOV3kh04HMxXy672o4DIZsUqWMYiOaB2ow4RyHcq4N8O917NOkHwFqbtKsb4aioWb1ck2Lup4zxIAKvGYcUsWfDz35QRb6SnD2sQKlRdJJaDqcC40jrnrteiLJep/5Il0VM6olxO7ktkhEXidR4qJH6Aj+pnO5pgMPcwD33KoGGCIFjuKQAaN9TEQ=

# Поиск индекса элемента в списке товаров


def search_product(list_, name):
    for i, product in enumerate(list_):
        if product == name:
            return i
    return None


product_list = ["Зельц", "Картофель белый", "Каша гречневая",
         "Каша перловая", "Сало вареное", "Сало вареное",
         "Печень куриная", 'Яблоко "Голден"', "Зельц"]

print("В наличии:")
for product in product_list:
    print(product)
print("\nВведите товар для поиска: ")
name = input()

print("Искомый товар", '"'+name+'"', "находится под индексом",
      search_product(product_list, name))
