from keen.client import keenClient
from config import *
from pymongo import MongoClient


client = MongoClient('mongodb://40.78.151.253:27017/')

db = client.stocks
tweets = db.tweets

client = keenClient(
    project_id = "5607e40a90e4bd64cce7a519",
    write_key = "b35b65d73d01d668d5c2a46803019978052886134cfe6444c9e48133dd48e21f0b28d1dd06f6d2b0291c75c6893e2fe1a60f5a3d4f6de28b9afad5a3e3f0e51a46aeb7a67289eec62ac215fe18412bede8c84995ff1d135946cc5bcdde2651abcacd555a16b7464473c3ab02c11520d9",
    read_key = "d43177a53fe2eea6152212b95ec8fe626c4f20aec9faec5dcd422f3b0de77ec520d035b7b2547ac12df2db55a9bd301af57db1bf48d2865bbe25b135650a036b71c953e3510ee5ef772154ead7bf9126d66f3dca51f2ab62f7ced9f966041c36a9fd8779e847ffb1151aa8000b61b873",
    master_key = "C92821DA1EACC8FBA57F376E767B2878"
)

client.add_event({'stuff':list(tweets.find({'name':'IBM'}))});
