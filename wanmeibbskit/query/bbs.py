from typing import Union

from wanmeibbskit.basics.client import WanmeiBBSClient
from wanmeibbskit.utils.safely_getters import secure_json_retrieve
from wanmeibbskit.utils.decorators import method_need_login


class BBSApp(WanmeiBBSClient):
    @method_need_login
    async def roleList(self, uid: int) -> Union[dict, None]:
        resp_ = await self.client.post(
            '/game/roleList',
            params={
                "uid": uid,
                "oneAppId": 1256,
            }
        )
        print(resp_.headers, resp_.url.params)
        print(self.device_info)
        return secure_json_retrieve(resp_, restrict_status_code=True)
