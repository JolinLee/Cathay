import pymongo

myclient = pymongo.MongoClient("localhost:27017")
house_db = myclient["house_db"]


def save_house(house_list):
    house_coll = house_db['house_coll']
    house_coll.insert_many(house_list)

    return 1


def search_house(parm):
    house_filter = {}
    if ('region_name' in parm) and (parm['region_name'] != ''):
        house_filter['region_name'] = parm['region_name']
    if ('sex_requirement' in parm) and (parm['sex_requirement'] != 0):
        house_filter['sex_requirement'] = parm['sex_requirement']
    if ('phone' in parm) and (parm['phone'] != ''):
        house_filter['phone'] = parm['phone']
    if ('owner_sex' in parm) and (parm['owner_sex'] != 0):
        house_filter['owner_sex'] = parm['owner_sex']
    if ('landlord_first_name' in parm) and (parm['landlord_first_name'] != ''):
        house_filter['landlord_first_name'] = parm['landlord_first_name']
    if ('is_owner' in parm) and (parm['is_owner'] is not None):
        house_filter['is_owner'] = parm['is_owner']

    house_coll = house_db['house_coll']
    cursor = house_coll.find(house_filter)
    result = [i for i in cursor]
    return result
