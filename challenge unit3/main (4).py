"""Write a function called linear_search_product that takes the list of products and a target product name as input. The function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found."""
def linearSearchproduct(productList,targetproduct):
  indices=[]
  for index, product in enumerate(productList):
    if product == targetproduct:
      indices.append(index)
  return indices
products = ["shoes","boot","loafer","shoes","sandal","shoes"]
target = "shoes"
target2 = 'apple'
result = linearSearchproduct(products,target)
print(result)

  