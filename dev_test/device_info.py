from wanmeibbs.basics.device_generator import get_rand_device

if __name__ == "__main__":
    print(
        get_rand_device(
            app_id="10021",
            channel_id=1991,
            sub_app_id="com.wanmei.tiger"
        ).json()
    )
