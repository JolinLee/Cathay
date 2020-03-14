import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
house_db = myclient["house_db"]

def save_house(house_list):
    house_coll = house_db['house_coll']
    house_coll.insert_many(house_list)

    return 1

def search_house(parm):
    house_filter = {}
    if ('aa' in parm) and (parm['aa'] != ''):
        house_filter['aa'] = parm['aa']

    house_coll = house_db['house_coll']
    result = house_coll.find(house_filter)
    return result