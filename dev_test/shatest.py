from wanmeibbs.consts import TigerAPPConsts
from wanmeibbs.basics.sha1utils import Sha1Utils


if __name__ == "__main__":
    params = 'circleId=1&deviceInfo={"buildVersion":"105","phoneSystemVersion":"13","device_model":"M2102J2SC",' \
             '"device_type":"Xiaomi","version":"9.0.5","deviceId":"29f540fe16b446fbb56dbb73a1573c41","appId":"10' \
             '021","osType":"2","packageName":"com.wanmei.tiger","channelId":"1991","subAppId":"com.wanmei.tiger' \
             '"}&roleId=62200000000&timestamp=0&uid=100000000'
    foo = Sha1Utils.signParamsString(params, TigerAPPConsts.RSA_PRIVATE_KEY)
    print(foo)
