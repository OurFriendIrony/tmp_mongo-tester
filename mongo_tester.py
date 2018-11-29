from pymongo import MongoClient
import pprint

PORT = 3306
ENV = "aat6"
HOSTS = ["gpc-mongodb-1.%s.soa.indev01.aws.travisperkins.cloud:3306" % (ENV),
         "gpc-mongodb-2.%s.soa.indev01.aws.travisperkins.cloud:3306" % (ENV),
         "gpc-mongodb-3.%s.soa.indev01.aws.travisperkins.cloud:3306" % (ENV)]

DB = "pricetask_DB_uat_config"

USER = "pricetask_rw_uat"
PASSWORD = ""
REPLICASET = "bc0gpcrs11"

client = MongoClient(
    "mongodb://%s:%s@%s/%s?replicaSet=%s" % (
        USER,
        PASSWORD,
        ",".join(HOSTS),
        DB,
        REPLICASET
    )
)

db = client[DB]
posts = db.posts

collection = db.get_collection('config').find_one({"_id": 'gpcDbConfig'})

pprint.pprint(client.address)
pprint.pprint(collection)

#db.copyDatabase("pricetask_DB_uat_config", "pricetask_DB_uat_config", "gpc-mongodb-2.aat1.soa.indev01.aws.travisperkins.cloud:3306", "pricetask_ro_uat", "PASSWORD");


