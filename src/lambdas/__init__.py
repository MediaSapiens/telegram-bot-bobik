# -*- coding: utf-8 -*-

import json
import random
import telegram


bot = telegram.Bot(token='TOKEN')


def bobik(event, context):
    update = telegram.Update.de_json(event, bot)
    chat_id = update.message.chat.id
    text = update.message.text.encode('utf-8')
    bot.sendMessage(chat_id=chat_id, text=u'Зацени бобика!')
    bot.sendPhoto(chat_id=chat_id, photo=random.choice(dog_urls))

dog_urls = [
    "https://drscdn.500px.org/photo/72620283/q%3D80_h%3D450/8ca93a5455d3796800294d676d2dbe67",
    "https://drscdn.500px.org/photo/76226477/q%3D80_h%3D450/52a959530c4825313b3c44eabc8433f2",
    "https://drscdn.500px.org/photo/5892762/q%3D80_h%3D450/67f1f996f6d8a08bd23087aee32e4b66",
    "https://drscdn.500px.org/photo/90268349/q%3D80_h%3D450/f28479e5dc9ac830807f2117a5cf2229",
    "https://drscdn.500px.org/photo/28060921/q%3D80_h%3D450/98159c583eb523a5ba5943dcaeda005e",
    "https://drscdn.500px.org/photo/5892542/q%3D80_h%3D450/50b30595221a42a85dde93fa0012919a",
    "https://drscdn.500px.org/photo/142585301/q%3D80_h%3D600/c0e72a9726e86cf561cafa82cb62f341",
    "https://drscdn.500px.org/photo/82892433/q%3D80_h%3D600/c21df06570e69d4b32f101ce779f19c2",
    "https://drscdn.500px.org/photo/95593837/q%3D80_h%3D600/b7a69f2055eb19a57682e05dc67b9022",
    "https://drscdn.500px.org/photo/48964844/q%3D80_h%3D450/7df5050089105490a89e9b7d5c97c904",
    "https://drscdn.500px.org/photo/98826023/q%3D80_h%3D450/b1e31c8b8e05c39d86f68094dcecd25f",
    "https://drscdn.500px.org/photo/93637389/q%3D80_h%3D450/ab15e9d81e7fd6839b40921e251a53b0",
    "https://drscdn.500px.org/photo/100068253/q%3D80_h%3D450/7c18bb64331b77a310c7faae1c743b41",
    "https://drscdn.500px.org/photo/81280023/q%3D80_h%3D450/d802f76ff694544cb36d077822822fee",
    "https://drscdn.500px.org/photo/188901623/q%3D80_h%3D450/baee83c71badd09234586c0de1de0181",
    "https://drscdn.500px.org/photo/99129945/q%3D80_h%3D450/2bfe573d7ade0883976393c78d5a60d4",
    "https://drscdn.500px.org/photo/99242785/q%3D80_h%3D450/71e989b18201fb702ebbba5e744f8bd7",
    "https://drscdn.500px.org/photo/99248557/q%3D80_h%3D450/7c2b8bf77f18440a4792e4d4940dae6c",
    "https://drscdn.500px.org/photo/137147679/q%3D80_h%3D450/dfa1c5884f179c49e7a6cd308c981f93",
    "https://drscdn.500px.org/photo/192929655/q%3D80_h%3D450/0c633cd4c19b305a139cd8af90ac24e7",
    "https://drscdn.500px.org/photo/103037415/q%3D80_h%3D450/a673f86f41ba84f52f40229b54be7639",
    "https://drscdn.500px.org/photo/76096165/q%3D80_h%3D450/90e523e5f235fb7faf3de494d1ec1108",
    "https://drscdn.500px.org/photo/125067049/q%3D80_h%3D450/b422dfacb9e3c39ac3c83f14e383ff84",
    "https://drscdn.500px.org/photo/115270351/q%3D80_h%3D450/b3c281a045e8d2ddfef6a809c6524b8d",
    "https://drscdn.500px.org/photo/108454481/q%3D80_h%3D450/5628ca2445dcc1177c66cdb1c170db31",
    "https://drscdn.500px.org/photo/59383330/q%3D80_h%3D450/cbc80a95bc51d925bd5470e1c4ccf0f6",
    "https://drscdn.500px.org/photo/126831757/q%3D80_h%3D450/fd4599b0f4a5f86e3fd78b1617ada848",
    "https://drscdn.500px.org/photo/140850047/q%3D80_h%3D450/20eaa561f1247c1313b5d2a3a379c3e3",
    "https://drscdn.500px.org/photo/92802071/q%3D80_h%3D450/190f70adaac0ae6e0e4bf9def7a7b046",
    "https://drscdn.500px.org/photo/74063881/q%3D80_h%3D600/ac16f40c46c708455cdf24465cd6b2eb",
    "https://drscdn.500px.org/photo/81731091/q%3D80_h%3D600/c72e4014a7f9c807e13589dfbeae2826",
    "https://drscdn.500px.org/photo/146102015/q%3D80_h%3D600/7436db2ac47dc5090c956f2ac09604c1",
    "https://drscdn.500px.org/photo/108499625/q%3D80_h%3D600/969fc144cfd5c5d8602e905b34aacee5",
    "https://drscdn.500px.org/photo/3877490/q%3D80_h%3D600/544cbf46346a77aab2a8704c9427a69f",
    "https://drscdn.500px.org/photo/77933995/q%3D80_h%3D600/556e10332880fe5af4400d4cd2c47859",
    "https://drscdn.500px.org/photo/148271329/q%3D80_h%3D450/1b8470fcf016c3e912ee673656d78f95",
    "https://drscdn.500px.org/photo/94796387/q%3D80_h%3D450/f42b2fb5de4a295be64184d1ca6815fb",
    "https://drscdn.500px.org/photo/66509129/q%3D80_h%3D450/a45752bc3f547cbee0c2c5dfbdcfeadb",
    "https://drscdn.500px.org/photo/59271904/q%3D80_h%3D450/893231ece1c6dcf8a30c7e0ece2338f9",
    "https://drscdn.500px.org/photo/83005605/q%3D80_h%3D600/f31478c88d8a45b416dd28ceffdbf0a0",
    "https://drscdn.500px.org/photo/100239993/q%3D80_h%3D600/170fa704c031f361878e3bb838c78cf7",
    "https://drscdn.500px.org/photo/80553665/q%3D80_h%3D600_k%3D1/34f84c8f90e223cdac34f8708a291e36",
    "https://drscdn.500px.org/photo/130258353/q%3D80_h%3D450/9b1e0f55f880b65ddd1d21919781df87",
    "https://drscdn.500px.org/photo/80798119/q%3D80_h%3D450/63eed47e1cb445ed20a3f434149d421d",
    "https://drscdn.500px.org/photo/37961472/q%3D80_h%3D450/dc7e6999d4b5c3c2608981d1bafec1c4",
    "https://drscdn.500px.org/photo/92977825/q%3D80_h%3D450/f9fa1dc72ff6f502cdd6afbe29e869f1",
    "https://drscdn.500px.org/photo/85648721/q%3D80_h%3D450/fa759bb36b889c3e0210566ef1d2153b",
    "https://drscdn.500px.org/photo/104552655/q%3D80_h%3D450/9d6fb23ab2b7ea4a340beb6a9cfd711e",
    "https://drscdn.500px.org/photo/90543023/q%3D80_h%3D450/84b7076e9b24640d239a3709e45c044a",
    "https://drscdn.500px.org/photo/112128287/q%3D80_h%3D450/8c5208bcc792ebda6b588f0f1c8f9ad9",
    "https://drscdn.500px.org/photo/109086727/q%3D80_h%3D450/f7aeea39dc15ae50a996301f4a096398",
    "https://drscdn.500px.org/photo/98923679/q%3D80_h%3D450/93bd0b06dcd56938447d280c11e41190",
    "https://drscdn.500px.org/photo/91935261/q%3D80_h%3D450/a7b55b0f7171c6fc0178db384183929a",
    "https://drscdn.500px.org/photo/114755995/q%3D80_h%3D450/2967f3fa02a0191a3f5ce9b8e6f711e4",
    "https://drscdn.500px.org/photo/116916261/q%3D80_h%3D450/dc34b6dcc88d78e6806c79a621cd3c09",
    "https://drscdn.500px.org/photo/91896303/q%3D80_h%3D450/39cd5229400d41d3fdb433643e9abac4",
    "https://drscdn.500px.org/photo/80553661/q%3D80_h%3D450/61f17b137c454c9b51fe9e5ae9a0e13b",
    "https://drscdn.500px.org/photo/91056999/q%3D80_h%3D450/6e8868b191c90a09db8b08fb2db384db",
    "https://drscdn.500px.org/photo/108365781/q%3D80_h%3D600/1cd5081e37a83dd4447552a222f829d8",
    "https://drscdn.500px.org/photo/116916669/q%3D80_h%3D600/20762ff59b893fc83069010d34dec434",
    "https://drscdn.500px.org/photo/22273167/q%3D80_h%3D600/3186359c61b6e0d219bd2c8b8e3c3a3b",
    "https://drscdn.500px.org/photo/96399775/q%3D80_h%3D600/cb55d440a25719ddd3918cb4c50aa81f",
    "https://drscdn.500px.org/photo/108618181/q%3D80_h%3D450/05c4aa3c1a7958dafb1b9f9ae8df9b09",
    "https://drscdn.500px.org/photo/72986253/q%3D80_h%3D450/c4fadc67791895e7ccc1f6aeef8de56b",
    "https://drscdn.500px.org/photo/78845307/q%3D80_h%3D450/95ef59837e937eecef6a4cf2c72162a3",
    "https://drscdn.500px.org/photo/76359987/q%3D80_h%3D450/0d7dc53f247466ef01a911e72c6e181a",
    "https://drscdn.500px.org/photo/126121925/q%3D80_h%3D450/19a4cd0223fc49d40a4a2519223d9277",
    "https://drscdn.500px.org/photo/89530483/q%3D80_h%3D450/878e1417747891bc8294d18653510b4e",
    "https://drscdn.500px.org/photo/81241355/q%3D80_h%3D600/b34a16d1b73056dde1482bea89b36d44",
    "https://drscdn.500px.org/photo/75732705/q%3D80_h%3D600/14527b080761540732172ecb0caf3a8d",
    "https://drscdn.500px.org/photo/98232415/q%3D80_h%3D450/cec86f7a27806c62d0de3ed68d58acf7",
    "https://drscdn.500px.org/photo/123708111/q%3D80_h%3D450/a84727775c2fd3e607607787bef5fc0f",
    "https://drscdn.500px.org/photo/75439559/q%3D80_h%3D450/d5af5f0e7e9ff555e7c7640fc948153d",
    "https://drscdn.500px.org/photo/124319341/q%3D80_h%3D450/6769f5ba5fe2f49df1dfa1636af26a29",
    "https://drscdn.500px.org/photo/106720885/q%3D80_h%3D450/0bc9b943b85ca065d1b12d53a9eaed03",
    "https://drscdn.500px.org/photo/109127397/q%3D80_h%3D450/f4a6b7038365c12e9d5c0cbd44e5edc2",
    "https://drscdn.500px.org/photo/76220529/q%3D80_h%3D450/78eff6f3a707f66193525c071a2e1c8c",
    "https://drscdn.500px.org/photo/193501529/q%3D80_h%3D450/36359e691182c6aa23b721103696e77b",
    "https://drscdn.500px.org/photo/128257261/q%3D80_h%3D450/f846dea57238b8e3dcd3cbc2a9a64487",
    "https://drscdn.500px.org/photo/143197405/q%3D80_h%3D600/ffeb955c7a30b9bfa7064e9ce441b5cc",
    "https://drscdn.500px.org/photo/134694689/q%3D80_h%3D600/b92f0a7ac5f68eabf68bfce110300049",
    "https://drscdn.500px.org/photo/114998419/q%3D80_h%3D600/4481decb3dfe8e0cd16ce9e8d3b508a9",
    "https://drscdn.500px.org/photo/145775015/q%3D80_h%3D450/c58808a2c0acb719ade98ddf33f00248",
    "https://drscdn.500px.org/photo/114678901/q%3D80_h%3D450/62f7657324ee5b74d02d9220a8449f8a",
    "https://drscdn.500px.org/photo/140328701/q%3D80_h%3D450/c8d86e760e4f0dcb5b2632a031cccc98",
    "https://drscdn.500px.org/photo/142802367/q%3D80_h%3D450/8cff2cb706391fdce1ce9aed2f34fc8e",
    "https://drscdn.500px.org/photo/91974691/q%3D80_h%3D600/bbd0ab88b41ca668f782fe236039ecd6",
    "https://drscdn.500px.org/photo/138363775/q%3D80_h%3D600/bd22548bc0e96af2b248fb16b550379b",
    "https://drscdn.500px.org/photo/129943423/q%3D80_h%3D600/35efd36725457c8909e0735de841cf01",
    "https://drscdn.500px.org/photo/85724383/q%3D80_h%3D600/3231b05ecc9a58a0b89c1a10e4e95f69",
    "https://drscdn.500px.org/photo/140381041/q%3D80_h%3D600_k%3D1/de958b31f985607cef44722601639af9",
    "https://drscdn.500px.org/photo/145858803/q%3D80_h%3D600_k%3D1/54d461af7bea6a3afc1e859e990769a0",
    "https://drscdn.500px.org/photo/137247735/q%3D80_h%3D600_k%3D1/ba559cb69bae41040ee24bcacd02404d",
    "https://drscdn.500px.org/photo/138905849/q%3D80_h%3D450/20d11485ae0cb07bd87078e270fa059f",
    "https://drscdn.500px.org/photo/137937425/q%3D80_h%3D450/0708d5c8382ce7c26757ab33e2bc8f70",
    "https://drscdn.500px.org/photo/133021433/q%3D80_h%3D450/bd3ca4c8d8b50a9ed747f2b51c7833f6",
    "https://drscdn.500px.org/photo/114519217/q%3D80_h%3D450/91f2749d81ef6038400644cc5460d8da",
    "https://drscdn.500px.org/photo/137813895/q%3D80_h%3D450/5ef1baf872e539df19421e36e6afc1a1",
    "https://drscdn.500px.org/photo/139837853/q%3D80_h%3D450/55768d62a88654a477e3683bb5f9daf6",
    "https://drscdn.500px.org/photo/91672173/q%3D80_h%3D450/f05d69d830ec3e223a8df8ae677082b8",
]
