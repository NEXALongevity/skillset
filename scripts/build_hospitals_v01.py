#!/usr/bin/env python3
"""Build data/hospitals/*.yaml for v0.1 from the 2023年度中国医院专科声誉排行榜 (Fudan).

Rankings transcribed on 2026-11-27 from the list images published, with the
Fudan Institute's authorisation, by 健康界 (cn-healthcare.com).
"""
from pathlib import Path
import yaml

SRC_LIST = "复旦大学医院管理研究所《2023年度中国医院专科声誉排行榜》（2024-11-16 发布）"
SRC_URL = "https://www.cn-healthcare.com/article/20241116/content-585244.html"
VERIFIED = "2026-11-27"

# id: (name_zh, name_en, city, province, type)
H = {
 "cams-cancer-hospital": ("中国医学科学院肿瘤医院", "Cancer Hospital, Chinese Academy of Medical Sciences", "北京", "北京", "public"),
 "sysucc": ("中山大学肿瘤防治中心", "Sun Yat-sen University Cancer Center", "广州", "广东", "public"),
 "fudan-cancer": ("复旦大学附属肿瘤医院", "Fudan University Shanghai Cancer Center", "上海", "上海", "public"),
 "pku-cancer": ("北京大学肿瘤医院", "Peking University Cancer Hospital", "北京", "北京", "public"),
 "tmu-cancer": ("天津医科大学肿瘤医院", "Tianjin Medical University Cancer Institute and Hospital", "天津", "天津", "public"),
 "shandong-cancer": ("山东省肿瘤医院（山东省肿瘤防治研究院）", "Shandong Cancer Hospital and Institute", "济南", "山东", "public"),
 "zhejiang-cancer": ("中国科学院大学附属肿瘤医院（浙江省肿瘤医院）", "Zhejiang Cancer Hospital (Cancer Hospital of the University of Chinese Academy of Sciences)", "杭州", "浙江", "public"),
 "west-china": ("四川大学华西医院", "West China Hospital, Sichuan University", "成都", "四川", "public"),
 "jiangsu-cancer": ("江苏省肿瘤医院", "Jiangsu Cancer Hospital", "南京", "江苏", "public"),
 "sichuan-cancer": ("四川省肿瘤医院", "Sichuan Cancer Hospital", "成都", "四川", "public"),
 "fuwai": ("中国医学科学院阜外医院", "Fuwai Hospital, Chinese Academy of Medical Sciences", "北京", "北京", "public"),
 "zhongshan-fudan": ("复旦大学附属中山医院", "Zhongshan Hospital, Fudan University", "上海", "上海", "public"),
 "anzhen": ("首都医科大学附属北京安贞医院", "Beijing Anzhen Hospital, Capital Medical University", "北京", "北京", "public"),
 "northern-theater": ("中国人民解放军北部战区总医院", "General Hospital of Northern Theater Command, PLA", "沈阳", "辽宁", "public"),
 "zju-2nd": ("浙江大学医学院附属第二医院", "Second Affiliated Hospital, Zhejiang University School of Medicine", "杭州", "浙江", "public"),
 "guangdong-provincial": ("广东省人民医院", "Guangdong Provincial People's Hospital", "广州", "广东", "public"),
 "hmu-2nd": ("哈尔滨医科大学附属第二医院", "Second Affiliated Hospital of Harbin Medical University", "哈尔滨", "黑龙江", "public"),
 "ruijin": ("上海交通大学医学院附属瑞金医院", "Ruijin Hospital, Shanghai Jiao Tong University School of Medicine", "上海", "上海", "public"),
 "pku-first": ("北京大学第一医院", "Peking University First Hospital", "北京", "北京", "public"),
 "pku-third": ("北京大学第三医院", "Peking University Third Hospital", "北京", "北京", "public"),
 "zzu-first": ("郑州大学第一附属医院", "First Affiliated Hospital of Zhengzhou University", "郑州", "河南", "public"),
 "sdu-reproductive": ("山东大学附属生殖医院", "Reproductive Hospital Affiliated to Shandong University", "济南", "山东", "public"),
 "citic-xiangya": ("中信湘雅生殖与遗传专科医院", "Reproductive & Genetic Hospital of CITIC-Xiangya", "长沙", "湖南", "private"),
 "drum-tower": ("南京大学医学院附属鼓楼医院", "Nanjing Drum Tower Hospital, Affiliated Hospital of Nanjing University Medical School", "南京", "江苏", "public"),
 "sysu-first": ("中山大学附属第一医院", "First Affiliated Hospital, Sun Yat-sen University", "广州", "广东", "public"),
 "chongqing-mch": ("重庆市妇幼保健院", "Chongqing Health Center for Women and Children", "重庆", "重庆", "public"),
 "tongji-wuhan": ("华中科技大学同济医学院附属同济医院", "Tongji Hospital, Tongji Medical College, Huazhong University of Science and Technology", "武汉", "湖北", "public"),
 "renji": ("上海交通大学医学院附属仁济医院", "Renji Hospital, Shanghai Jiao Tong University School of Medicine", "上海", "上海", "public"),
 "zju-womens": ("浙江大学医学院附属妇产科医院", "Women's Hospital, Zhejiang University School of Medicine", "杭州", "浙江", "public"),
 "plagh": ("中国人民解放军总医院", "Chinese PLA General Hospital", "北京", "北京", "public"),
 "sichuan-provincial": ("四川省人民医院", "Sichuan Provincial People's Hospital", "成都", "四川", "public"),
 "jiangsu-provincial": ("江苏省人民医院（南京医科大学第一附属医院）", "Jiangsu Province Hospital (First Affiliated Hospital of Nanjing Medical University)", "南京", "江苏", "public"),
 "qdu-affiliated": ("青岛大学附属医院", "Affiliated Hospital of Qingdao University", "青岛", "山东", "public"),
 "xiangya": ("中南大学湘雅医院", "Xiangya Hospital, Central South University", "长沙", "湖南", "public"),
 "anhui-provincial": ("中国科学技术大学附属第一医院（安徽省立医院）", "First Affiliated Hospital of USTC (Anhui Provincial Hospital)", "合肥", "安徽", "public"),
 "xiangya-3rd": ("中南大学湘雅三医院", "Third Xiangya Hospital, Central South University", "长沙", "湖南", "public"),
 "shenzhen-peoples": ("深圳市人民医院", "Shenzhen People's Hospital", "深圳", "广东", "public"),
 "southwest": ("陆军军医大学第一附属医院（西南医院）", "First Affiliated Hospital of Army Medical University (Southwest Hospital)", "重庆", "重庆", "public"),
 "jst": ("北京积水潭医院", "Beijing Jishuitan Hospital", "北京", "北京", "public"),
 "shanghai-sixth": ("上海市第六人民医院", "Shanghai Sixth People's Hospital", "上海", "上海", "public"),
 "pumch": ("中国医学科学院北京协和医院", "Peking Union Medical College Hospital", "北京", "北京", "public"),
 "hebmu-third": ("河北医科大学第三医院", "Third Hospital of Hebei Medical University", "石家庄", "河北", "public"),
 "changzheng": ("海军军医大学第二附属医院（上海长征医院）", "Second Affiliated Hospital of Naval Medical University (Shanghai Changzheng Hospital)", "上海", "上海", "public"),
 "pku-peoples": ("北京大学人民医院", "Peking University People's Hospital", "北京", "北京", "public"),
 "tianjin-hospital": ("天津市天津医院", "Tianjin Hospital", "天津", "天津", "public"),
 "ninth-sh": ("上海交通大学医学院附属第九人民医院", "Shanghai Ninth People's Hospital, Shanghai Jiao Tong University School of Medicine", "上海", "上海", "public"),
 "cams-plastic": ("中国医学科学院整形外科医院", "Plastic Surgery Hospital, Chinese Academy of Medical Sciences", "北京", "北京", "public"),
 "nanfang": ("南方医科大学南方医院", "Nanfang Hospital, Southern Medical University", "广州", "广东", "public"),
 "xijing": ("空军军医大学第一附属医院（西京医院）", "Xijing Hospital, Air Force Medical University", "西安", "陕西", "public"),
 "union-wuhan": ("华中科技大学同济医学院附属协和医院", "Union Hospital, Tongji Medical College, Huazhong University of Science and Technology", "武汉", "湖北", "public"),
 "cmu-first": ("中国医科大学附属第一医院", "First Hospital of China Medical University", "沈阳", "辽宁", "public"),
}

