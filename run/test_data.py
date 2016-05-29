#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

__author__ = 'yinzishao'

"""
测试api 的虚拟数据
"""

RUNNING_RESULT = {
    "id": "1",
    "token": "ss",
    "run": {
        "distance": "222.22",
        "duration": "30.22",
        "locations": [
            {
                "longitude": "100.2",
                "latitude": "100.2",
                "time": "1464273280"
            },
            {
                "longitude": "200.3",
                "latitude": "200.3",
                "time": "1464273290"
            },
            {
                "longitude": "300.5",
                "latitude": "300.5",
                "time": "1464273310"
            }
        ]
    }
}

RUNNING_MUL_RESULT = {
    "id": "1",
    "token": "ss",
    "run": [
        {
        "distance": "222.22",
        "duration": "30.22",
        "locations": [
            {
                "longitude": "100.2",
                "latitude": "100.2",
                "time": "1464273280"
            },
            {
                "longitude": "200.3",
                "latitude": "200.3",
                "time": "1464273290"
            },
            {
                "longitude": "300.5",
                "latitude": "300.5",
                "time": "1464273310"
            }
        ]
        },
        {
        "distance": "222.22",
        "duration": "30.22",
        "locations": [
            {
                "longitude": "100.2",
                "latitude": "100.2",
                "time": "1464273280"
            },
            {
                "longitude": "200.3",
                "latitude": "200.3",
                "time": "1464273290"
            },
            {
                "longitude": "300.5",
                "latitude": "300.5",
                "time": "1464273310"
            }
        ]
        }
    ]
}

RUNNING_RESULT_2={
    "id": "1",
    "token": "1b5aXp:ZT1dNurOZHOKRellL-FxtDRYH18",
    "run": {
        "distance": "24.27618026733398",
        "duration": "4",
        "locations": [
            {
                "longitude": "37.32888846",
                "latitude": "122.02686653",
                "time": "1464522773.159730"
            },
            {
                "longitude": "200",
                "latitude": "200",
                "time": "200"
            },
            {
                "longitude": "300",
                "latitude": "300",
                "time": "300"
            }
        ]
    }
}
# RUNNING_MUL_RESULT.append(RUNNING_RESULT)
# RUNNING_MUL_RESULT.append(RUNNING_RESULT)
# RUNNING_MUL_RESULT.append(RUNNING_RESULT)

