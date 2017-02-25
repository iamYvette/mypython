#coding=utf-8
# 做为AppleStoreApp独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用python如何生成200个激活码（或者优惠券）
import random,string
def random_coupon(count,length):
    forSelect = string.ascii_letters+"0123456789"
    for x in range(count):
        coupon=""
        for y in range(length):
            coupon += random.choice(forSelect)
        print(coupon)

if __name__=="__main__":
    random_coupon(200,20)