LISTS = {
 "oncology": ("肿瘤学", ["cams-cancer-hospital","sysucc","fudan-cancer","pku-cancer","tmu-cancer","shandong-cancer","zhejiang-cancer","west-china","jiangsu-cancer","sichuan-cancer"]),
 "cardio-cerebrovascular": ("心血管病", ["fuwai","zhongshan-fudan","anzhen","northern-theater","zju-2nd","guangdong-provincial","west-china","hmu-2nd","ruijin","pku-first"]),
 "reproductive": ("生殖医学", ["pku-third","zzu-first","sdu-reproductive","citic-xiangya","drum-tower","sysu-first","chongqing-mch","tongji-wuhan","renji","zju-womens"]),
 "checkup-longevity": ("健康管理", ["plagh","sichuan-provincial","jiangsu-provincial","qdu-affiliated","zju-2nd","xiangya","anhui-provincial","xiangya-3rd","shenzhen-peoples","southwest"]),
 "orthopedics": ("骨科", ["jst","shanghai-sixth","plagh","pku-third","pumch","west-china","hebmu-third","changzheng","pku-peoples","tianjin-hospital"]),
 "aesthetics": ("整形外科", ["ninth-sh","cams-plastic","nanfang","pumch","xijing","union-wuhan","zhongshan-fudan","southwest","cmu-first","pku-third"]),
}

out = Path(__file__).resolve().parent.parent / "data" / "hospitals"
out.mkdir(parents=True, exist_ok=True)
for direction, (specialty, ids) in LISTS.items():
    recs = []
    for rank, hid in enumerate(ids, 1):
        zh, en, city, prov, typ = H[hid]
        r = {"id": hid, "name_zh": zh, "name_en": en, "directions": [direction], "type": typ,
             "city": city, "province": prov, "strengths": [specialty],
             "ranking": {"list": "复旦版中国医院专科声誉排行榜", "year": 2023, "specialty": specialty, "rank": rank},
             "source_list": SRC_LIST, "source_url": SRC_URL, "verified_on": VERIFIED}
        if typ == "private":
            r["notes"] = "民营专科医院，按榜单原样收录 / Private specialty hospital, included as ranked"
        recs.append(r)
    header = (f"# {specialty} · {direction} — v0.1\n# 来源 Source: {SRC_LIST}\n# {SRC_URL}\n"
              f"# 核实日期 Verified: {VERIFIED}\n# © NEXA Longevity · CC BY 4.0\n")
    (out / f"{direction}.yaml").write_text(header + yaml.safe_dump(recs, allow_unicode=True, sort_keys=False), encoding="utf-8")
    print(direction, len(recs))
