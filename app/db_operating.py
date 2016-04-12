import pymongo


def get_coll():
    client = pymongo.MongoClient("localhost", 12345)
    db = client.users
    return db


class User(object):
    def __init__(self, stu_id, wechat_id, library_password, zhengfang_password):
        self.stu_id = stu_id
        self.wechat_id = wechat_id
        self.library_password = library_password
        self.zhengfang_password = zhengfang_password

    def save(self):
        user_info = {
            "stu_id": self.stu_id,
            "wechat_id": self.wechat_id,
            "library_password": self.library_password,
            "zhengfang_password": self.zhengfang_password
        }
        coll = get_coll()
        id = coll.users.insert(user_info)
        print id
        return user_info

    @staticmethod
    def check_if_binding(wechat_id):
        flag = get_coll().users.find_one({"we_chat": wechat_id})
        if flag is not None:
            return True
        else:
            return False

    @staticmethod
    def cancel_building(wechat_id):
        get_coll().users.remove({"we_chat": wechat_id})

    @staticmethod
    def query():
        users = get_coll().users.find()
        for i in users:
            print i
        return users
