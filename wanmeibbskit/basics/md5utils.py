import hashlib
from typing import Any, Mapping

from wanmeibbskit.consts import Salts

__all__ = ['MD5Utils']


class MD5Utils:  # com.wanmei.tiger.zx2.utils.h
    @staticmethod
    def getParamsStringHash(params_string: str) -> str:  # h.a
        """
        使用MD5对URL参数字符串进行哈希处理(内置盐)
        :param params_string:
        :return: 哈希结果
        """
        return MD5Utils.hashParamsString(salt=Salts.COMMON, params_string=params_string)

    @staticmethod
    def hashParamsString(salt: str, params_string: str) -> str:  # h.b
        """
        使用MD5对URL参数字符串进行哈希处理
        :param salt: 盐值
        :param params_string: 待哈希参数
        :return: 哈希结果
        """
        text = ''.join(
            param_.split('=')[1] for param_ in
            sorted(params_string.split('&'))
        )
        print(text)
        return MD5Utils.md5Hash(
            text + salt
        )

    @staticmethod
    def hashParams(salt: str, params: Mapping[str, Any]) -> str:  # h.c
        """
        使用MD5对URL参数进行哈希处理
        :param salt:
        :param params:
        :return: 哈希结果
        """
        return MD5Utils.md5Hash(
            text=''.join(param_[1] for param_ in sorted(params.items(), key=lambda x: x[0])) + salt
        )

    @staticmethod
    def getParamsHash(params: Mapping[str, Any]) -> str:  # h.d
        """
        使用MD5对URL参数字典进行哈希处理(内置盐)
        :param params: 待哈希参数
        :return: 哈希结果
        """
        return MD5Utils.hashParams(salt=Salts.COMMON, params=params)

    @staticmethod
    def md5Hash(text: str) -> str:  # h.e
        """
        使用MD5对数据进行哈希处理
        :param text: 待哈希数据
        :return: 哈希结果
        """
        return hashlib.md5(text.encode('utf-8')).hexdigest()
