import json
import gzip

reviews_path = "reviews_Cell_Phones_and_Accessories_5.json.gz"
meta_path = "meta_Cell_Phones_and_Accessories.json.gz"

def num_users(data):
    myset = set([])
    count = 0
    for review in data:
        user = review["reviewerID"]
        if user not in myset:
            myset.add(user)
            count = count + 1
    return count

def num_products_reviewed(data):
    myset = set([])
    count = 0
    for point in data:
        product = point["asin"]
        if product not in myset:
            myset.add(product)
            count = count + 1
    return count

def num_reviews(data):
    return len(data)

def num_reviews_per_product():
    mydict = {}
    for review in reviews:
        asin = review["asin"]
        if asin in mydict:
            count = mydict[asin]
            mydict[asin] = count + 1
        else:
            mydict[asin] = 1
    return mydict

def num_reviews_per_user():
    mydict = {}
    for review in reviews:
        id = review["reviewerID"]
        if id in mydict:
            count = mydict[id]
            mydict[id] = count + 1
        else:
            mydict[id] = 1
    return mydict

def num_categories():
    return 0

def avg_purchase_per_user():
    rev_count = num_reviews_per_user()
    vals = rev_count.values()
    total = sum(vals)
    return total / users


def avg_reviews_per_product():
    prod_rev_count = num_reviews_per_product()
    vals = prod_rev_count.values()
    total = sum(vals)
    return total / len(meta)

def avg_rating_per_product():
    count = 0
    for review in reviews:
        rating = review["overall"]
        count = count + rating

    return count / len(reviews)


def parse(path):
  g = gzip.open(path, 'r')
  for l in g:
    yield eval(l)


if __name__ == '__main__':

    reviews = []
    for e in parse(reviews_path):
        reviews.append(e)

    meta = []
    for e in parse(meta_path):
        meta.append(e) 

    users = num_users(reviews)
    print("num users: ", users)
    
    print("num products: ", len(meta))

    print("num products reviewed: ", num_products_reviewed(reviews)) 

    rev = num_reviews(reviews)
    print("num reviews: ", rev)
    
    print("avg reviews per product: ", avg_reviews_per_product())

    print("avg reviews/purchases per user: ", avg_purchase_per_user())

    print("avg rating per reviewed products: ", avg_rating_per_product())

    print("done!")