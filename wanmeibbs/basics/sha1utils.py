import base64
import collections
from typing import Optional

import orjson
from cryptography.exceptions import InvalidKey
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_der_private_key
from cryptography.hazmat.primitives.serialization import load_der_public_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey

__all__ = ['Sha1Utils']


class Sha1Utils:
    @staticmethod
    def signature(data: str, private_key: RSAPrivateKey) -> str:  # com.wanmei.basic.e.s.a
        """
        对数据进行SHA-1签名处理
        :param data: 待签名数据
        :param private_key: 私钥
        :return: 签名结果
        """
        signature = private_key.sign(
            data.encode('utf-8'),
            padding.PKCS1v15(),
            hashes.SHA1()
        )
        return base64.b64encode(signature).decode()

    @staticmethod
    def signParams(params: dict, b64_private_key: str) -> str:  # com.wanmei.basic.e.s.c
        """
        对URL参数字典进行SHA-1签名处理
        :param params: 待签名参数
        :param b64_private_key: base64格式私钥
        :return: 签名结果
        """
        sorted_params = collections.OrderedDict(sorted(params.items()))
        param_str = '&'.join([
            f'{k}={v if not isinstance(v, dict) else orjson.dumps(v).decode()}'
            for k, v in sorted_params.items()
        ])
        signature = Sha1Utils.signature(
            param_str, Sha1Utils.loadPrivateKey(b64_private_key)
        )
        return signature

    @staticmethod
    def signParamsString(params: str, b64_private_key: str) -> str:  # com.wanmei.basic.e.s.b
        """
        对URL参数字符串进行SHA-1签名处理
        :param params: 待签名参数
        :param b64_private_key: base64格式私钥
        :return:
        """
        return Sha1Utils.signature(
            '&'.join(sorted(params.split('&'))),
            Sha1Utils.loadPrivateKey(b64_private_key)
        )

    @staticmethod
    def loadPrivateKey(b64_private_key: str, password: Optional[str] = None) -> RSAPrivateKey:  # com.wanmei.basic.e.s.d
        """
        将base64编码的PKCS8格式的字符串转换为PrivateKey对象
        :param b64_private_key: base64编码的PKCS8格式的私钥字符串
        :param password: 私钥密码
        :return: RSAPrivateKey对象
        """
        private_key_ = load_der_private_key(base64.b64decode(b64_private_key), password=password)
        return private_key_

    @staticmethod
    def loadPublicKey(b64_public_key: str) -> RSAPublicKey:  # com.wanmei.basic.e.s.e
        """
        将base64编码的PKCS8格式的字符串转换为PrivateKey对象
        :param b64_public_key: base64编码的PKCS8格式的公钥字符串
        :return: RSAPublicKey对象
        """
        private_key_ = load_der_public_key(base64.b64decode(b64_public_key))
        return private_key_

    @staticmethod
    def verifySignString(after_sign: str, before_sign: str, public_key: RSAPublicKey) -> bool:  # com.wanmei.basic.e.s.f
        """
        验证签名数据
        :param after_sign: 待验证的签名后的base64字符串
        :param before_sign: 签名前的原始数据字符串
        :param public_key: RSAPublicKey对象
        :return: 验证结果
        """
        try:
            public_key.verify(
                base64.b64decode(after_sign),
                before_sign.encode('utf-8'),
                padding.PKCS1v15(),
                hashes.SHA1()
            )
            return True
        except InvalidKey:
            return False

    @staticmethod
    def verifySign(after_sign: str, params_before: dict, b64_public_key: str) -> bool:
        """
        验证签名参数
        :param after_sign: 待验证的签名后的base64字符串
        :param params_before: 签名前的原始数据字典
        :param b64_public_key: base64编码的PKCS8格式的公钥字符串
        :return: 验证结果
        """
        sorted_params = collections.OrderedDict(sorted(params_before.items()))
        param_str = '&'.join([f'{k}={v}' for k, v in sorted_params.items()])
        return Sha1Utils.verifySignString(
            after_sign=after_sign,
            before_sign=param_str,
            public_key=Sha1Utils.loadPublicKey(b64_public_key)
        )
