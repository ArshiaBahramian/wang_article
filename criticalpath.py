import networkx as nx


class CriticalPath:
    def __init__(self, activities):
        activities['start'] = 0
        activities['end'] = 0
        self.activities = activities

    def calculate_critical_path(self):
        dependencies = {
            '1': ['start'],
            '2': ['1'],
            '3': ['2'],
            '4': ['3'],
            '5': ['4'],
            '6': ['5'],
            '7': ['5'],
            '8': ['7'],
            '9': ['8'],
            '10': ['9'],
            '11': ['7'],
            '12': ['8', '11'],
            '13': ['9', '12'],
            '14': ['10', '13'],
            '15': ['11'],
            '16': ['15', '12'],
            '17': ['13', '16'],
            '18': ['14', '17'],
            '19': ['18'],
            '20': ['19'],
            'end': ['20', '6']
        }

        # ایجاد یک گراف جهت‌دار
        G = nx.DiGraph()
        activities = self.activities
        # اضافه کردن گره‌ها به گراف با وزن برابر با زمان اجرای فعالیت
        for activity, duration in activities.items():
            G.add_node(activity, duration=duration)

        # اضافه کردن یال‌ها بر اساس پیش‌نیازها
        for activity, prereqs in dependencies.items():
            for prereq in prereqs:
                # افزودن یک یال از پیش‌نیاز به فعالیت با وزن برابر با زمان اجرای پیش‌نیاز
                G.add_edge(prereq, activity, weight=activities[prereq])

        # محاسبه مسیر بحرانی با استفاده از طولانی‌ترین مسیر
        critical_path = nx.dag_longest_path(G)
        critical_path_duration = nx.dag_longest_path_length(G)

        return critical_path_duration

# activities = {
#     '1': 2,
#     '2': 10,
#     '3': 2,
#     '4': 3,
#     '5': 7,
#     '6': 3,
#     '7': 11,
#     '8': 3,
#     '9': 5,
#     '10': 11,
#     '11': 11,
#     '12': 2,
#     '13': 5,
#     '14': 10,
#     '15': 10,
#     '16': 3,
#     '17': 4,
#     '18': 9,
#     '19': 6,
#     '20': 4,
# }
# cp = CriticalPath(activities)
# total_duration = cp.calculate_critical_path()
# # print(critical_path)
# print(total_duration)