avatar="""<89504e47 0d0a1a0a 0000000d 49484452 0000003a 0000003a 08060000 00e1bb4a 28000000 01735247 4200aece 1ce90000 001c6944 4f540000 00020000 00000000 001d0000 00280000 001d0000 001d0000 060dd3f6 a0540000 05d94944 41546805 cc99696c 15651486 9bf84b83 4b1457dc c10d45a1 b55516ad 16d04a6b 6bb1528b ad54aca8 84485414 4544c4b5 2c8a6d6c 409b5690 da526cb1 d0d022c5 8d54311a 139226fa 5bff1824 26161392 f34defeb fbdd996f 663a77bf b76dbcc9 6192b9d3 649efb9e f39ef31d b2d4b4d3 a1a69f01 9533012a ef2ca899 6743cd39 072aff5c a8828950 f3cf8714 5e005574 11a4e412 a8b24990 f2cb2015 9743165f 09a9be0a 523319f2 f814c8b2 6b214f5f 0f597103 64e554c8 7337415e b819f2d2 2d905766 40d66543 5ebf15f2 662ee49d db201b6f 876c9905 d93a1bd2 7007a431 1fb2fd2e 48d3dd90 96b9909d f321adf7 40da0b21 7bee8374 1541ba8b 21fb4b20 bda59083 6590c30b 215f9743 be7b0832 500139fa 30e4a7c5 905faa20 c7aa2183 4b20bfd6 206b24e8 99514195 0f541282 5e17009d 36b6a0fd 06745112 a033622b 2a545415 5ee82a9a 3ce88d8e a2a980de e9285ae0 283acf51 f45e4fd1 2fa8680f 153de028 9a12a89b ba4145cf 0ba76e66 8a065337 274eea1a d040eab6 f940fda9 fb2553d7 054d2375 c5ad5103 9a8ea2e9 d4680c50 7f8d1a45 4d8dc604 7d245e8d 06cd2812 34b11905 6b34a868 3c330a82 9ad43566 b400a241 fd661413 34053312 c77575ea 8ae3bac9 d7a85134 951a4dc3 755dd00c cd48b717 63468aed 2579d031 30a34eb6 9798a99b 0c684c33 9a08db75 33513498 bac99891 715dd347 639891ee a3aea2a3 6446e9a7 6e1034c9 1a6d4e30 3044b497 20683433 8ad9473d 3332a0e3 6e46bbfc 93512a66 140d3446 ea8e8e19 a5a2e8b8 99517060 b0675d63 467ad61d 1f33e2c0 104e5db6 97b0a24e 8dfacd28 22759331 23377523 41ff1766 e49f8c4c 1f8d000d d668127d 34d164a4 e29e5e46 69608867 4666d68d 3b0246ab 5157517b 328a066a cc28f9d4 3503432a 351a9c8c d85efc66 6452574f 46091535 a08fa676 4cd3a07a 60185bd7 cdc48cd2 48dde0c1 3bbe195d ed1cbcaf 710ede26 75339c8c 8c19850f dee36846 66c33022 752bb969 a8ba82a0 dc342c25 f013dc32 3c45e015 dc32e80d c3b38c55 dc32ace6 bcbb865b 86e086a1 8e5b86cd 3321ef73 cb503f07 f221b70c dba86ac4 86c101d5 1b066346 094f2f49 9891a7a8 1918bc55 8a945d0a 553e0952 3905ea31 8e73b59c 7496e572 85924740 bef84abe f833d309 c9d5c96a befc1ac6 5a02bcc6 eb7a7ee7 5fa56ce1 a8b79503 4103411a 7942d9ce 75491361 9a3918c4 5ba56833 d2a0e99b 91dd5ea2 9991a728 7be922aa 579a05c9 66cc62e4 33e63116 308a184b 194f322a 19358c5a c672c68b a741de98 cd83377f 90b7f903 bdca7beb 181b186f 31ea189b 19f58c66 fe087a67 e437a394 143566b4 24be1909 97637a32 1ad9472f a69a5c84 1148bd5c 0dabb713 d6813dbc 32fa9ceb 57dd500d aba0ea9f 87f5ed3e 58fdbcdf bf1b56cf 4750db96 5365426c e0926c53 01acc33b 61fdd00d ebfb2e58 47f7c2fa 91d79ff9 37039f42 7650d51d 1c1c5aa9 b6ffe0ed df30643a d47ba96b 262393ba dc0456b0 e672b260 b5bc8758 1feb1bbe f4a1ce88 af4396c0 3af23997 65fca11a 1e44e8d4 50c433fa 46e8d43f 04a48bb6 30dd5b99 ceed51cc 28a24633 9c8cecf3 a80daa4a 3428dd34 8fa01fd7 d92f393c 0c98b0ac f03deb10 15ec6db3 bfd7f742 7c4687f3 519fad87 bc9b8dd0 d009fbce b0f38cbe f2131a3a 4ec07282 b2b63568 b4c92802 34a3f6e2 99913d30 388ae612 b469a3fd 92fe7f35 303fe174 ed6bb7bf f101c201 b18e74b2 562720f4 efdfce33 a111d7d0 c9132341 8da2c1bd 6e5c33aa 8ab23372 27a34466 e4812a03 eabc63f8 4d5dd00e d66c10d4 7bd0ea69 a4f94cf6 813a6a87 ec674227 ff0a80d2 913bf402 bb980b6c 3aeefefb 4777328a 34234e47 ba4699ba 49833af0 702086ff f88d6634 956da518 5ab9f0c7 f9ce3c13 011a4e5d c275d2a0 f6d2897b d85a4637 753d3332 a96b40dd d4f584b2 6b956f6e f5fb14d5 a046a9e3 bfb33639 cf86cd68 a157a3b1 403fd135 4a357753 c576fe5d 174da9af 16b28fc0 bd0fd8ff 25e1ae52 3230234f 51b3d7f5 148d0faa db8d93ba 41450707 206bd962 3e284d0c dac29edb c6bdd02e f6dd8eb9 18fe7310 ea185b4f 27a7af3e 9acf41c2 baa0f1cd e83f0000 00ffff65 de567000 00056449 444154cd 99fb6f14 551cc59b f813c657 00012518 dfa28882 952a0aa2 55a00a16 d1daf210 4189a246 c1986848 d06283d2 d8881a89 22522c36 6081522c 69430b34 52515a5f ad0a048d 863fc060 0cc157fc ded93d9e 79dcceee ecececcc ec1a4bf2 dd9d9d3b 2dfbb9e7 dc73bf33 2d52e387 404d3813 aaf82ca8 92b3a126 9f0b35e5 3ca86943 a14a8741 a69f0f55 3602326b 14a49c55 752d6452 118cfa3a 58ff92f6 9bf59a48 586f4657 338cceed f680730e 49f742b5 ab0eb276 1c927ffc 665f93b4 7f4e5f93 fcfd2464 db0390c6 3248c338 484b2512 274f58d7 aabecdfc 7c35a4b3 12b2ef3e 48d7fd90 83159043 0f420e57 41be9807 f97a01a4 ff21c8f7 8b20c716 437e5882 223f5049 015516e8 48280754 8502dde9 826a08f3 6bea89e8 6985ac19 1e0cdac4 2ffa5e11 54db7224 4fff624f 085f553f 417773b2 3b09b66f 6e00e8c2 20d073d2 14154751 49515455 71864b4c 455fb3ff 73f3cbeb 320ceb9c 7160078c 8e267bdc 3ca7c713 cef897ed 9057c710 e057e777 f0bc3921 ce78f234 15dd380c 6aef8b48 fe75caf9 3dca7a57 7df52141 b5a20f67 57d4b5ee 70d88a8e 70159d37 1e524cd0 2d6fd85f c0e7d5e8 6e85d1d5 e233629f 32faf743 5e1905fc f3a7ef35 c9bf4fc1 e86bf61d 53df7e48 eb8ef5b1 2ead9cd3 ba13f51a 4d575495 6a506ddd 0ba02aae 80cca0a5 5e5e8644 6f37123d 9fd8d57b 909f79dc 7f186a53 0dd4fbab 91f8ae07 89af78ee 1b5e6756 1faf39c2 71678d1a 543671f4 731847ba 611cfd14 8963ace3 9ff1f800 8ce3bcfe e75e183f 72eca743 3ce6f913 fcd9ee6a c89e6990 0eaecd40 eb6a4503 d6a8aba8 378c2e84 cc65555e 0a995364 5958a6f2 bd943593 359b55ce 5aca5ac6 5ac87a84 f518eb49 d633ac15 ac978642 6a6f8654 f378356b 0d6b2dab 8eb58eb5 9ef50e6b 03ab9ed5 c06a3c03 f2d110da b614d23e 07b29795 2f68f630 32414753 d5d190f9 9741165f 0f797402 4126429e b801f254 31612641 965f0779 96632f10 66e564c8 aa5b0875 2ba4660a 2d7b1bd7 273fd796 405ebf1d f2e69d90 b7ef22d8 7486cf0c c82626ed 66d696bb 215b6713 ee5ec88e 72c82e26 ecc70c9f 3d3c6ee3 b98e5ca0 b1c268a4 b3bdd8a0 523186db cc459005 17431651 dd25845e 4a4b3f7e 2595e3fa 799af1bf 82a1f51c d3f17942 af24f42a 4e463527 a3e646c2 72326a6f a2829c88 75847e8b 93b07e2a e45d5a72 23e1eba9 5a0327a0 91f0db08 bf9de0cd 04df3d8b a0846f23 6c4e506d dd106124 5ca3e9fb a81fe825 0ee8e50e e8550ee8 350e28c3 2b3428d5 b640eff0 076d0902 2d681845 01d58ac6 01d58ad2 d296a233 6d454dd0 562adaee a76818d0 d09d5114 50ada8d7 ba5cc759 ad9b45d1 26073496 750352d7 2f8cec16 300e681c 457dacbb d3b34673 a66e8430 327b5db3 619032bd 8fc601f5 2a1a1446 5e45b575 53c2c8b4 6ea4300a 50d4dd47 07711865 281a668d 0e7446de bb176f67 1445d17c c2485b97 8a6e35b7 171d46f7 b8615468 50bdbdd8 772f5140 f309239d ba7a1ff5 84914edd fd41772f 7a1f0db0 6e61c328 e61afd20 a0613041 3314e56d 5b5a53ef 174603d6 f536f56e 18c54fdd 98a05667 a4adabc3 c8b1ae19 46a14173 7446c227 0c7e9d91 62af9bde 02e6ea8c a280ea16 50af516d 5d0d1ad4 197915f5 b3ee80a2 83288c2c ebeaed45 87514a67 94a1689e a9abc3c8 b4ae2a8f 12463a75 bd8a86e9 8c728451 e1f7517b 8dba0fc7 a280664b dd900d43 ae3032ef 5e025337 308cbcd6 75c3a870 db4b48d0 bc6fd334 688c308a 66dd388a fa8491d5 30308ccc 5eb785a9 1bf97e34 601fcd6c 01e3f4ba 7a8de6d3 d4ff0f61 645a379a a21a349f 30f2809a b769ff4d 531f1c46 ca7a9452 c87d34e5 ee255718 656c2fde 7d54afd1 54eb7af6 51bf1670 d085512c d02c4f18 f4937a73 7b096fdd b19e6746 5eeb06a5 ae378cb4 757567e4 0923dfed 65beefdf 5efe0558 b8ab32fd a6900a00 00000049 454e44ae 426082>"""

