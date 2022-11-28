import random
place = ["瑜家山", "紫菘", "沁苑", "东九", "西十二", "西五", "南一", "韵苑", "东十二", "绝望坡", "集贸", "主图",
         "湖溪河",
         "科技楼", "百景园", "梧桐雨", "中操", "西操", "东操", "韵体", "西体", "光体", "西八", "国光", "启明",
         "工训中心", "小吃街"]

animal = ["鼠鼠", "野猪", "的蛇", "浣熊", "松鼠", "单身狗", "的猫", "白狐", "孔雀", "梅花鹿", "大黄牛", "白鹭",
          "小黄鸭", "大白鹅", "柯基", "吉娃娃", "哈士奇", "藏獒", "腊肠犬", "野鱼", "猫猫虫", "牧羊犬"]

def generate_name_animal(post_id, user_id):
    random.seed(post_id + user_id)
    name1=random.choice(place)
    random.seed(post_id + user_id)
    name2=random.choice(animal)
    return name1 + name2