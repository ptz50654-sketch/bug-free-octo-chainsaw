import time

class Game:
    def __init__(self):
        # 初始状态
        self.money = 1500      # 金钱
        self.health = 80       # 身体状况 (0-100)
        self.mind = 70         # 心理状态 (0-100)
        self.relations = {
            "莫空": 0,
            "张思凡": 0,
            "胡玉牛": 0,
            "林夕晨": 0,
            "王海峰": 0,
            "陈淑艳": 0
        }
        self.has_job = False   # 是否有工作
        self.in_face = False   # 是否在面馆工作过
        self.in_supermarket = False # 是否在超市工作
        self.in_house = False  # 是否有住处
        self.roommate = False  # 是否有合租室友
        self.confessed = False # 是否向林夕晨告白

    def show_status(self):
        print("\n【当前状态】")
        print(f"金钱: {self.money}元 | 身体状况: {self.health} | 心理状态: {self.mind}")
        print(f"人际关系: 莫空{self.relations['莫空']} 张思凡{self.relations['张思凡']} 胡玉牛{self.relations['胡玉牛']} 林夕晨{self.relations['林夕晨']}")
        print()

    def wait(self):
        input("\n按回车键继续...")

    def run(self):
        print("="*50)
        print("《药娘的天空：初入小城》")
        print("一个关于成长、梦想与选择的故事")
        print("="*50)
        time.sleep(1)
        self.scene_intro()

    def scene_intro(self):
        print("\n2004年，春。")
        print("你（苏雨晴）因父母无法接受你服用雌性激素药物，愤而离家出走。")
        print("你乘火车来到了一个陌生的小城市，身上只有1500元。")
        print("天色已晚，你必须先找到今晚的落脚之处。")
        self.wait()
        self.scene_railway_station()

    def scene_railway_station(self):
        print("\n【小城市火车站】")
        print("你站在火车站出口，看着陌生的街道，心中一片茫然。")
        print("你现在最需要的是：")
        print("1. 去找工作，解决生存问题。")
        print("2. 先找个便宜的地方住下来。")
        print("3. 在附近逛逛，熟悉环境。")
        choice = input("请选择 (1/2/3): ").strip()
        if choice == "1":
            self.scene_job_agency()
        elif choice == "2":
            self.scene_find_house()
        elif choice == "3":
            self.scene_stroll()
        else:
            print("输入无效，请重新选择。")
            self.scene_railway_station()

    def scene_job_agency(self):
        print("\n【中介所】")
        print("你走进一家贴满招工纸条的中介所。")
        print("墙上有一张招工信息：面馆帮工，月薪300元，包吃，中介费5元。")
        print("1. 付钱，接下这份工作。")
        print("2. 再看看别的工作。")
        print("3. 发现自己钱包不见了！")
        choice = input("请选择 (1/2/3): ").strip()
        if choice == "1":
            if self.money >= 5:
                self.money -= 5
                print("你付了中介费，记下面馆的地址。")
                self.has_job = True
                self.scene_noodle_shop()
            else:
                print("你发现钱包里已经没有钱了！")
                self.money = 0
                self.scene_lost_wallet()
        elif choice == "2":
            print("你觉得工资太低，决定再看看。")
            self.scene_railway_station()
        elif choice == "3":
            self.money = 0
            print("你惊恐地发现钱包不见了！")
            self.scene_lost_wallet()
        else:
            self.scene_job_agency()

    def scene_find_house(self):
        print("\n【农民房区】")
        print("你找到一位叫“老虎”的房东，她还有一间空房，月租150元，但需付三个月。")
        print("1. 太贵了，再找找。")
        print("2. 咬咬牙租下来。")
        choice = input("请选择 (1/2): ").strip()
        if choice == "1":
            print("你决定再找找更便宜的住处。")
            self.scene_railway_station()
        elif choice == "2":
            if self.money >= 450:
                self.money -= 450
                self.in_house = True
                print("你租下了这间小屋，拥有了自己的小窝。")
                self.scene_small_home()
            else:
                print("钱不够，你只好放弃。")
                self.scene_railway_station()
        else:
            self.scene_find_house()

    def scene_small_home(self):
        print("\n【你的小窝】")
        print("你终于有了一个属于自己的小房间，虽然简陋，但让你感到一丝安心。")
        print("你开始布置房间，这让你暂时忘记了离家的忧伤。")
        self.wait()
        self.scene_next_day()

    def scene_stroll(self):
        print("\n【火车站附近】")
        print("你在街上漫无目的地走着，天色渐晚，你又累又饿。")
        print("1. 买一个当地小吃嵌糕充饥（2元）。")
        print("2. 找一家小旅馆住下（30元）。")
        print("3. 实在走不动了，就在路边凑合一晚。")
        choice = input("请选择 (1/2/3): ").strip()
        if choice == "1" and self.money >= 2:
            self.money -= 2
            print("你吃了嵌糕，感觉舒服了一些。")
            self.scene_meet_mokong()
        elif choice == "2" and self.money >= 30:
            self.money -= 30
            print("你在小旅馆里度过了一夜，但想家的情绪让你难以入眠。")
            self.mind -= 5
            self.scene_next_day()
        elif choice == "3":
            print("你在街角蜷缩了一夜，第二天起来头晕眼花。")
            self.health -= 15
            self.mind -= 10
            self.scene_next_day()
        else:
            print("你无法执行这个选项。")
            self .scene_stroll()

    def scene_lost_wallet(self):
        print("\n【身无分文】")
        print("你身无分文，又饿又冷，只能蹲在路边。")
        print("一位和蔼的大叔路过，看到你的窘境。")
        print("1. 鼓起勇气向他求助。")
        print("2. 拒绝帮助，自己想办法。")
        choice = input("请选择 (1/2): ").strip()
        if choice == "1":
            print("大叔帮你买了食物，并介绍你去一家面馆打零工。")
            self.has_job = True
            self.money = 50
            self.health -= 5
            self.scene_noodle_shop()
        elif choice == "2":
            print("你拒绝了帮助，又冷又饿地熬过了一夜，第二天好不容易找到一家小餐馆洗碗。")
            self.has_job = True
            self.money = 100
            self.health -= 20
            self.mind -= 15
            self.scene_noodle_shop()
        else:
            self.scene_lost_wallet()

    def scene_noodle_shop(self):
        print("\n【无名面馆】")
        print("你按地址找到了“无名面馆”，见到了善良的老板和老板娘（张阿姨和李叔叔）。")
        print("他们愿意雇佣你做帮工，月薪300元，包吃住（住在店里）。")
        print("你欣然接受了这份工作。")
        self.in_face = True
        self.money = 0  # 身上没现金了
        print("你开始了在面馆的生活，虽然辛苦，但至少安稳了下来。")
        self.wait()
        self.scene_meet_mokong()

    def scene_meet_mokong(self):
        print("\n【河堤边】")
        print("一天休息日，你来到河堤边散心。")
        print("你遇到一个不修边幅但气质温和的年轻人，他正在钓鱼。")
        print("他主动和你搭话，并给你讲了一个“想要变成鹰的鱼”的故事。")
        print("1. 被故事打动，和他多聊几句。")
        print("2. 害怕陌生人，匆匆离开。")
        choice = input("请选择 (1/2): ").strip()
        if choice == "1":
            self.relations["莫空"] += 10
            self.mind += 5
            print("你们聊了很久，你觉得他好像能理解你的心情。")
        else:
            print("你礼貌地告别，离开了河堤。")
        self.wait()
        self.scene_meet_zhang_sifan()

    def scene_meet_zhang_sifan(self):
        print("\n【黑网吧】")
        print("你偶尔去网吧上网，在一个药娘论坛里结识了一位ID叫“月橙”的朋友。")
        print("你们聊得很投机，对方告诉你她也住在小城市。")
        print("你们约定在中心广场见面。")
        print("见面当天，你发现“月橙”是一个穿着男装的帅气女生（其实也是药娘）。")
        print("她自称张思凡，性格开朗。")
        self.relations["张思凡"] += 15
        self.mind += 10
        print("你们成了很好的朋友。")
        self.wait()
        self.scene_parents_find()

    def scene_parents_find(self):
        print("\n【面馆门口】")
        print("一天早上，你去面馆上班，远远看见自己的父母正站在门口和张阿姨说话。")
        print("他们来找你了！")
        print("1. 冲出去和他们相见，把一切说清楚。")
        print("2. 他们不会理解我的，必须逃离这里。")
        choice = input("请选择 (1/2): ").strip()
        if choice == "1":
            print("你跑向父母，扑进妈妈怀里痛哭。")
            print("经过一番艰难的沟通，父母虽然不理解，但看到你瘦弱的身体，最终还是妥协了。")
            print("你回到了家，生活重新开始。")
            print("\n【结局1：回家】")
            print("你重新回到学校，父母默许你继续服药，约定等你成年后再做选择。")
            print("虽然前路未知，但至少家还在。")
            self.wait()
            self.end_game()
        elif choice == "2":
            print("你害怕地转身就跑，回家收拾行李，在张思凡的帮助下搬到了郊区的集装箱房。")
            print("你离开了面馆，也暂时躲开了父母。")
            self.scene_container_life()
        else:
            self.scene_parents_find()

    def scene_container_life(self):
        print("\n【郊区的集装箱房】")
        print("你搬进了张思凡的集装箱房，这里虽然简陋，但很温馨。")
        print("不久后，你们又迎来了新的室友：温柔的方莜莜、壮硕但内心少女的胡玉牛。")
        print("后来，沉默寡言的绘画天才林夕晨也住了进来。")
        print("你们组成了一个特殊的大家庭。")
        self.in_house = True
        self.roommate = True
        self.mind += 10
        self.wait()
        self.scene_supermarket_job()

    def scene_supermarket_job(self):
        print("\n【大润发超市】")
        print("你在张思凡的介绍下，去大润发超市应聘，成功成为了一名理货员。")
        print("你被分到零食部门，主管是个小个子男人王海峰，虽然说话有点欠揍，但很照顾你。")
        print("你开始了新的工作，生活渐渐步入正轨。")
        self.has_job = True
        self.in_supermarket = True
        self.money += 1500  # 第一个月工资
        self.relations["王海峰"] = 10
        self.relations["陈淑艳"] = 5
        self.wait()
        self.scene_bar_job()

    def scene_bar_job(self):
        print("\n【酒吧兼职】")
        print("张思凡约你晚上去酒吧做兼职，报酬很高。")
        print("1. 太危险了，不去。")
        print("2. 为了钱，去试试。")
        choice = input("请选择 (1/2): ").strip()
        if choice == "1":
            print("你拒绝了，选择老老实实上班。")
        elif choice == "2":
            print("你去了酒吧，却被客人灌酒，差点出事，幸好莫空及时出现救了你。")
            self.money += 600
            self.health -= 10
            self.mind -= 10
            self.relations["莫空"] += 10
            print("你得到了600元小费，但心里留下了阴影。")
        else:
            self.scene_bar_job()
        self.wait()
        self.scene_hu_yuniu_confession()

    def scene_hu_yuniu_confession(self):
        print("\n【合租房里】")
        print("胡玉牛偶然发现你吃的药，知道了你的秘密。")
        print("他向你倾诉，他也想变成女孩子。")
        print("看着他那壮硕的身躯，你内心很复杂。")
        print("1. 支持他，鼓励他追寻梦想。")
        print("2. 劝他放弃，觉得他不适合。")
        choice = input("请选择 (1/2): ").strip()
        if choice == "1":
            self.relations["胡玉牛"] += 15
            print("你告诉他，每个人都有追求梦想的权利。")
        elif choice == "2":
            self.relations["胡玉牛"] -= 10
            print("你委婉地说他可能不太适合这条路，他沉默了。")
        else:
            self.scene_hu_yuniu_confession()
        self.wait()
        self.scene_supermarket_conflict()

    def scene_supermarket_conflict(self):
        print("\n【超市收银台】")
        print("这天，你正在收银，一个顾客因小事和收银员发生激烈冲突。")
        print("顾客动手打人，收银员一怒之下用剪刀刺伤了对方。")
        print("鲜血流了一地，你吓得浑身发抖。")
        print("1. 跑到一旁呕吐。")
        print("2. 虽然害怕，但还是帮忙报警。")
        choice = input("请选择 (1/2): ").strip()
        if choice == "1":
            self.mind -= 15
            print("你被血腥场面吓坏了，好几天都做噩梦。")
        elif choice == "2":
            self.mind += 5
            print("你强忍恐惧，拨打了120和110，事后被经理表扬。")
        else:
            self.scene_supermarket_conflict()
        self.wait()
        self.scene_lin_xichen_arrival()

    def scene_lin_xichen_arrival(self):
        print("\n【合租房】")
        print("方莜莜的朋友林夕晨搬了进来。")
        print("她有着惊人的巨乳和一张永远面无表情的脸。")
        print("1. 主动向她示好，给她拿牛奶。")
        print("2. 有点怕她，保持距离。")
        choice = input("请选择 (1/2): ").strip()
        if choice == "1":
            self.relations["林夕晨"] += 15
            print("她接过牛奶，轻轻点了点头。你们的关系似乎拉近了一些。")
        elif choice == "2":
            print("你只是礼貌地打了个招呼。")
        else:
            self.scene_lin_xichen_arrival()
        self.wait()
        self.scene_body_changes()

    def scene_body_changes(self):
        print("\n【身体的变化】")
        print("服药已经好几个月了，你的身体开始出现明显变化：胸部微微隆起，皮肤更加细腻。")
        print("但同时，药物的副作用也让你频繁起夜，精神不济。")
        print("1. 感到欣喜，这是离梦想更近的一步。")
        print("2. 感到担忧，害怕未来会怎样。")
        choice = input("请选择 (1/2): ").strip()
        if choice == "1":
            self.mind += 10
            print("你对着镜子里的自己微笑，觉得一切付出都值得。")
        elif choice == "2":
            self.mind -= 10
            print("你开始怀疑自己是否做出了正确的选择。")
        else:
            self.scene_body_changes()
        self.wait()
        self.scene_wang_haifeng_help()

    def scene_wang_haifeng_help(self):
        print("\n【超市】")
        print("主管王海峰总是把轻松的活儿派给你，把脏活累活派给陈淑艳。")
        print("翁锡芽和徐嫂似乎有些不满。")
        print("1. 坦然接受，更加认真地工作。")
        print("2. 觉得不好意思，主动要求做脏活。")
        choice = input("请选择 (1/2): ").strip()
        if choice == "1":
            print("你努力工作，赢得了更多人的好感。")
        elif choice == "2":
            self.relations["王海峰"] += 5
            self.relations["陈淑艳"] += 10
            print("王海峰和陈淑艳觉得你懂事，更加照顾你。")
        else:
            self.scene_wang_haifeng_help()
        self.wait()
        self.scene_night_talk()

    def scene_night_talk(self):
        print("\n【客厅夜谈】")
        print("一个晚上，你和张思凡、方莜莜聊起未来。")
        print("张思凡说，我们这样的人，可能只能活到40岁。")
        print("1. “如果只能活到40岁，那更要抓紧时间实现梦想啊！”")
        print("2. “那……我们是不是选错了？”")
        choice = input("请选择 (1/2): ").strip()
        if choice == "1":
            self.mind += 10
            print("你们相视一笑，更加坚定了信念。")
        elif choice == "2":
            self.mind -= 10
            print("气氛变得沉重起来，你陷入了沉思。")
        else:
            self.scene_night_talk()
        self.wait()
        self.scene_teach_painting()

    def scene_teach_painting(self):
        print("\n【阳台上】")
        print("林夕晨在教你画画，她突然从背后握住你的手。")
        print("你能感受到她柔软的身体和淡淡的荷花香。")
        print("1. 心跳加速，希望时间停止。")
        print("2. 感到害羞，不动声色地拉开距离。")
        choice = input("请选择 (1/2): ").strip()
        if choice == "1":
            self.relations["林夕晨"] += 20
            self.mind += 5
            print("你们靠得更近了，似乎有什么悄悄在发芽。")
        elif choice == "2":
            print("你装作若无其事，继续画画。")
        else:
            self.scene_teach_painting()
        self.wait()
        self.scene_fang_youyou_decision()

    def scene_fang_youyou_decision(self):
        print("\n【合租房】")
        print("方莜莜告诉大家，她决定辞职，去做去势手术。")
        print("1. 羡慕她的勇气，祝福她。")
        print("2. 有些害怕，担心手术的风险。")
        choice = input("请选择 (1/2): ").strip()
        if choice == "1":
            self.mind += 5
            print("你为她的决心感到敬佩。")
        elif choice == "2":
            self.mind -= 5
            print("你开始担心自己未来的手术。")
        else:
            self.scene_fang_youyou_decision()
        self.wait()
        self.scene_work_mistake()

    def scene_work_mistake(self):
        print("\n【超市收银台】")
        print("这天你实在太困，迷迷糊糊中把几张彩票当作百元钞票收下。")
        print("下班时才发现账目对不上，需要赔偿700元。")
        print("1. 自认倒霉，用自己的积蓄悄悄补上。")
        print("2. 向主管王海峰坦白。")
        choice = input("请选择 (1/2): ").strip()
        if choice == "1" and self.money >= 700:
            self.money -= 700
            self.mind -= 10
            print("你补上了钱，但心里非常难受。")
        elif choice == "2":
            if self.relations["王海峰"] >= 10:
                print("王海峰知道你平时工作认真，帮你担了责任，只让你赔了200元。")
                self.money -= 200
                self.mind += 5
            else:
                print("王海峰虽然没说什么，但对你有些失望。你赔了700元。")
                self.money -= 700
                self.mind -= 10
        else:
            print("你无力赔偿，只好向同事借钱，欠下人情。")
            self.money -= 700
            self.mind -= 15
        self.wait()
        self.scene_christmas_eve()

    def scene_christmas_eve(self):
        print("\n【圣诞夜】")
        print("大雪纷飞的圣诞夜，你和林夕晨在海边散步。")
        print("烟花在夜空中绽放，你终于鼓起勇气。")
        print("1. “夕子姐姐，我……喜欢你。”")
        print("2. 把这份感情藏在心里，就这样陪着她。")
        choice = input("请选择 (1/2): ").strip()
        if choice == "1":
            self.confessed = True
            print("林夕晨看了你很久，然后轻轻地点了点头。")
            print("你们在烟花下紧紧相拥。")
            self.scene_ending_love()
        elif choice == "2":
            print("你没有说出口，只是默默牵起她的手。")
            print("你们就这样静静地看着烟花。")
            self.scene_ending_friend()
        else:
            self.scene_christmas_eve()

    def scene_ending_love(self):
        print("\n【结局2：百合花开】")
        print("你们确定了关系，在合租房里成为公开的秘密。")
        print("你们一起画画，一起上班，一起攒钱，期待着能一起去做手术的那一天。")
        print("虽然前路依然艰难，但至少不再孤单。")
        self.wait()
        self.end_game()

    def scene_ending_friend(self):
        print("\n【结局3：幻梦一场】")
        print("你最终还是没有说出那句话。")
        print("林夕晨依然面无表情地坐在阳台上画画，你也依然在超市里辛苦工作。")
        print("你们的关系就像两条平行线，永远互相陪伴，却永远不会相交。")
        print("你将那份爱意深埋心底，看着她，是你在这条路上唯一的慰藉。")
        self.wait()
        self.end_game()

    def scene_next_day(self):
        print("\n第二天，你继续在小城市寻找出路。")
        self.wait()
        self.scene_railway_station()

    def end_game(self):
        print("\n感谢游玩！")
        print("游戏结束。")
        exit()

if __name__ == "__main__":
    game = Game()
    game.run()