USER_INF={
    "token":"1b5aXp:ZT1dNurOZHOKRellL-FxtDRYH18",
    "id":"1",
    # "user_avatar":avatar,
    "user_height":"170",
    "user_weight":"55",
    "user_sex":"男",
    "user_birth":"1995-1-18",
    "realname":"中心及"
}

MONTH_REQUEST={
    "token":"1b5aXp:ZT1dNurOZHOKRellL-FxtDRYH18",
    "id":"1",
    "month":"2016-5"

}

UPLOAD_PIC={
    "token":"1b6gYD:8P3oqpq5RYVwlfh9epdTUvp3lwU",
    "id":"16",
    "avatar":avatar
}

UPLOAD_PIC_2={
    "token":"1b5aXp:ZT1dNurOZHOKRellL-FxtDRYH18",
    "id":"1",
    "avatar":avatar
}



WALK ={
    "id":"1",
    "walk":["222","333"],
    "time":"2016-05"
}

PWD={
    "token":"1b5aXp:ZT1dNurOZHOKRellL-FxtDRYH18",
    "id":"1",
    "old_password":"yinzishao",
    "new_password":"yinzishao"
}

RANK={
    "token":"1b5aXp:ZT1dNurOZHOKRellL-FxtDRYH18",
    "id":"1",
    "running_result_id":"12",

}
