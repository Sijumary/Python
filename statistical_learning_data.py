import json
from collections import Counter


def count():
    """
    Calculate the number of courses and users in the JSON file.
    JSON file is located at ~/project/user_study.json

    Returns:
        count_user(int): Total number of users.
        count_course(int): Total number of courses.
    """
    
    user_ids = set()
    courses = set()
    count_user = 0
    count_course = 0

    try:
        with open("user_study.json", "r") as file:
            data = json.load(file)
            
            if isinstance(data, list):
                for entry in data:
                    user_ids.add(entry.get("user_id"))
                    courses.add(entry.get("course"))
            else:
                user_ids.add(data.get("user_id"))
                courses.add(data.get("course"))
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON.")
    
    return len(user_ids), len(courses)

if __name__ == "__main__":
    # Print the number of unique user IDs and course names
    count_user, count_course = count()
    print(f"The file contains {count_user} users and {count_course} courses")



###################################################################################################
JSON file 
######################################################################################################

[
  {
    "minutes": 30,
    "created_at": "2016-05-01 00:00:10",
    "user_id": 199071,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 00:00:15",
    "user_id": 199373,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 00:01:49",
    "user_id": 173927,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-01 00:03:41",
    "user_id": 185399,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 00:05:10",
    "user_id": 139642,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 00:10:08",
    "user_id": 144042,
    "lab": "Flask\u8fd0\u884c\u53ca\u8c03\u8bd5\u6a21\u5f0f",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 00:13:00",
    "user_id": 139642,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 00:17:44",
    "user_id": 176435,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 00:30:04",
    "user_id": 131866,
    "lab": "\u8ba4\u8bc6 JDBC",
    "course": "JDBC \u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 00:36:45",
    "user_id": 118522,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0b\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 00:46:38",
    "user_id": 199071,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 00:48:19",
    "user_id": 186469,
    "lab": "\u64cd\u4f5c\u7cfb\u7edf\u7684\u5f15\u5bfc",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 01:00:51",
    "user_id": 131866,
    "lab": "JDBC \u57fa\u7840",
    "course": "JDBC \u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 01:03:14",
    "user_id": 193581,
    "lab": "Laravel\u5b9e\u73b0\u7528\u6237\u6ce8\u518c\u767b\u5f55",
    "course": "Laravel\u5b9e\u73b0\u7528\u6237\u6ce8\u518c\u767b\u5f55"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 01:15:30",
    "user_id": 119886,
    "lab": "\u88c5\u9970\u8005\u6a21\u5f0f",
    "course": "Java\u8fdb\u9636\u4e4b\u8bbe\u8ba1\u6a21\u5f0f"
  },
  {
    "minutes": 84,
    "created_at": "2016-05-01 01:23:42",
    "user_id": 199071,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 01:27:57",
    "user_id": 131866,
    "lab": "JDBC \u63a5\u53e3",
    "course": "JDBC \u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 02:02:03",
    "user_id": 60532,
    "lab": "\u521d\u8bc6MySQL",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 02:03:25",
    "user_id": 131866,
    "lab": "JDBC \u7ed3\u679c\u96c6",
    "course": "JDBC \u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 02:11:23",
    "user_id": 199264,
    "lab": "\u4ecb\u7ecd",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 02:21:12",
    "user_id": 171915,
    "lab": "Python\u804a\u5929\u5ba4",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python\u804a\u5929\u5ba4"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 02:26:12",
    "user_id": 187529,
    "lab": "Flask\u8fd0\u884c\u53ca\u8c03\u8bd5\u6a21\u5f0f",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 02:44:40",
    "user_id": 199144,
    "lab": "\u4ecb\u7ecd",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 02:53:31",
    "user_id": 171915,
    "lab": "Flask\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 03:38:08",
    "user_id": 196341,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 03:50:22",
    "user_id": 143598,
    "lab": "\u57fa\u4e8eNode.js+Express\u5b9e\u73b0\u7b80\u6613\u535a\u5ba2\u7cfb\u7edf",
    "course": "[\u5df2\u4e0b\u7ebf] \u57fa\u4e8eNode.js+Express\u5b9e\u73b0\u7b80\u6613\u535a\u5ba2\u7cfb\u7edf"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 04:14:14",
    "user_id": 176435,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 72,
    "created_at": "2016-05-01 05:07:51",
    "user_id": 176435,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-01 06:43:45",
    "user_id": 68077,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-01 07:03:08",
    "user_id": 198993,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 07:03:22",
    "user_id": 165666,
    "lab": "\u5b57\u7b26\u4e32\uff08\u4e00\uff09",
    "course": "\u7ecf\u5178\u7b97\u6cd5\u89e3\u9898\u5b9e\u6218"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-01 07:07:36",
    "user_id": 165475,
    "lab": "Python\u6df1\u5165\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 07:16:20",
    "user_id": 68077,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 07:17:09",
    "user_id": 116171,
    "lab": "\u8f93\u5165\u548c\u8f93\u51fa",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 07:23:02",
    "user_id": 68077,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 07:39:47",
    "user_id": 198693,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 07:40:46",
    "user_id": 196525,
    "lab": "\u591a\u8bf4,markdown\u548c\u4ee3\u7801\u9ad8\u4eae",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 07:41:29",
    "user_id": 197012,
    "lab": "c\u8bed\u8a00\u5236\u4f5c2048",
    "course": "C\u8bed\u8a00\u5236\u4f5c2048"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 07:45:08",
    "user_id": 199079,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 07:47:24",
    "user_id": 68077,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 07:54:32",
    "user_id": 198056,
    "lab": "\u6269\u5c55\u6b63\u5219\u8868\u8fbe\u5f0f",
    "course": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-01 07:56:06",
    "user_id": 165475,
    "lab": "Python\u6df1\u5165\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 07:57:15",
    "user_id": 196525,
    "lab": "Template\u548c\u52a8\u6001URL",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 11,
    "created_at": "2016-05-01 08:02:14",
    "user_id": 198693,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 08:02:56",
    "user_id": 198635,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 08:03:13",
    "user_id": 197775,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-01 08:03:15",
    "user_id": 170834,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 08:04:03",
    "user_id": 29606,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 08:12:21",
    "user_id": 29606,
    "lab": "Python \u6d41\u7a0b\u63a7\u5236",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-01 08:23:43",
    "user_id": 198635,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 08:24:55",
    "user_id": 197012,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 08:26:31",
    "user_id": 120179,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 08:27:07",
    "user_id": 196942,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 84,
    "created_at": "2016-05-01 08:31:49",
    "user_id": 197423,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 08:39:03",
    "user_id": 199395,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 08:40:46",
    "user_id": 197012,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-01 08:47:47",
    "user_id": 197961,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 57,
    "created_at": "2016-05-01 08:48:12",
    "user_id": 191080,
    "lab": "makefile",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 08:51:01",
    "user_id": 181735,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 08:52:13",
    "user_id": 199398,
    "lab": "k-\u8fd1\u90bb\u7b97\u6cd5\u6539\u8fdb\u7ea6\u4f1a\u7f51\u7ad9\u914d\u5bf9\u6548\u679c",
    "course": "\u6df1\u5165\u5b66\u4e60\u300a\u673a\u5668\u5b66\u4e60\u5b9e\u6218\u300b"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-01 08:52:29",
    "user_id": 199394,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-01 08:53:31",
    "user_id": 116171,
    "lab": "\u8f93\u5165\u548c\u8f93\u51fa",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 08:54:35",
    "user_id": 197012,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 08:56:37",
    "user_id": 199399,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 63,
    "created_at": "2016-05-01 08:57:03",
    "user_id": 176435,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 08:57:19",
    "user_id": 181735,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-01 08:58:33",
    "user_id": 173169,
    "lab": "\u8868\u8fbe\u5f0f\u7684\u8ba1\u7b97",
    "course": "Scala \u5f00\u53d1\u4e8c\u5341\u56db\u70b9\u6e38\u620f"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 08:59:01",
    "user_id": 170834,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-01 08:59:27",
    "user_id": 196942,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 08:59:45",
    "user_id": 194951,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 09:03:02",
    "user_id": 170979,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 09:04:11",
    "user_id": 170834,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-01 09:06:09",
    "user_id": 198646,
    "lab": "makefile",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 09:06:35",
    "user_id": 199400,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-01 09:09:37",
    "user_id": 5078,
    "lab": "\u753b\u51fa\u4e00\u4e9b\u6709\u8da3\u7684\u56fe\u6848",
    "course": "[\u5df2\u4e0b\u7ebf] C++\u4e09\u6bb5\u4ee3\u7801\u673a\u5668\u7ed8\u56fe"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 09:10:12",
    "user_id": 170834,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-01 09:13:05",
    "user_id": 161174,
    "lab": "\u6587\u4ef6IO\uff08\u4e00\uff09",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 09:13:55",
    "user_id": 136676,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 09:16:03",
    "user_id": 80666,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 09:18:51",
    "user_id": 170834,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 153,
    "created_at": "2016-05-01 09:22:05",
    "user_id": 184568,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 09:22:31",
    "user_id": 174908,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 09:24:43",
    "user_id": 161159,
    "lab": "\u4e2d\u7ea7\u6280\u80fd\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 09:30:46",
    "user_id": 170760,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 09:31:23",
    "user_id": 199394,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 09:31:42",
    "user_id": 187235,
    "lab": "\u9000\u51fa\u548c\u9000\u51fa\u72b6\u6001\u7801",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-01 09:32:07",
    "user_id": 149280,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-01 09:32:36",
    "user_id": 181461,
    "lab": "\u6a21\u5757\u5316\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-01 09:33:13",
    "user_id": 199307,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 09:35:12",
    "user_id": 185857,
    "lab": "\u535a\u5ba2\u7684\u9996\u9875\u4e0e\u6295\u7a3f\u8bbe\u8ba1",
    "course": "\u57fa\u4e8eGO\u8bed\u8a00Revel\u6846\u67b6\u548cmgo\u7684\u535a\u5ba2"
  },
  {
    "minutes": 69,
    "created_at": "2016-05-01 09:35:55",
    "user_id": 116171,
    "lab": "\u9762\u5411\u5bf9\u8c61\u7f16\u7a0b",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 09:37:01",
    "user_id": 46640,
    "lab": "Java\u7248\u56fe\u5f62\u754c\u9762\u8ba1\u7b97\u5668",
    "course": "Java\u5f00\u53d1\u7b80\u5355\u7684\u8ba1\u7b97\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 09:39:48",
    "user_id": 146910,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 09:41:19",
    "user_id": 199405,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 09:41:39",
    "user_id": 196942,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 09:42:00",
    "user_id": 3595,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 09:42:43",
    "user_id": 82545,
    "lab": "\u64cd\u4f5c\u7cfb\u7edf\u7684\u5f15\u5bfc",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 09:44:48",
    "user_id": 149905,
    "lab": "MapReduce\u5e94\u7528\u6848\u4f8b",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-01 09:45:10",
    "user_id": 199394,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 09:46:01",
    "user_id": 56376,
    "lab": "\u5b66\u4e60\u4f7f\u7528\u5916\u90e8\u6a21\u5757",
    "course": "Node.js\u5305\u6559\u4e0d\u5305\u4f1a"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 09:46:41",
    "user_id": 90811,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-01 09:47:55",
    "user_id": 166138,
    "lab": "scikit-learn \u673a\u5668\u5b66\u4e60",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e8c)"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 09:48:00",
    "user_id": 199407,
    "lab": "\u6253\u9020\u7f51\u9875\u7248\u300c\u5927\u767d\u300d- Baymax",
    "course": "\u7eaf CSS \u6253\u9020\u7f51\u9875\u7248\u300c\u5927\u767d\u300d"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 09:49:01",
    "user_id": 161778,
    "lab": "\u4e00\u4e2a\u6700\u7b80\u5355\u7684 express \u5e94\u7528",
    "course": "Node.js\u5305\u6559\u4e0d\u5305\u4f1a"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-01 09:49:11",
    "user_id": 128327,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 69,
    "created_at": "2016-05-01 09:50:38",
    "user_id": 90811,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 09:53:02",
    "user_id": 173927,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 09:53:17",
    "user_id": 197775,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-01 09:53:54",
    "user_id": 186465,
    "lab": "Java  \u8fd0\u7b97\u7b26",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 09:54:06",
    "user_id": 187235,
    "lab": "\u6761\u4ef6\u5224\u65ad",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 09:54:35",
    "user_id": 170834,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 09:55:05",
    "user_id": 197961,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 09:56:42",
    "user_id": 198893,
    "lab": "C\u8bed\u8a00\u5b9e\u73b0WEB\u670d\u52a1\u5668",
    "course": "C\u8bed\u8a00\u5b9e\u73b0\u4e00\u4e2a\u652f\u6301PHP\u7684\u7b80\u6613WEB\u670d\u52a1\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 09:57:31",
    "user_id": 186876,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 09:57:36",
    "user_id": 195750,
    "lab": "Redis\u7cfb\u7edf\u7ba1\u7406",
    "course": "Redis\u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 09:59:15",
    "user_id": 186286,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 10:00:30",
    "user_id": 196382,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 10:00:30",
    "user_id": 185430,
    "lab": "Node.js\u8bfe\u7a0b\u4ecb\u7ecd",
    "course": "Node.js \u6559\u7a0b"
  },
  {
    "minutes": 84,
    "created_at": "2016-05-01 10:01:04",
    "user_id": 199216,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e8c\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 10:01:53",
    "user_id": 196766,
    "lab": "LAMP\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "LAMP\u90e8\u7f72\u53ca\u914d\u7f6e"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-01 10:02:37",
    "user_id": 174908,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 10:03:19",
    "user_id": 199384,
    "lab": "\u6570\u636e\u7ed3\u6784-\u5b57\u7b26\u4e32\uff08String\uff09",
    "course": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 10:05:06",
    "user_id": 3595,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 10:05:28",
    "user_id": 78772,
    "lab": "\u5165\u95e8",
    "course": "Bootstrap3.0\u5165\u95e8\u5b66\u4e60"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-01 10:05:54",
    "user_id": 190712,
    "lab": "makefile",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 10:06:04",
    "user_id": 198635,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 10:08:59",
    "user_id": 199405,
    "lab": "Kaggle\u5165\u95e8",
    "course": "Kaggle\u5165\u95e8\uff1a\u6cf0\u5766\u5c3c\u514b\u53f7\u5e78\u5b58\u8005\u9879\u76ee"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 10:09:09",
    "user_id": 192549,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 10:09:51",
    "user_id": 27306,
    "lab": "\u8ddf\u8e2a\u5206\u6790Linux\u5185\u6838\u7684\u542f\u52a8\u8fc7\u7a0b",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 10:09:57",
    "user_id": 186082,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 10:10:02",
    "user_id": 185857,
    "lab": "\u8bc4\u8bba\u548c\u7559\u8a00\u677f\u529f\u80fd",
    "course": "\u57fa\u4e8eGO\u8bed\u8a00Revel\u6846\u67b6\u548cmgo\u7684\u535a\u5ba2"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 10:10:20",
    "user_id": 185430,
    "lab": "Node.js\u6a21\u5757",
    "course": "Node.js \u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 10:11:36",
    "user_id": 198933,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 10:13:13",
    "user_id": 78772,
    "lab": "\u6805\u683c\u7cfb\u7edf\u539f\u7406",
    "course": "Bootstrap3.0\u5165\u95e8\u5b66\u4e60"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 10:13:13",
    "user_id": 149395,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 10:17:09",
    "user_id": 199337,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 10:18:34",
    "user_id": 199014,
    "lab": "\u4e00\u4e2a\u6700\u7b80\u5355\u7684 express \u5e94\u7528",
    "course": "Node.js\u5305\u6559\u4e0d\u5305\u4f1a"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 10:19:20",
    "user_id": 170834,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 10:19:29",
    "user_id": 170979,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 10:19:56",
    "user_id": 149280,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-01 10:20:04",
    "user_id": 191868,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 10:20:30",
    "user_id": 186876,
    "lab": "\u5f00\u53d1\u73af\u5883\u548c\u5256\u6790\u7b2c\u4e00\u4e2a C \u8bed\u8a00",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 10:20:48",
    "user_id": 199411,
    "lab": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668",
    "course": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 10:21:13",
    "user_id": 116665,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 10:22:05",
    "user_id": 174846,
    "lab": "\u7b2c9\u5468\u8bfe\u5802\u5b9e\u9a8c-\u5b9e\u9a8c1",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 10:23:04",
    "user_id": 52227,
    "lab": "\u95ed\u5305\uff0c\u9012\u5f52",
    "course": "Go by Example \u4e2d\u6587\u7248"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 10:23:27",
    "user_id": 199117,
    "lab": "\u64cd\u4f5c\u7cfb\u7edf\u7684\u5f15\u5bfc",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 10:23:34",
    "user_id": 170979,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 10:23:42",
    "user_id": 199384,
    "lab": "\u6570\u636e\u7ed3\u6784-\u5b57\u7b26\u4e32\uff08String\uff09",
    "course": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-01 10:23:46",
    "user_id": 197227,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 10:24:13",
    "user_id": 197986,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 10:25:03",
    "user_id": 30185,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 10:27:51",
    "user_id": 78772,
    "lab": "\u6805\u683c\u7cfb\u7edf\u6848\u4f8b",
    "course": "Bootstrap3.0\u5165\u95e8\u5b66\u4e60"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 10:28:19",
    "user_id": 170979,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 10:28:28",
    "user_id": 125438,
    "lab": "\u57fa\u4e8escrapy\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u57fa\u4e8escrapy\u722c\u866b\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6(python)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 10:28:38",
    "user_id": 170834,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-01 10:29:13",
    "user_id": 174210,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 10:29:32",
    "user_id": 149280,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u7684\u7ea6\u675f",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 10:29:53",
    "user_id": 174846,
    "lab": "\u7b2c9\u5468\u8bfe\u5802\u5b9e\u9a8c-\u5b9e\u9a8c1",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 69,
    "created_at": "2016-05-01 10:31:45",
    "user_id": 185857,
    "lab": "\u8bc4\u8bba\u548c\u7559\u8a00\u677f\u529f\u80fd",
    "course": "\u57fa\u4e8eGO\u8bed\u8a00Revel\u6846\u67b6\u548cmgo\u7684\u535a\u5ba2"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 10:32:13",
    "user_id": 78772,
    "lab": "\u6392\u7248",
    "course": "Bootstrap3.0\u5165\u95e8\u5b66\u4e60"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 10:32:25",
    "user_id": 197948,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 10:33:29",
    "user_id": 72923,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 10:34:12",
    "user_id": 199253,
    "lab": "\u6587\u6863\uff08document\uff09\u57fa\u672c\u64cd\u4f5c",
    "course": "MongoDB \u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 10:34:42",
    "user_id": 171915,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 10:34:44",
    "user_id": 177141,
    "lab": "\u7b2c10-11\u5468\u8bfe\u5802\u5b9e\u9a8c-\u5b9e\u9a8c\u4e8c \u7ee7\u627f\u6027\u7684\u5b9e\u73b0\uff081-2\uff09",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 10:36:32",
    "user_id": 179731,
    "lab": "Java \u65b9\u6cd5",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 10:37:33",
    "user_id": 27306,
    "lab": "\u8ddf\u8e2a\u5206\u6790Linux\u5185\u6838\u7684\u542f\u52a8\u8fc7\u7a0b",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-01 10:37:35",
    "user_id": 199337,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 10:37:53",
    "user_id": 197961,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 10:39:34",
    "user_id": 199014,
    "lab": "\u5b66\u4e60\u4f7f\u7528\u5916\u90e8\u6a21\u5757",
    "course": "Node.js\u5305\u6559\u4e0d\u5305\u4f1a"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 10:39:52",
    "user_id": 116665,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 10:40:10",
    "user_id": 9267,
    "lab": "Docker \u6982\u5ff5\u53ca\u57fa\u672c\u7528\u6cd5",
    "course": "\u52a8\u624b\u5b9e\u6218\u5b66Docker (15\u4e2a\u5b9e\u9a8c+54\u4e2a\u89c6\u9891)"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 10:41:07",
    "user_id": 72923,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 10:41:18",
    "user_id": 199064,
    "lab": "\u57fa\u4e8escrapy\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u57fa\u4e8escrapy\u722c\u866b\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6(python)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 10:43:17",
    "user_id": 199414,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 10:43:30",
    "user_id": 198635,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-01 10:44:42",
    "user_id": 186876,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e00\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 10:44:43",
    "user_id": 199349,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 10:44:44",
    "user_id": 85549,
    "lab": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c",
    "course": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 10:44:54",
    "user_id": 128327,
    "lab": "Bash\u4e2d\u7684\u7279\u6b8a\u5b57\u7b26\uff08\u4e0a\uff09",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 10:45:21",
    "user_id": 171915,
    "lab": "\u7b2c2\u5468\uff1a\u865a\u62df\u5316\u4e0e\u4e91\u8ba1\u7b97\u6280\u672f",
    "course": "\u4effOpenStack\u5f00\u53d1\u4e91\u8ba1\u7b97\u7ba1\u7406\u8f6f\u4ef6"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 10:46:52",
    "user_id": 197961,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 10:47:11",
    "user_id": 199415,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 10:47:27",
    "user_id": 199174,
    "lab": "\u8bfe\u540e\u4e60\u9898\u4e00",
    "course": "PHP\u4f1a\u8bdd\u63a7\u5236"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-01 10:50:43",
    "user_id": 199307,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 10:52:31",
    "user_id": 34532,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 10:52:44",
    "user_id": 45301,
    "lab": "LAMP\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "LAMP\u90e8\u7f72\u53ca\u914d\u7f6e"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-01 10:52:44",
    "user_id": 173169,
    "lab": "\u5f00\u542f\u795e\u5947\u7684Scala\u7f16\u7a0b\u4e4b\u65c5",
    "course": "Scala\u5f00\u53d1\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 10:54:31",
    "user_id": 172073,
    "lab": "\u7b2c10-11\u5468\u8bfe\u5802\u5b9e\u9a8c-\u5b9e\u9a8c\u4e8c \u7ee7\u627f\u6027\u7684\u5b9e\u73b0\uff081-2\uff09",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 10:54:55",
    "user_id": 60135,
    "lab": "\u5165\u95e8",
    "course": "Bootstrap3.0\u5165\u95e8\u5b66\u4e60"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 10:54:57",
    "user_id": 174908,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 10:55:37",
    "user_id": 165177,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 10:56:19",
    "user_id": 47745,
    "lab": "\u4e2d\u7ea7\u6280\u80fd\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 10:57:25",
    "user_id": 176412,
    "lab": "RethinkDB 10\u5206\u949f\u5165\u95e8",
    "course": "\u57fa\u4e8eFlask/RethinkDB\u5b9e\u73b0TODO List"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 11:00:32",
    "user_id": 29988,
    "lab": "java.lang \u5305",
    "course": "JDK \u6838\u5fc3 API"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-01 11:00:32",
    "user_id": 128327,
    "lab": "Bash\u4e2d\u7684\u7279\u6b8a\u5b57\u7b26\uff08\u4e0b\uff09",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 11:01:49",
    "user_id": 87315,
    "lab": "\u901a\u8fc7\u53cd\u6c47\u7f16\u4e00\u4e2a\u7b80\u5355\u7684C\u7a0b\u5e8f\uff0c\u5206\u6790\u6c47\u7f16\u4ee3\u7801\u7406\u89e3\u8ba1\u7b97\u673a\u662f\u5982\u4f55\u5de5\u4f5c\u7684",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 11:01:52",
    "user_id": 128580,
    "lab": "\u6587\u4ef6IO\uff08\u4e8c\uff09",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-01 11:03:44",
    "user_id": 186465,
    "lab": "Java \u8bed\u8a00\u57fa\u7840",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 11:03:44",
    "user_id": 196766,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 11:03:47",
    "user_id": 199117,
    "lab": "\u64cd\u4f5c\u7cfb\u7edf\u7684\u5f15\u5bfc",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 11:04:25",
    "user_id": 198635,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 11:06:02",
    "user_id": 181279,
    "lab": "Ubuntu 14.04 \u4e0a\u6700\u597d\u7684 GNOME Shell \u4e3b\u9898",
    "course": "Ubuntu\u684c\u9762\u4f53\u9a8c\u8bfe"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-01 11:06:28",
    "user_id": 189187,
    "lab": "makefile",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-01 11:07:12",
    "user_id": 199328,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-01 11:07:37",
    "user_id": 199117,
    "lab": "\u64cd\u4f5c\u7cfb\u7edf\u7684\u5f15\u5bfc",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 11:07:49",
    "user_id": 78772,
    "lab": "\u8868\u683c",
    "course": "Bootstrap3.0\u5165\u95e8\u5b66\u4e60"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 11:08:23",
    "user_id": 57977,
    "lab": "Redis\u6570\u636e\u7c7b\u578b ",
    "course": "Redis\u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-01 11:09:29",
    "user_id": 199174,
    "lab": "session\u57fa\u7840\u4e0e\u5b9e\u6218",
    "course": "PHP\u4f1a\u8bdd\u63a7\u5236"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 11:10:00",
    "user_id": 199337,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 99,
    "created_at": "2016-05-01 11:12:17",
    "user_id": 197423,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0b\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 11:12:26",
    "user_id": 51867,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 11:12:32",
    "user_id": 87879,
    "lab": "\u8bfe\u7a0b\u8bf4\u660e\u4e0e\u5b66\u4e60\u65b9\u6cd5\uff08HowTo\uff09",
    "course": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 11:12:40",
    "user_id": 158425,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 11:13:37",
    "user_id": 174908,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 11:15:00",
    "user_id": 194274,
    "lab": "\u6570\u636e\u7ed3\u6784-\u5b57\u7b26\u4e32\uff08String\uff09",
    "course": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 11:15:44",
    "user_id": 199014,
    "lab": "\u4f7f\u7528 superagent \u4e0e cheerio \u5b8c\u6210\u7b80\u5355\u722c\u866b",
    "course": "Node.js\u5305\u6559\u4e0d\u5305\u4f1a"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 11:15:52",
    "user_id": 199268,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 11:16:44",
    "user_id": 172073,
    "lab": "\u7b2c10-11\u5468\u8bfe\u5802\u5b9e\u9a8c-\u5b9e\u9a8c\u4e8c \u7ee7\u627f\u6027\u7684\u5b9e\u73b0\uff081-2\uff09",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 11:17:47",
    "user_id": 199421,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 8,
    "created_at": "2016-05-01 11:18:08",
    "user_id": 199417,
    "lab": "\u6570\u636e\u7ed3\u6784-\u5b57\u7b26\u4e32\uff08String\uff09",
    "course": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-01 11:18:52",
    "user_id": 192178,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 11:20:03",
    "user_id": 87315,
    "lab": "\u5b8c\u6210\u4e00\u4e2a\u7b80\u5355\u7684\u65f6\u95f4\u7247\u8f6e\u8f6c\u591a\u9053\u7a0b\u5e8f\u5185\u6838\u4ee3\u7801",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 11:21:40",
    "user_id": 52227,
    "lab": "\u6307\u9488\uff0c\u7ed3\u6784\u4f53\uff0c\u65b9\u6cd5\uff0c\u63a5\u53e3",
    "course": "Go by Example \u4e2d\u6587\u7248"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 11:23:19",
    "user_id": 158425,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 11:23:19",
    "user_id": 193356,
    "lab": "\u8ba4\u8bc6J2SE",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 11:26:56",
    "user_id": 97942,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 11:29:51",
    "user_id": 199425,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 11:31:19",
    "user_id": 101086,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 11:32:12",
    "user_id": 194274,
    "lab": "\u6570\u636e\u7ed3\u6784-\u94fe\u8868\uff08Linked List\uff09",
    "course": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 11:32:42",
    "user_id": 158026,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 11:33:36",
    "user_id": 188670,
    "lab": "\u6a21\u578b\uff08\u4e8c\uff09",
    "course": "[\u5df2\u4e0b\u7ebf] Python Django Web\u6846\u67b6"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 11:34:16",
    "user_id": 199425,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 11:34:19",
    "user_id": 196942,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-01 11:34:55",
    "user_id": 199337,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 11:35:59",
    "user_id": 197986,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-01 11:36:10",
    "user_id": 199316,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 11:37:06",
    "user_id": 193497,
    "lab": "\u6570\u636e\u7ed3\u6784-\u5b57\u7b26\u4e32\uff08String\uff09",
    "course": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 11:38:46",
    "user_id": 72782,
    "lab": "\u4f7f\u7528 eventproxy \u63a7\u5236\u5e76\u53d1",
    "course": "Node.js\u5305\u6559\u4e0d\u5305\u4f1a"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 11:41:39",
    "user_id": 193497,
    "lab": "\u6570\u636e\u7ed3\u6784-\u94fe\u8868\uff08Linked List\uff09",
    "course": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 11:44:59",
    "user_id": 146207,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 11:45:57",
    "user_id": 176412,
    "lab": "Python\u6587\u672c\u89e3\u91ca\u5668",
    "course": "Python\u6587\u672c\u89e3\u6790\u5668"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 11:47:40",
    "user_id": 199430,
    "lab": "PHP\u7b80\u4ecb",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 11:48:55",
    "user_id": 199423,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 11:54:43",
    "user_id": 181461,
    "lab": "\u6a21\u5757\u5316\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 11:55:12",
    "user_id": 199433,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 11:55:16",
    "user_id": 199314,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 11:57:51",
    "user_id": 150634,
    "lab": "\u4f20\u8f93\u5c42\uff1aUDP\u534f\u8bae",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 11:58:24",
    "user_id": 157089,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e00\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 11:58:39",
    "user_id": 199429,
    "lab": "Java \u8bed\u8a00\u57fa\u7840",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 69,
    "created_at": "2016-05-01 11:58:58",
    "user_id": 136676,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 11:59:52",
    "user_id": 78772,
    "lab": "\u6309\u94ae",
    "course": "Bootstrap3.0\u5165\u95e8\u5b66\u4e60"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 12:00:39",
    "user_id": 140305,
    "lab": "\u6570\u636e\u5e93",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 12:01:39",
    "user_id": 199436,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 12:06:38",
    "user_id": 197330,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 12:08:10",
    "user_id": 193213,
    "lab": "css\u5165\u95e8\u57fa\u7840",
    "course": "CSS\u901f\u6210\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 12:08:19",
    "user_id": 191567,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 12:10:15",
    "user_id": 128580,
    "lab": "\u6587\u4ef6IO\uff08\u4e8c\uff09",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 12:11:29",
    "user_id": 199337,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 132,
    "created_at": "2016-05-01 12:11:46",
    "user_id": 140305,
    "lab": "\u7528\u6237\u767b\u5f55",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 12:12:13",
    "user_id": 198933,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 12:14:38",
    "user_id": 174846,
    "lab": "\u7b2c10-11\u5468\u8bfe\u5802\u5b9e\u9a8c-\u5b9e\u9a8c\u4e8c \u7ee7\u627f\u6027\u7684\u5b9e\u73b0\uff081-2\uff09",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-01 12:18:08",
    "user_id": 199328,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 12:19:08",
    "user_id": 192178,
    "lab": "\u8def\u7531",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 12:20:28",
    "user_id": 149395,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0b\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-01 12:23:28",
    "user_id": 115662,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 12:24:14",
    "user_id": 174846,
    "lab": "\u7b2c10-11\u5468\u8bfe\u5802\u5b9e\u9a8c-\u5b9e\u9a8c\u4e8c \u7ee7\u627f\u6027\u7684\u5b9e\u73b0\uff081-2\uff09",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 12:26:03",
    "user_id": 199337,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 12:27:37",
    "user_id": 199438,
    "lab": "Hadoop\u4ecb\u7ecd\u53ca1.X\u4f2a\u5206\u5e03\u5f0f\u5b89\u88c5",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 12:27:58",
    "user_id": 45301,
    "lab": "LAMP\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "LAMP\u90e8\u7f72\u53ca\u914d\u7f6e"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 12:29:23",
    "user_id": 195063,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 12:30:08",
    "user_id": 184704,
    "lab": "PHP\u7b80\u4ecb",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-01 12:30:11",
    "user_id": 193213,
    "lab": "\u57fa\u7840\u9009\u62e9\u5668",
    "course": "CSS\u901f\u6210\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 12:30:40",
    "user_id": 186294,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 12:31:48",
    "user_id": 160153,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 12:32:10",
    "user_id": 175180,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 12:34:29",
    "user_id": 199337,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 78,
    "created_at": "2016-05-01 12:36:19",
    "user_id": 175180,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 12:37:08",
    "user_id": 186294,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 12:37:25",
    "user_id": 173414,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 12:38:44",
    "user_id": 61339,
    "lab": "Node.js\u8bfe\u7a0b\u4ecb\u7ecd",
    "course": "Node.js \u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 12:41:44",
    "user_id": 84362,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 12:41:50",
    "user_id": 150634,
    "lab": "\u5e94\u7528\u5c42\u534f\u8bae\u4e00",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 90,
    "created_at": "2016-05-01 12:45:28",
    "user_id": 45301,
    "lab": "LAMP\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "LAMP\u90e8\u7f72\u53ca\u914d\u7f6e"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 12:48:40",
    "user_id": 84362,
    "lab": "\u5f00\u53d1\u73af\u5883\u548c\u5256\u6790\u7b2c\u4e00\u4e2a C \u8bed\u8a00",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 12:49:14",
    "user_id": 199337,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-01 12:49:21",
    "user_id": 197961,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 12:51:52",
    "user_id": 199441,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 12:55:23",
    "user_id": 176291,
    "lab": "\u6307\u9488\uff08\u4e00\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 12:55:23",
    "user_id": 78772,
    "lab": "\u5de5\u5177Class",
    "course": "Bootstrap3.0\u5165\u95e8\u5b66\u4e60"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 12:56:54",
    "user_id": 150634,
    "lab": "\u6982\u8ff0",
    "course": "\u5b9e\u7528Linux Shell\u7f16\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 12:58:39",
    "user_id": 199337,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 12:59:55",
    "user_id": 79909,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 13:00:27",
    "user_id": 193213,
    "lab": "css\u57fa\u672c\u6837\u5f0f\uff08\u4e00\uff09",
    "course": "CSS\u901f\u6210\u6559\u7a0b"
  },
  {
    "minutes": 120,
    "created_at": "2016-05-01 13:01:15",
    "user_id": 199426,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-01 13:05:17",
    "user_id": 84362,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e00\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-01 13:09:19",
    "user_id": 170979,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 13:10:15",
    "user_id": 198635,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 13:11:39",
    "user_id": 193213,
    "lab": "\u5de5\u5382\u6a21\u5f0f",
    "course": "Java\u8fdb\u9636\u4e4b\u8bbe\u8ba1\u6a21\u5f0f"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 13:11:47",
    "user_id": 196288,
    "lab": "\u57fa\u7840\u6b63\u5219\u8868\u8fbe\u5f0f\u4ecb\u7ecd\u4e0e\u7ec3\u4e60",
    "course": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 13:12:06",
    "user_id": 173414,
    "lab": "git\u4ecb\u7ecd",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 78,
    "created_at": "2016-05-01 13:16:39",
    "user_id": 174304,
    "lab": "\u6307\u9488\uff08\u4e00\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-01 13:17:10",
    "user_id": 128580,
    "lab": "\u6587\u4ef6IO\uff08\u4e8c\uff09",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-01 13:19:04",
    "user_id": 126124,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-01 13:24:11",
    "user_id": 199316,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 13:24:56",
    "user_id": 199448,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 13:26:44",
    "user_id": 199440,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 13:28:56",
    "user_id": 185857,
    "lab": "\u8bc4\u8bba\u548c\u7559\u8a00\u677f\u529f\u80fd",
    "course": "\u57fa\u4e8eGO\u8bed\u8a00Revel\u6846\u67b6\u548cmgo\u7684\u535a\u5ba2"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 13:30:41",
    "user_id": 175364,
    "lab": "\u8ba4\u8bc6wxpython",
    "course": "\u7528Python\u505a2048\u6e38\u620f"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 13:31:11",
    "user_id": 199440,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 13:37:21",
    "user_id": 60135,
    "lab": "\u5165\u95e8",
    "course": "Bootstrap3.0\u5165\u95e8\u5b66\u4e60"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 13:40:16",
    "user_id": 76508,
    "lab": "\u6570\u636e\u7c7b\u578b\uff08\u4e00\uff09",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 13:40:23",
    "user_id": 193511,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-01 13:42:24",
    "user_id": 199253,
    "lab": "\u67e5\u8be2\u3001\u7d22\u5f15\u4e0e\u805a\u5408",
    "course": "MongoDB \u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 13:49:39",
    "user_id": 199425,
    "lab": "\u8bbe\u8ba1\u6a21\u5f0f\u7b80\u4ecb",
    "course": "Java\u8fdb\u9636\u4e4b\u8bbe\u8ba1\u6a21\u5f0f"
  },
  {
    "minutes": 78,
    "created_at": "2016-05-01 13:50:08",
    "user_id": 174846,
    "lab": "\u7b2c10-11\u5468\u8bfe\u5802\u5b9e\u9a8c-\u5b9e\u9a8c\u4e8c \u7ee7\u627f\u6027\u7684\u5b9e\u73b0\uff081-2\uff09",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 13:52:14",
    "user_id": 199450,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 13:52:30",
    "user_id": 84362,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e8c\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-01 13:52:57",
    "user_id": 76508,
    "lab": "ThinkPHP\u5b89\u88c5\u4e0e\u914d\u7f6e",
    "course": "ThinkPHP\u6846\u67b6\u5b9e\u8df5"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 13:53:10",
    "user_id": 195663,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 13:57:00",
    "user_id": 32346,
    "lab": "\u8ddf\u8e2a\u5206\u6790Linux\u5185\u6838\u7684\u542f\u52a8\u8fc7\u7a0b",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 13:57:05",
    "user_id": 182621,
    "lab": "\u7b2c1\u5468\uff1aC++\u57fa\u7840\u5165\u95e8\uff08\u7b2c1\u7ae0\u81f3\u7b2c3\u7ae0\uff09",
    "course": "\u6df1\u5165\u5b66\u4e60 \u300aC++ Primer \u7b2c\u4e94\u7248\u300b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 13:57:07",
    "user_id": 193511,
    "lab": "DOS\u53caDEBUG\u4ecb\u7ecd",
    "course": "\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u90d1\u6653\u8587\u7f16\u8457\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-01 13:57:39",
    "user_id": 199307,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 14:00:37",
    "user_id": 199425,
    "lab": "\u5de5\u5382\u6a21\u5f0f",
    "course": "Java\u8fdb\u9636\u4e4b\u8bbe\u8ba1\u6a21\u5f0f"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 14:00:43",
    "user_id": 174178,
    "lab": "\u4e00\u4e2a\u6700\u7b80\u5355\u7684 express \u5e94\u7528",
    "course": "Node.js\u5305\u6559\u4e0d\u5305\u4f1a"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 14:01:25",
    "user_id": 199014,
    "lab": "\u4f7f\u7528 eventproxy \u63a7\u5236\u5e76\u53d1",
    "course": "Node.js\u5305\u6559\u4e0d\u5305\u4f1a"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 14:02:06",
    "user_id": 199452,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 14:02:12",
    "user_id": 175364,
    "lab": "\u8ba4\u8bc6wxpython",
    "course": "\u7528Python\u505a2048\u6e38\u620f"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 14:05:17",
    "user_id": 199454,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-01 14:05:27",
    "user_id": 163762,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 14:07:03",
    "user_id": 192069,
    "lab": "\u9879\u76ee\u4e94\uff1a\u6587\u5b57\u804a\u5929\u5ba4",
    "course": "Python \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 14:08:34",
    "user_id": 198080,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-01 14:11:16",
    "user_id": 116171,
    "lab": "Python\u6807\u51c6\u5e93\u57fa\u7840",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 111,
    "created_at": "2016-05-01 14:11:18",
    "user_id": 80485,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 14:13:15",
    "user_id": 179356,
    "lab": "\u7b2c10-11\u5468\u8bfe\u5802\u5b9e\u9a8c-\u5b9e\u9a8c\u4e8c \u7ee7\u627f\u6027\u7684\u5b9e\u73b0\uff081-2\uff09",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 14:14:32",
    "user_id": 185857,
    "lab": "\u5f52\u6863\u548c\u63d0\u9192\u529f\u80fd",
    "course": "\u57fa\u4e8eGO\u8bed\u8a00Revel\u6846\u67b6\u548cmgo\u7684\u535a\u5ba2"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-01 14:14:46",
    "user_id": 199454,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-01 14:16:05",
    "user_id": 173414,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 14:17:02",
    "user_id": 172073,
    "lab": "\u7b2c10-11\u5468\u8bfe\u5802\u5b9e\u9a8c-\u5b9e\u9a8c\u4e8c \u7ee7\u627f\u6027\u7684\u5b9e\u73b0\uff081-2\uff09",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 14:17:07",
    "user_id": 199452,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 14:18:48",
    "user_id": 199456,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 14:19:21",
    "user_id": 76508,
    "lab": "ThinkPHP \u8def\u7531",
    "course": "ThinkPHP\u6846\u67b6\u5b9e\u8df5"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-01 14:20:25",
    "user_id": 197775,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 14:21:11",
    "user_id": 114336,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 14:22:02",
    "user_id": 159200,
    "lab": "\u9000\u51fa\u548c\u9000\u51fa\u72b6\u6001\u7801",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-01 14:23:41",
    "user_id": 192178,
    "lab": "Python\u6df1\u5165\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 14:23:48",
    "user_id": 196472,
    "lab": "HTML\u8d85\u6587\u672c\uff08\u4e00\uff09",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 2,
    "created_at": "2016-05-01 14:24:29",
    "user_id": 110824,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 14:24:39",
    "user_id": 113750,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 14:27:30",
    "user_id": 199270,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 14:27:32",
    "user_id": 108295,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 14:27:55",
    "user_id": 198823,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 14:29:18",
    "user_id": 126124,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 14:30:37",
    "user_id": 165946,
    "lab": "Docker \u6982\u5ff5\u53ca\u57fa\u672c\u7528\u6cd5",
    "course": "\u52a8\u624b\u5b9e\u6218\u5b66Docker (15\u4e2a\u5b9e\u9a8c+54\u4e2a\u89c6\u9891)"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 14:31:46",
    "user_id": 114336,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 14:32:22",
    "user_id": 184704,
    "lab": "PHP\u7b80\u4ecb",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 14:32:24",
    "user_id": 110824,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 14:35:01",
    "user_id": 196906,
    "lab": "HTML\u8d85\u6587\u672c\uff08\u4e00\uff09",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 14:35:16",
    "user_id": 157089,
    "lab": "\u57fa\u7840\u6b63\u5219\u8868\u8fbe\u5f0f\u4ecb\u7ecd\u4e0e\u7ec3\u4e60",
    "course": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-01 14:35:49",
    "user_id": 87315,
    "lab": "lab0\uff1aCoding!",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u5b9e\u9a8c\uff0d\u57fa\u4e8euCore OS"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 14:36:13",
    "user_id": 108295,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 14:37:25",
    "user_id": 199071,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 14:38:10",
    "user_id": 113750,
    "lab": "Docker \u6982\u5ff5\u53ca\u57fa\u672c\u7528\u6cd5",
    "course": "\u52a8\u624b\u5b9e\u6218\u5b66Docker (15\u4e2a\u5b9e\u9a8c+54\u4e2a\u89c6\u9891)"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-01 14:39:36",
    "user_id": 198847,
    "lab": "Linux\u7cfb\u7edf\u547d\u4ee4",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 14:41:48",
    "user_id": 150606,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-01 14:41:50",
    "user_id": 76508,
    "lab": "ThinkPHP\u5b89\u88c5\u4e0e\u914d\u7f6e",
    "course": "ThinkPHP\u6846\u67b6\u5b9e\u8df5"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 14:43:11",
    "user_id": 198080,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 14:44:26",
    "user_id": 174149,
    "lab": "\u9879\u76ee\u4e94\uff1a\u6587\u5b57\u804a\u5929\u5ba4",
    "course": "Python \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 14:44:50",
    "user_id": 80356,
    "lab": "\u6a21\u62dfATM\u81ea\u52a8\u53d6\u6b3e\u673a\u7cfb\u7edf",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011C\u8bed\u8a00\u6a21\u62dfATM\u81ea\u52a8\u53d6\u6b3e\u673a\u7cfb\u7edf"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 14:45:15",
    "user_id": 199440,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 14:45:15",
    "user_id": 196942,
    "lab": "cookie\u57fa\u7840\u548c\u5e94\u7528",
    "course": "PHP\u4f1a\u8bdd\u63a7\u5236"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 14:45:29",
    "user_id": 126124,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 14:49:17",
    "user_id": 182192,
    "lab": "\u56fe\u7b97\u6cd5",
    "course": "\u7ecf\u5178\u7b97\u6cd5\u89e3\u9898\u5b9e\u6218"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-01 14:49:59",
    "user_id": 159200,
    "lab": "\u6761\u4ef6\u5224\u65ad",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 14:50:47",
    "user_id": 150606,
    "lab": "HTML5\u5b9e\u73b0\u522e\u522e\u4e50\u6548\u679c",
    "course": "\u57fa\u4e8e HTML5 \u5b9e\u73b0\u522e\u522e\u4e50\u6548\u679c"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-01 14:51:44",
    "user_id": 157089,
    "lab": "grep\u547d\u4ee4\u4e0e\u6b63\u5219\u8868\u8fbe\u5f0f",
    "course": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 14:52:33",
    "user_id": 100497,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 14:54:13",
    "user_id": 199461,
    "lab": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668",
    "course": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-01 14:54:52",
    "user_id": 198933,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-01 14:56:37",
    "user_id": 118507,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 14:59:06",
    "user_id": 199461,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 15:00:17",
    "user_id": 172073,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 15:00:51",
    "user_id": 199435,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 15:00:59",
    "user_id": 165499,
    "lab": "Yii 2\u7684\u5b89\u88c5",
    "course": "Yii 2\u7cfb\u5217\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 15:02:44",
    "user_id": 170979,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 15:03:20",
    "user_id": 199071,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-01 15:04:16",
    "user_id": 114336,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-01 15:08:20",
    "user_id": 199235,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 15:09:09",
    "user_id": 199465,
    "lab": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668",
    "course": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 15:10:16",
    "user_id": 199457,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 15:13:13",
    "user_id": 65915,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 15:13:32",
    "user_id": 199461,
    "lab": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668",
    "course": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 15:13:33",
    "user_id": 7600,
    "lab": "\u521d\u8bc6MySQL",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 15:15:33",
    "user_id": 149592,
    "lab": "PHP\u7559\u8a00\u672c",
    "course": "PHP \u5b9e\u73b0\u7559\u8a00\u672c"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 15:16:14",
    "user_id": 199467,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 15:16:33",
    "user_id": 196942,
    "lab": "\u8bfe\u540e\u4e60\u9898\u4e00",
    "course": "PHP\u4f1a\u8bdd\u63a7\u5236"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 15:16:58",
    "user_id": 193392,
    "lab": "\u57fa\u7840\u7ec4\u4ef6\uff083\uff09 - Content Provider",
    "course": "Android\u5e94\u7528\u5f00\u53d1\u57fa\u7840"
  },
  {
    "minutes": 5,
    "created_at": "2016-05-01 15:19:08",
    "user_id": 199466,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 15:21:04",
    "user_id": 198365,
    "lab": "\u5f52\u6863, AboutMe\u548c\u6807\u7b7e\u5206\u7c7b",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 63,
    "created_at": "2016-05-01 15:21:05",
    "user_id": 185000,
    "lab": "C++\u7b80\u5355\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "\u300aC++\u8bed\u8a00\u7a0b\u5e8f\u8bbe\u8ba1\uff08\u7b2c4\u7248\uff09\u300b\uff08\u90d1\u8389\u8457\uff09\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 15:21:34",
    "user_id": 173414,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 15:23:04",
    "user_id": 186649,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-01 15:23:16",
    "user_id": 158717,
    "lab": "Hadoop\u4ecb\u7ecd\u53ca1.X\u4f2a\u5206\u5e03\u5f0f\u5b89\u88c5",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-01 15:25:06",
    "user_id": 195663,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 15:25:32",
    "user_id": 157089,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u8fd0\u7528\u4e4b sed\u5de5\u5177\u547d\u4ee4 ",
    "course": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 15:28:27",
    "user_id": 157232,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 15:28:56",
    "user_id": 195306,
    "lab": "JavaScript \u7b80\u4ecb",
    "course": "Javascript\u57fa\u7840\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 15:30:55",
    "user_id": 198335,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 15:32:27",
    "user_id": 108295,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 120,
    "created_at": "2016-05-01 15:33:54",
    "user_id": 7600,
    "lab": "MySQL\u57fa\u672c\u64cd\u4f5c",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 15:36:41",
    "user_id": 186876,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e8c\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 15:36:49",
    "user_id": 76508,
    "lab": "ThinkPHP \u8def\u7531",
    "course": "ThinkPHP\u6846\u67b6\u5b9e\u8df5"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 15:37:34",
    "user_id": 198847,
    "lab": "vi\u7f16\u8bd1\u5668\u7684\u4f7f\u7528",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 15:37:49",
    "user_id": 199471,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 15:38:34",
    "user_id": 199270,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 15:39:32",
    "user_id": 176758,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 15:39:55",
    "user_id": 108295,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 15:42:12",
    "user_id": 199472,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 15:42:34",
    "user_id": 196942,
    "lab": "session\u57fa\u7840\u4e0e\u5b9e\u6218",
    "course": "PHP\u4f1a\u8bdd\u63a7\u5236"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 15:42:36",
    "user_id": 173414,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 15:42:49",
    "user_id": 199473,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 15:44:45",
    "user_id": 196472,
    "lab": "HTML\u8d85\u6587\u672c\uff08\u4e00\uff09",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 2,
    "created_at": "2016-05-01 15:45:50",
    "user_id": 110824,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 15:46:45",
    "user_id": 125064,
    "lab": "HDFS\u539f\u7406\u53ca\u64cd\u4f5c",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 15:46:56",
    "user_id": 198365,
    "lab": "Models\u548cAdmin\u4ee5\u53caViews\u548cURL",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 15:47:52",
    "user_id": 199080,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 15:48:21",
    "user_id": 199474,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 15:48:50",
    "user_id": 198847,
    "lab": "gcc\u7f16\u8bd1\u5668\u7684\u4f7f\u7528",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 15:52:11",
    "user_id": 27371,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 15:54:49",
    "user_id": 197961,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-01 15:55:23",
    "user_id": 198365,
    "lab": "Template\u548c\u52a8\u6001URL",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 15:56:08",
    "user_id": 186876,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e8c\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 15:57:16",
    "user_id": 170979,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 15:57:47",
    "user_id": 199080,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 15:59:11",
    "user_id": 183304,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:02:16",
    "user_id": 192178,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-01 16:02:22",
    "user_id": 136676,
    "lab": "Python\u6df1\u5165\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 16:03:14",
    "user_id": 193581,
    "lab": "\u5165\u95e8",
    "course": "Bootstrap3.0\u5165\u95e8\u5b66\u4e60"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 16:03:19",
    "user_id": 199233,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:05:04",
    "user_id": 172334,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 16:05:18",
    "user_id": 143891,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:05:45",
    "user_id": 199476,
    "lab": "\u5f00\u542f\u795e\u5947\u7684Scala\u7f16\u7a0b\u4e4b\u65c5",
    "course": "Scala\u5f00\u53d1\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 16:11:46",
    "user_id": 173414,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 16:11:46",
    "user_id": 157770,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 16:11:47",
    "user_id": 186658,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-01 16:12:21",
    "user_id": 170768,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 16:13:34",
    "user_id": 172334,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 16:15:08",
    "user_id": 199233,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 16:16:24",
    "user_id": 114767,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:16:55",
    "user_id": 173494,
    "lab": "  HTML5\u4e24\u6b65\u5b9e\u73b0\u62fc\u56fe\u6e38\u620f",
    "course": "\u7f51\u9875\u7248\u62fc\u56fe\u6e38\u620f"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:16:55",
    "user_id": 199080,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 16:17:02",
    "user_id": 192549,
    "lab": "\u6570\u636e\u7ed3\u6784",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 16:19:03",
    "user_id": 199454,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 16:19:15",
    "user_id": 145739,
    "lab": "\u591a\u7ebf\u7a0b\u7f16\u7a0b",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 16:19:26",
    "user_id": 199479,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:21:07",
    "user_id": 185857,
    "lab": "\u5f52\u6863\u548c\u63d0\u9192\u529f\u80fd",
    "course": "\u57fa\u4e8eGO\u8bed\u8a00Revel\u6846\u67b6\u548cmgo\u7684\u535a\u5ba2"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 16:22:58",
    "user_id": 184616,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:23:32",
    "user_id": 186658,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 16:26:46",
    "user_id": 114336,
    "lab": "C\u8bed\u8a00\u7248\u626b\u96f7\u6e38\u620f",
    "course": "C\u8bed\u8a00\u7248\u626b\u96f7\u6e38\u620f"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 16:27:14",
    "user_id": 196878,
    "lab": "LNMP\u7cfb\u7edf\u5b89\u88c5",
    "course": "Linux Web\u8fd0\u7ef4\uff08Nginx\uff09\u5b9e\u6218 "
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 16:28:42",
    "user_id": 186658,
    "lab": "Bash\u4ecb\u7ecd\u4e0e\u5165\u95e8",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 16:29:21",
    "user_id": 115662,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-01 16:29:53",
    "user_id": 170073,
    "lab": "\u64cd\u4f5c\u7cfb\u7edf\u7684\u5f15\u5bfc",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 16:30:02",
    "user_id": 139688,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:30:04",
    "user_id": 199233,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:30:22",
    "user_id": 196080,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 16:31:41",
    "user_id": 199390,
    "lab": "\u7528\u65f6\u95f4\u5e8f\u5217\u9884\u6d4b\u80a1\u7968\u6536\u76ca",
    "course": "[\u5df2\u4e0b\u7ebf] R\u8bed\u8a00\u80a1\u7968\u6570\u636e\u5206\u6790"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-01 16:31:47",
    "user_id": 171973,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 16:33:09",
    "user_id": 163015,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:33:40",
    "user_id": 199233,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-01 16:33:50",
    "user_id": 116727,
    "lab": "Python\u8865\u5145",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:34:01",
    "user_id": 199480,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-01 16:34:04",
    "user_id": 80485,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:34:19",
    "user_id": 199483,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:34:27",
    "user_id": 165586,
    "lab": "HTML5\u7684\u65b0\u7684\u7ed3\u6784\u5143\u7d20\u4ecb\u7ecd",
    "course": "HTML5\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:36:01",
    "user_id": 196878,
    "lab": "LNMP\u7cfb\u7edf\u5b89\u88c5",
    "course": "Linux Web\u8fd0\u7ef4\uff08Nginx\uff09\u5b9e\u6218 "
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:37:16",
    "user_id": 72923,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 16:38:42",
    "user_id": 199481,
    "lab": "\u57fa\u4e8escrapy\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u57fa\u4e8escrapy\u722c\u866b\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6(python)"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-01 16:38:48",
    "user_id": 53927,
    "lab": "Python\u6807\u51c6\u5e93\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:39:32",
    "user_id": 199142,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:40:23",
    "user_id": 199486,
    "lab": "\u5728Android Studio\u4e2d\u521b\u5efa\u9879\u76ee\u548c\u865a\u62df\u673a",
    "course": "Android Studio\u9879\u76ee\u521b\u5efa\u548c\u6a21\u62df\u5668\u914d\u7f6e"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:41:28",
    "user_id": 119886,
    "lab": "\u89c2\u5bdf\u8005\u6a21\u5f0f",
    "course": "Java\u8fdb\u9636\u4e4b\u8bbe\u8ba1\u6a21\u5f0f"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-01 16:43:05",
    "user_id": 199488,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 78,
    "created_at": "2016-05-01 16:43:11",
    "user_id": 52524,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-01 16:43:27",
    "user_id": 197775,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 16:44:23",
    "user_id": 199233,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 16:45:04",
    "user_id": 139688,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 16:45:30",
    "user_id": 184616,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 16:45:44",
    "user_id": 199480,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 17,
    "created_at": "2016-05-01 16:46:39",
    "user_id": 165586,
    "lab": "Redis\u7b80\u4ecb\u4e0e\u5b89\u88c5",
    "course": "Redis\u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:46:46",
    "user_id": 78243,
    "lab": "\u5728Android Studio\u4e2d\u521b\u5efa\u9879\u76ee\u548c\u865a\u62df\u673a",
    "course": "Android Studio\u9879\u76ee\u521b\u5efa\u548c\u6a21\u62df\u5668\u914d\u7f6e"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:47:56",
    "user_id": 91431,
    "lab": "Docker \u6982\u5ff5\u53ca\u57fa\u672c\u7528\u6cd5",
    "course": "\u52a8\u624b\u5b9e\u6218\u5b66Docker (15\u4e2a\u5b9e\u9a8c+54\u4e2a\u89c6\u9891)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:48:30",
    "user_id": 198416,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:49:33",
    "user_id": 199483,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 16:49:33",
    "user_id": 198365,
    "lab": "\u5f52\u6863, AboutMe\u548c\u6807\u7b7e\u5206\u7c7b",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 16:49:46",
    "user_id": 173414,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-01 16:52:48",
    "user_id": 193213,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:54:24",
    "user_id": 199483,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 16:55:13",
    "user_id": 199491,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:56:04",
    "user_id": 199270,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 16:57:10",
    "user_id": 30185,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 16:57:54",
    "user_id": 184616,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 16:59:06",
    "user_id": 72782,
    "lab": "\u4f7f\u7528 eventproxy \u63a7\u5236\u5e76\u53d1",
    "course": "Node.js\u5305\u6559\u4e0d\u5305\u4f1a"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-01 17:00:53",
    "user_id": 199480,
    "lab": "pandas \u56de\u987e",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python \u6570\u636e\u5206\u6790\uff08\u4e00\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 17:06:10",
    "user_id": 196766,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 17:06:39",
    "user_id": 198465,
    "lab": "\u7b80\u5355\u7684\u8bcd\u6cd5\u5206\u6790\u5668\uff08c++\u8bed\u8a00\uff09",
    "course": "\u7b80\u5355\u8bcd\u6cd5\u5206\u6790\u5668\uff08C++\u8bed\u8a00\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 17:08:10",
    "user_id": 189821,
    "lab": "Python\u6df1\u5165\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 17:08:54",
    "user_id": 3459,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 17:09:10",
    "user_id": 190560,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 17:09:25",
    "user_id": 165586,
    "lab": "Redis\u6570\u636e\u7c7b\u578b ",
    "course": "Redis\u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 17:10:04",
    "user_id": 199233,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 17:10:45",
    "user_id": 116727,
    "lab": "Python\u6807\u51c6\u5e93\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 17:10:57",
    "user_id": 24141,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 17:11:18",
    "user_id": 3384,
    "lab": "Flask \u7684 Web \u8868\u5355",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 17:12:25",
    "user_id": 198365,
    "lab": "\u641c\u7d22\u548cReadmore\u4e0eRSS\u548c\u5206\u9875",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-01 17:15:00",
    "user_id": 190560,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-01 17:17:42",
    "user_id": 196766,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 17:17:58",
    "user_id": 199497,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 69,
    "created_at": "2016-05-01 17:18:53",
    "user_id": 81189,
    "lab": "\u5730\u5740\u6620\u5c04\u4e0e\u5171\u4eab",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 17:19:47",
    "user_id": 72782,
    "lab": "\u4f7f\u7528 async \u63a7\u5236\u5e76\u53d1",
    "course": "Node.js\u5305\u6559\u4e0d\u5305\u4f1a"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 17:21:57",
    "user_id": 187252,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-01 17:22:09",
    "user_id": 186465,
    "lab": "Java \u8bed\u8a00\u57fa\u7840",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 17:23:22",
    "user_id": 199496,
    "lab": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668",
    "course": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-01 17:24:23",
    "user_id": 199479,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 17:30:21",
    "user_id": 187252,
    "lab": "\u5f00\u53d1\u73af\u5883\u548c\u5256\u6790\u7b2c\u4e00\u4e2a C \u8bed\u8a00",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 17:31:57",
    "user_id": 198915,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 17:35:01",
    "user_id": 24141,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 17:36:01",
    "user_id": 172334,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 17:37:54",
    "user_id": 198693,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 17:38:38",
    "user_id": 187252,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e00\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 17:39:21",
    "user_id": 3384,
    "lab": "Flask \u7684 Web \u8868\u5355",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 17:40:20",
    "user_id": 190560,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 17:43:25",
    "user_id": 199268,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 17:45:05",
    "user_id": 171973,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-01 17:47:00",
    "user_id": 84362,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u8fd0\u7b97\u7b26\u548c\u6570\u636e\u8f6c\u6362",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 17:50:00",
    "user_id": 191429,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 17:54:18",
    "user_id": 199270,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 17:58:43",
    "user_id": 146207,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 18:03:07",
    "user_id": 3384,
    "lab": "\u6570\u636e\u5e93",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 18:03:43",
    "user_id": 199510,
    "lab": "\u5f00\u53d1\u73af\u5883\u4ee5\u53ca\u9879\u76ee\u4e0eApp",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 18:05:27",
    "user_id": 198933,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 18:12:59",
    "user_id": 199509,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 18:13:37",
    "user_id": 196766,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 18:15:42",
    "user_id": 186286,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 18:16:05",
    "user_id": 154247,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u8fd0\u7b97\u7b26\u548c\u6570\u636e\u8f6c\u6362",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-01 18:16:53",
    "user_id": 198933,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-01 18:17:17",
    "user_id": 175134,
    "lab": "Python\u6807\u51c6\u5e93\uff08\u4e2d\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 18:18:28",
    "user_id": 187941,
    "lab": "\u6570\u636e\u7ed3\u6784-\u94fe\u8868\uff08Linked List\uff09",
    "course": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 18:19:48",
    "user_id": 199517,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 18:20:15",
    "user_id": 199507,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 18:20:21",
    "user_id": 186465,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 18:20:52",
    "user_id": 157770,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 18:22:08",
    "user_id": 199516,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 18:24:24",
    "user_id": 198635,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 18:26:06",
    "user_id": 85944,
    "lab": "\u8bfe\u7a0b\u8bf4\u660e\u4e0e\u5b66\u4e60\u65b9\u6cd5",
    "course": "Go by Example \u4e2d\u6587\u7248"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 18:26:50",
    "user_id": 62497,
    "lab": "HTML5 \u672c\u5730\u88c1\u526a\u56fe\u7247",
    "course": "\u57fa\u4e8e HTML5 \u5b9e\u73b0\u672c\u5730\u56fe\u7247\u88c1\u526a"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 18:30:53",
    "user_id": 196766,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 18:31:45",
    "user_id": 199507,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 18:32:56",
    "user_id": 199517,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 18:33:31",
    "user_id": 197928,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-01 18:34:14",
    "user_id": 191129,
    "lab": "makefile",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 18:34:19",
    "user_id": 85944,
    "lab": "\u503c\uff0c\u53d8\u91cf\uff0c\u5e38\u91cf",
    "course": "Go by Example \u4e2d\u6587\u7248"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 18:35:48",
    "user_id": 199519,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 18:39:09",
    "user_id": 199307,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 18:39:43",
    "user_id": 193213,
    "lab": "\u62bd\u8c61\u5de5\u5382\u6a21\u5f0f",
    "course": "Java\u8fdb\u9636\u4e4b\u8bbe\u8ba1\u6a21\u5f0f"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-01 18:42:26",
    "user_id": 170073,
    "lab": "\u64cd\u4f5c\u7cfb\u7edf\u7684\u5f15\u5bfc",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 18:43:35",
    "user_id": 199307,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 18:45:11",
    "user_id": 24141,
    "lab": "Python\u6df1\u5165\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 18:49:09",
    "user_id": 81189,
    "lab": "\u7ec8\u7aef\u8bbe\u5907\u7684\u63a7\u5236",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 18:50:02",
    "user_id": 199519,
    "lab": "Linux\u57fa\u7840\u77e5\u8bc6\u4e0e\u5e38\u7528\u547d\u4ee4",
    "course": "\u5b9e\u7528Linux Shell\u7f16\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 18:50:52",
    "user_id": 199516,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 18:52:35",
    "user_id": 199307,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-01 18:53:23",
    "user_id": 199519,
    "lab": "Bash\u5185\u7f6e\u547d\u4ee4\u4e0e\u73af\u5883\u7b80\u4ecb",
    "course": "\u5b9e\u7528Linux Shell\u7f16\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 18:53:30",
    "user_id": 80187,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 18:53:45",
    "user_id": 186505,
    "lab": "\u521d\u8bc6HTML",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-01 18:56:54",
    "user_id": 84362,
    "lab": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668",
    "course": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 18:57:52",
    "user_id": 199307,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 18:58:15",
    "user_id": 85944,
    "lab": "\u901a\u9053\uff0c\u901a\u9053\u7f13\u51b2\uff0c\u901a\u9053\u540c\u6b65\uff0c\u901a\u9053\u65b9\u5411\uff0c\u901a\u9053\u9009\u62e9\u5668",
    "course": "Go by Example \u4e2d\u6587\u7248"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 18:58:48",
    "user_id": 192549,
    "lab": "\u57fa\u7840\u6b63\u5219\u8868\u8fbe\u5f0f\u4ecb\u7ecd\u4e0e\u7ec3\u4e60",
    "course": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 19:00:12",
    "user_id": 30185,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 19:02:32",
    "user_id": 50252,
    "lab": "\u521d\u8bc6MySQL",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-01 19:05:08",
    "user_id": 171973,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 19:08:10",
    "user_id": 80187,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0b\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-01 19:09:50",
    "user_id": 171977,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 19:11:21",
    "user_id": 192549,
    "lab": "grep\u547d\u4ee4\u4e0e\u6b63\u5219\u8868\u8fbe\u5f0f",
    "course": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 19:14:26",
    "user_id": 199270,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 19:15:12",
    "user_id": 190750,
    "lab": "\u6587\u4ef6IO\u57fa\u7840",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-01 19:16:37",
    "user_id": 52227,
    "lab": "\u901a\u9053\uff0c\u901a\u9053\u7f13\u51b2\uff0c\u901a\u9053\u540c\u6b65\uff0c\u901a\u9053\u65b9\u5411\uff0c\u901a\u9053\u9009\u62e9\u5668",
    "course": "Go by Example \u4e2d\u6587\u7248"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 19:17:10",
    "user_id": 24141,
    "lab": "Django\uff08\u4e0a\uff09[\u5b9e\u9a8c\u8fc7\u671f\u5df2\u4e0b\u7ebf]",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 19:18:26",
    "user_id": 197961,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 19:20:17",
    "user_id": 199460,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 19:21:05",
    "user_id": 186505,
    "lab": "HTML\u6587\u672c",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 19:21:45",
    "user_id": 97922,
    "lab": "Java \u7c7b\u4e0e\u5bf9\u8c61",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 19:22:18",
    "user_id": 80485,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 19:23:25",
    "user_id": 199307,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 19:23:46",
    "user_id": 139688,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 19:24:06",
    "user_id": 199524,
    "lab": "\u6280\u672f\u6808\u4ecb\u7ecd",
    "course": "\u57fa\u4e8eFlask/RethinkDB\u5b9e\u73b0TODO List"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 19:24:23",
    "user_id": 94862,
    "lab": "DOS\u53caDEBUG\u4ecb\u7ecd",
    "course": "\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u90d1\u6653\u8587\u7f16\u8457\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 19:24:51",
    "user_id": 199144,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0b\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 68,
    "created_at": "2016-05-01 19:25:10",
    "user_id": 126650,
    "lab": "Linux\u5185\u6838\u5b66\u4e60\u603b\u7ed3",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-01 19:26:23",
    "user_id": 170073,
    "lab": "\u64cd\u4f5c\u7cfb\u7edf\u7684\u5f15\u5bfc",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 19:26:33",
    "user_id": 199516,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 19:27:57",
    "user_id": 199524,
    "lab": "\u6b22\u8fce\u6765\u5230 Flask \u7684\u4e16\u754c",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 19:28:48",
    "user_id": 186286,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 19:30:16",
    "user_id": 199307,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 19:32:45",
    "user_id": 189821,
    "lab": "Python\u6df1\u5165\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 19:33:04",
    "user_id": 199526,
    "lab": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668",
    "course": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 19:33:25",
    "user_id": 199460,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e00\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 19:33:47",
    "user_id": 60135,
    "lab": "\u5165\u95e8",
    "course": "Bootstrap3.0\u5165\u95e8\u5b66\u4e60"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 19:33:49",
    "user_id": 198356,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 19:36:45",
    "user_id": 199528,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 19:37:55",
    "user_id": 199529,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 19:38:08",
    "user_id": 144481,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 19:38:19",
    "user_id": 109937,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 19:38:37",
    "user_id": 193213,
    "lab": "\u9002\u914d\u5668\u6a21\u5f0f",
    "course": "Java\u8fdb\u9636\u4e4b\u8bbe\u8ba1\u6a21\u5f0f"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 19:38:57",
    "user_id": 199527,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 19:39:46",
    "user_id": 198933,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 19:40:51",
    "user_id": 197948,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-01 19:43:44",
    "user_id": 84362,
    "lab": "\u5faa\u73af\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-01 19:49:33",
    "user_id": 175176,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 19:51:50",
    "user_id": 69472,
    "lab": "\u64cd\u4f5c\u7cfb\u7edf\u7684\u5f15\u5bfc",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 19:53:49",
    "user_id": 188551,
    "lab": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668",
    "course": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-01 19:54:43",
    "user_id": 198416,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 19:57:56",
    "user_id": 24084,
    "lab": "PHP\u7b80\u4ecb",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 19:58:16",
    "user_id": 199467,
    "lab": "PythonChallenge_1",
    "course": "\u5168\u9762\u89e3\u6790PythonChallenge"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 19:59:05",
    "user_id": 192966,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-01 19:59:19",
    "user_id": 193159,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 19:59:32",
    "user_id": 173414,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0b\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 19:59:36",
    "user_id": 109937,
    "lab": "Java \u8bed\u8a00\u57fa\u7840",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 20:01:37",
    "user_id": 199536,
    "lab": "\u57fa\u4e8eNode.js+Express\u5b9e\u73b0\u7b80\u6613\u535a\u5ba2\u7cfb\u7edf",
    "course": "[\u5df2\u4e0b\u7ebf] \u57fa\u4e8eNode.js+Express\u5b9e\u73b0\u7b80\u6613\u535a\u5ba2\u7cfb\u7edf"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 20:03:57",
    "user_id": 199528,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 20:04:13",
    "user_id": 157232,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 20:04:25",
    "user_id": 52320,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 20:05:27",
    "user_id": 91031,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 20:05:38",
    "user_id": 199524,
    "lab": "Flask \u7684 Web \u8868\u5355",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 20:08:01",
    "user_id": 185574,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 20:09:19",
    "user_id": 192966,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 20:10:47",
    "user_id": 108378,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 20:11:54",
    "user_id": 199527,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 20:11:55",
    "user_id": 173414,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0b\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 57,
    "created_at": "2016-05-01 20:14:08",
    "user_id": 196545,
    "lab": "C \u8bed\u8a00\u6570\u7ec4",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 20:14:42",
    "user_id": 199535,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 20:15:24",
    "user_id": 173414,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0b\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-01 20:15:26",
    "user_id": 159656,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 20:18:07",
    "user_id": 160697,
    "lab": "\u5165\u95e8",
    "course": "Bootstrap3.0\u5165\u95e8\u5b66\u4e60"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-01 20:19:33",
    "user_id": 199071,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-01 20:19:38",
    "user_id": 185574,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-01 20:21:48",
    "user_id": 199538,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 20:23:49",
    "user_id": 193472,
    "lab": "Python \u7834\u89e3\u9a8c\u8bc1\u7801",
    "course": "Python \u7834\u89e3\u9a8c\u8bc1\u7801"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 20:23:49",
    "user_id": 157770,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-01 20:24:22",
    "user_id": 157232,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 20:25:56",
    "user_id": 195921,
    "lab": "Java \u5c01\u88c5",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 90,
    "created_at": "2016-05-01 20:29:06",
    "user_id": 198975,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 20:29:48",
    "user_id": 175176,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 20:29:56",
    "user_id": 192966,
    "lab": "\u94fe\u8def\u5c42\u4ecb\u7ecd",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 20:31:18",
    "user_id": 91031,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 120,
    "created_at": "2016-05-01 20:31:57",
    "user_id": 45301,
    "lab": "LAMP\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "LAMP\u90e8\u7f72\u53ca\u914d\u7f6e"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-01 20:32:12",
    "user_id": 115138,
    "lab": "\u9879\u76ee\u516d\uff1aFlask\u4e2a\u4eba\u535a\u5ba2",
    "course": "Python \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 20:36:09",
    "user_id": 170482,
    "lab": "\u6587\u4ef6\u548c\u6587\u4ef6\u7684\u8f93\u5165\u4e0e\u8f93\u51fa",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 20:36:45",
    "user_id": 198693,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 20:38:42",
    "user_id": 190560,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-01 20:40:10",
    "user_id": 199546,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 20:40:44",
    "user_id": 199544,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 20:42:02",
    "user_id": 199540,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 20:42:14",
    "user_id": 160697,
    "lab": "\u6805\u683c\u7cfb\u7edf\u539f\u7406",
    "course": "Bootstrap3.0\u5165\u95e8\u5b66\u4e60"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 20:43:26",
    "user_id": 127224,
    "lab": "pandas \u56de\u987e",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python \u6570\u636e\u5206\u6790\uff08\u4e00\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 20:43:28",
    "user_id": 199508,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 20:45:36",
    "user_id": 192966,
    "lab": "PythonChallenge_1",
    "course": "\u5168\u9762\u89e3\u6790PythonChallenge"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-01 20:45:47",
    "user_id": 190560,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 20:46:02",
    "user_id": 3384,
    "lab": "\u7528\u6237\u767b\u5f55",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 20:46:32",
    "user_id": 83409,
    "lab": "\u5982\u4f55\u5728\u7ec8\u7aef\u4f7f\u7528\u540e\u53f0\u8fd0\u884c\u6a21\u5f0f\u542f\u52a8\u4e00\u4e2aLinux\u5e94\u7528\u7a0b\u5e8f",
    "course": "CentOS 7\u4f53\u9a8c\u8bfe"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 20:46:56",
    "user_id": 199071,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-01 20:46:57",
    "user_id": 173414,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0b\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 20:47:50",
    "user_id": 198889,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 20:49:31",
    "user_id": 199479,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 20:50:22",
    "user_id": 185574,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 20:50:41",
    "user_id": 199540,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 20:50:45",
    "user_id": 15385,
    "lab": "\u4fe1\u53f7\u91cf\u7684\u5b9e\u73b0\u548c\u5e94\u7528",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-01 20:51:12",
    "user_id": 84362,
    "lab": "\u5faa\u73af\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 20:51:12",
    "user_id": 199527,
    "lab": "PHP\u7b80\u4ecb",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 20:51:13",
    "user_id": 198416,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 20:53:05",
    "user_id": 198693,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 20:55:19",
    "user_id": 154247,
    "lab": "C \u8bed\u8a00\u6570\u7ec4",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 20:56:07",
    "user_id": 56056,
    "lab": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668",
    "course": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-01 20:57:30",
    "user_id": 199334,
    "lab": "Linux\u7cfb\u7edf\u547d\u4ee4",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 20:58:25",
    "user_id": 2898,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-01 20:59:20",
    "user_id": 187121,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 21:01:16",
    "user_id": 199216,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 21:03:03",
    "user_id": 199467,
    "lab": "python\u751f\u6210\u6c49\u5b57\u56fe\u7247\u5b57\u5e93",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011python\u751f\u6210\u6c49\u5b57\u56fe\u7247\u5b57\u5e93"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 21:03:44",
    "user_id": 159656,
    "lab": "\u6982\u8ff0",
    "course": "\u5b9e\u7528Linux Shell\u7f16\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 21:04:03",
    "user_id": 6432,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 21:04:45",
    "user_id": 80029,
    "lab": "\u5feb\u901f\u5b9e\u9a8c\u4e94\u5b50\u68cb",
    "course": "C\u8bed\u8a00\u5feb\u901f\u5b9e\u73b0\u4e94\u5b50\u68cb"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 21:09:41",
    "user_id": 196682,
    "lab": "\u7ebf\u6027\u7ed3\u6784-\u7ebf\u6027\u8868",
    "course": "\u6570\u636e\u7ed3\u6784(\u65b0\u7248)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 21:10:08",
    "user_id": 100009,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 21:11:02",
    "user_id": 191383,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 21:11:36",
    "user_id": 159656,
    "lab": "Linux\u57fa\u7840\u77e5\u8bc6\u4e0e\u5e38\u7528\u547d\u4ee4",
    "course": "\u5b9e\u7528Linux Shell\u7f16\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 21:12:02",
    "user_id": 157232,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 21:12:34",
    "user_id": 199549,
    "lab": "Hello World",
    "course": "Android\u5e94\u7528\u5f00\u53d1\u57fa\u7840"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 21:12:47",
    "user_id": 199540,
    "lab": "Node.js\u8bfe\u7a0b\u4ecb\u7ecd",
    "course": "Node.js \u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 21:13:06",
    "user_id": 198889,
    "lab": "\u7ebf\u6027\u7ed3\u6784-\u6808\u548c\u961f\u5217",
    "course": "\u6570\u636e\u7ed3\u6784(\u65b0\u7248)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 21:14:09",
    "user_id": 199237,
    "lab": "\u57fa\u7840\u8bed\u6cd5",
    "course": "Ruby\u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-01 21:14:54",
    "user_id": 170979,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-01 21:15:55",
    "user_id": 196977,
    "lab": "makefile",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 21:16:22",
    "user_id": 186465,
    "lab": "Java \u8bed\u8a00\u57fa\u7840",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-01 21:16:23",
    "user_id": 199551,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 21:17:41",
    "user_id": 170768,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 21:20:36",
    "user_id": 199216,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 21:22:36",
    "user_id": 198889,
    "lab": "Java\u5b9e\u73b0\u8bb0\u4e8b\u672c",
    "course": "Java\u5b9e\u73b0\u8bb0\u4e8b\u672c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 21:22:46",
    "user_id": 52835,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 21:23:49",
    "user_id": 199549,
    "lab": "Hello World",
    "course": "Android\u5e94\u7528\u5f00\u53d1\u57fa\u7840"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 21:24:01",
    "user_id": 199540,
    "lab": "Node.js\u6a21\u5757",
    "course": "Node.js \u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 21:26:20",
    "user_id": 196786,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 21:26:23",
    "user_id": 199517,
    "lab": "\u9009\u62e9\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 21:27:38",
    "user_id": 199554,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 21:28:31",
    "user_id": 199553,
    "lab": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668",
    "course": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 21:29:08",
    "user_id": 170768,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-01 21:32:32",
    "user_id": 198056,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 21:34:21",
    "user_id": 199554,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 21:36:15",
    "user_id": 170768,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 21:37:02",
    "user_id": 199540,
    "lab": "Node.js Events\u6a21\u5757",
    "course": "Node.js \u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 21:37:23",
    "user_id": 109937,
    "lab": "Java  \u8fd0\u7b97\u7b26",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 21:38:41",
    "user_id": 198889,
    "lab": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668",
    "course": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-01 21:39:02",
    "user_id": 177351,
    "lab": "C \u8bed\u8a00\u6570\u7ec4",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 21:39:53",
    "user_id": 90838,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 69,
    "created_at": "2016-05-01 21:40:30",
    "user_id": 171718,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 21:40:49",
    "user_id": 145739,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 21:41:46",
    "user_id": 98252,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e00\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 21:42:34",
    "user_id": 197889,
    "lab": "Models\u548cAdmin\u4ee5\u53caViews\u548cURL",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 21:42:36",
    "user_id": 74549,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 21:46:05",
    "user_id": 127224,
    "lab": "\u8bfb\u5199\u6587\u672c\u683c\u5f0f\u7684\u6570\u636e",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python \u6570\u636e\u5206\u6790\uff08\u4e00\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 21:46:32",
    "user_id": 199543,
    "lab": "git\u4ecb\u7ecd",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 63,
    "created_at": "2016-05-01 21:47:13",
    "user_id": 196545,
    "lab": "\u6a21\u5757\u5316\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 21:48:17",
    "user_id": 199334,
    "lab": "Linux\u7cfb\u7edf\u547d\u4ee4",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 21:49:03",
    "user_id": 90838,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 21:50:13",
    "user_id": 199543,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 21:50:19",
    "user_id": 199454,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 21:51:02",
    "user_id": 107263,
    "lab": "\u57fa\u672c\u6982\u5ff5",
    "course": "\u6570\u636e\u7ed3\u6784(\u65b0\u7248)"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 21:51:23",
    "user_id": 52611,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 21:53:14",
    "user_id": 23135,
    "lab": "LNMP\u7cfb\u7edf\u5b89\u88c5",
    "course": "Linux Web\u8fd0\u7ef4\uff08Nginx\uff09\u5b9e\u6218 "
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 21:53:18",
    "user_id": 147831,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e00\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 21:53:35",
    "user_id": 199479,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 21:53:58",
    "user_id": 199538,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 21:55:41",
    "user_id": 186465,
    "lab": "Java  \u8fd0\u7b97\u7b26",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 21:55:43",
    "user_id": 90838,
    "lab": "\u5f00\u53d1\u73af\u5883\u548c\u5256\u6790\u7b2c\u4e00\u4e2a C \u8bed\u8a00",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 21:55:47",
    "user_id": 167421,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-01 21:56:12",
    "user_id": 170768,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 21:56:42",
    "user_id": 196472,
    "lab": "HTML\u8d85\u6587\u672c\uff08\u4e00\uff09",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 21:58:10",
    "user_id": 197423,
    "lab": "\u4e2d\u7ea7\u6280\u80fd\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 21:59:15",
    "user_id": 118813,
    "lab": "\u57fa\u4e8escrapy\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u57fa\u4e8escrapy\u722c\u866b\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6(python)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 22:01:46",
    "user_id": 186502,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 22:02:40",
    "user_id": 52611,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 22:02:54",
    "user_id": 120304,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 22:02:59",
    "user_id": 161159,
    "lab": "\u4e2d\u7ea7\u6280\u80fd\uff08\u4e0b\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-01 22:03:16",
    "user_id": 32046,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 22:03:22",
    "user_id": 127224,
    "lab": "\u4f7f\u7528\u6570\u636e\u5e93",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python \u6570\u636e\u5206\u6790\uff08\u4e00\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 22:03:34",
    "user_id": 84362,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 22:03:53",
    "user_id": 199517,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 22:04:18",
    "user_id": 197889,
    "lab": "Template\u548c\u52a8\u6001URL",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 22:04:23",
    "user_id": 167421,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 22:04:50",
    "user_id": 164830,
    "lab": "git\u4ecb\u7ecd",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 22:05:34",
    "user_id": 199117,
    "lab": "\u7cfb\u7edf\u8c03\u7528",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 22:05:43",
    "user_id": 199559,
    "lab": "\u8f6c\u76d8\u62bd\u5956",
    "course": "PHP\u5b9e\u73b0\u8f6c\u76d8\u62bd\u5956"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 22:05:52",
    "user_id": 199561,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 22:07:11",
    "user_id": 198693,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 22:08:05",
    "user_id": 145739,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u7684\u7ea6\u675f",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 22:08:05",
    "user_id": 52835,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-01 22:09:29",
    "user_id": 167421,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 22:11:59",
    "user_id": 199071,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 22:14:04",
    "user_id": 147831,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u8fd0\u7b97\u7b26\u548c\u6570\u636e\u8f6c\u6362",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 22:14:17",
    "user_id": 199565,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-01 22:14:23",
    "user_id": 197889,
    "lab": "Template\u548c\u52a8\u6001URL",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 22:15:25",
    "user_id": 169399,
    "lab": "LAMP\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "LAMP\u90e8\u7f72\u53ca\u914d\u7f6e"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 22:17:16",
    "user_id": 164830,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 22:20:44",
    "user_id": 56056,
    "lab": "\u8bfe\u7a0b\u8bf4\u660e\u4e0e\u5b66\u4e60\u65b9\u6cd5\uff08HowTo\uff09",
    "course": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 22:20:46",
    "user_id": 76108,
    "lab": "Hadoop\u4ecb\u7ecd\u53ca1.X\u4f2a\u5206\u5e03\u5f0f\u5b89\u88c5",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 22:21:08",
    "user_id": 199334,
    "lab": "Linux\u7cfb\u7edf\u547d\u4ee4",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 22:21:44",
    "user_id": 107263,
    "lab": "Laravel\u5b9e\u73b0\u7528\u6237\u6ce8\u518c\u767b\u5f55",
    "course": "Laravel\u5b9e\u73b0\u7528\u6237\u6ce8\u518c\u767b\u5f55"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 22:24:08",
    "user_id": 56056,
    "lab": "\u6570\u636e\u7ed3\u6784-\u5b57\u7b26\u4e32\uff08String\uff09",
    "course": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 22:24:31",
    "user_id": 199568,
    "lab": "\u8ba4\u8bc6wxpython",
    "course": "\u7528Python\u505a2048\u6e38\u620f"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-01 22:24:32",
    "user_id": 199071,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 22:26:39",
    "user_id": 199454,
    "lab": "Python\u6df1\u5165\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 22:26:40",
    "user_id": 23135,
    "lab": "Linux\u7cfb\u7edf\u76d1\u63a7\u5de5\u5177\u2014\u2014Nagios",
    "course": "Linux\u7cfb\u7edf\u76d1\u63a7\u5b9e\u6218"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 22:27:20",
    "user_id": 118813,
    "lab": "\u6570\u636e\u5e93\u548c\u96c6\u5408\u57fa\u672c\u64cd\u4f5c",
    "course": "MongoDB \u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 22:28:44",
    "user_id": 147831,
    "lab": "\u9009\u62e9\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 22:29:00",
    "user_id": 199080,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 22:29:23",
    "user_id": 199555,
    "lab": "\u6a21\u5757\u5316\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 22:29:42",
    "user_id": 189131,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 22:31:17",
    "user_id": 103891,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 22:31:24",
    "user_id": 127382,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 22:32:10",
    "user_id": 199570,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 78,
    "created_at": "2016-05-01 22:35:50",
    "user_id": 167421,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 22:37:26",
    "user_id": 199087,
    "lab": "\u591a\u8bf4,markdown\u548c\u4ee3\u7801\u9ad8\u4eae",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-01 22:40:17",
    "user_id": 199572,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 22:40:49",
    "user_id": 119886,
    "lab": "\u5355\u4f8b\u6a21\u5f0f",
    "course": "Java\u8fdb\u9636\u4e4b\u8bbe\u8ba1\u6a21\u5f0f"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 22:41:59",
    "user_id": 175078,
    "lab": "Android UI\u7f16\u7a0b",
    "course": "Android\u5e94\u7528\u5f00\u53d1\u57fa\u7840"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 22:42:13",
    "user_id": 145739,
    "lab": "\u57fa\u7840\u7bc7 - SELECT \u8bed\u53e5\u8be6\u89e3",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 22:44:18",
    "user_id": 138418,
    "lab": "Java  \u8fd0\u7b97\u7b26",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-01 22:44:47",
    "user_id": 170980,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 22:45:39",
    "user_id": 198635,
    "lab": "LNMP\u7cfb\u7edf\u5b89\u88c5",
    "course": "Linux Web\u8fd0\u7ef4\uff08Nginx\uff09\u5b9e\u6218 "
  },
  {
    "minutes": 66,
    "created_at": "2016-05-01 22:48:56",
    "user_id": 187235,
    "lab": "\u6761\u4ef6\u5224\u65ad",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-01 22:53:13",
    "user_id": 198991,
    "lab": "SQL\u8bed\u53e5\u8bed\u6cd5",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 22:55:07",
    "user_id": 198635,
    "lab": "Nginx\u6a21\u5757\u5f00\u53d1\u5b9e\u9a8c",
    "course": "Linux Web\u8fd0\u7ef4\uff08Nginx\uff09\u5b9e\u6218 "
  },
  {
    "minutes": 21,
    "created_at": "2016-05-01 22:57:24",
    "user_id": 138418,
    "lab": "Java \u63a7\u5236\u8bed\u53e5",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 23:00:38",
    "user_id": 3384,
    "lab": "\u7528\u6237\u767b\u5f55",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 23:06:50",
    "user_id": 94765,
    "lab": "k-\u8fd1\u90bb\u7b97\u6cd5\u6539\u8fdb\u7ea6\u4f1a\u7f51\u7ad9\u914d\u5bf9\u6548\u679c",
    "course": "\u6df1\u5165\u5b66\u4e60\u300a\u673a\u5668\u5b66\u4e60\u5b9e\u6218\u300b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 23:06:50",
    "user_id": 199546,
    "lab": "Rails \u4ecb\u7ecd\u4e0e\u73af\u5883\u914d\u7f6e",
    "course": "Rails\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 23:07:37",
    "user_id": 199080,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 23:10:52",
    "user_id": 139642,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 105,
    "created_at": "2016-05-01 23:13:00",
    "user_id": 45301,
    "lab": "Apache \u914d\u7f6e",
    "course": "LAMP\u90e8\u7f72\u53ca\u914d\u7f6e"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-01 23:13:15",
    "user_id": 22092,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 23:13:37",
    "user_id": 199570,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-01 23:14:41",
    "user_id": 199569,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 23:16:07",
    "user_id": 194560,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 23:16:53",
    "user_id": 94864,
    "lab": "\u591a\u8bf4,markdown\u548c\u4ee3\u7801\u9ad8\u4eae",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 23:18:45",
    "user_id": 197015,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 23:20:47",
    "user_id": 172334,
    "lab": "\u8bfe\u7a0b\u57fa\u7840\u5305\uff08\u4e0a\uff09\uff0d\u5355\u9009\u7c7b\u578b\u8868\u5355\u81ea\u52a8\u63d0\u4ea4",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python\u81ea\u52a8\u586b\u95ee\u5377\u661f"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 23:21:52",
    "user_id": 198635,
    "lab": "linux\u7cfb\u7edf\u76d1\u63a7\u5e38\u7528\u547d\u4ee4\uff08\u4e00\uff09",
    "course": "Linux\u7cfb\u7edf\u76d1\u63a7\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 23:22:07",
    "user_id": 138418,
    "lab": "Java \u6570\u7ec4",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 23:23:23",
    "user_id": 94864,
    "lab": "\u641c\u7d22\u548cReadmore\u4e0eRSS\u548c\u5206\u9875",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 23:24:49",
    "user_id": 199080,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 23:24:59",
    "user_id": 196984,
    "lab": "PythonChallenge_2",
    "course": "\u6bcf\u5929\u4e00\u4e2aPythonChallenge\u300a\u4efb\u52a1\u4e8c\u300b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 23:25:04",
    "user_id": 199576,
    "lab": "java.lang \u5305",
    "course": "JDK \u6838\u5fc3 API"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-01 23:26:32",
    "user_id": 196875,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 23:29:49",
    "user_id": 199579,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 23:30:43",
    "user_id": 199570,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-01 23:32:17",
    "user_id": 199580,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 23:34:27",
    "user_id": 22092,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 23:36:55",
    "user_id": 167550,
    "lab": "ThinkPHP\u5b89\u88c5\u4e0e\u914d\u7f6e",
    "course": "ThinkPHP\u6846\u67b6\u5b9e\u8df5"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 23:37:13",
    "user_id": 197015,
    "lab": "\u5f00\u53d1\u73af\u5883\u548c\u5256\u6790\u7b2c\u4e00\u4e2a C \u8bed\u8a00",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 23:38:02",
    "user_id": 193159,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-01 23:38:34",
    "user_id": 198991,
    "lab": "MySQL\u89e6\u53d1\u5668",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 23:47:34",
    "user_id": 184294,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 23:48:36",
    "user_id": 25133,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 23:48:58",
    "user_id": 199253,
    "lab": "\u9ad8\u7ea7\u67e5\u8be2\u4e0e\u7d22\u5f15",
    "course": "MongoDB \u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-01 23:50:24",
    "user_id": 196875,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-01 23:54:47",
    "user_id": 193161,
    "lab": "",
    "course": ""
  },
  {
    "minutes": 3,
    "created_at": "2016-05-01 23:55:54",
    "user_id": 182621,
    "lab": "\u7b2c1\u5468\uff1aC++\u57fa\u7840\u5165\u95e8\uff08\u7b2c1\u7ae0\u81f3\u7b2c3\u7ae0\uff09",
    "course": "\u6df1\u5165\u5b66\u4e60 \u300aC++ Primer \u7b2c\u4e94\u7248\u300b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-01 23:56:34",
    "user_id": 184294,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 00:04:15",
    "user_id": 199454,
    "lab": "\u5f00\u53d1\u73af\u5883\u4ee5\u53ca\u9879\u76ee\u4e0eApp",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 00:04:28",
    "user_id": 170440,
    "lab": "\u6570\u636e\u7ed3\u6784-\u5b57\u7b26\u4e32\uff08String\uff09",
    "course": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 00:05:02",
    "user_id": 199253,
    "lab": "\u8bfe\u7a0b\u8bf4\u660e\u4e0e\u5b66\u4e60\u65b9\u6cd5",
    "course": "Go by Example \u4e2d\u6587\u7248"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 00:05:38",
    "user_id": 149790,
    "lab": "\u7f51\u9875\u7248\u522b\u8e29\u767d\u5757",
    "course": "\u7f51\u9875\u7248\u522b\u8e29\u767d\u5757\u6e38\u620f"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 00:07:03",
    "user_id": 197654,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 00:07:58",
    "user_id": 74477,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 00:09:12",
    "user_id": 170440,
    "lab": "\u8bfe\u7a0b\u8bf4\u660e\u4e0e\u5b66\u4e60\u65b9\u6cd5\uff08HowTo\uff09",
    "course": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 00:13:47",
    "user_id": 199569,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 00:17:15",
    "user_id": 199590,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-02 00:17:22",
    "user_id": 74797,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 00:17:46",
    "user_id": 186528,
    "lab": "\u5f00\u53d1\u73af\u5883\u4ee5\u53ca\u9879\u76ee\u4e0eApp",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 00:23:08",
    "user_id": 134191,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 00:27:42",
    "user_id": 194989,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 00:30:16",
    "user_id": 199580,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 00:37:28",
    "user_id": 196984,
    "lab": "PythonChallenge_2",
    "course": "\u6bcf\u5929\u4e00\u4e2aPythonChallenge\u300a\u4efb\u52a1\u4e8c\u300b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 01:04:06",
    "user_id": 128580,
    "lab": "\u591a\u8fdb\u7a0b\uff08\u4e00\uff09",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 01:11:22",
    "user_id": 170979,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 01:19:25",
    "user_id": 199087,
    "lab": "Template\u548c\u52a8\u6001URL",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 01:19:40",
    "user_id": 119886,
    "lab": "\u8ba4\u8bc6J2SE",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 01:46:48",
    "user_id": 94859,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 01:53:41",
    "user_id": 147110,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 01:55:52",
    "user_id": 199599,
    "lab": "PHP\u7559\u8a00\u672c",
    "course": "PHP \u5b9e\u73b0\u7559\u8a00\u672c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 02:32:23",
    "user_id": 199599,
    "lab": "\u521d\u8bc6MySQL",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 02:34:30",
    "user_id": 147110,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 02:39:34",
    "user_id": 199599,
    "lab": "MySQL\u57fa\u672c\u64cd\u4f5c",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 03:43:44",
    "user_id": 199472,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 03:54:30",
    "user_id": 199603,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 04:04:26",
    "user_id": 91048,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 04:13:27",
    "user_id": 7471,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 129,
    "created_at": "2016-05-02 05:52:08",
    "user_id": 45301,
    "lab": "Apache \u914d\u7f6e",
    "course": "LAMP\u90e8\u7f72\u53ca\u914d\u7f6e"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 06:07:07",
    "user_id": 197775,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 06:16:36",
    "user_id": 197775,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 06:26:56",
    "user_id": 197775,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 06:51:40",
    "user_id": 3384,
    "lab": "\u7528\u6237\u767b\u5f55",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 06:59:50",
    "user_id": 199607,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-02 07:04:20",
    "user_id": 198933,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 60,
    "created_at": "2016-05-02 07:16:48",
    "user_id": 3384,
    "lab": "\u7528\u6237\u9996\u9875\u548c\u53d1\u5e03\u535a\u5ba2",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 07:41:54",
    "user_id": 199610,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 07:47:59",
    "user_id": 198933,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-02 07:48:25",
    "user_id": 195098,
    "lab": "\u7528\u65f6\u95f4\u5e8f\u5217\u9884\u6d4b\u80a1\u7968\u6536\u76ca",
    "course": "[\u5df2\u4e0b\u7ebf] R\u8bed\u8a00\u80a1\u7968\u6570\u636e\u5206\u6790"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 07:53:03",
    "user_id": 74493,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 08:26:33",
    "user_id": 94862,
    "lab": "DOS\u53caDEBUG\u4ecb\u7ecd",
    "course": "\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u90d1\u6653\u8587\u7f16\u8457\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 08:28:50",
    "user_id": 199614,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 08:29:37",
    "user_id": 92940,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-02 08:30:26",
    "user_id": 198079,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 08:31:18",
    "user_id": 173414,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 08:35:37",
    "user_id": 60135,
    "lab": "\u5165\u95e8",
    "course": "Bootstrap3.0\u5165\u95e8\u5b66\u4e60"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 08:42:59",
    "user_id": 199615,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 08:44:30",
    "user_id": 25255,
    "lab": "linux\u7cfb\u7edf\u76d1\u63a7\u5e38\u7528\u547d\u4ee4\uff08\u4e00\uff09",
    "course": "Linux\u7cfb\u7edf\u76d1\u63a7\u5b9e\u6218"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 08:45:15",
    "user_id": 60135,
    "lab": "\u6805\u683c\u7cfb\u7edf\u539f\u7406",
    "course": "Bootstrap3.0\u5165\u95e8\u5b66\u4e60"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 08:50:22",
    "user_id": 92940,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u7684\u7ea6\u675f",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 08:51:02",
    "user_id": 174908,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 08:51:39",
    "user_id": 194989,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 08:52:50",
    "user_id": 165475,
    "lab": "Python\u6df1\u5165\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 08:57:08",
    "user_id": 36065,
    "lab": "\u901a\u8fc7\u53cd\u6c47\u7f16\u4e00\u4e2a\u7b80\u5355\u7684C\u7a0b\u5e8f\uff0c\u5206\u6790\u6c47\u7f16\u4ee3\u7801\u7406\u89e3\u8ba1\u7b97\u673a\u662f\u5982\u4f55\u5de5\u4f5c\u7684",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 09:01:01",
    "user_id": 199617,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 09:01:25",
    "user_id": 199618,
    "lab": "\u57fa\u4e8escrapy\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u57fa\u4e8escrapy\u722c\u866b\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6(python)"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 09:02:46",
    "user_id": 174908,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 09:03:39",
    "user_id": 36065,
    "lab": "\u5b8c\u6210\u4e00\u4e2a\u7b80\u5355\u7684\u65f6\u95f4\u7247\u8f6e\u8f6c\u591a\u9053\u7a0b\u5e8f\u5185\u6838\u4ee3\u7801",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 09:04:58",
    "user_id": 25255,
    "lab": " Linux \u76d1\u63a7\u7684 Python \u811a\u672c",
    "course": "Linux\u7cfb\u7edf\u76d1\u63a7\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 09:05:38",
    "user_id": 199617,
    "lab": "\u5f00\u53d1\u73af\u5883\u548c\u5256\u6790\u7b2c\u4e00\u4e2a C \u8bed\u8a00",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 09:07:51",
    "user_id": 199156,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-02 09:12:29",
    "user_id": 171853,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 09:13:13",
    "user_id": 199618,
    "lab": "\u57fa\u4e8escrapy\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u57fa\u4e8escrapy\u722c\u866b\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6(python)"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 09:16:59",
    "user_id": 165475,
    "lab": "Python\u8865\u5145",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 09:17:08",
    "user_id": 199619,
    "lab": "\u521d\u8bc6HTML",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 5,
    "created_at": "2016-05-02 09:18:21",
    "user_id": 199617,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 09:22:36",
    "user_id": 199618,
    "lab": "Django\u5165\u95e8",
    "course": "[\u5df2\u4e0b\u7ebf] Python Django Web\u6846\u67b6"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 09:22:47",
    "user_id": 198889,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 78,
    "created_at": "2016-05-02 09:27:48",
    "user_id": 195632,
    "lab": "\u6307\u9488\uff08\u4e00\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 09:31:09",
    "user_id": 199610,
    "lab": "python\u751f\u6210\u6c49\u5b57\u56fe\u7247\u5b57\u5e93",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011python\u751f\u6210\u6c49\u5b57\u56fe\u7247\u5b57\u5e93"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 09:32:59",
    "user_id": 176435,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 09:36:28",
    "user_id": 94862,
    "lab": "\u6307\u4ee4\u7cfb\u7edf\u4e0e\u5bfb\u5740\u65b9\u5f0f",
    "course": "\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u90d1\u6653\u8587\u7f16\u8457\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 09:37:42",
    "user_id": 198465,
    "lab": "\u7b80\u5355\u7684\u8bcd\u6cd5\u5206\u6790\u5668\uff08c++\u8bed\u8a00\uff09",
    "course": "\u7b80\u5355\u8bcd\u6cd5\u5206\u6790\u5668\uff08C++\u8bed\u8a00\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 09:40:33",
    "user_id": 199618,
    "lab": "PythonChallenge_1",
    "course": "\u5168\u9762\u89e3\u6790PythonChallenge"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 09:41:15",
    "user_id": 172294,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 09:41:24",
    "user_id": 197961,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 09:42:06",
    "user_id": 187263,
    "lab": "PHP\u7559\u8a00\u672c",
    "course": "PHP \u5b9e\u73b0\u7559\u8a00\u672c"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 09:44:09",
    "user_id": 165475,
    "lab": "Python\u6807\u51c6\u5e93\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 09:45:44",
    "user_id": 176435,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 09:46:09",
    "user_id": 188551,
    "lab": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668",
    "course": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 09:50:37",
    "user_id": 172294,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 09:50:53",
    "user_id": 198915,
    "lab": "Java  \u8fd0\u7b97\u7b26",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 09:51:21",
    "user_id": 81509,
    "lab": "\u53d8\u91cf\u548c\u53c2\u6570",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 09:52:49",
    "user_id": 187235,
    "lab": "\u6761\u4ef6\u5224\u65ad",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 60,
    "created_at": "2016-05-02 09:53:02",
    "user_id": 198079,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-02 09:53:26",
    "user_id": 144990,
    "lab": "C\u8bed\u8a00\u7248flappy_bird",
    "course": "C\u8bed\u8a00\u7248flappy_bird"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 09:53:38",
    "user_id": 84265,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-02 09:54:35",
    "user_id": 198915,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 09:54:57",
    "user_id": 74797,
    "lab": "lab0\uff1aCoding!",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u5b9e\u9a8c\uff0d\u57fa\u4e8euCore OS"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 09:55:00",
    "user_id": 199623,
    "lab": "\u57fa\u4e8escrapy\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u57fa\u4e8escrapy\u722c\u866b\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6(python)"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 09:59:04",
    "user_id": 191598,
    "lab": "makefile",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-02 10:00:31",
    "user_id": 198056,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 10:00:45",
    "user_id": 196984,
    "lab": "PythonChallenge_2",
    "course": "\u6bcf\u5929\u4e00\u4e2aPythonChallenge\u300a\u4efb\u52a1\u4e8c\u300b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 10:02:45",
    "user_id": 190889,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-02 10:03:41",
    "user_id": 171853,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 10:04:20",
    "user_id": 172294,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u7684\u7ea6\u675f",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 10:05:40",
    "user_id": 199487,
    "lab": "\u5bc6\u94a5\u52a0\u89e3\u5bc6\u5b9e\u9a8c\uff08\u4e0a\uff09",
    "course": "\u5bc6\u94a5\u52a0\u89e3\u5bc6\u5b9e\u9a8c"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 10:07:14",
    "user_id": 158424,
    "lab": "\u56de\u5f52",
    "course": "[\u5df2\u4e0b\u7ebf] \u4f7f\u7528R\u8bed\u8a00\u8fdb\u884c\u6570\u636e\u6316\u6398"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 10:08:21",
    "user_id": 176347,
    "lab": "\u6b22\u8fce\u6765\u5230 Flask \u7684\u4e16\u754c",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-02 10:08:35",
    "user_id": 174908,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 10:10:05",
    "user_id": 94862,
    "lab": "\u6c47\u7f16\u8bed\u8a00\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u90d1\u6653\u8587\u7f16\u8457\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 10:10:27",
    "user_id": 199624,
    "lab": "Welcome to Django!",
    "course": "[\u5df2\u4e0b\u7ebf] Python Django Web\u6846\u67b6"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 10:11:50",
    "user_id": 199487,
    "lab": "Linux\u7cfb\u7edf\u76d1\u63a7\u5de5\u5177\u2014\u2014Nagios",
    "course": "Linux\u7cfb\u7edf\u76d1\u63a7\u5b9e\u6218"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 10:13:06",
    "user_id": 194659,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 10:14:19",
    "user_id": 165475,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 10:16:57",
    "user_id": 16710,
    "lab": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c",
    "course": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 10:18:01",
    "user_id": 165499,
    "lab": "Yii 2\u7684\u5b89\u88c5",
    "course": "Yii 2\u7cfb\u5217\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 10:18:15",
    "user_id": 165475,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 10:19:46",
    "user_id": 180696,
    "lab": "\u8d70\u5411\u5206\u652f",
    "course": "[\u79c1\u6709]\u8fbd\u5b81\u5e08\u8303\u5927\u5b66\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u5b9e\u9a8c\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 10:21:00",
    "user_id": 20049,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 10:21:44",
    "user_id": 172294,
    "lab": "\u57fa\u7840\u7bc7 - SELECT \u8bed\u53e5\u8be6\u89e3",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 10:22:17",
    "user_id": 165475,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 10:22:59",
    "user_id": 146207,
    "lab": "Python \u6d41\u7a0b\u63a7\u5236",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 10:23:57",
    "user_id": 147110,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 10:24:42",
    "user_id": 199628,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 10:26:40",
    "user_id": 198889,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-02 10:26:42",
    "user_id": 128327,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 10:28:22",
    "user_id": 6432,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 10:28:43",
    "user_id": 170760,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 10:29:06",
    "user_id": 186502,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 10:30:16",
    "user_id": 165499,
    "lab": "Yii 2\u7684\u5b89\u88c5",
    "course": "Yii 2\u7cfb\u5217\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 10:30:19",
    "user_id": 32649,
    "lab": "\u9759\u6001\u6587\u4ef6\u53ca\u6e32\u67d3\u6a21\u7248",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-02 10:31:07",
    "user_id": 171718,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 10:31:16",
    "user_id": 165475,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u7684\u7ea6\u675f",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 10:32:42",
    "user_id": 199624,
    "lab": "\u89c6\u56fe\u548cURL\u914d\u7f6e",
    "course": "[\u5df2\u4e0b\u7ebf] Python Django Web\u6846\u67b6"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 10:32:47",
    "user_id": 199488,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 10:35:20",
    "user_id": 199517,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-02 10:37:04",
    "user_id": 170765,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 10:37:10",
    "user_id": 50698,
    "lab": "JavaScript \u5b9e\u73b0\u60c5\u4eba\u8282\u73ab\u7470",
    "course": "\u57fa\u4e8e JavaScript \u5b9e\u73b0\u73ab\u7470\u82b1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 10:37:39",
    "user_id": 16710,
    "lab": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c",
    "course": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 10:38:21",
    "user_id": 187235,
    "lab": "\u6761\u4ef6\u5224\u65ad",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-02 10:38:23",
    "user_id": 171841,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 10:38:52",
    "user_id": 198889,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-02 10:40:21",
    "user_id": 175180,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 10:40:28",
    "user_id": 199014,
    "lab": "\u4f7f\u7528 eventproxy \u63a7\u5236\u5e76\u53d1",
    "course": "Node.js\u5305\u6559\u4e0d\u5305\u4f1a"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 10:41:19",
    "user_id": 199454,
    "lab": "Models\u548cAdmin\u4ee5\u53caViews\u548cURL",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 10:42:19",
    "user_id": 147831,
    "lab": "\u9009\u62e9\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 10:43:59",
    "user_id": 172294,
    "lab": "\u57fa\u7840\u7bc7 - \u6570\u636e\u5e93\u53ca\u8868\u7684\u4fee\u6539\u548c\u5220\u9664",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 10:44:06",
    "user_id": 131184,
    "lab": "\u4f20\u8f93\u5c42\uff1aUDP\u534f\u8bae",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 10:44:09",
    "user_id": 165475,
    "lab": "\u57fa\u7840\u7bc7 - SELECT \u8bed\u53e5\u8be6\u89e3",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 10:45:31",
    "user_id": 29988,
    "lab": "Java \u96c6\u5408\u6846\u67b6",
    "course": "JDK \u6838\u5fc3 API"
  },
  {
    "minutes": 105,
    "created_at": "2016-05-02 10:48:13",
    "user_id": 196545,
    "lab": "\u6a21\u5757\u5316\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 10:49:05",
    "user_id": 196984,
    "lab": "PythonChallenge_3",
    "course": "\u6bcf\u5929\u4e00\u4e2aPythonChallenge\u300a\u4efb\u52a1\u4e09\u300b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 10:49:51",
    "user_id": 144538,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 10:52:19",
    "user_id": 171001,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 10:53:45",
    "user_id": 170760,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 10:54:37",
    "user_id": 186502,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 10:58:03",
    "user_id": 131184,
    "lab": "\u4f20\u8f93\u5c42\uff1aTCP\u534f\u8bae",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 11:00:42",
    "user_id": 193159,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 11:00:48",
    "user_id": 199546,
    "lab": "Rails \u63a7\u5236\u5668\u4e0e\u8def\u7531",
    "course": "Rails\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 11:01:24",
    "user_id": 194989,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 11:02:27",
    "user_id": 135161,
    "lab": "LAMP\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "LAMP\u90e8\u7f72\u53ca\u914d\u7f6e"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 11:04:21",
    "user_id": 199572,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 11:05:02",
    "user_id": 196962,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 11:07:50",
    "user_id": 133757,
    "lab": "lab0\uff1aCoding!",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u5b9e\u9a8c\uff0d\u57fa\u4e8euCore OS"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 11:08:23",
    "user_id": 198889,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-02 11:08:36",
    "user_id": 199546,
    "lab": "Rails \u63a7\u5236\u5668\u4e0e\u8def\u7531",
    "course": "Rails\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 11:08:56",
    "user_id": 141792,
    "lab": "Django\u5165\u95e8",
    "course": "[\u5df2\u4e0b\u7ebf] Python Django Web\u6846\u67b6"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 11:09:37",
    "user_id": 174908,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 11:11:15",
    "user_id": 172294,
    "lab": "\u57fa\u7840\u7bc7 - \u5176\u4ed6\u57fa\u672c\u64cd\u4f5c",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 11:12:16",
    "user_id": 194989,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 60,
    "created_at": "2016-05-02 11:12:17",
    "user_id": 170760,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 11:12:44",
    "user_id": 170183,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 11:15:04",
    "user_id": 84265,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 11:15:44",
    "user_id": 170841,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 11:15:48",
    "user_id": 146207,
    "lab": "Python \u6d41\u7a0b\u63a7\u5236",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 11:17:39",
    "user_id": 178167,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-02 11:19:09",
    "user_id": 107571,
    "lab": "\u8ba4\u8bc6J2SE",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 11:19:10",
    "user_id": 170730,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 11:19:57",
    "user_id": 47713,
    "lab": "HTML5 \u672c\u5730\u88c1\u526a\u56fe\u7247",
    "course": "\u57fa\u4e8e HTML5 \u5b9e\u73b0\u672c\u5730\u56fe\u7247\u88c1\u526a"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 11:22:30",
    "user_id": 75030,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 11:23:24",
    "user_id": 196962,
    "lab": "Python \u7834\u89e3\u9a8c\u8bc1\u7801",
    "course": "Python \u7834\u89e3\u9a8c\u8bc1\u7801"
  },
  {
    "minutes": 72,
    "created_at": "2016-05-02 11:24:14",
    "user_id": 179636,
    "lab": "\u8d70\u5411\u5206\u652f",
    "course": "[\u79c1\u6709]\u8fbd\u5b81\u5e08\u8303\u5927\u5b66\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u5b9e\u9a8c\u8bfe\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 11:24:16",
    "user_id": 170730,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 11:24:19",
    "user_id": 165475,
    "lab": "\u57fa\u7840\u7bc7 - \u6570\u636e\u5e93\u53ca\u8868\u7684\u4fee\u6539\u548c\u5220\u9664",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 11:25:06",
    "user_id": 198889,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-02 11:25:12",
    "user_id": 94862,
    "lab": "\u6c47\u7f16\u8bed\u8a00\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u90d1\u6653\u8587\u7f16\u8457\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 11:25:36",
    "user_id": 157089,
    "lab": "grep\u547d\u4ee4\u4e0e\u6b63\u5219\u8868\u8fbe\u5f0f",
    "course": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 11:27:13",
    "user_id": 199454,
    "lab": "\u5f00\u53d1\u73af\u5883\u4ee5\u53ca\u9879\u76ee\u4e0eApp",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 11:27:18",
    "user_id": 198036,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 11:29:50",
    "user_id": 50348,
    "lab": "Python\u5e76\u884c\u8ba1\u7b97",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 11:31:10",
    "user_id": 198933,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 11:31:27",
    "user_id": 66074,
    "lab": "SET-UID\u7a0b\u5e8f\u6f0f\u6d1e\u5b9e\u9a8c",
    "course": "SET-UID\u7a0b\u5e8f\u6f0f\u6d1e\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 11:32:03",
    "user_id": 165475,
    "lab": "\u57fa\u7840\u7bc7 - \u5176\u4ed6\u57fa\u672c\u64cd\u4f5c",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 11:32:48",
    "user_id": 52227,
    "lab": "\u8d85\u65f6\u5904\u7406\uff0c\u975e\u963b\u585e\u901a\u9053\u64cd\u4f5c\uff0c\u901a\u9053\u7684\u5173\u95ed\uff0c\u901a\u9053\u904d\u5386",
    "course": "Go by Example \u4e2d\u6587\u7248"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 11:33:30",
    "user_id": 190530,
    "lab": "vi\u7f16\u8bd1\u5668\u7684\u4f7f\u7528",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 11:35:11",
    "user_id": 175610,
    "lab": "\u7b2c10-11\u5468\u8bfe\u5802\u5b9e\u9a8c-\u5b9e\u9a8c\u4e8c \u7ee7\u627f\u6027\u7684\u5b9e\u73b0\uff081-2\uff09",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 11:36:32",
    "user_id": 199640,
    "lab": "lab0\uff1aCoding!",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u5b9e\u9a8c\uff0d\u57fa\u4e8euCore OS"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 11:38:10",
    "user_id": 199454,
    "lab": "Models\u548cAdmin\u4ee5\u53caViews\u548cURL",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 11:39:07",
    "user_id": 176880,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-02 11:39:17",
    "user_id": 171968,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 11:40:13",
    "user_id": 142568,
    "lab": "PHP\u7559\u8a00\u672c",
    "course": "PHP \u5b9e\u73b0\u7559\u8a00\u672c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 11:40:52",
    "user_id": 198889,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 11:42:13",
    "user_id": 197889,
    "lab": "Template\u548c\u52a8\u6001URL",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 11:42:22",
    "user_id": 199572,
    "lab": "PythonChallenge_1",
    "course": "\u5168\u9762\u89e3\u6790PythonChallenge"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 11:45:33",
    "user_id": 199543,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 11:47:33",
    "user_id": 84265,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 11:50:09",
    "user_id": 131184,
    "lab": "\u5e94\u7528\u5c42\u534f\u8bae\u4e00",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 120,
    "created_at": "2016-05-02 11:50:48",
    "user_id": 195792,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 11:53:01",
    "user_id": 7758,
    "lab": "\u6570\u636e\u7ed3\u6784-\u4e8c\u53c9\u6811\uff08Binary Tree\uff09",
    "course": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 11:53:31",
    "user_id": 199117,
    "lab": "\u7cfb\u7edf\u8c03\u7528",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 11:56:31",
    "user_id": 199102,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 11:57:04",
    "user_id": 190530,
    "lab": "gcc\u7f16\u8bd1\u5668\u7684\u4f7f\u7528",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 11:57:39",
    "user_id": 150618,
    "lab": "",
    "course": ""
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 11:57:40",
    "user_id": 196984,
    "lab": "python\u751f\u6210\u6c49\u5b57\u56fe\u7247\u5b57\u5e93",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011python\u751f\u6210\u6c49\u5b57\u56fe\u7247\u5b57\u5e93"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 11:58:51",
    "user_id": 78784,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 11:59:56",
    "user_id": 179356,
    "lab": "\u7b2c9\u5468\u8bfe\u5802\u5b9e\u9a8c-\u5b9e\u9a8c1",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 12:00:55",
    "user_id": 199643,
    "lab": "c\u8bed\u8a00\u5236\u4f5c2048",
    "course": "C\u8bed\u8a00\u5236\u4f5c2048"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 12:03:01",
    "user_id": 193335,
    "lab": "git\u4ecb\u7ecd",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 12:04:23",
    "user_id": 74797,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 12:06:16",
    "user_id": 94862,
    "lab": "\u8d70\u5411\u5206\u652f",
    "course": "\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u90d1\u6653\u8587\u7f16\u8457\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 12:07:50",
    "user_id": 197889,
    "lab": "\u591a\u8bf4,markdown\u548c\u4ee3\u7801\u9ad8\u4eae",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 12:09:30",
    "user_id": 193846,
    "lab": "\u7f51\u7edc\u5c42\u5176\u5b83\u534f\u8bae",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 12:11:39",
    "user_id": 95911,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 12:13:46",
    "user_id": 78784,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 12:13:52",
    "user_id": 123512,
    "lab": "SSH \u6846\u67b6\u5e94\u7528\u5b9e\u4f8b",
    "course": "SSH \u6846\u67b6\u5e94\u7528\u5b9e\u4f8b"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-02 12:14:43",
    "user_id": 170760,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 12:15:14",
    "user_id": 85918,
    "lab": "Redis\u6570\u636e\u7c7b\u578b ",
    "course": "Redis\u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 12:16:19",
    "user_id": 171682,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 12:18:00",
    "user_id": 170768,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 12:19:39",
    "user_id": 74797,
    "lab": "\u64cd\u4f5c\u7cfb\u7edf\u7684\u5f15\u5bfc",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 12:23:15",
    "user_id": 199645,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 12:26:32",
    "user_id": 197961,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 12:27:05",
    "user_id": 193497,
    "lab": "C++\u7b80\u5355\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "\u300aC++\u8bed\u8a00\u7a0b\u5e8f\u8bbe\u8ba1\uff08\u7b2c4\u7248\uff09\u300b\uff08\u90d1\u8389\u8457\uff09\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 12:27:16",
    "user_id": 188937,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 12:27:25",
    "user_id": 16328,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 12:28:08",
    "user_id": 170165,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-02 12:29:45",
    "user_id": 111834,
    "lab": "Java\u548cWebSocket\u5f00\u53d1\u7f51\u9875\u804a\u5929\u5ba4",
    "course": "Java\u548cWebSocket\u5f00\u53d1\u7f51\u9875\u804a\u5929\u5ba4"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 12:30:00",
    "user_id": 190530,
    "lab": "makefile",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 12:30:28",
    "user_id": 27112,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 12:31:26",
    "user_id": 3384,
    "lab": "\u5206\u9875",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 12:33:23",
    "user_id": 140305,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 12:33:43",
    "user_id": 171925,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-02 12:33:53",
    "user_id": 186876,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u8fd0\u7b97\u7b26\u548c\u6570\u636e\u8f6c\u6362",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 12:34:36",
    "user_id": 170979,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 12:34:52",
    "user_id": 78784,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 60,
    "created_at": "2016-05-02 12:35:29",
    "user_id": 170768,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 57,
    "created_at": "2016-05-02 12:36:12",
    "user_id": 170730,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 12:38:11",
    "user_id": 199648,
    "lab": "cookie\u57fa\u7840\u548c\u5e94\u7528",
    "course": "PHP\u4f1a\u8bdd\u63a7\u5236"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 12:40:34",
    "user_id": 128580,
    "lab": "\u591a\u8fdb\u7a0b\uff08\u4e09\uff09",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-02 12:41:48",
    "user_id": 190530,
    "lab": "makefile",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-02 12:43:29",
    "user_id": 176568,
    "lab": "\u7b2c2\u8282 HTML\u8d85\u6587\u672c\uff08\u4e00\uff09",
    "course": "\u7f51\u9875\u5236\u4f5c[\u4eba\u6587\u7d20\u8d28\u9009\u4fee\u8bfe]"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 12:44:04",
    "user_id": 167421,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 12:46:13",
    "user_id": 128327,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 12:46:39",
    "user_id": 127224,
    "lab": "groupby \u6280\u672f",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python \u6570\u636e\u5206\u6790\uff08\u4e8c\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 12:47:55",
    "user_id": 199650,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 12:48:07",
    "user_id": 199327,
    "lab": "\u4ecb\u7ecd",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 57,
    "created_at": "2016-05-02 12:48:58",
    "user_id": 198056,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-02 12:49:27",
    "user_id": 66074,
    "lab": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c",
    "course": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 12:50:40",
    "user_id": 84265,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-02 12:52:33",
    "user_id": 199327,
    "lab": "\u5f00\u53d1\u73af\u5883\u4ee5\u53ca\u9879\u76ee\u4e0eApp",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 12:52:59",
    "user_id": 199102,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 12:54:58",
    "user_id": 188937,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 12:56:12",
    "user_id": 195897,
    "lab": "\u521d\u8bc6HTML",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 12:56:20",
    "user_id": 95664,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e8c\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 12:56:51",
    "user_id": 199652,
    "lab": "\u521d\u8bc6HTML",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 12:57:22",
    "user_id": 127224,
    "lab": "\u65f6\u95f4\u5e8f\u5217",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python \u6570\u636e\u5206\u6790\uff08\u4e8c\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 12:57:28",
    "user_id": 199102,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-02 12:58:57",
    "user_id": 171968,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 12:59:23",
    "user_id": 27112,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 12:59:25",
    "user_id": 128327,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 12:59:50",
    "user_id": 199651,
    "lab": "Hadoop2.X 64\u4f4d\u7f16\u8bd1",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 12:59:56",
    "user_id": 193846,
    "lab": "\u4f20\u8f93\u5c42\uff1aUDP\u534f\u8bae",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 13:01:43",
    "user_id": 171686,
    "lab": "Java \u8bed\u8a00\u57fa\u7840",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-02 13:02:29",
    "user_id": 193248,
    "lab": "Android UI\u7f16\u7a0b",
    "course": "Android\u5e94\u7528\u5f00\u53d1\u57fa\u7840"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 13:04:42",
    "user_id": 189185,
    "lab": "\u5165\u95e8",
    "course": "Bootstrap3.0\u5165\u95e8\u5b66\u4e60"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 13:06:04",
    "user_id": 116680,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 13:07:54",
    "user_id": 199655,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 13:08:30",
    "user_id": 25854,
    "lab": "cookie\u57fa\u7840\u548c\u5e94\u7528",
    "course": "PHP\u4f1a\u8bdd\u63a7\u5236"
  },
  {
    "minutes": 78,
    "created_at": "2016-05-02 13:09:24",
    "user_id": 198635,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 13:09:52",
    "user_id": 169506,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 13:10:13",
    "user_id": 197912,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 13:11:09",
    "user_id": 170440,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 63,
    "created_at": "2016-05-02 13:13:59",
    "user_id": 171977,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 13:15:29",
    "user_id": 195043,
    "lab": "Bash\u4ecb\u7ecd\u4e0e\u5165\u95e8",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 13:17:43",
    "user_id": 3384,
    "lab": "\u5206\u9875",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 13:18:27",
    "user_id": 169356,
    "lab": "\u8ddf\u8e2a\u5206\u6790Linux\u5185\u6838\u7684\u542f\u52a8\u8fc7\u7a0b",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-02 13:19:30",
    "user_id": 167421,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 13:19:56",
    "user_id": 170979,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 13:21:27",
    "user_id": 193497,
    "lab": "\u7ebf\u6027\u7ed3\u6784-\u6808\u548c\u961f\u5217",
    "course": "\u6570\u636e\u7ed3\u6784(\u65b0\u7248)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 13:21:52",
    "user_id": 198933,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 13:23:32",
    "user_id": 179356,
    "lab": "\u7b2c10-11\u5468\u8bfe\u5802\u5b9e\u9a8c-\u5b9e\u9a8c\u4e8c \u7ee7\u627f\u6027\u7684\u5b9e\u73b0\uff081-2\uff09",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-02 13:25:00",
    "user_id": 198481,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 13:29:09",
    "user_id": 185000,
    "lab": "C++\u51fd\u6570",
    "course": "\u300aC++\u8bed\u8a00\u7a0b\u5e8f\u8bbe\u8ba1\uff08\u7b2c4\u7248\uff09\u300b\uff08\u90d1\u8389\u8457\uff09\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 13:30:05",
    "user_id": 31189,
    "lab": "LAMP\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "LAMP\u90e8\u7f72\u53ca\u914d\u7f6e"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-02 13:31:23",
    "user_id": 198933,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 13:31:34",
    "user_id": 169506,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 13:31:36",
    "user_id": 199659,
    "lab": "PHP\u7b80\u4ecb",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 13:32:17",
    "user_id": 190025,
    "lab": "\u7b2c\u4e00\u5355\u5143\u4e0a\u673a\u5b9e\u9a8c  HTML\u57fa\u7840\u6c47\u603b\u5b9e\u9a8c",
    "course": "\u7f51\u9875\u5236\u4f5c[\u4eba\u6587\u7d20\u8d28\u9009\u4fee\u8bfe]"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 13:32:26",
    "user_id": 64633,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 13:32:30",
    "user_id": 3384,
    "lab": "\u5206\u9875",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 13:35:45",
    "user_id": 170979,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 13:36:56",
    "user_id": 193911,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 13:37:29",
    "user_id": 199660,
    "lab": "\u7b2c\u4e00\u7ae0  Hello C++",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 13:38:13",
    "user_id": 64633,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-02 13:38:27",
    "user_id": 172969,
    "lab": "MapReduce\u5e94\u7528\u6848\u4f8b",
    "course": "BTBU-\u7814\u7a76\u751f2015\u7ea7-Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 13:40:12",
    "user_id": 66074,
    "lab": "ShellShock \u653b\u51fb\u5b9e\u9a8c",
    "course": "ShellShock \u653b\u51fb\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 13:41:27",
    "user_id": 169506,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 13:41:49",
    "user_id": 190025,
    "lab": "\u7b2c3\u8282  HTML\u8d85\u6587\u672c\uff08\u4e8c\uff09",
    "course": "\u7f51\u9875\u5236\u4f5c[\u4eba\u6587\u7d20\u8d28\u9009\u4fee\u8bfe]"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 13:43:18",
    "user_id": 174304,
    "lab": "\u6307\u9488\uff08\u4e8c\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 13:43:52",
    "user_id": 171968,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-02 13:44:26",
    "user_id": 16328,
    "lab": "\u5f00\u53d1\u73af\u5883\u548c\u5256\u6790\u7b2c\u4e00\u4e2a C \u8bed\u8a00",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 13:45:36",
    "user_id": 169506,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 13:47:16",
    "user_id": 199080,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 13:48:40",
    "user_id": 170440,
    "lab": "\u6570\u636e\u7ed3\u6784-\u4e8c\u53c9\u6811\uff08Binary Tree\uff09",
    "course": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 13:49:25",
    "user_id": 197912,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 78,
    "created_at": "2016-05-02 13:49:56",
    "user_id": 198423,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 13:54:20",
    "user_id": 170979,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 13:54:59",
    "user_id": 199505,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 13:55:06",
    "user_id": 184958,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 13:57:34",
    "user_id": 171778,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 13:57:49",
    "user_id": 199327,
    "lab": "\u5f00\u53d1\u73af\u5883\u4ee5\u53ca\u9879\u76ee\u4e0eApp",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 80,
    "created_at": "2016-05-02 14:01:09",
    "user_id": 199546,
    "lab": "Rails \u6570\u636e\u5e93\u6a21\u578b",
    "course": "Rails\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 14:01:31",
    "user_id": 184958,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 14:04:25",
    "user_id": 140305,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 14:04:26",
    "user_id": 199304,
    "lab": "linux\u7cfb\u7edf\u76d1\u63a7\u5e38\u7528\u547d\u4ee4\uff08\u4e00\uff09",
    "course": "Linux\u7cfb\u7edf\u76d1\u63a7\u5b9e\u6218"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 14:05:16",
    "user_id": 190025,
    "lab": "\u7b2c\u4e00\u5355\u5143\u4e0a\u673a\u5b9e\u9a8c  HTML\u57fa\u7840\u6c47\u603b\u5b9e\u9a8c",
    "course": "\u7f51\u9875\u5236\u4f5c[\u4eba\u6587\u7d20\u8d28\u9009\u4fee\u8bfe]"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 14:05:22",
    "user_id": 199668,
    "lab": "\u521d\u8bc6HTML",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-02 14:05:44",
    "user_id": 167421,
    "lab": "Python\u6df1\u5165\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-02 14:06:16",
    "user_id": 199670,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 14:07:02",
    "user_id": 193911,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 14:08:42",
    "user_id": 197961,
    "lab": "Bash\u4ecb\u7ecd\u4e0e\u5165\u95e8",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-02 14:08:46",
    "user_id": 171682,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 14:09:59",
    "user_id": 199345,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 14:11:20",
    "user_id": 148917,
    "lab": "\u94fe\u8def\u5c42\u4ecb\u7ecd",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 14:13:15",
    "user_id": 199572,
    "lab": "Python\u6587\u672c\u89e3\u91ca\u5668",
    "course": "Python\u6587\u672c\u89e3\u6790\u5668"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 14:13:53",
    "user_id": 199672,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 14:14:03",
    "user_id": 184958,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-02 14:14:14",
    "user_id": 197961,
    "lab": "Bash\u4e2d\u7684\u7279\u6b8a\u5b57\u7b26\uff08\u4e0a\uff09",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 14:14:32",
    "user_id": 148917,
    "lab": "IP\u7f51\u9645\u534f\u8bae",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 14:15:08",
    "user_id": 199669,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 14:15:25",
    "user_id": 171968,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-02 14:18:20",
    "user_id": 171841,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-02 14:18:42",
    "user_id": 199665,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 14:18:45",
    "user_id": 192978,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 14:19:50",
    "user_id": 66151,
    "lab": "\u6805\u683c\u7cfb\u7edf\u539f\u7406",
    "course": "Bootstrap3.0\u5165\u95e8\u5b66\u4e60"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 14:21:19",
    "user_id": 159200,
    "lab": "\u6761\u4ef6\u5224\u65ad",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 14:22:09",
    "user_id": 198056,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0b\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 14:22:46",
    "user_id": 124888,
    "lab": "css\u5165\u95e8\u57fa\u7840",
    "course": "CSS\u901f\u6210\u6559\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 14:23:08",
    "user_id": 198933,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-02 14:23:15",
    "user_id": 140305,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 14:23:36",
    "user_id": 170979,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 14:23:59",
    "user_id": 85073,
    "lab": "Python \u6d41\u7a0b\u63a7\u5236",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 14:29:25",
    "user_id": 199102,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 14:29:43",
    "user_id": 119886,
    "lab": "\u5b57\u7b26\u4e32\u4e0e\u5305\u88c5\u7c7b",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 14:30:22",
    "user_id": 158394,
    "lab": "\u57fa\u7840\u7bc7 - \u6570\u636e\u5e93\u53ca\u8868\u7684\u4fee\u6539\u548c\u5220\u9664",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 14:30:34",
    "user_id": 52524,
    "lab": "Python\u6df1\u5165\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 14:30:59",
    "user_id": 190025,
    "lab": "css\u57fa\u7840",
    "course": "\u7f51\u9875\u5236\u4f5c[\u4eba\u6587\u7d20\u8d28\u9009\u4fee\u8bfe]"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 14:31:14",
    "user_id": 197602,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 14:32:03",
    "user_id": 199623,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 14:33:09",
    "user_id": 66151,
    "lab": "\u6805\u683c\u7cfb\u7edf\u6848\u4f8b",
    "course": "Bootstrap3.0\u5165\u95e8\u5b66\u4e60"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 14:34:02",
    "user_id": 192069,
    "lab": "\u9879\u76ee\u4e94\uff1a\u6587\u5b57\u804a\u5929\u5ba4",
    "course": "Python \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 81,
    "created_at": "2016-05-02 14:34:11",
    "user_id": 171970,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 14:34:27",
    "user_id": 199668,
    "lab": "HTML\u6587\u672c",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 14:35:10",
    "user_id": 170875,
    "lab": "\u57fa\u4e8escrapy\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u57fa\u4e8escrapy\u722c\u866b\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6(python)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 14:35:25",
    "user_id": 199270,
    "lab": "Python\u6df1\u5165\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 14:36:21",
    "user_id": 199102,
    "lab": "\u5f00\u53d1\u73af\u5883\u548c\u5256\u6790\u7b2c\u4e00\u4e2a C \u8bed\u8a00",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 14:36:26",
    "user_id": 171915,
    "lab": "\u7b2c2\u5468\uff1a\u865a\u62df\u5316\u4e0e\u4e91\u8ba1\u7b97\u6280\u672f",
    "course": "\u4effOpenStack\u5f00\u53d1\u4e91\u8ba1\u7b97\u7ba1\u7406\u8f6f\u4ef6"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 14:36:27",
    "user_id": 124888,
    "lab": "css\u5165\u95e8\u57fa\u7840",
    "course": "CSS\u901f\u6210\u6559\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 14:37:58",
    "user_id": 109937,
    "lab": "Java \u63a7\u5236\u8bed\u53e5",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-02 14:38:19",
    "user_id": 171969,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 14:39:00",
    "user_id": 185203,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 14:39:21",
    "user_id": 199675,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 14:39:28",
    "user_id": 116727,
    "lab": "Python\u6807\u51c6\u5e93\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 14:39:31",
    "user_id": 131514,
    "lab": "Yii2 \u6570\u636e\u5e93\u548cGii",
    "course": "Yii 2\u7cfb\u5217\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 14:39:37",
    "user_id": 199640,
    "lab": "lab0\uff1aCoding!",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u5b9e\u9a8c\uff0d\u57fa\u4e8euCore OS"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 14:40:26",
    "user_id": 170980,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 14:41:46",
    "user_id": 173414,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 14:42:20",
    "user_id": 199307,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 14:42:56",
    "user_id": 167421,
    "lab": "Python\u6df1\u5165\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 14:43:03",
    "user_id": 199327,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 14:43:33",
    "user_id": 199672,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 14:44:22",
    "user_id": 81189,
    "lab": "c\u8bed\u8a00\u5229\u7528epoll\u5b9e\u73b0\u804a\u5929\u5ba4",
    "course": "C\u8bed\u8a00\u5229\u7528epoll\u5b9e\u73b0\u9ad8\u5e76\u53d1\u804a\u5929\u5ba4"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 14:45:02",
    "user_id": 199102,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e00\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 14:48:22",
    "user_id": 173414,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 14:50:13",
    "user_id": 199463,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 14:51:47",
    "user_id": 170156,
    "lab": "\u8ddf\u8e2a\u5206\u6790Linux\u5185\u6838\u7684\u542f\u52a8\u8fc7\u7a0b",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 14:51:53",
    "user_id": 174950,
    "lab": "Mahout\u4ecb\u7ecd\u3001\u5b89\u88c5\u4e0e\u5e94\u7528\u6848\u4f8b",
    "course": "BTBU-\u7814\u7a76\u751f2015\u7ea7-Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-02 14:52:39",
    "user_id": 171682,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 14:52:59",
    "user_id": 197775,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 14:56:32",
    "user_id": 171841,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 14:57:18",
    "user_id": 170875,
    "lab": "Python\u6587\u672c\u89e3\u91ca\u5668",
    "course": "Python\u6587\u672c\u89e3\u6790\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 14:58:18",
    "user_id": 171001,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 15:01:24",
    "user_id": 158394,
    "lab": "\u57fa\u7840\u7bc7 - \u5176\u4ed6\u57fa\u672c\u64cd\u4f5c",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 15:01:37",
    "user_id": 199538,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 15:03:14",
    "user_id": 140305,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 15:06:34",
    "user_id": 197865,
    "lab": "\u57fa\u4e8escrapy\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u57fa\u4e8escrapy\u722c\u866b\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6(python)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 15:07:01",
    "user_id": 199440,
    "lab": "\u4ecb\u7ecd",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 15:07:01",
    "user_id": 199463,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 15:08:00",
    "user_id": 170980,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 15:08:13",
    "user_id": 8365,
    "lab": "Bash\u4ecb\u7ecd\u4e0e\u5165\u95e8",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 15:08:24",
    "user_id": 170156,
    "lab": "\u8ddf\u8e2a\u5206\u6790Linux\u5185\u6838\u7684\u542f\u52a8\u8fc7\u7a0b",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 15:08:34",
    "user_id": 199680,
    "lab": "\u5f00\u53d1\u73af\u5883\u4ee5\u53ca\u9879\u76ee\u4e0eApp",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 15:09:52",
    "user_id": 140305,
    "lab": "\u6570\u636e\u7ed3\u6784-\u5b57\u7b26\u4e32\uff08String\uff09",
    "course": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 15:10:07",
    "user_id": 199307,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 15:12:17",
    "user_id": 199102,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e8c\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 15:12:18",
    "user_id": 192549,
    "lab": "cookie\u57fa\u7840\u548c\u5e94\u7528",
    "course": "PHP\u4f1a\u8bdd\u63a7\u5236"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-02 15:13:00",
    "user_id": 171001,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 15:13:00",
    "user_id": 199440,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 15:13:58",
    "user_id": 199463,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 15:15:00",
    "user_id": 59262,
    "lab": "C\u8bed\u8a00\u7248flappy_bird",
    "course": "C\u8bed\u8a00\u7248flappy_bird"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 15:15:44",
    "user_id": 199670,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 15:15:50",
    "user_id": 27112,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 15:16:00",
    "user_id": 173414,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 15:17:23",
    "user_id": 175137,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 15:17:33",
    "user_id": 170980,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 15:18:36",
    "user_id": 174149,
    "lab": "\u9879\u76ee\u516d\uff1aFlask\u4e2a\u4eba\u535a\u5ba2",
    "course": "Python \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 15:19:49",
    "user_id": 199307,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-02 15:21:05",
    "user_id": 171975,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 15:21:32",
    "user_id": 199686,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 15:21:41",
    "user_id": 190025,
    "lab": "\u7b2c4\u8282  css\u57fa\u7840\u9009\u62e9\u5668",
    "course": "\u7f51\u9875\u5236\u4f5c[\u4eba\u6587\u7d20\u8d28\u9009\u4fee\u8bfe]"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 15:21:59",
    "user_id": 199651,
    "lab": "Hadoop2.X 64\u4f4d\u7f16\u8bd1",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 15:23:12",
    "user_id": 199463,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 15:23:42",
    "user_id": 199125,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 15:24:34",
    "user_id": 199580,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 15:25:22",
    "user_id": 170979,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 15:26:44",
    "user_id": 59262,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 15:27:00",
    "user_id": 199659,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 69,
    "created_at": "2016-05-02 15:27:21",
    "user_id": 170760,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 15:27:46",
    "user_id": 199670,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 15:28:11",
    "user_id": 26092,
    "lab": "PythonChallenge_3",
    "course": "\u6bcf\u5929\u4e00\u4e2aPythonChallenge\u300a\u4efb\u52a1\u4e09\u300b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 15:29:03",
    "user_id": 199688,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 15:29:43",
    "user_id": 199102,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 15:29:49",
    "user_id": 145873,
    "lab": "cookie\u57fa\u7840\u548c\u5e94\u7528",
    "course": "PHP\u4f1a\u8bdd\u63a7\u5236"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 15:30:18",
    "user_id": 199680,
    "lab": "Models\u548cAdmin\u4ee5\u53caViews\u548cURL",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 15:30:53",
    "user_id": 47745,
    "lab": "\u4e2d\u7ea7\u6280\u80fd\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 96,
    "created_at": "2016-05-02 15:31:29",
    "user_id": 199125,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 15:32:27",
    "user_id": 199505,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 15:32:44",
    "user_id": 171682,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 15:34:12",
    "user_id": 8376,
    "lab": "R\u8bed\u8a00\u8bfe\u7a0b\u4ecb\u7ecd",
    "course": "[\u7ef4\u62a4\u4e2d] R\u8bed\u8a00\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 15:34:33",
    "user_id": 199102,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 15:35:39",
    "user_id": 199682,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 15:36:22",
    "user_id": 171958,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 15:36:44",
    "user_id": 158394,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 15:38:37",
    "user_id": 199659,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 15:40:02",
    "user_id": 199102,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 15:40:08",
    "user_id": 192549,
    "lab": "session\u57fa\u7840\u4e0e\u5b9e\u6218",
    "course": "PHP\u4f1a\u8bdd\u63a7\u5236"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 15:41:03",
    "user_id": 171960,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 15:42:40",
    "user_id": 178526,
    "lab": "\u7b2c10-11\u5468\u8bfe\u5802\u5b9e\u9a8c-\u5b9e\u9a8c\u4e8c \u7ee7\u627f\u6027\u7684\u5b9e\u73b0\uff081-2\uff09",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 15:43:44",
    "user_id": 162532,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 15:43:47",
    "user_id": 199489,
    "lab": "\u521d\u8bc6HTML",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-02 15:44:08",
    "user_id": 80485,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 15:45:28",
    "user_id": 170156,
    "lab": "\u8ddf\u8e2a\u5206\u6790Linux\u5185\u6838\u7684\u542f\u52a8\u8fc7\u7a0b",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 15:45:50",
    "user_id": 85085,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 15:46:15",
    "user_id": 174172,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 15:47:36",
    "user_id": 86495,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-02 15:48:01",
    "user_id": 171958,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 15:48:01",
    "user_id": 27112,
    "lab": "python\u751f\u6210\u6c49\u5b57\u56fe\u7247\u5b57\u5e93",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011python\u751f\u6210\u6c49\u5b57\u56fe\u7247\u5b57\u5e93"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-02 15:50:47",
    "user_id": 199463,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 57,
    "created_at": "2016-05-02 15:52:46",
    "user_id": 170980,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 15:52:47",
    "user_id": 171977,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 15:53:06",
    "user_id": 197602,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 15:53:30",
    "user_id": 50777,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 15:54:16",
    "user_id": 98977,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 15:55:29",
    "user_id": 179221,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 15:56:59",
    "user_id": 103555,
    "lab": "PythonChallenge_1",
    "course": "\u5168\u9762\u89e3\u6790PythonChallenge"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 15:57:35",
    "user_id": 199670,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 15:57:43",
    "user_id": 190025,
    "lab": "\u7b2c5\u8282  css\u57fa\u672c\u6837\u5f0f\uff08\u4e00\uff09",
    "course": "\u7f51\u9875\u5236\u4f5c[\u4eba\u6587\u7d20\u8d28\u9009\u4fee\u8bfe]"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 15:59:10",
    "user_id": 199692,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 16:00:55",
    "user_id": 27112,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 60,
    "created_at": "2016-05-02 16:00:59",
    "user_id": 52524,
    "lab": "Python\u6df1\u5165\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 16:01:25",
    "user_id": 199659,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 16:01:50",
    "user_id": 98977,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 132,
    "created_at": "2016-05-02 16:01:55",
    "user_id": 175137,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 16:02:35",
    "user_id": 197602,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:03:25",
    "user_id": 173414,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 16:04:08",
    "user_id": 174172,
    "lab": "Java  \u8fd0\u7b97\u7b26",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-02 16:04:14",
    "user_id": 198423,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 16:04:29",
    "user_id": 171682,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 16:05:55",
    "user_id": 197961,
    "lab": "Bash\u4e2d\u7684\u7279\u6b8a\u5b57\u7b26\uff08\u4e0b\uff09",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 16:06:20",
    "user_id": 85085,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-02 16:06:40",
    "user_id": 173414,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-02 16:07:05",
    "user_id": 171964,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-02 16:07:18",
    "user_id": 162532,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-02 16:08:11",
    "user_id": 186876,
    "lab": "\u9009\u62e9\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-02 16:08:18",
    "user_id": 94862,
    "lab": "\u8d70\u5411\u5206\u652f",
    "course": "\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u90d1\u6653\u8587\u7f16\u8457\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:08:37",
    "user_id": 8365,
    "lab": "Bash\u4e2d\u7684\u7279\u6b8a\u5b57\u7b26\uff08\u4e0a\uff09",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:08:40",
    "user_id": 171970,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:08:58",
    "user_id": 190025,
    "lab": "\u7b2c7\u8282  css\u76d2\u5b50\u6a21\u578b",
    "course": "\u7f51\u9875\u5236\u4f5c[\u4eba\u6587\u7d20\u8d28\u9009\u4fee\u8bfe]"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 16:09:05",
    "user_id": 179221,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:11:40",
    "user_id": 199102,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 16:11:44",
    "user_id": 193846,
    "lab": "\u4f20\u8f93\u5c42\uff1aTCP\u534f\u8bae",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 16:11:47",
    "user_id": 113828,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:12:02",
    "user_id": 192549,
    "lab": "JavaScript \u7b80\u4ecb",
    "course": "Javascript\u57fa\u7840\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:13:36",
    "user_id": 199692,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 16:13:46",
    "user_id": 159200,
    "lab": "\u6761\u4ef6\u5224\u65ad",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 16:13:52",
    "user_id": 199696,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 16:14:01",
    "user_id": 199659,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 16:16:24",
    "user_id": 118124,
    "lab": "HTML\u8d85\u6587\u672c\uff08\u4e8c\uff09",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 16:16:32",
    "user_id": 50252,
    "lab": "\u521d\u8bc6MySQL",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:16:40",
    "user_id": 29988,
    "lab": "Java \u96c6\u5408\u6846\u67b6",
    "course": "JDK \u6838\u5fc3 API"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-02 16:17:20",
    "user_id": 175176,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-02 16:17:47",
    "user_id": 192178,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:18:00",
    "user_id": 195406,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 16:19:42",
    "user_id": 192069,
    "lab": "\u9879\u76ee\u4e94\uff1a\u6587\u5b57\u804a\u5929\u5ba4",
    "course": "Python \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 16:20:29",
    "user_id": 171682,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 108,
    "created_at": "2016-05-02 16:20:30",
    "user_id": 171975,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 16:20:58",
    "user_id": 174172,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:21:31",
    "user_id": 199694,
    "lab": "\u670d\u52a1\u5668\u7684\u8bf7\u6c42\u548c\u54cd\u5e94",
    "course": "\u8f7b\u677e\u521b\u5efa Node.js \u670d\u52a1\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:23:52",
    "user_id": 108463,
    "lab": "Nginx\u529f\u80fd\u63cf\u8ff0",
    "course": "Linux Web\u8fd0\u7ef4\uff08Nginx\uff09\u5b9e\u6218 "
  },
  {
    "minutes": 36,
    "created_at": "2016-05-02 16:23:57",
    "user_id": 171001,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 16:24:06",
    "user_id": 100863,
    "lab": "C \u8bed\u8a00\u6570\u7ec4",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:24:36",
    "user_id": 171970,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 16:24:59",
    "user_id": 171388,
    "lab": "\u7b2c10-11\u5468\u8bfe\u5802\u5b9e\u9a8c-\u5b9e\u9a8c\u4e8c \u7ee7\u627f\u6027\u7684\u5b9e\u73b0\uff081-2\uff09",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:25:00",
    "user_id": 186528,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 16:27:14",
    "user_id": 199659,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-02 16:28:17",
    "user_id": 199463,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-02 16:28:59",
    "user_id": 179764,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 16:29:11",
    "user_id": 34691,
    "lab": "\u901a\u8fc7\u53cd\u6c47\u7f16\u4e00\u4e2a\u7b80\u5355\u7684C\u7a0b\u5e8f\uff0c\u5206\u6790\u6c47\u7f16\u4ee3\u7801\u7406\u89e3\u8ba1\u7b97\u673a\u662f\u5982\u4f55\u5de5\u4f5c\u7684",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:29:45",
    "user_id": 196306,
    "lab": "DOS\u53caDEBUG\u4ecb\u7ecd",
    "course": "\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u90d1\u6653\u8587\u7f16\u8457\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 16:30:34",
    "user_id": 197602,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 16:30:58",
    "user_id": 199307,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 16:31:03",
    "user_id": 199700,
    "lab": "\u8bfe\u7a0b\u57fa\u7840\u5305\uff08\u4e0a\uff09\uff0d\u5355\u9009\u7c7b\u578b\u8868\u5355\u81ea\u52a8\u63d0\u4ea4",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python\u81ea\u52a8\u586b\u95ee\u5377\u661f"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 16:31:08",
    "user_id": 104375,
    "lab": "Hadoop\u4ecb\u7ecd\u53ca1.X\u4f2a\u5206\u5e03\u5f0f\u5b89\u88c5",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-02 16:31:55",
    "user_id": 171959,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 16:34:08",
    "user_id": 197404,
    "lab": "\u521d\u8bc6HTML",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 16:36:18",
    "user_id": 98977,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u7684\u7ea6\u675f",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 16:38:42",
    "user_id": 171977,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:39:05",
    "user_id": 199703,
    "lab": "\u8868\u8fbe\u5f0f\u7684\u8ba1\u7b97",
    "course": "Scala \u5f00\u53d1\u4e8c\u5341\u56db\u70b9\u6e38\u620f"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:39:24",
    "user_id": 199706,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-02 16:39:36",
    "user_id": 199659,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:40:20",
    "user_id": 173266,
    "lab": "MapReduce\u5e94\u7528\u6848\u4f8b",
    "course": "BTBU-\u7814\u7a76\u751f2015\u7ea7-Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 16:40:24",
    "user_id": 174172,
    "lab": "Java  \u8fd0\u7b97\u7b26",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 16:40:28",
    "user_id": 80485,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 16:40:48",
    "user_id": 62403,
    "lab": "Go\u8bed\u8a00\u4ecb\u7ecd",
    "course": "Go\u8bed\u8a00\u7f16\u7a0b"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-02 16:43:57",
    "user_id": 171958,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:45:04",
    "user_id": 60663,
    "lab": "Java\u5b9e\u73b0\u8bb0\u4e8b\u672c",
    "course": "Java\u5b9e\u73b0\u8bb0\u4e8b\u672c"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 16:45:58",
    "user_id": 199307,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 16:46:13",
    "user_id": 199270,
    "lab": "Python\u6df1\u5165\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 75,
    "created_at": "2016-05-02 16:46:18",
    "user_id": 171970,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:47:12",
    "user_id": 199707,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:47:18",
    "user_id": 199538,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-02 16:48:03",
    "user_id": 170760,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 16:48:04",
    "user_id": 171968,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 16:48:44",
    "user_id": 199572,
    "lab": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668",
    "course": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 16:50:00",
    "user_id": 112635,
    "lab": "\u901a\u8fc7\u53cd\u6c47\u7f16\u4e00\u4e2a\u7b80\u5355\u7684C\u7a0b\u5e8f\uff0c\u5206\u6790\u6c47\u7f16\u4ee3\u7801\u7406\u89e3\u8ba1\u7b97\u673a\u662f\u5982\u4f55\u5de5\u4f5c\u7684",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-02 16:50:30",
    "user_id": 197865,
    "lab": "\u57fa\u4e8escrapy\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u57fa\u4e8escrapy\u722c\u866b\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6(python)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:51:35",
    "user_id": 171977,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-02 16:54:02",
    "user_id": 175176,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:55:12",
    "user_id": 153459,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 16:55:20",
    "user_id": 187252,
    "lab": "\u5f00\u53d1\u73af\u5883\u548c\u5256\u6790\u7b2c\u4e00\u4e2a C \u8bed\u8a00",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 16:55:22",
    "user_id": 130246,
    "lab": "\u5165\u95e8",
    "course": "Bootstrap3.0\u5165\u95e8\u5b66\u4e60"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:56:10",
    "user_id": 199712,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:56:45",
    "user_id": 171977,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:57:08",
    "user_id": 199700,
    "lab": "\u8bfe\u7a0b\u57fa\u7840\u5305\uff08\u4e0b\uff09\uff0d\u5168\u80fd\u8868\u5355\u63d0\u4ea4\u738b",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python\u81ea\u52a8\u586b\u95ee\u5377\u661f"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 16:57:23",
    "user_id": 104375,
    "lab": "HDFS\u539f\u7406\u53ca\u64cd\u4f5c",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 16:57:35",
    "user_id": 193846,
    "lab": "\u5e94\u7528\u5c42\u534f\u8bae\u4e00",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 16:58:01",
    "user_id": 193511,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 16:58:39",
    "user_id": 98977,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u7684\u7ea6\u675f",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 16:59:28",
    "user_id": 66151,
    "lab": "\u9879\u76ee\u56db\uff1a\u7f51\u7ad9\u4fe1\u606f\u722c\u866b",
    "course": "Python \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-02 17:00:21",
    "user_id": 179636,
    "lab": "\u8d70\u5411\u5206\u652f",
    "course": "[\u79c1\u6709]\u8fbd\u5b81\u5e08\u8303\u5927\u5b66\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u5b9e\u9a8c\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 17:00:46",
    "user_id": 171977,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 17:02:25",
    "user_id": 171968,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 17:02:45",
    "user_id": 187286,
    "lab": "Python\u6807\u51c6\u5e93\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 17:03:00",
    "user_id": 199712,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 17:04:57",
    "user_id": 171977,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 17:05:06",
    "user_id": 197961,
    "lab": "Bash\u4e2d\u7684\u7279\u6b8a\u5b57\u7b26\uff08\u4e0b\uff09",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 17:05:31",
    "user_id": 199563,
    "lab": "lab0\uff1aCoding!",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u5b9e\u9a8c\uff0d\u57fa\u4e8euCore OS"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 17:05:34",
    "user_id": 145739,
    "lab": "\u8ba4\u8bc6 JDBC",
    "course": "JDBC \u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 17:06:13",
    "user_id": 68077,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 17:07:31",
    "user_id": 128701,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 17:09:28",
    "user_id": 161159,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0b\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 17:10:01",
    "user_id": 98977,
    "lab": "\u57fa\u7840\u7bc7 - SELECT \u8bed\u53e5\u8be6\u89e3",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 17:10:02",
    "user_id": 130246,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 17:10:27",
    "user_id": 171977,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 17:11:13",
    "user_id": 171964,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 17:12:32",
    "user_id": 86495,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 17:12:36",
    "user_id": 128701,
    "lab": "\u5f00\u53d1\u73af\u5883\u548c\u5256\u6790\u7b2c\u4e00\u4e2a C \u8bed\u8a00",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 17:12:41",
    "user_id": 199717,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 17:13:42",
    "user_id": 68077,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 17:15:28",
    "user_id": 171977,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 17:15:37",
    "user_id": 199307,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 17:15:43",
    "user_id": 197961,
    "lab": "\u53d8\u91cf\u548c\u53c2\u6570",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 17:17:32",
    "user_id": 68077,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-02 17:18:09",
    "user_id": 74744,
    "lab": "python\u751f\u6210\u6c49\u5b57\u56fe\u7247\u5b57\u5e93",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011python\u751f\u6210\u6c49\u5b57\u56fe\u7247\u5b57\u5e93"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-02 17:18:17",
    "user_id": 198561,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 17:18:45",
    "user_id": 68346,
    "lab": "\u8f6c\u76d8\u62bd\u5956",
    "course": "PHP\u5b9e\u73b0\u8f6c\u76d8\u62bd\u5956"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 17:19:30",
    "user_id": 199659,
    "lab": "PHP\u7b80\u4ecb",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 17:20:52",
    "user_id": 104375,
    "lab": "MapReduce\u539f\u7406\u53ca\u64cd\u4f5c",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 17:22:25",
    "user_id": 171969,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-02 17:23:29",
    "user_id": 140305,
    "lab": "\u7528\u6237\u767b\u5f55",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-02 17:24:15",
    "user_id": 58968,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 17:24:33",
    "user_id": 171977,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 17:25:41",
    "user_id": 199718,
    "lab": "linux\u7cfb\u7edf\u76d1\u63a7\u5e38\u7528\u547d\u4ee4\uff08\u4e8c\uff09",
    "course": "Linux\u7cfb\u7edf\u76d1\u63a7\u5b9e\u6218"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 17:25:47",
    "user_id": 199436,
    "lab": "\u8bfe\u7a0b\u57fa\u7840\u5305\uff08\u4e0a\uff09\uff0d\u5355\u9009\u7c7b\u578b\u8868\u5355\u81ea\u52a8\u63d0\u4ea4",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python\u81ea\u52a8\u586b\u95ee\u5377\u661f"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-02 17:25:50",
    "user_id": 175176,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 17:28:09",
    "user_id": 128701,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e00\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 17:28:10",
    "user_id": 113828,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-02 17:28:17",
    "user_id": 199463,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 17:31:14",
    "user_id": 191090,
    "lab": "makefile",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 17:31:52",
    "user_id": 84557,
    "lab": "\u8d2a\u5403\u86c7\u6838\u5fc3\u7f16\u7a0b",
    "course": "\u7ec8\u7aef\u8d2a\u5403\u86c7"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 17:33:21",
    "user_id": 175819,
    "lab": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c",
    "course": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c"
  },
  {
    "minutes": 2,
    "created_at": "2016-05-02 17:34:06",
    "user_id": 199700,
    "lab": "\u591a\u5f20\u56fe\u7247\u62fc\u63a5\u4e0e\u5c42\u53e0",
    "course": "\u591a\u5f20\u56fe\u7247\u62fc\u63a5\u4e0e\u5c42\u53e0"
  },
  {
    "minutes": 57,
    "created_at": "2016-05-02 17:34:57",
    "user_id": 50252,
    "lab": "MySQL\u57fa\u672c\u64cd\u4f5c",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 17:35:10",
    "user_id": 199436,
    "lab": "\u8bfe\u7a0b\u57fa\u7840\u5305\uff08\u4e0a\uff09\uff0d\u5355\u9009\u7c7b\u578b\u8868\u5355\u81ea\u52a8\u63d0\u4ea4",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python\u81ea\u52a8\u586b\u95ee\u5377\u661f"
  },
  {
    "minutes": 105,
    "created_at": "2016-05-02 17:35:17",
    "user_id": 84362,
    "lab": "C \u8bed\u8a00\u6570\u7ec4",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 17:35:25",
    "user_id": 171969,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 17:35:31",
    "user_id": 94862,
    "lab": "\u8d70\u5411\u5206\u652f",
    "course": "\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u90d1\u6653\u8587\u7f16\u8457\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 17:35:55",
    "user_id": 171977,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 17:36:15",
    "user_id": 159200,
    "lab": "\u64cd\u4f5c\u7b26",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 17:37:45",
    "user_id": 196766,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 17:38:23",
    "user_id": 167421,
    "lab": "Python\u6df1\u5165\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 17:40:54",
    "user_id": 111770,
    "lab": "\u901a\u8fc7\u53cd\u6c47\u7f16\u4e00\u4e2a\u7b80\u5355\u7684C\u7a0b\u5e8f\uff0c\u5206\u6790\u6c47\u7f16\u4ee3\u7801\u7406\u89e3\u8ba1\u7b97\u673a\u662f\u5982\u4f55\u5de5\u4f5c\u7684",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 17:42:05",
    "user_id": 168318,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 17:42:25",
    "user_id": 64633,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 75,
    "created_at": "2016-05-02 17:43:13",
    "user_id": 171964,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-02 17:44:17",
    "user_id": 171959,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-02 17:44:19",
    "user_id": 170760,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 17:44:59",
    "user_id": 171977,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 17:45:46",
    "user_id": 196766,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 17:47:13",
    "user_id": 68077,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 17:48:26",
    "user_id": 171841,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 17:48:43",
    "user_id": 168318,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 17:49:03",
    "user_id": 164034,
    "lab": "lab0\uff1aCoding!",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u5b9e\u9a8c\uff0d\u57fa\u4e8euCore OS"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 17:49:18",
    "user_id": 144538,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 17:50:25",
    "user_id": 195931,
    "lab": "LAMP\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "LAMP\u90e8\u7f72\u53ca\u914d\u7f6e"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 17:50:28",
    "user_id": 196766,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-02 17:51:01",
    "user_id": 199663,
    "lab": "Hadoop\u4ecb\u7ecd\u53ca1.X\u4f2a\u5206\u5e03\u5f0f\u5b89\u88c5",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 17:52:25",
    "user_id": 171977,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-02 17:52:30",
    "user_id": 199659,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 17:53:28",
    "user_id": 68077,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 17:54:34",
    "user_id": 170980,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 17:55:30",
    "user_id": 171969,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 17:56:31",
    "user_id": 68077,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 17:56:57",
    "user_id": 199709,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 17:57:05",
    "user_id": 102421,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 17:59:48",
    "user_id": 198561,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 87,
    "created_at": "2016-05-02 18:01:34",
    "user_id": 171718,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 18:01:59",
    "user_id": 58968,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 18:02:02",
    "user_id": 159200,
    "lab": "\u53d8\u91cf\u91cd\u6e38",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 18:02:14",
    "user_id": 153459,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 18:02:37",
    "user_id": 199087,
    "lab": "Template\u548c\u52a8\u6001URL",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 18:04:50",
    "user_id": 198561,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 18:06:00",
    "user_id": 168318,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 18:06:38",
    "user_id": 186528,
    "lab": "Hello World",
    "course": "Android\u5e94\u7528\u5f00\u53d1\u57fa\u7840"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-02 18:06:56",
    "user_id": 170980,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 18:06:57",
    "user_id": 199726,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 18:07:38",
    "user_id": 171969,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 18:08:38",
    "user_id": 199463,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 18:08:51",
    "user_id": 199727,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 18:10:27",
    "user_id": 177199,
    "lab": "Bash\u4ecb\u7ecd\u4e0e\u5165\u95e8",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 18:10:39",
    "user_id": 198710,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 18:10:59",
    "user_id": 68077,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 18:12:03",
    "user_id": 199517,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 102,
    "created_at": "2016-05-02 18:12:15",
    "user_id": 179636,
    "lab": "\u8d70\u5411\u5206\u652f",
    "course": "[\u79c1\u6709]\u8fbd\u5b81\u5e08\u8303\u5927\u5b66\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u5b9e\u9a8c\u8bfe\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 18:12:44",
    "user_id": 58968,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 18:13:26",
    "user_id": 199480,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-02 18:13:31",
    "user_id": 162448,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 18:13:51",
    "user_id": 62403,
    "lab": "Go\u8bed\u8a00\u4ecb\u7ecd",
    "course": "Go\u8bed\u8a00\u7f16\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 18:14:16",
    "user_id": 153459,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 18:15:49",
    "user_id": 6698,
    "lab": "Node.js\u8bfe\u7a0b\u4ecb\u7ecd",
    "course": "Node.js \u6559\u7a0b"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-02 18:16:39",
    "user_id": 191090,
    "lab": "makefile",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 18:17:42",
    "user_id": 168318,
    "lab": "Flask\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 18:17:50",
    "user_id": 26927,
    "lab": "c\u8bed\u8a00\u7f16\u5199\u4e07\u5e74\u5386",
    "course": "C\u8bed\u8a00\u7f16\u5199\u4e07\u5e74\u5386"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-02 18:17:53",
    "user_id": 175819,
    "lab": "DOS\u53caDEBUG\u4ecb\u7ecd",
    "course": "\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u90d1\u6653\u8587\u7f16\u8457\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-02 18:18:28",
    "user_id": 171969,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 18:18:45",
    "user_id": 192069,
    "lab": "\u9879\u76ee\u4e94\uff1a\u6587\u5b57\u804a\u5929\u5ba4",
    "course": "Python \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 18:18:47",
    "user_id": 199480,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 18:19:01",
    "user_id": 177199,
    "lab": "Bash\u4e2d\u7684\u7279\u6b8a\u5b57\u7b26\uff08\u4e0a\uff09",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 18:20:08",
    "user_id": 199463,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 18:21:00",
    "user_id": 185517,
    "lab": "Kaggle\u5165\u95e8",
    "course": "Kaggle\u5165\u95e8\uff1a\u6cf0\u5766\u5c3c\u514b\u53f7\u5e78\u5b58\u8005\u9879\u76ee"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-02 18:23:24",
    "user_id": 197948,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-02 18:23:46",
    "user_id": 199670,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 2,
    "created_at": "2016-05-02 18:24:02",
    "user_id": 199614,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 18:24:44",
    "user_id": 64633,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 18:24:51",
    "user_id": 171977,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 18:25:16",
    "user_id": 171682,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 18:25:30",
    "user_id": 58968,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 18:26:29",
    "user_id": 199728,
    "lab": "\u6b22\u8fce\u6765\u5230 Flask \u7684\u4e16\u754c",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 18:26:56",
    "user_id": 48093,
    "lab": "cookie\u57fa\u7840\u548c\u5e94\u7528",
    "course": "PHP\u4f1a\u8bdd\u63a7\u5236"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 18:27:31",
    "user_id": 171973,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 18:29:30",
    "user_id": 170979,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-02 18:31:16",
    "user_id": 171975,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 18:31:49",
    "user_id": 171977,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 18:34:17",
    "user_id": 199727,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 18:34:28",
    "user_id": 198561,
    "lab": "git\u4ecb\u7ecd",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 18:35:35",
    "user_id": 11647,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 18:36:02",
    "user_id": 89166,
    "lab": "JavaScript \u57fa\u672c\u8bed\u6cd5\uff08\u4e0a\uff09",
    "course": "Javascript\u57fa\u7840\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 18:36:27",
    "user_id": 69472,
    "lab": "\u64cd\u4f5c\u7cfb\u7edf\u7684\u5f15\u5bfc",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 18:37:43",
    "user_id": 153459,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 18:37:58",
    "user_id": 29988,
    "lab": "Java \u96c6\u5408\u6846\u67b6",
    "course": "JDK \u6838\u5fc3 API"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 18:38:48",
    "user_id": 168318,
    "lab": "Flask\u8fd0\u884c\u53ca\u8c03\u8bd5\u6a21\u5f0f",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 18:39:07",
    "user_id": 198561,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 18:39:55",
    "user_id": 196682,
    "lab": "\u7ebf\u6027\u7ed3\u6784-\u6808\u548c\u961f\u5217",
    "course": "\u6570\u636e\u7ed3\u6784(\u65b0\u7248)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 18:40:20",
    "user_id": 199707,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 18:41:01",
    "user_id": 177199,
    "lab": "\u5f15\u7528\u548c\u8f6c\u4e49",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 129,
    "created_at": "2016-05-02 18:41:56",
    "user_id": 171841,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 18:44:26",
    "user_id": 199730,
    "lab": "\u4e00\u4e2a\u6700\u7b80\u5355\u7684 express \u5e94\u7528",
    "course": "Node.js\u5305\u6559\u4e0d\u5305\u4f1a"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 18:44:49",
    "user_id": 197961,
    "lab": "\u5f15\u7528\u548c\u8f6c\u4e49",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 18:44:50",
    "user_id": 199733,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 18:45:40",
    "user_id": 199307,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 86,
    "created_at": "2016-05-02 18:45:41",
    "user_id": 171001,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 18:46:03",
    "user_id": 171959,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-02 18:46:10",
    "user_id": 199728,
    "lab": "Flask \u6a21\u677f",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 18:46:27",
    "user_id": 170974,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 18:46:52",
    "user_id": 199599,
    "lab": "MySQL\u57fa\u672c\u64cd\u4f5c",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 18:47:05",
    "user_id": 199732,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 18:47:05",
    "user_id": 168318,
    "lab": "Flask\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 18:47:13",
    "user_id": 199734,
    "lab": "Perl\u7b80\u5355\u4ecb\u7ecd",
    "course": "Perl\u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 18:47:56",
    "user_id": 199659,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 18:49:38",
    "user_id": 118312,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 18:50:56",
    "user_id": 168318,
    "lab": "Flask\u8fd0\u884c\u53ca\u8c03\u8bd5\u6a21\u5f0f",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-02 18:51:25",
    "user_id": 170841,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 18:52:00",
    "user_id": 172003,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 18:53:19",
    "user_id": 172072,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 18:54:52",
    "user_id": 199071,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 18:56:59",
    "user_id": 199737,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 18:57:18",
    "user_id": 199663,
    "lab": "HDFS\u539f\u7406\u53ca\u64cd\u4f5c",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 18:57:37",
    "user_id": 168318,
    "lab": "\u8def\u7531",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 18:59:02",
    "user_id": 199686,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 18:59:08",
    "user_id": 159200,
    "lab": "\u5faa\u73af\u4e0e\u5206\u652f",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 18:59:15",
    "user_id": 171682,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 18:59:24",
    "user_id": 176828,
    "lab": "Go\u8bed\u8a00\u4ecb\u7ecd",
    "course": "Go\u8bed\u8a00\u7f16\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 18:59:30",
    "user_id": 199527,
    "lab": "LNMP\u7cfb\u7edf\u5b89\u88c5",
    "course": "Linux Web\u8fd0\u7ef4\uff08Nginx\uff09\u5b9e\u6218 "
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 19:01:36",
    "user_id": 199739,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 19:01:59",
    "user_id": 199599,
    "lab": "MySQL\u57fa\u672c\u64cd\u4f5c",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 11,
    "created_at": "2016-05-02 19:02:55",
    "user_id": 199732,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 19:03:04",
    "user_id": 199722,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 19:04:06",
    "user_id": 170979,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 19:04:16",
    "user_id": 171682,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 19:09:34",
    "user_id": 48851,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 19:10:24",
    "user_id": 171682,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 104,
    "created_at": "2016-05-02 19:12:45",
    "user_id": 171177,
    "lab": "\u7528\u6237\u767b\u5f55",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 19:14:09",
    "user_id": 34691,
    "lab": "\u5b8c\u6210\u4e00\u4e2a\u7b80\u5355\u7684\u65f6\u95f4\u7247\u8f6e\u8f6c\u591a\u9053\u7a0b\u5e8f\u5185\u6838\u4ee3\u7801",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 19:14:39",
    "user_id": 190674,
    "lab": "makefile",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-02 19:15:13",
    "user_id": 175819,
    "lab": "\u6307\u4ee4\u7cfb\u7edf\u4e0e\u5bfb\u5740\u65b9\u5f0f",
    "course": "\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u90d1\u6653\u8587\u7f16\u8457\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 19:15:25",
    "user_id": 199742,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 19:15:54",
    "user_id": 199733,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 19:15:58",
    "user_id": 171959,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 63,
    "created_at": "2016-05-02 19:16:10",
    "user_id": 175137,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 19:16:45",
    "user_id": 58968,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 19:18:20",
    "user_id": 199743,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 19:19:42",
    "user_id": 170979,
    "lab": "\u64cd\u4f5c\u7cfb\u7edf\u7684\u5f15\u5bfc",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 19:19:52",
    "user_id": 52524,
    "lab": "Python\u8865\u5145",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 19:22:42",
    "user_id": 199527,
    "lab": "LNMP\u7cfb\u7edf\u5b89\u88c5",
    "course": "Linux Web\u8fd0\u7ef4\uff08Nginx\uff09\u5b9e\u6218 "
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 19:23:09",
    "user_id": 53927,
    "lab": "\u8ba4\u8bc6wxpython",
    "course": "\u7528Python\u505a2048\u6e38\u620f"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 19:23:51",
    "user_id": 175172,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 19:24:52",
    "user_id": 171964,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-02 19:24:54",
    "user_id": 197948,
    "lab": "Python\u6df1\u5165\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-02 19:25:11",
    "user_id": 174172,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 19:25:44",
    "user_id": 198200,
    "lab": "\u6253\u9020\u7f51\u9875\u7248\u300c\u5927\u767d\u300d- Baymax",
    "course": "\u7eaf CSS \u6253\u9020\u7f51\u9875\u7248\u300c\u5927\u767d\u300d"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 19:27:24",
    "user_id": 199737,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 19:32:12",
    "user_id": 198268,
    "lab": "C\u8bed\u8a00\u5b9e\u73b0ping\u7a0b\u5e8f",
    "course": "C\u8bed\u8a00\u5b9e\u73b0ping\u7a0b\u5e8f"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 19:33:31",
    "user_id": 171964,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 19:34:51",
    "user_id": 128791,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 19:35:06",
    "user_id": 199663,
    "lab": "Kaggle\u5165\u95e8",
    "course": "Kaggle\u5165\u95e8\uff1a\u6cf0\u5766\u5c3c\u514b\u53f7\u5e78\u5b58\u8005\u9879\u76ee"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 19:36:16",
    "user_id": 52835,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 66,
    "created_at": "2016-05-02 19:36:18",
    "user_id": 170831,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 19:36:48",
    "user_id": 199087,
    "lab": "Template\u548c\u52a8\u6001URL",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 19:37:45",
    "user_id": 171964,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 19:38:13",
    "user_id": 179764,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 19:39:19",
    "user_id": 199728,
    "lab": "Flask \u7684 Web \u8868\u5355",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-02 19:41:04",
    "user_id": 170810,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 19:42:25",
    "user_id": 173266,
    "lab": "MapReduce\u5e94\u7528\u6848\u4f8b",
    "course": "BTBU-\u7814\u7a76\u751f2015\u7ea7-Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 19:42:41",
    "user_id": 159783,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 19:43:21",
    "user_id": 172072,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 19:43:59",
    "user_id": 8376,
    "lab": "R\u8bed\u6cd5\u5b66\u4e60\uff08\u4e00\uff09",
    "course": "[\u7ef4\u62a4\u4e2d] R\u8bed\u8a00\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 19:45:28",
    "user_id": 81509,
    "lab": "\u5f15\u7528\u548c\u8f6c\u4e49",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 19:46:45",
    "user_id": 170780,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 19:48:47",
    "user_id": 171969,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-02 19:48:54",
    "user_id": 64633,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 57,
    "created_at": "2016-05-02 19:50:36",
    "user_id": 160099,
    "lab": "Collabtive\u7cfb\u7edf\u8de8\u7ad9\u8bf7\u6c42\u4f2a\u9020\u653b\u51fb\u5b9e\u9a8c",
    "course": "Collabtive\u7cfb\u7edf\u8de8\u7ad9\u8bf7\u6c42\u4f2a\u9020\u653b\u51fb\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 19:51:54",
    "user_id": 192069,
    "lab": "\u9879\u76ee\u4e94\uff1a\u6587\u5b57\u804a\u5929\u5ba4",
    "course": "Python \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 19:52:10",
    "user_id": 172003,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 60,
    "created_at": "2016-05-02 19:52:44",
    "user_id": 175172,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-02 19:53:38",
    "user_id": 170841,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 99,
    "created_at": "2016-05-02 19:54:19",
    "user_id": 166473,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 19:57:42",
    "user_id": 199751,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 19:59:16",
    "user_id": 85430,
    "lab": "Hello World",
    "course": "Android\u5e94\u7528\u5f00\u53d1\u57fa\u7840"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 20:00:14",
    "user_id": 53917,
    "lab": "\u57fa\u7840\u6b63\u5219\u8868\u8fbe\u5f0f\u4ecb\u7ecd\u4e0e\u7ec3\u4e60",
    "course": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 20:00:27",
    "user_id": 199703,
    "lab": "\u5f00\u542f\u795e\u5947\u7684Scala\u7f16\u7a0b\u4e4b\u65c5",
    "course": "Scala\u5f00\u53d1\u6559\u7a0b"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-02 20:02:39",
    "user_id": 175819,
    "lab": "\u6c47\u7f16\u8bed\u8a00\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u90d1\u6653\u8587\u7f16\u8457\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 20:02:44",
    "user_id": 172072,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 20:03:04",
    "user_id": 199722,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 20:04:38",
    "user_id": 197432,
    "lab": "Java \u7ee7\u627f",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 20:05:32",
    "user_id": 170813,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 20:05:42",
    "user_id": 53917,
    "lab": "grep\u547d\u4ee4\u4e0e\u6b63\u5219\u8868\u8fbe\u5f0f",
    "course": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 20:06:02",
    "user_id": 162448,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 20:06:55",
    "user_id": 101443,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 20:07:00",
    "user_id": 173414,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0b\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 20:07:46",
    "user_id": 167421,
    "lab": "Python\u6df1\u5165\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-02 20:08:48",
    "user_id": 199125,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 20:11:47",
    "user_id": 199728,
    "lab": "css\u5165\u95e8\u57fa\u7840",
    "course": "CSS\u901f\u6210\u6559\u7a0b"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 20:12:03",
    "user_id": 170811,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 75,
    "created_at": "2016-05-02 20:12:46",
    "user_id": 175180,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 20:15:24",
    "user_id": 172072,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-02 20:17:18",
    "user_id": 170713,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 20:17:34",
    "user_id": 153502,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 20:18:14",
    "user_id": 53917,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u8fd0\u7528\u4e4b sed\u5de5\u5177\u547d\u4ee4 ",
    "course": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 20:19:21",
    "user_id": 199757,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 20:19:58",
    "user_id": 168628,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u7684\u7ea6\u675f",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 20:20:28",
    "user_id": 172072,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 20:20:58",
    "user_id": 153502,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 20:21:15",
    "user_id": 171964,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 20:21:18",
    "user_id": 187256,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 20:21:30",
    "user_id": 167421,
    "lab": "Python\u8865\u5145",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 20:21:57",
    "user_id": 199753,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 20:22:09",
    "user_id": 170810,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 20:24:20",
    "user_id": 173414,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0b\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 20:24:48",
    "user_id": 199651,
    "lab": "Hadoop2.X 64\u4f4d\u7f16\u8bd1",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-02 20:25:21",
    "user_id": 199394,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 20:27:18",
    "user_id": 199570,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 20:27:56",
    "user_id": 171853,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 20:28:15",
    "user_id": 199755,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-02 20:28:24",
    "user_id": 173414,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0b\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 20:28:26",
    "user_id": 172072,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 20:28:37",
    "user_id": 167421,
    "lab": "Python\u6807\u51c6\u5e93\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 20:28:38",
    "user_id": 76108,
    "lab": "GCC\u7684\u4f7f\u7528",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 20:29:02",
    "user_id": 171964,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 20:29:33",
    "user_id": 199758,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 20:29:39",
    "user_id": 126198,
    "lab": "\u5206\u6790Linux\u5185\u6838\u521b\u5efa\u4e00\u4e2a\u65b0\u8fdb\u7a0b\u7684\u8fc7\u7a0b",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 20:30:23",
    "user_id": 170822,
    "lab": "\u5f00\u53d1\u73af\u5883\u548c\u5256\u6790\u7b2c\u4e00\u4e2a C \u8bed\u8a00",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 20:31:27",
    "user_id": 133579,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-02 20:32:14",
    "user_id": 168628,
    "lab": "\u57fa\u7840\u7bc7 - SELECT \u8bed\u53e5\u8be6\u89e3",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 20:33:02",
    "user_id": 126198,
    "lab": "Linux\u5185\u6838\u5982\u4f55\u88c5\u8f7d\u548c\u542f\u52a8\u4e00\u4e2a\u53ef\u6267\u884c\u7a0b\u5e8f",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 20:33:05",
    "user_id": 199757,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 20:33:14",
    "user_id": 199758,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 5,
    "created_at": "2016-05-02 20:33:26",
    "user_id": 32875,
    "lab": "CentOS 7\u5b9e\u9a8c\u73af\u5883",
    "course": "CentOS 7\u4f53\u9a8c\u8bfe"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 20:34:32",
    "user_id": 53917,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-02 20:36:02",
    "user_id": 191350,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-02 20:36:57",
    "user_id": 197865,
    "lab": "\u57fa\u4e8escrapy\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u57fa\u4e8escrapy\u722c\u866b\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6(python)"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-02 20:37:02",
    "user_id": 52524,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 20:37:06",
    "user_id": 127482,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e5d\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 20:37:18",
    "user_id": 164034,
    "lab": "lab0\uff1aCoding!",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u5b9e\u9a8c\uff0d\u57fa\u4e8euCore OS"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 20:37:19",
    "user_id": 126198,
    "lab": "\u5206\u6790Linux\u5185\u6838\u521b\u5efa\u4e00\u4e2a\u65b0\u8fdb\u7a0b\u7684\u8fc7\u7a0b",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 20:37:28",
    "user_id": 171985,
    "lab": "\u7b2c10-11\u5468\u8bfe\u5802\u5b9e\u9a8c-\u5b9e\u9a8c\u4e8c \u7ee7\u627f\u6027\u7684\u5b9e\u73b0\uff081-2\uff09",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 20:37:50",
    "user_id": 172072,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 20:38:43",
    "user_id": 194128,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 20:39:41",
    "user_id": 32753,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 20:39:51",
    "user_id": 162448,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 20:41:04",
    "user_id": 33739,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 20:41:25",
    "user_id": 172072,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 20:41:33",
    "user_id": 126198,
    "lab": "\u5206\u6790Linux\u5185\u6838\u521b\u5efa\u4e00\u4e2a\u65b0\u8fdb\u7a0b\u7684\u8fc7\u7a0b",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 20:41:47",
    "user_id": 199755,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 20:43:03",
    "user_id": 133579,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-02 20:43:09",
    "user_id": 170841,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 20:43:32",
    "user_id": 87934,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-02 20:43:42",
    "user_id": 198887,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 20:44:33",
    "user_id": 171969,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 20:45:34",
    "user_id": 171853,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-02 20:45:43",
    "user_id": 197948,
    "lab": "Python\u6df1\u5165\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 20:46:00",
    "user_id": 196366,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u7684\u7ea6\u675f",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 20:47:02",
    "user_id": 170974,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 20:47:12",
    "user_id": 199570,
    "lab": "\u5f00\u53d1\u73af\u5883\u548c\u5256\u6790\u7b2c\u4e00\u4e2a C \u8bed\u8a00",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-02 20:48:34",
    "user_id": 199758,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 20:48:55",
    "user_id": 199757,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 20:49:00",
    "user_id": 100863,
    "lab": "C \u8bed\u8a00\u6570\u7ec4",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 20:49:18",
    "user_id": 199755,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 20:49:18",
    "user_id": 196605,
    "lab": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668",
    "course": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 20:49:58",
    "user_id": 199663,
    "lab": "Kaggle\u5165\u95e8",
    "course": "Kaggle\u5165\u95e8\uff1a\u6cf0\u5766\u5c3c\u514b\u53f7\u5e78\u5b58\u8005\u9879\u76ee"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 20:51:07",
    "user_id": 127482,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u5341\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 20:51:46",
    "user_id": 172072,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 20:51:52",
    "user_id": 101443,
    "lab": "\u5f00\u53d1\u73af\u5883\u548c\u5256\u6790\u7b2c\u4e00\u4e2a C \u8bed\u8a00",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 20:52:51",
    "user_id": 171959,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 20:53:02",
    "user_id": 118813,
    "lab": "\u57fa\u4e8escrapy\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u57fa\u4e8escrapy\u722c\u866b\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6(python)"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 20:53:31",
    "user_id": 53917,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 20:53:59",
    "user_id": 52227,
    "lab": "\u5b9a\u65f6\u5668\uff0c\u6253\u70b9\u5668\uff0c\u5de5\u4f5c\u6c60\uff0c\u901f\u7387\u9650\u5236\uff0c\u539f\u5b50\u8ba1\u6570\u5668",
    "course": "Go by Example \u4e2d\u6587\u7248"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 20:55:21",
    "user_id": 84265,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 20:57:05",
    "user_id": 199709,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 78,
    "created_at": "2016-05-02 20:57:45",
    "user_id": 170762,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-02 20:58:48",
    "user_id": 171853,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 20:59:06",
    "user_id": 193248,
    "lab": "\u4e8b\u4ef6\u5904\u7406\u4e0e\u5185\u90e8\u901a\u4fe1",
    "course": "Android\u5e94\u7528\u5f00\u53d1\u57fa\u7840"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 20:59:37",
    "user_id": 171969,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 21:00:08",
    "user_id": 53927,
    "lab": "Django\uff08\u4e0a\uff09[\u5b9e\u9a8c\u8fc7\u671f\u5df2\u4e0b\u7ebf]",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 21:00:47",
    "user_id": 33739,
    "lab": "\u64cd\u4f5c\u7cfb\u7edf\u7684\u5f15\u5bfc",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:04:08",
    "user_id": 60135,
    "lab": "\u6392\u7248",
    "course": "Bootstrap3.0\u5165\u95e8\u5b66\u4e60"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 21:04:24",
    "user_id": 196366,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u7684\u7ea6\u675f",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-02 21:07:49",
    "user_id": 127482,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 21:08:24",
    "user_id": 135935,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:09:34",
    "user_id": 172125,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:09:36",
    "user_id": 64762,
    "lab": "\u5728Android Studio\u4e2d\u521b\u5efa\u9879\u76ee\u548c\u865a\u62df\u673a",
    "course": "Android Studio\u9879\u76ee\u521b\u5efa\u548c\u6a21\u62df\u5668\u914d\u7f6e"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 21:10:00",
    "user_id": 191690,
    "lab": "\u4ecb\u7ecd",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 87,
    "created_at": "2016-05-02 21:10:17",
    "user_id": 199394,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 21:10:19",
    "user_id": 194816,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:11:01",
    "user_id": 195375,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-02 21:11:32",
    "user_id": 170822,
    "lab": "\u5f00\u53d1\u73af\u5883\u548c\u5256\u6790\u7b2c\u4e00\u4e2a C \u8bed\u8a00",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:12:01",
    "user_id": 81509,
    "lab": "\u9000\u51fa\u548c\u9000\u51fa\u72b6\u6001\u7801",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:12:26",
    "user_id": 52227,
    "lab": "\u4e92\u65a5\u9501\uff0cGo\u72b6\u6001\u534f\u7a0b",
    "course": "Go by Example \u4e2d\u6587\u7248"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 21:12:35",
    "user_id": 173601,
    "lab": "\u6307\u9488\uff08\u4e00\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 57,
    "created_at": "2016-05-02 21:12:45",
    "user_id": 105763,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e5d\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 21:12:53",
    "user_id": 119886,
    "lab": "\u679a\u4e3e\u548c\u6cdb\u578b",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 21:12:54",
    "user_id": 199737,
    "lab": "\u5feb\u901f\u5b9e\u9a8c\u4e94\u5b50\u68cb",
    "course": "C\u8bed\u8a00\u5feb\u901f\u5b9e\u73b0\u4e94\u5b50\u68cb"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-02 21:13:06",
    "user_id": 172072,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:13:25",
    "user_id": 187256,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:14:50",
    "user_id": 198080,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:15:57",
    "user_id": 52835,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 21:16:36",
    "user_id": 171841,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:17:08",
    "user_id": 170957,
    "lab": "\u7cfb\u7edf\u8c03\u7528",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 21:17:11",
    "user_id": 170713,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:17:16",
    "user_id": 186294,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-02 21:17:21",
    "user_id": 157770,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 21:18:11",
    "user_id": 72538,
    "lab": "Hadoop\u4ecb\u7ecd\u53ca1.X\u4f2a\u5206\u5e03\u5f0f\u5b89\u88c5",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 21:18:41",
    "user_id": 199454,
    "lab": "Template\u548c\u52a8\u6001URL",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 21:19:21",
    "user_id": 190677,
    "lab": "python\u751f\u6210\u6c49\u5b57\u56fe\u7247\u5b57\u5e93",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011python\u751f\u6210\u6c49\u5b57\u56fe\u7247\u5b57\u5e93"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 21:20:42",
    "user_id": 52835,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:20:46",
    "user_id": 171969,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 21:21:02",
    "user_id": 106960,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 21:21:32",
    "user_id": 194816,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 63,
    "created_at": "2016-05-02 21:22:41",
    "user_id": 149790,
    "lab": "  HTML5\u4e24\u6b65\u5b9e\u73b0\u62fc\u56fe\u6e38\u620f",
    "course": "\u7f51\u9875\u7248\u62fc\u56fe\u6e38\u620f"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 21:23:08",
    "user_id": 165662,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 21:23:29",
    "user_id": 199651,
    "lab": "Hadoop2.X 64\u4f4d\u73af\u5883\u642d\u5efa",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:26:45",
    "user_id": 199125,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-02 21:28:44",
    "user_id": 199227,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:30:16",
    "user_id": 73064,
    "lab": "\u8bfe\u7a0b\u8bf4\u660e\u4e0e\u5b66\u4e60\u65b9\u6cd5",
    "course": "Go by Example \u4e2d\u6587\u7248"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 21:30:33",
    "user_id": 33739,
    "lab": "\u64cd\u4f5c\u7cfb\u7edf\u7684\u5f15\u5bfc",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 21:30:36",
    "user_id": 197961,
    "lab": "\u5f15\u7528\u548c\u8f6c\u4e49",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 21:31:49",
    "user_id": 81509,
    "lab": "\u6761\u4ef6\u5224\u65ad",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 2,
    "created_at": "2016-05-02 21:32:26",
    "user_id": 199779,
    "lab": "CentOS 7\u5b9e\u9a8c\u73af\u5883",
    "course": "CentOS 7\u4f53\u9a8c\u8bfe"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 21:32:36",
    "user_id": 199125,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 21:32:38",
    "user_id": 175174,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 21:33:22",
    "user_id": 197404,
    "lab": "HTML\u6587\u672c",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 21:34:38",
    "user_id": 171853,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 21:34:40",
    "user_id": 66074,
    "lab": "Python \u7834\u89e3\u9a8c\u8bc1\u7801",
    "course": "Python \u7834\u89e3\u9a8c\u8bc1\u7801"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 21:35:50",
    "user_id": 73064,
    "lab": "\u503c\uff0c\u53d8\u91cf\uff0c\u5e38\u91cf",
    "course": "Go by Example \u4e2d\u6587\u7248"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:36:01",
    "user_id": 42272,
    "lab": "\u6587\u4ef6IO\uff08\u4e00\uff09",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-02 21:37:03",
    "user_id": 135935,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 21:37:11",
    "user_id": 2685,
    "lab": "LAMP\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "LAMP\u90e8\u7f72\u53ca\u914d\u7f6e"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:37:12",
    "user_id": 170942,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 21:37:58",
    "user_id": 171961,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 21:38:06",
    "user_id": 199570,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e00\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 21:38:38",
    "user_id": 53917,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 21:39:02",
    "user_id": 194816,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 21:39:09",
    "user_id": 172003,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:39:29",
    "user_id": 170713,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 21:40:02",
    "user_id": 170979,
    "lab": "\u64cd\u4f5c\u7cfb\u7edf\u7684\u5f15\u5bfc",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 21:41:28",
    "user_id": 172125,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 21:41:29",
    "user_id": 199516,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:41:39",
    "user_id": 170841,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 57,
    "created_at": "2016-05-02 21:42:03",
    "user_id": 170942,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 21:42:26",
    "user_id": 199780,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 21:42:47",
    "user_id": 173414,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0b\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 21:43:31",
    "user_id": 195375,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e00\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:43:43",
    "user_id": 85085,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:44:00",
    "user_id": 73064,
    "lab": "For\u5faa\u73af\uff0cif/else\u5206\u652f\uff0c\u5206\u652f\u7ed3\u6784",
    "course": "Go by Example \u4e2d\u6587\u7248"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:44:23",
    "user_id": 49568,
    "lab": "\u9759\u6001\u6587\u4ef6\u53ca\u6e32\u67d3\u6a21\u7248",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 21:44:52",
    "user_id": 175172,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 21:45:46",
    "user_id": 168628,
    "lab": "\u57fa\u7840\u7bc7 - \u6570\u636e\u5e93\u53ca\u8868\u7684\u4fee\u6539\u548c\u5220\u9664",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:46:18",
    "user_id": 33739,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-02 21:46:19",
    "user_id": 198056,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:46:43",
    "user_id": 86495,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 21:46:48",
    "user_id": 199782,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 21:47:16",
    "user_id": 176880,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:47:24",
    "user_id": 198098,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:48:08",
    "user_id": 199218,
    "lab": "\u521b\u5efa\u4e91\u8bb0\u8d26\u9879\u76ee",
    "course": "\u57fa\u4e8edjango\u7684\u4e91\u8bb0\u8d26\u9879\u76ee\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 21:48:35",
    "user_id": 76108,
    "lab": "GCC\u7684\u4f7f\u7528",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 21:48:47",
    "user_id": 160153,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 21:49:30",
    "user_id": 73064,
    "lab": "\u6570\u7ec4\uff0c\u5207\u7247\uff0c\u5173\u8054\u6570\u7ec4\uff0cRange\u904d\u5386",
    "course": "Go by Example \u4e2d\u6587\u7248"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 21:49:32",
    "user_id": 85085,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:49:32",
    "user_id": 199480,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u7684\u7ea6\u675f",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:49:32",
    "user_id": 191690,
    "lab": "\u5907\u4efd\u7a0b\u5e8f-\u57fa\u7840",
    "course": "\u57fa\u4e8e Python \u7684\u6587\u4ef6\u5907\u4efd"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 21:51:05",
    "user_id": 175172,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-02 21:51:10",
    "user_id": 175174,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 21:51:49",
    "user_id": 167421,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-02 21:52:50",
    "user_id": 198098,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 21:55:28",
    "user_id": 76363,
    "lab": "\u8ddf\u8e2a\u5206\u6790Linux\u5185\u6838\u7684\u542f\u52a8\u8fc7\u7a0b",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 21:56:03",
    "user_id": 188318,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 21:59:11",
    "user_id": 165662,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 22:00:26",
    "user_id": 171841,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 22:00:50",
    "user_id": 139658,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e5d\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 22:02:40",
    "user_id": 167421,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 22:03:19",
    "user_id": 173414,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0b\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 22:03:56",
    "user_id": 161067,
    "lab": "\u57fa\u7840\u7ec4\u4ef6\uff081\uff09 - Activity",
    "course": "Android\u5e94\u7528\u5f00\u53d1\u57fa\u7840"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 22:04:15",
    "user_id": 199785,
    "lab": "\u8ba4\u8bc6J2SE",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 22:04:43",
    "user_id": 199765,
    "lab": "\u9879\u76ee\u4e00\uff1a\u7b80\u5355\u8ba1\u7b97\u5668",
    "course": "Python \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 22:04:44",
    "user_id": 199786,
    "lab": "\u6280\u672f\u6808\u4ecb\u7ecd",
    "course": "\u57fa\u4e8eFlask/RethinkDB\u5b9e\u73b0TODO List"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-02 22:05:06",
    "user_id": 116421,
    "lab": "\u4ecb\u7ecd",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 22:06:29",
    "user_id": 165662,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 22:06:42",
    "user_id": 110458,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 22:07:45",
    "user_id": 72538,
    "lab": "Hadoop2.X 64\u4f4d\u7f16\u8bd1",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 22:08:22",
    "user_id": 31169,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 22:08:42",
    "user_id": 182145,
    "lab": "lab0\uff1aCoding!",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u5b9e\u9a8c\uff0d\u57fa\u4e8euCore OS"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-02 22:08:47",
    "user_id": 199779,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 22:08:51",
    "user_id": 191690,
    "lab": "\u4ecb\u7ecd",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 22:08:55",
    "user_id": 76363,
    "lab": "\u8ddf\u8e2a\u5206\u6790Linux\u5185\u6838\u7684\u542f\u52a8\u8fc7\u7a0b",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 22:09:21",
    "user_id": 154096,
    "lab": "Hadoop\u4ecb\u7ecd\u53ca1.X\u4f2a\u5206\u5e03\u5f0f\u5b89\u88c5",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 22:09:29",
    "user_id": 199758,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 22:09:54",
    "user_id": 173716,
    "lab": "Kaggle\u5165\u95e8",
    "course": "Kaggle\u5165\u95e8\uff1a\u6cf0\u5766\u5c3c\u514b\u53f7\u5e78\u5b58\u8005\u9879\u76ee"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 22:10:54",
    "user_id": 199789,
    "lab": "PythonChallenge_1",
    "course": "\u5168\u9762\u89e3\u6790PythonChallenge"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 22:10:56",
    "user_id": 146602,
    "lab": "c\u8bed\u8a00\u5229\u7528epoll\u5b9e\u73b0\u804a\u5929\u5ba4",
    "course": "C\u8bed\u8a00\u5229\u7528epoll\u5b9e\u73b0\u9ad8\u5e76\u53d1\u804a\u5929\u5ba4"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 22:12:31",
    "user_id": 166285,
    "lab": "HBase\u4ecb\u7ecd\u3001\u5b89\u88c5\u4e0e\u5e94\u7528\u6848\u4f8b",
    "course": "BTBU-\u7814\u7a76\u751f2015\u7ea7-Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 5,
    "created_at": "2016-05-02 22:13:14",
    "user_id": 199788,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 22:14:30",
    "user_id": 53927,
    "lab": "\u57fa\u672c\u8bed\u6cd5",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 22:14:30",
    "user_id": 170789,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 22:14:46",
    "user_id": 199791,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 22:14:46",
    "user_id": 199780,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 22:14:51",
    "user_id": 187235,
    "lab": "\u64cd\u4f5c\u7b26",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 22:15:26",
    "user_id": 199790,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-02 22:15:48",
    "user_id": 199117,
    "lab": "\u7cfb\u7edf\u8c03\u7528",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 22:16:05",
    "user_id": 173716,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-02 22:17:05",
    "user_id": 196545,
    "lab": "\u6a21\u5757\u5316\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-02 22:19:08",
    "user_id": 176880,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 22:19:54",
    "user_id": 53927,
    "lab": "PHP\u7b80\u4ecb",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-02 22:20:03",
    "user_id": 170672,
    "lab": "Docker \u6982\u5ff5\u53ca\u57fa\u672c\u7528\u6cd5",
    "course": "\u52a8\u624b\u5b9e\u6218\u5b66Docker (15\u4e2a\u5b9e\u9a8c+54\u4e2a\u89c6\u9891)"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-02 22:20:47",
    "user_id": 155473,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-02 22:21:39",
    "user_id": 195705,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 22:21:49",
    "user_id": 195375,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e8c\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 75,
    "created_at": "2016-05-02 22:22:13",
    "user_id": 53699,
    "lab": "Python\u6807\u51c6\u5e93\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 84,
    "created_at": "2016-05-02 22:22:16",
    "user_id": 68077,
    "lab": "Laravel\u5b9e\u73b0\u7528\u6237\u6ce8\u518c\u767b\u5f55",
    "course": "Laravel\u5b9e\u73b0\u7528\u6237\u6ce8\u518c\u767b\u5f55"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 22:25:43",
    "user_id": 194470,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 22:25:54",
    "user_id": 190767,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 22:26:45",
    "user_id": 199758,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 22:26:45",
    "user_id": 23982,
    "lab": "C\u8bed\u8a00\u7248\u626b\u96f7\u6e38\u620f",
    "course": "C\u8bed\u8a00\u7248\u626b\u96f7\u6e38\u620f"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 22:27:39",
    "user_id": 171964,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 22:29:17",
    "user_id": 173716,
    "lab": "IP\u7f51\u9645\u534f\u8bae",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 22:30:21",
    "user_id": 199772,
    "lab": "lab0\uff1aCoding!",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u5b9e\u9a8c\uff0d\u57fa\u4e8euCore OS"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 22:30:44",
    "user_id": 185459,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 22:32:05",
    "user_id": 161067,
    "lab": "Android UI\u7f16\u7a0b",
    "course": "Android\u5e94\u7528\u5f00\u53d1\u57fa\u7840"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 22:32:18",
    "user_id": 199788,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-02 22:32:26",
    "user_id": 52835,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 22:34:03",
    "user_id": 198704,
    "lab": "HTML5 Canvas\u5c0f\u6e38\u620f",
    "course": "\u57fa\u4e8eHTML5 Canvas\u5b9e\u73b0\u5c0f\u6e38\u620f"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 22:34:42",
    "user_id": 196875,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 22:35:20",
    "user_id": 171853,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 22:36:09",
    "user_id": 176435,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 22:36:39",
    "user_id": 149790,
    "lab": "\u5728Android Studio\u4e2d\u521b\u5efa\u9879\u76ee\u548c\u865a\u62df\u673a",
    "course": "Android Studio\u9879\u76ee\u521b\u5efa\u548c\u6a21\u62df\u5668\u914d\u7f6e"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 22:36:56",
    "user_id": 160153,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-02 22:38:29",
    "user_id": 191690,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 72,
    "created_at": "2016-05-02 22:38:37",
    "user_id": 197798,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 22:40:46",
    "user_id": 199799,
    "lab": "Laravel\u5b9e\u73b0\u7528\u6237\u6ce8\u518c\u767b\u5f55",
    "course": "Laravel\u5b9e\u73b0\u7528\u6237\u6ce8\u518c\u767b\u5f55"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 22:41:57",
    "user_id": 171853,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-02 22:43:27",
    "user_id": 197012,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 22:44:11",
    "user_id": 179764,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 22:44:31",
    "user_id": 149790,
    "lab": "\u8ba4\u8bc6J2SE",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 22:45:34",
    "user_id": 190343,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-02 22:45:59",
    "user_id": 106808,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 22:46:29",
    "user_id": 199780,
    "lab": "Python\u6587\u672c\u89e3\u91ca\u5668",
    "course": "Python\u6587\u672c\u89e3\u6790\u5668"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-02 22:48:25",
    "user_id": 198704,
    "lab": "HTML5 Canvas\u5c0f\u6e38\u620f",
    "course": "\u57fa\u4e8eHTML5 Canvas\u5b9e\u73b0\u5c0f\u6e38\u620f"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 22:48:32",
    "user_id": 198635,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 22:49:03",
    "user_id": 107571,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 22:49:40",
    "user_id": 81509,
    "lab": "\u6761\u4ef6\u5224\u65ad",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 22:51:36",
    "user_id": 190767,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 22:51:41",
    "user_id": 2476,
    "lab": "\u5f00\u542f\u795e\u5947\u7684Scala\u7f16\u7a0b\u4e4b\u65c5",
    "course": "Scala\u5f00\u53d1\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 22:53:04",
    "user_id": 63281,
    "lab": "\u901a\u8fc7\u53cd\u6c47\u7f16\u4e00\u4e2a\u7b80\u5355\u7684C\u7a0b\u5e8f\uff0c\u5206\u6790\u6c47\u7f16\u4ee3\u7801\u7406\u89e3\u8ba1\u7b97\u673a\u662f\u5982\u4f55\u5de5\u4f5c\u7684",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 22:54:07",
    "user_id": 190677,
    "lab": "python\u751f\u6210\u6c49\u5b57\u56fe\u7247\u5b57\u5e93",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011python\u751f\u6210\u6c49\u5b57\u56fe\u7247\u5b57\u5e93"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-02 22:55:13",
    "user_id": 76108,
    "lab": "gdb\u4f7f\u7528",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 22:56:35",
    "user_id": 199802,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 22:57:26",
    "user_id": 116421,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 23:01:43",
    "user_id": 196366,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-02 23:01:57",
    "user_id": 170946,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 23:02:34",
    "user_id": 199758,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 23:03:51",
    "user_id": 170672,
    "lab": "Rails \u4ecb\u7ecd\u4e0e\u73af\u5883\u914d\u7f6e",
    "course": "Rails\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 23:03:54",
    "user_id": 199802,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 23:04:14",
    "user_id": 174348,
    "lab": "HTML5\u5b9e\u73b0\u64ad\u653e\u5668",
    "course": "[\u5df2\u4e0b\u7ebf] Ajax\u6b4c\u8bcd\u540c\u6b65\u64ad\u653e\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 23:04:22",
    "user_id": 81509,
    "lab": "\u64cd\u4f5c\u7b26",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 23:05:57",
    "user_id": 185535,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 23:09:45",
    "user_id": 199805,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-02 23:10:41",
    "user_id": 199813,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 23:16:47",
    "user_id": 170672,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 23:19:19",
    "user_id": 199814,
    "lab": "\u6587\u4ef6IO\uff08\u4e00\uff09",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 23:21:29",
    "user_id": 188119,
    "lab": "\u5927\u5c4f\u5e55\u4ecb\u7ecd\u3001\u9875\u9762\u6807\u9898\u3001\u7f29\u7565\u56fe\u3001\u8b66\u793a\u6846\u3001Well",
    "course": "Bootstrap3.0\u5165\u95e8\u5b66\u4e60"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 23:23:07",
    "user_id": 107571,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 23:23:25",
    "user_id": 170672,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 23:25:31",
    "user_id": 115805,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 23:27:59",
    "user_id": 79270,
    "lab": "Fragment\u7b80\u4ecb\u53ca\u57fa\u672c\u4f7f\u7528",
    "course": "Android\u5c0f\u6848\u4f8b - Fragment\uff08\u7247\u6bb5\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 23:28:07",
    "user_id": 176915,
    "lab": "HTML\u57fa\u7840\u6c47\u603b\u5b9e\u9a8c",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 5,
    "created_at": "2016-05-02 23:28:44",
    "user_id": 110824,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 23:29:14",
    "user_id": 178329,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 23:30:16",
    "user_id": 199817,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 23:30:36",
    "user_id": 166285,
    "lab": "HBase\u4ecb\u7ecd\u3001\u5b89\u88c5\u4e0e\u5e94\u7528\u6848\u4f8b",
    "course": "BTBU-\u7814\u7a76\u751f2015\u7ea7-Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 23:31:51",
    "user_id": 115805,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-02 23:32:16",
    "user_id": 187121,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 23:35:12",
    "user_id": 163952,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 23:35:50",
    "user_id": 155473,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 23:36:12",
    "user_id": 199715,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 23:37:43",
    "user_id": 199463,
    "lab": "\u57fa\u672c\u6982\u5ff5",
    "course": "\u6570\u636e\u7ed3\u6784(\u65b0\u7248)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 23:40:54",
    "user_id": 199758,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 78,
    "created_at": "2016-05-02 23:41:22",
    "user_id": 155473,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 23:41:40",
    "user_id": 163952,
    "lab": "\u94fe\u8def\u5c42\u4ecb\u7ecd",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 23:41:54",
    "user_id": 199755,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 23:41:57",
    "user_id": 160876,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 23:42:44",
    "user_id": 106808,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-02 23:47:39",
    "user_id": 162435,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-02 23:49:31",
    "user_id": 119886,
    "lab": "Swing\u5165\u95e8",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 23:50:06",
    "user_id": 163952,
    "lab": "IP\u7f51\u9645\u534f\u8bae",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-02 23:52:38",
    "user_id": 176435,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-02 23:52:50",
    "user_id": 199589,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-02 23:53:07",
    "user_id": 190677,
    "lab": "Python \u7834\u89e3\u9a8c\u8bc1\u7801",
    "course": "Python \u7834\u89e3\u9a8c\u8bc1\u7801"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-02 23:53:17",
    "user_id": 199463,
    "lab": "HTML\u6587\u672c",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-02 23:53:40",
    "user_id": 103452,
    "lab": "\u7b2c9\u5468\u8bfe\u5802\u5b9e\u9a8c-\u5b9e\u9a8c1",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 00:00:28",
    "user_id": 62403,
    "lab": "Go\u8bed\u8a00\u4ecb\u7ecd",
    "course": "Go\u8bed\u8a00\u7f16\u7a0b"
  },
  {
    "minutes": 2,
    "created_at": "2016-05-03 00:01:01",
    "user_id": 199817,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 00:01:03",
    "user_id": 176915,
    "lab": "PHP\u7b80\u4ecb",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 00:02:37",
    "user_id": 199758,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 00:05:37",
    "user_id": 199589,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 00:05:51",
    "user_id": 199463,
    "lab": "\u521d\u8bc6MySQL",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 00:10:27",
    "user_id": 199817,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 00:10:58",
    "user_id": 175129,
    "lab": "lab1\uff1a\u542f\u52a8\u64cd\u4f5c\u7cfb\u7edf",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u5b9e\u9a8c\uff0d\u57fa\u4e8euCore OS"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 00:11:18",
    "user_id": 173266,
    "lab": "HBase\u4ecb\u7ecd\u3001\u5b89\u88c5\u4e0e\u5e94\u7528\u6848\u4f8b",
    "course": "BTBU-\u7814\u7a76\u751f2015\u7ea7-Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 00:12:53",
    "user_id": 175417,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 00:14:00",
    "user_id": 139668,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 00:14:25",
    "user_id": 163952,
    "lab": "\u7f51\u7edc\u5c42\u5176\u5b83\u534f\u8bae",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 00:21:02",
    "user_id": 107571,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 00:22:30",
    "user_id": 76876,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 00:25:35",
    "user_id": 197799,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 00:25:55",
    "user_id": 199463,
    "lab": "LAMP\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "LAMP\u90e8\u7f72\u53ca\u914d\u7f6e"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 00:26:24",
    "user_id": 163952,
    "lab": "\u4f20\u8f93\u5c42\uff1aUDP\u534f\u8bae",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 00:27:26",
    "user_id": 176915,
    "lab": "\u6570\u636e\u7c7b\u578b\uff08\u4e00\uff09",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 00:28:30",
    "user_id": 170788,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 00:30:00",
    "user_id": 199589,
    "lab": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668",
    "course": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 00:33:21",
    "user_id": 197799,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 00:35:36",
    "user_id": 199463,
    "lab": "ThinkPHP\u5b89\u88c5\u4e0e\u914d\u7f6e",
    "course": "ThinkPHP\u6846\u67b6\u5b9e\u8df5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 00:41:19",
    "user_id": 163952,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 00:49:11",
    "user_id": 50300,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 00:51:12",
    "user_id": 199835,
    "lab": "\u591a\u5f20\u56fe\u7247\u62fc\u63a5\u4e0e\u5c42\u53e0",
    "course": "\u591a\u5f20\u56fe\u7247\u62fc\u63a5\u4e0e\u5c42\u53e0"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 00:52:49",
    "user_id": 199589,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 01:17:25",
    "user_id": 155473,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 01:21:27",
    "user_id": 133579,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 01:23:28",
    "user_id": 30088,
    "lab": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668",
    "course": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 01:26:16",
    "user_id": 160934,
    "lab": "\u7c7b\u548c\u5bf9\u8c61\uff08\u4e8c\uff09",
    "course": "Scala\u5f00\u53d1\u6559\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 01:40:20",
    "user_id": 133579,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 01:57:35",
    "user_id": 30287,
    "lab": "Nginx\u529f\u80fd\u63cf\u8ff0",
    "course": "Linux Web\u8fd0\u7ef4\uff08Nginx\uff09\u5b9e\u6218 "
  },
  {
    "minutes": 39,
    "created_at": "2016-05-03 02:02:09",
    "user_id": 133579,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 02:16:34",
    "user_id": 176778,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 02:29:39",
    "user_id": 189169,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 02:42:18",
    "user_id": 199144,
    "lab": "SciPy - \u79d1\u5b66\u8ba1\u7b97\u5e93\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 03:31:41",
    "user_id": 176435,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 03:34:41",
    "user_id": 198116,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-03 04:34:03",
    "user_id": 176435,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 05:03:24",
    "user_id": 183248,
    "lab": "\u4ecb\u7ecd",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 06:40:27",
    "user_id": 198635,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 06:44:04",
    "user_id": 199739,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 07:02:39",
    "user_id": 192178,
    "lab": "\u8def\u7531",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 07:07:23",
    "user_id": 176778,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-03 07:10:23",
    "user_id": 199614,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 07:19:48",
    "user_id": 192178,
    "lab": "\u9759\u6001\u6587\u4ef6\u53ca\u6e32\u67d3\u6a21\u7248",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 07:34:06",
    "user_id": 199839,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 07:41:13",
    "user_id": 192549,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 07:46:00",
    "user_id": 198889,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 07:47:43",
    "user_id": 199739,
    "lab": "\u8ba4\u8bc6wxpython",
    "course": "\u7528Python\u505a2048\u6e38\u620f"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 07:55:26",
    "user_id": 199418,
    "lab": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668",
    "course": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 08:02:58",
    "user_id": 60135,
    "lab": "Hello World",
    "course": "Android\u5e94\u7528\u5f00\u53d1\u57fa\u7840"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 08:06:17",
    "user_id": 181001,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 08:06:29",
    "user_id": 192549,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 08:07:56",
    "user_id": 177351,
    "lab": "\u6a21\u5757\u5316\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 08:09:26",
    "user_id": 1235,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 08:11:49",
    "user_id": 198635,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 08:13:29",
    "user_id": 181006,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 08:13:32",
    "user_id": 194951,
    "lab": "\u57fa\u4e8escrapy\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u57fa\u4e8escrapy\u722c\u866b\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6(python)"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 08:14:04",
    "user_id": 181040,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 08:14:19",
    "user_id": 198889,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 2,
    "created_at": "2016-05-03 08:16:56",
    "user_id": 199418,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 08:17:13",
    "user_id": 118124,
    "lab": "HTML\u57fa\u7840\u6c47\u603b\u5b9e\u9a8c",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 08:20:16",
    "user_id": 192549,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 08:20:57",
    "user_id": 191857,
    "lab": "\u57fa\u7840\u6b63\u5219\u8868\u8fbe\u5f0f\u4ecb\u7ecd\u4e0e\u7ec3\u4e60",
    "course": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 08:21:22",
    "user_id": 198635,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 08:21:45",
    "user_id": 199804,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 08:21:57",
    "user_id": 171962,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 08:22:21",
    "user_id": 194922,
    "lab": "\u521d\u8bc6HTML",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 08:25:08",
    "user_id": 146602,
    "lab": "c\u8bed\u8a00\u5229\u7528epoll\u5b9e\u73b0\u804a\u5929\u5ba4",
    "course": "C\u8bed\u8a00\u5229\u7528epoll\u5b9e\u73b0\u9ad8\u5e76\u53d1\u804a\u5929\u5ba4"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 08:26:33",
    "user_id": 192178,
    "lab": "Python\u6df1\u5165\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 08:26:50",
    "user_id": 180985,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 08:29:55",
    "user_id": 198007,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 08:30:41",
    "user_id": 199846,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 08:32:23",
    "user_id": 196366,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 08:32:46",
    "user_id": 32210,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 08:33:35",
    "user_id": 181041,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 08:34:15",
    "user_id": 198889,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 08:34:51",
    "user_id": 180986,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 08:35:02",
    "user_id": 180985,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-03 08:35:31",
    "user_id": 199610,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 08:36:27",
    "user_id": 181015,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 08:37:59",
    "user_id": 198889,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 08:40:08",
    "user_id": 187235,
    "lab": "\u53d8\u91cf\u91cd\u6e38",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 08:42:37",
    "user_id": 194922,
    "lab": "HTML\u6587\u672c",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 08:44:17",
    "user_id": 1235,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 08:44:45",
    "user_id": 180981,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 08:45:15",
    "user_id": 194593,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 08:45:33",
    "user_id": 187570,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 08:47:18",
    "user_id": 181008,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 08:47:40",
    "user_id": 189632,
    "lab": "PHP\u7b80\u4ecb",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 08:48:00",
    "user_id": 151608,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 08:48:24",
    "user_id": 32210,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 08:48:35",
    "user_id": 181000,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 63,
    "created_at": "2016-05-03 08:48:42",
    "user_id": 81425,
    "lab": "\u516c\u94a5\u52a0\u5bc6\u4e0ePKI",
    "course": "\u516c\u94a5\u52a0\u5bc6\u4e0ePKI\u5b9e\u9a8c"
  },
  {
    "minutes": 81,
    "created_at": "2016-05-03 08:49:20",
    "user_id": 195632,
    "lab": "\u6307\u9488\uff08\u4e8c\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 08:50:43",
    "user_id": 198889,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 08:52:20",
    "user_id": 144990,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e00\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 08:52:36",
    "user_id": 180995,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 08:53:45",
    "user_id": 192746,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 08:53:57",
    "user_id": 199847,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 08:54:18",
    "user_id": 187210,
    "lab": "MySQL\u51fd\u6570\u548c\u64cd\u4f5c\u7b26",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 08:54:25",
    "user_id": 175385,
    "lab": "MySQL\u57fa\u672c\u64cd\u4f5c",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 08:54:27",
    "user_id": 100970,
    "lab": "MySQL\u89e6\u53d1\u5668",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 08:56:33",
    "user_id": 195298,
    "lab": "php\u8fd0\u7b97\u7b26",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 08:58:12",
    "user_id": 180999,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 08:58:35",
    "user_id": 182237,
    "lab": "\u5f00\u53d1\u73af\u5883\u4ee5\u53ca\u9879\u76ee\u4e0eApp",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 08:58:53",
    "user_id": 144990,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e8c\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 08:59:39",
    "user_id": 96519,
    "lab": "\u57fa\u4e8escrapy\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u57fa\u4e8escrapy\u722c\u866b\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6(python)"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 09:01:00",
    "user_id": 47974,
    "lab": "c\u8bed\u8a00\u5229\u7528epoll\u5b9e\u73b0\u804a\u5929\u5ba4",
    "course": "C\u8bed\u8a00\u5229\u7528epoll\u5b9e\u73b0\u9ad8\u5e76\u53d1\u804a\u5929\u5ba4"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 09:01:30",
    "user_id": 1235,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 09:01:34",
    "user_id": 168981,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 09:01:53",
    "user_id": 100970,
    "lab": "Java\u5b9e\u73b0MD5\u6587\u4ef6\u6821\u9a8c",
    "course": "Java\u5b9e\u73b0MD5\u6587\u4ef6\u6821\u9a8c"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 09:03:32",
    "user_id": 111249,
    "lab": "\u4e00\u4e2a\u6700\u7b80\u5355\u7684 express \u5e94\u7528",
    "course": "Node.js\u5305\u6559\u4e0d\u5305\u4f1a"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 09:06:46",
    "user_id": 72662,
    "lab": "Java\u5b9e\u73b0\u8bb0\u4e8b\u672c",
    "course": "Java\u5b9e\u73b0\u8bb0\u4e8b\u672c"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 09:07:56",
    "user_id": 181040,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 09:08:25",
    "user_id": 181015,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 09:08:30",
    "user_id": 61232,
    "lab": "HTML\u8d85\u6587\u672c\uff08\u4e8c\uff09",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 09:08:59",
    "user_id": 79270,
    "lab": "Fragment\u7b80\u4ecb\u53ca\u57fa\u672c\u4f7f\u7528",
    "course": "Android\u5c0f\u6848\u4f8b - Fragment\uff08\u7247\u6bb5\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 09:09:24",
    "user_id": 188752,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 09:10:07",
    "user_id": 177351,
    "lab": "\u6a21\u5757\u5316\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 09:10:10",
    "user_id": 194922,
    "lab": "HTML\u8d85\u6587\u672c\uff08\u4e00\uff09",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 09:11:16",
    "user_id": 146698,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-03 09:11:22",
    "user_id": 182237,
    "lab": "Models\u548cAdmin\u4ee5\u53caViews\u548cURL",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 09:11:38",
    "user_id": 144990,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u56db\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 09:11:48",
    "user_id": 60135,
    "lab": "\u57fa\u7840\u7ec4\u4ef6\uff081\uff09 - Activity",
    "course": "Android\u5e94\u7528\u5f00\u53d1\u57fa\u7840"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 09:12:36",
    "user_id": 198635,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 09:14:17",
    "user_id": 180974,
    "lab": "Node.js\u6a21\u5757",
    "course": "Node.js \u6559\u7a0b"
  },
  {
    "minutes": 84,
    "created_at": "2016-05-03 09:15:15",
    "user_id": 199117,
    "lab": "\u7cfb\u7edf\u8c03\u7528",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 09:16:27",
    "user_id": 146698,
    "lab": "\u5f00\u53d1\u73af\u5883\u548c\u5256\u6790\u7b2c\u4e00\u4e2a C \u8bed\u8a00",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 09:16:44",
    "user_id": 72662,
    "lab": "\u7ed3\u5408\u4e03\u725b\u642d\u5efa\u4e2a\u4eba\u76f8\u518c ",
    "course": "\u7ed3\u5408\u4e03\u725b\u642d\u5efa\u4e2a\u4eba\u76f8\u518c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 09:16:55",
    "user_id": 192746,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 09:17:05",
    "user_id": 140305,
    "lab": "Flask\u9879\u76ee\u5b9e\u62181",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 09:17:08",
    "user_id": 195616,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 09:17:49",
    "user_id": 184713,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 09:18:15",
    "user_id": 94767,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e8c\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 09:18:19",
    "user_id": 190681,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 09:20:09",
    "user_id": 191690,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 09:20:12",
    "user_id": 156356,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 09:20:54",
    "user_id": 32210,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u7684\u7ea6\u675f",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 09:21:22",
    "user_id": 188212,
    "lab": "Python\u6807\u51c6\u5e93\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 09:22:00",
    "user_id": 181040,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 09:22:38",
    "user_id": 199659,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 09:23:01",
    "user_id": 173414,
    "lab": "SciPy - \u79d1\u5b66\u8ba1\u7b97\u5e93\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 09:23:23",
    "user_id": 188931,
    "lab": "css\u5165\u95e8\u57fa\u7840",
    "course": "CSS\u901f\u6210\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 09:23:42",
    "user_id": 127482,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 09:26:56",
    "user_id": 60135,
    "lab": "Hello World",
    "course": "Android\u5e94\u7528\u5f00\u53d1\u57fa\u7840"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 09:30:06",
    "user_id": 168981,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0b\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 09:30:22",
    "user_id": 86495,
    "lab": "\u6307\u9488\uff08\u4e00\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 09:30:45",
    "user_id": 181040,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 09:31:04",
    "user_id": 84557,
    "lab": "\u8d2a\u5403\u86c7\u4ecb\u7ecd",
    "course": "\u7ec8\u7aef\u8d2a\u5403\u86c7"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 09:31:44",
    "user_id": 199840,
    "lab": "\u516c\u94a5\u52a0\u5bc6\u4e0ePKI",
    "course": "\u516c\u94a5\u52a0\u5bc6\u4e0ePKI\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 09:32:09",
    "user_id": 184931,
    "lab": "\u6307\u9488\uff08\u4e8c\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 57,
    "created_at": "2016-05-03 09:32:20",
    "user_id": 2863,
    "lab": "Python\u6df1\u5165\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 09:32:39",
    "user_id": 196083,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 09:34:16",
    "user_id": 128327,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 09:34:48",
    "user_id": 193817,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 09:35:02",
    "user_id": 9473,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 09:35:11",
    "user_id": 195152,
    "lab": "ThinkPHP\u5b89\u88c5\u4e0e\u914d\u7f6e",
    "course": "ThinkPHP\u6846\u67b6\u5b9e\u8df5"
  },
  {
    "minutes": 72,
    "created_at": "2016-05-03 09:35:22",
    "user_id": 199394,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 09:36:01",
    "user_id": 158009,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-03 09:36:54",
    "user_id": 135552,
    "lab": "No2\u3001\u5b9e\u73b0\u529f\u80fd",
    "course": "\u81ea\u5df1\u7684Java\u7f16\u8f91\u5668"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 09:39:03",
    "user_id": 113542,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 09:39:53",
    "user_id": 191690,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 09:40:55",
    "user_id": 113273,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 09:41:06",
    "user_id": 108985,
    "lab": "\u8ba4\u8bc6J2SE",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 09:43:15",
    "user_id": 46343,
    "lab": "Kubernetes",
    "course": "\u52a8\u624b\u5b9e\u6218\u5b66Docker (15\u4e2a\u5b9e\u9a8c+54\u4e2a\u89c6\u9891)"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 09:45:29",
    "user_id": 144591,
    "lab": "\u5b9e\u9a8c\u4e00\uff1a\u5199\u4e00\u4e2ahello world\u5c0f\u7a0b\u5e8f",
    "course": "\u8f6f\u4ef6\u5de5\u7a0b(C\u7f16\u7801\u5b9e\u8df5\u7bc7)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 09:45:30",
    "user_id": 61232,
    "lab": "HTML\u57fa\u7840\u6c47\u603b\u5b9e\u9a8c",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 09:45:43",
    "user_id": 199011,
    "lab": "java.lang \u5305",
    "course": "JDK \u6838\u5fc3 API"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 09:45:45",
    "user_id": 170233,
    "lab": "\u9009\u62e9\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 09:46:04",
    "user_id": 197289,
    "lab": "Python\u6df1\u5165\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 09:46:17",
    "user_id": 146698,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e00\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 09:47:23",
    "user_id": 192746,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 09:47:33",
    "user_id": 97942,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 09:47:41",
    "user_id": 171962,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 09:48:15",
    "user_id": 82809,
    "lab": "\u5bc6\u94a5\u52a0\u89e3\u5bc6\u5b9e\u9a8c\uff08\u4e0a\uff09",
    "course": "\u5bc6\u94a5\u52a0\u89e3\u5bc6\u5b9e\u9a8c"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 09:48:31",
    "user_id": 171853,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 09:48:39",
    "user_id": 140305,
    "lab": "Flask\u9879\u76ee\u5b9e\u62182",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 09:49:03",
    "user_id": 175176,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 09:49:19",
    "user_id": 171963,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 09:49:26",
    "user_id": 189746,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e00\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 09:50:12",
    "user_id": 188752,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 09:50:50",
    "user_id": 171961,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 09:50:51",
    "user_id": 170724,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 09:51:03",
    "user_id": 199610,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 09:51:17",
    "user_id": 66806,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 09:52:34",
    "user_id": 170713,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 09:53:06",
    "user_id": 199624,
    "lab": "Models\u548cAdmin\u4ee5\u53caViews\u548cURL",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 09:53:15",
    "user_id": 175185,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 09:53:52",
    "user_id": 136235,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 09:53:52",
    "user_id": 171960,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 09:54:07",
    "user_id": 167421,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 09:54:14",
    "user_id": 171963,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 09:54:56",
    "user_id": 197569,
    "lab": "\u589e\u5f3a\u578b\u8868\u5355\u6807\u7b7e",
    "course": "HTML5\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-03 09:55:14",
    "user_id": 140305,
    "lab": "Flask\u9879\u76ee\u5b9e\u62183",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 09:55:26",
    "user_id": 199659,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 09:55:27",
    "user_id": 194951,
    "lab": "PythonChallenge_1",
    "course": "\u5168\u9762\u89e3\u6790PythonChallenge"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 09:55:27",
    "user_id": 192746,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 09:55:49",
    "user_id": 198439,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-03 09:56:18",
    "user_id": 86495,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 09:57:37",
    "user_id": 170730,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 09:57:52",
    "user_id": 111249,
    "lab": "\u4e00\u4e2a\u6700\u7b80\u5355\u7684 express \u5e94\u7528",
    "course": "Node.js\u5305\u6559\u4e0d\u5305\u4f1a"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 09:58:31",
    "user_id": 196083,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 09:58:46",
    "user_id": 196942,
    "lab": "LAMP\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "LAMP\u90e8\u7f72\u53ca\u914d\u7f6e"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 09:58:49",
    "user_id": 170779,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 09:59:51",
    "user_id": 198439,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 10:00:08",
    "user_id": 175137,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 10:00:57",
    "user_id": 51553,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 10:01:17",
    "user_id": 196771,
    "lab": "JavaScript \u7b80\u4ecb",
    "course": "Javascript\u57fa\u7840\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 10:01:35",
    "user_id": 188752,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 10:01:38",
    "user_id": 60135,
    "lab": "\u57fa\u7840\u7ec4\u4ef6\uff081\uff09 - Activity",
    "course": "Android\u5e94\u7528\u5f00\u53d1\u57fa\u7840"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 10:01:55",
    "user_id": 171778,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 57,
    "created_at": "2016-05-03 10:02:09",
    "user_id": 90735,
    "lab": "C \u8bed\u8a00\u6570\u7ec4",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 10:02:49",
    "user_id": 199856,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 10:04:52",
    "user_id": 175180,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 10:04:57",
    "user_id": 170775,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:05:15",
    "user_id": 179574,
    "lab": "PythonChallenge_1",
    "course": "\u5168\u9762\u89e3\u6790PythonChallenge"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 10:05:18",
    "user_id": 192828,
    "lab": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668",
    "course": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 10:05:25",
    "user_id": 108985,
    "lab": "\u5b57\u7b26\u4e32\u4e0e\u5305\u88c5\u7c7b",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:05:36",
    "user_id": 76059,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e00\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 10:05:42",
    "user_id": 61232,
    "lab": "JavaScript \u7b80\u4ecb",
    "course": "Javascript\u57fa\u7840\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 10:06:00",
    "user_id": 196083,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 10:06:03",
    "user_id": 171718,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 10:06:18",
    "user_id": 171001,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:06:58",
    "user_id": 188931,
    "lab": "css\u57fa\u672c\u6837\u5f0f\uff08\u4e00\uff09",
    "course": "CSS\u901f\u6210\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 10:08:16",
    "user_id": 51448,
    "lab": "\u6570\u636e\u5e93\u548c\u96c6\u5408\u57fa\u672c\u64cd\u4f5c",
    "course": "MongoDB \u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 10:09:07",
    "user_id": 81627,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 10:10:06",
    "user_id": 167421,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 72,
    "created_at": "2016-05-03 10:10:06",
    "user_id": 79515,
    "lab": "Kaggle\u5165\u95e8",
    "course": "Kaggle\u5165\u95e8\uff1a\u6cf0\u5766\u5c3c\u514b\u53f7\u5e78\u5b58\u8005\u9879\u76ee"
  },
  {
    "minutes": 60,
    "created_at": "2016-05-03 10:10:07",
    "user_id": 195663,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:10:25",
    "user_id": 76059,
    "lab": "Bash\u4ecb\u7ecd\u4e0e\u5165\u95e8",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 10:11:35",
    "user_id": 189427,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:12:03",
    "user_id": 97385,
    "lab": "\u7f16\u5199 DockerFile",
    "course": "\u52a8\u624b\u5b9e\u6218\u5b66Docker (15\u4e2a\u5b9e\u9a8c+54\u4e2a\u89c6\u9891)"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 10:13:18",
    "user_id": 154334,
    "lab": "\u67e5\u8be2\u3001\u7d22\u5f15\u4e0e\u805a\u5408",
    "course": "MongoDB \u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 7,
    "created_at": "2016-05-03 10:13:27",
    "user_id": 88131,
    "lab": "PHP\u7b80\u4ecb",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 10:14:08",
    "user_id": 175385,
    "lab": "MySQL\u5e38\u7528\u67e5\u8be2",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 10:14:18",
    "user_id": 22216,
    "lab": "\u6b22\u8fce\u6765\u5230 Flask \u7684\u4e16\u754c",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:14:21",
    "user_id": 135150,
    "lab": "Java  \u8fd0\u7b97\u7b26",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 10:14:44",
    "user_id": 195298,
    "lab": "Hadoop\u5355\u673a\u6a21\u5f0f\u5b89\u88c5",
    "course": "Hadoop\u90e8\u7f72\u53ca\u7ba1\u7406"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 10:15:30",
    "user_id": 128327,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 10:15:30",
    "user_id": 198056,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 10:16:19",
    "user_id": 170974,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 10:16:53",
    "user_id": 199863,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 10:16:57",
    "user_id": 108985,
    "lab": "\u96c6\u5408\u7c7b\u6846\u67b6",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 10:17:03",
    "user_id": 115138,
    "lab": "\u9879\u76ee\u516d\uff1aFlask\u4e2a\u4eba\u535a\u5ba2",
    "course": "Python \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 10:17:54",
    "user_id": 170789,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 10:18:06",
    "user_id": 149278,
    "lab": "Hadoop\u4ecb\u7ecd\u53ca1.X\u4f2a\u5206\u5e03\u5f0f\u5b89\u88c5",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 10:18:33",
    "user_id": 170957,
    "lab": "\u7cfb\u7edf\u8c03\u7528",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 10:19:32",
    "user_id": 199868,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 10:20:47",
    "user_id": 170965,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:21:29",
    "user_id": 188752,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 10:23:30",
    "user_id": 199870,
    "lab": "\u5b9e\u9a8c\u4e00\uff1a\u5199\u4e00\u4e2ahello world\u5c0f\u7a0b\u5e8f",
    "course": "\u8f6f\u4ef6\u5de5\u7a0b(C\u7f16\u7801\u5b9e\u8df5\u7bc7)"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 10:24:23",
    "user_id": 171990,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 10:24:35",
    "user_id": 148267,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-03 10:24:48",
    "user_id": 192178,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:25:12",
    "user_id": 186624,
    "lab": "linux\u7cfb\u7edf\u76d1\u63a7\u5e38\u7528\u547d\u4ee4\uff08\u4e00\uff09",
    "course": "Linux\u7cfb\u7edf\u76d1\u63a7\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:25:20",
    "user_id": 199011,
    "lab": "java.util \u5305",
    "course": "JDK \u6838\u5fc3 API"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 10:25:28",
    "user_id": 47673,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:25:34",
    "user_id": 185000,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 10:26:05",
    "user_id": 198635,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:26:14",
    "user_id": 198007,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 10:26:48",
    "user_id": 85073,
    "lab": "Python \u6d41\u7a0b\u63a7\u5236",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 10:27:39",
    "user_id": 188752,
    "lab": "Bash\u4ecb\u7ecd\u4e0e\u5165\u95e8",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 10:27:47",
    "user_id": 189746,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e8c\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 10:27:47",
    "user_id": 113542,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:28:09",
    "user_id": 27298,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 10:28:31",
    "user_id": 161790,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 10:29:25",
    "user_id": 171964,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 10:29:35",
    "user_id": 104645,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 10:29:52",
    "user_id": 172334,
    "lab": "PythonChallenge_1",
    "course": "\u5168\u9762\u89e3\u6790PythonChallenge"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:30:32",
    "user_id": 199864,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:31:12",
    "user_id": 171956,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 32,
    "created_at": "2016-05-03 10:31:12",
    "user_id": 199868,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 10:31:26",
    "user_id": 199873,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 10:32:08",
    "user_id": 111249,
    "lab": "\u5b66\u4e60\u4f7f\u7528\u5916\u90e8\u6a21\u5757",
    "course": "Node.js\u5305\u6559\u4e0d\u5305\u4f1a"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-03 10:32:20",
    "user_id": 146698,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e8c\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 10:32:49",
    "user_id": 76059,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e00\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 5,
    "created_at": "2016-05-03 10:32:59",
    "user_id": 146546,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:33:00",
    "user_id": 194951,
    "lab": "PythonChallenge_2",
    "course": "\u6bcf\u5929\u4e00\u4e2aPythonChallenge\u300a\u4efb\u52a1\u4e8c\u300b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 10:33:06",
    "user_id": 27298,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-03 10:33:21",
    "user_id": 108985,
    "lab": "\u6570\u5b66\u5de5\u5177",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 10:33:44",
    "user_id": 198416,
    "lab": "\u4e00\u4e2a\u6700\u7b80\u5355\u7684 express \u5e94\u7528",
    "course": "Node.js\u5305\u6559\u4e0d\u5305\u4f1a"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:34:14",
    "user_id": 199011,
    "lab": "Java \u96c6\u5408\u6846\u67b6",
    "course": "JDK \u6838\u5fc3 API"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 10:34:20",
    "user_id": 199843,
    "lab": "LAMP\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "LAMP\u90e8\u7f72\u53ca\u914d\u7f6e"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:35:18",
    "user_id": 171962,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 10:35:44",
    "user_id": 76471,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-03 10:36:01",
    "user_id": 170952,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 10:36:26",
    "user_id": 196766,
    "lab": "LAMP\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "LAMP\u90e8\u7f72\u53ca\u914d\u7f6e"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:36:40",
    "user_id": 188752,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 10:37:41",
    "user_id": 199875,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 10:38:17",
    "user_id": 112464,
    "lab": "\u5b9a\u65f6\u5668\uff0c\u6253\u70b9\u5668\uff0c\u5de5\u4f5c\u6c60\uff0c\u901f\u7387\u9650\u5236\uff0c\u539f\u5b50\u8ba1\u6570\u5668",
    "course": "Go by Example \u4e2d\u6587\u7248"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 10:38:38",
    "user_id": 171962,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:39:08",
    "user_id": 143361,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:39:32",
    "user_id": 199851,
    "lab": "Welcome to Django!",
    "course": "[\u5df2\u4e0b\u7ebf] Python Django Web\u6846\u67b6"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:40:16",
    "user_id": 190681,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:40:29",
    "user_id": 199877,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:41:03",
    "user_id": 171964,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 10:42:32",
    "user_id": 198969,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 10:42:55",
    "user_id": 47673,
    "lab": "\u57fa\u7840\u6b63\u5219\u8868\u8fbe\u5f0f\u4ecb\u7ecd\u4e0e\u7ec3\u4e60",
    "course": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:42:56",
    "user_id": 191690,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0b\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 10:43:00",
    "user_id": 199881,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 10:43:38",
    "user_id": 55107,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 10:43:39",
    "user_id": 196771,
    "lab": "\u4e8b\u4ef6",
    "course": "Javascript\u57fa\u7840\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 10:44:10",
    "user_id": 175174,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 10:44:38",
    "user_id": 122923,
    "lab": "\u5728Android Studio\u4e2d\u521b\u5efa\u9879\u76ee\u548c\u865a\u62df\u673a",
    "course": "Android Studio\u9879\u76ee\u521b\u5efa\u548c\u6a21\u62df\u5668\u914d\u7f6e"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 10:45:19",
    "user_id": 194818,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 10:45:29",
    "user_id": 199882,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:45:35",
    "user_id": 199883,
    "lab": "\u8ba4\u8bc6HTML5",
    "course": "HTML5\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 10:45:41",
    "user_id": 194641,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 10:46:28",
    "user_id": 174172,
    "lab": "Java \u8bed\u8a00\u57fa\u7840",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:46:44",
    "user_id": 61232,
    "lab": "JavaScript \u57fa\u672c\u8bed\u6cd5\uff08\u4e0b\uff09",
    "course": "Javascript\u57fa\u7840\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 10:48:06",
    "user_id": 199886,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 10:48:22",
    "user_id": 74737,
    "lab": "k-\u8fd1\u90bb\u7b97\u6cd5\u6539\u8fdb\u7ea6\u4f1a\u7f51\u7ad9\u914d\u5bf9\u6548\u679c",
    "course": "\u6df1\u5165\u5b66\u4e60\u300a\u673a\u5668\u5b66\u4e60\u5b9e\u6218\u300b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 10:48:44",
    "user_id": 171964,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 10:48:49",
    "user_id": 170713,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 10:49:13",
    "user_id": 84557,
    "lab": "\u8d2a\u5403\u86c7\u6838\u5fc3\u7f16\u7a0b",
    "course": "\u7ec8\u7aef\u8d2a\u5403\u86c7"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:49:15",
    "user_id": 199851,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 10:50:03",
    "user_id": 76471,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 10:50:15",
    "user_id": 199888,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 10:50:19",
    "user_id": 195298,
    "lab": "Hadoop\u4f2a\u5206\u5e03\u6a21\u5f0f\u914d\u7f6e\u90e8\u7f72",
    "course": "Hadoop\u90e8\u7f72\u53ca\u7ba1\u7406"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 10:50:33",
    "user_id": 195815,
    "lab": "\u88c5\u9970\u8005\u6a21\u5f0f",
    "course": "Java\u8fdb\u9636\u4e4b\u8bbe\u8ba1\u6a21\u5f0f"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 10:52:18",
    "user_id": 104645,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 10:52:27",
    "user_id": 199516,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 10:52:35",
    "user_id": 113542,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 10:53:11",
    "user_id": 61232,
    "lab": "\u4e8b\u4ef6",
    "course": "Javascript\u57fa\u7840\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 10:53:12",
    "user_id": 175315,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:53:28",
    "user_id": 199890,
    "lab": "git\u4ecb\u7ecd",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:53:30",
    "user_id": 88131,
    "lab": "\u6570\u636e\u7c7b\u578b\uff08\u4e00\uff09",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 10:54:20",
    "user_id": 189746,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 10:54:59",
    "user_id": 170974,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:56:36",
    "user_id": 47673,
    "lab": "\u6269\u5c55\u6b63\u5219\u8868\u8fbe\u5f0f",
    "course": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:57:23",
    "user_id": 167250,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 10:57:37",
    "user_id": 187226,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 10:58:27",
    "user_id": 199892,
    "lab": "Perl\u7b80\u5355\u4ecb\u7ecd",
    "course": "Perl\u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 10:58:40",
    "user_id": 158089,
    "lab": "\u9879\u76ee\u516d\uff1aFlask\u4e2a\u4eba\u535a\u5ba2",
    "course": "Python \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 10:59:48",
    "user_id": 199890,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 11:01:43",
    "user_id": 198997,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 11:02:45",
    "user_id": 128327,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 11:02:57",
    "user_id": 97942,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 11:03:45",
    "user_id": 197602,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-03 11:04:40",
    "user_id": 199516,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 11:04:47",
    "user_id": 187226,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:04:48",
    "user_id": 167250,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 11:05:02",
    "user_id": 143361,
    "lab": "Java \u63a7\u5236\u8bed\u53e5",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:05:36",
    "user_id": 71041,
    "lab": "Flask\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 11:05:37",
    "user_id": 148267,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 11:05:39",
    "user_id": 199895,
    "lab": "ShellShock \u653b\u51fb\u5b9e\u9a8c",
    "course": "ShellShock \u653b\u51fb\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:05:49",
    "user_id": 199610,
    "lab": "\u8ba4\u8bc6wxpython",
    "course": "\u7528Python\u505a2048\u6e38\u620f"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 11:06:56",
    "user_id": 170975,
    "lab": "Makefile\u4f7f\u7528",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 11:07:19",
    "user_id": 199900,
    "lab": "Go\u8bed\u8a00\u4ecb\u7ecd",
    "course": "Go\u8bed\u8a00\u7f16\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 11:08:08",
    "user_id": 140305,
    "lab": "Flask\u9879\u76ee\u5b9e\u62181",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 11:08:48",
    "user_id": 198566,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 11:09:09",
    "user_id": 109441,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-03 11:09:55",
    "user_id": 199480,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 11:10:17",
    "user_id": 166516,
    "lab": "Bash\u4ecb\u7ecd\u4e0e\u5165\u95e8",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 11:10:41",
    "user_id": 94767,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e8c\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 11:11:02",
    "user_id": 171964,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:11:02",
    "user_id": 172334,
    "lab": "PythonChallenge_2",
    "course": "\u6bcf\u5929\u4e00\u4e2aPythonChallenge\u300a\u4efb\u52a1\u4e8c\u300b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 11:11:10",
    "user_id": 167250,
    "lab": "JDBC \u6570\u636e\u7c7b\u578b\u4e0e\u4e8b\u52a1",
    "course": "JDBC \u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 11:12:30",
    "user_id": 199901,
    "lab": "PHP\u7559\u8a00\u672c",
    "course": "PHP \u5b9e\u73b0\u7559\u8a00\u672c"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 11:13:23",
    "user_id": 47673,
    "lab": "linux\u7cfb\u7edf\u76d1\u63a7\u5e38\u7528\u547d\u4ee4\uff08\u4e00\uff09",
    "course": "Linux\u7cfb\u7edf\u76d1\u63a7\u5b9e\u6218"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 11:13:25",
    "user_id": 153706,
    "lab": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668",
    "course": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 11:14:09",
    "user_id": 193335,
    "lab": "git\u4ecb\u7ecd",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 11:14:31",
    "user_id": 61232,
    "lab": "\u5bf9\u8c61",
    "course": "Javascript\u57fa\u7840\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 11:15:40",
    "user_id": 27101,
    "lab": "Redis\u7b80\u4ecb\u4e0e\u5b89\u88c5",
    "course": "Redis\u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:15:54",
    "user_id": 187226,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u7684\u7ea6\u675f",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 11:16:19",
    "user_id": 76021,
    "lab": "\u591a\u8fdb\u7a0b\uff08\u4e8c\uff09",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 11:16:25",
    "user_id": 198635,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0b\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 11:16:47",
    "user_id": 169257,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 11:17:35",
    "user_id": 189746,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:18:42",
    "user_id": 170968,
    "lab": "GCC\u7684\u4f7f\u7528",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 11:20:48",
    "user_id": 100970,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:20:51",
    "user_id": 199878,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 11:20:58",
    "user_id": 106447,
    "lab": "\u9879\u76ee\u4e00\uff1a\u7f51\u7ad9\u4fe1\u606f\u722c\u866b",
    "course": "Node.js \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:21:11",
    "user_id": 93896,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:21:23",
    "user_id": 135552,
    "lab": "No1\u3001\u5236\u4f5cGUI\u754c\u9762",
    "course": "\u81ea\u5df1\u7684Java\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:21:59",
    "user_id": 171841,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 11:22:00",
    "user_id": 171111,
    "lab": "Node.js\u8bfe\u7a0b\u4ecb\u7ecd",
    "course": "Node.js \u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 11:22:17",
    "user_id": 195873,
    "lab": "PythonChallenge_1",
    "course": "\u5168\u9762\u89e3\u6790PythonChallenge"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 11:22:25",
    "user_id": 46076,
    "lab": "\u57fa\u7840\u8bed\u6cd5",
    "course": "Ruby\u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 11:22:32",
    "user_id": 47673,
    "lab": "linux\u7cfb\u7edf\u76d1\u63a7\u5e38\u7528\u547d\u4ee4\uff08\u4e8c\uff09",
    "course": "Linux\u7cfb\u7edf\u76d1\u63a7\u5b9e\u6218"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 11:22:41",
    "user_id": 188070,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-03 11:22:44",
    "user_id": 192828,
    "lab": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668",
    "course": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 11:22:55",
    "user_id": 195729,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:23:12",
    "user_id": 196083,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:23:17",
    "user_id": 199875,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 11:23:48",
    "user_id": 186502,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:24:14",
    "user_id": 139642,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 11:24:15",
    "user_id": 167421,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 11:24:43",
    "user_id": 195298,
    "lab": "Hello World - Struts2",
    "course": "Struts\u6846\u67b6\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 11:25:06",
    "user_id": 151574,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 11:27:26",
    "user_id": 22216,
    "lab": "Flask \u6a21\u677f",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:28:31",
    "user_id": 199875,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:28:44",
    "user_id": 97385,
    "lab": "\u7f16\u5199 DockerFile",
    "course": "\u52a8\u624b\u5b9e\u6218\u5b66Docker (15\u4e2a\u5b9e\u9a8c+54\u4e2a\u89c6\u9891)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 11:29:48",
    "user_id": 187611,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 11:30:18",
    "user_id": 93896,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:30:31",
    "user_id": 171970,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 11:31:18",
    "user_id": 170775,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 11:31:29",
    "user_id": 196094,
    "lab": "PythonChallenge_1",
    "course": "\u5168\u9762\u89e3\u6790PythonChallenge"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:31:30",
    "user_id": 140305,
    "lab": "Flask\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 11:31:52",
    "user_id": 199707,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 11:31:58",
    "user_id": 175137,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 11:32:03",
    "user_id": 199907,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:32:16",
    "user_id": 199878,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 11:32:16",
    "user_id": 198566,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 11:32:22",
    "user_id": 169257,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 11:32:41",
    "user_id": 61232,
    "lab": "DOM",
    "course": "Javascript\u57fa\u7840\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:34:03",
    "user_id": 47673,
    "lab": " Linux \u76d1\u63a7\u7684 Python \u811a\u672c",
    "course": "Linux\u7cfb\u7edf\u76d1\u63a7\u5b9e\u6218"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 11:34:52",
    "user_id": 79515,
    "lab": "Kaggle\u5165\u95e8",
    "course": "Kaggle\u5165\u95e8\uff1a\u6cf0\u5766\u5c3c\u514b\u53f7\u5e78\u5b58\u8005\u9879\u76ee"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 11:34:53",
    "user_id": 27101,
    "lab": "Redis\u6570\u636e\u7c7b\u578b ",
    "course": "Redis\u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 11:35:10",
    "user_id": 199703,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 11:35:59",
    "user_id": 171111,
    "lab": "Node.js\u6a21\u5757",
    "course": "Node.js \u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:36:20",
    "user_id": 192528,
    "lab": "Flume\u4ecb\u7ecd\u4e0e\u5b89\u88c5",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:36:58",
    "user_id": 171718,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 81,
    "created_at": "2016-05-03 11:37:01",
    "user_id": 199659,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:37:19",
    "user_id": 151574,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 11:38:22",
    "user_id": 170760,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 11:38:29",
    "user_id": 199905,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e00\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:38:54",
    "user_id": 67281,
    "lab": "\u6570\u636e\u5e93\u548c\u96c6\u5408\u57fa\u672c\u64cd\u4f5c",
    "course": "MongoDB \u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:39:26",
    "user_id": 55107,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e00\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:39:34",
    "user_id": 173494,
    "lab": "HTML5 Canvas\u5c0f\u6e38\u620f",
    "course": "\u57fa\u4e8eHTML5 Canvas\u5b9e\u73b0\u5c0f\u6e38\u620f"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 11:39:36",
    "user_id": 195873,
    "lab": "\u57fa\u4e8escrapy\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u57fa\u4e8escrapy\u722c\u866b\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6(python)"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 11:39:43",
    "user_id": 104645,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 11:39:45",
    "user_id": 153706,
    "lab": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668",
    "course": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:40:30",
    "user_id": 151608,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:41:24",
    "user_id": 197602,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 11:43:06",
    "user_id": 191760,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 11:43:42",
    "user_id": 55107,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e8c\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:43:54",
    "user_id": 199873,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:44:12",
    "user_id": 181892,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:44:16",
    "user_id": 169257,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 11:44:56",
    "user_id": 108985,
    "lab": "Swing\u5165\u95e8",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:45:12",
    "user_id": 72662,
    "lab": "Java\u7248\u56fe\u5f62\u754c\u9762\u8ba1\u7b97\u5668",
    "course": "Java\u5f00\u53d1\u7b80\u5355\u7684\u8ba1\u7b97\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 11:45:36",
    "user_id": 11534,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 11:45:48",
    "user_id": 167250,
    "lab": "\u5b57\u7b26\u4e32\u4e0e\u5305\u88c5\u7c7b",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 11:50:15",
    "user_id": 199516,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 11:53:11",
    "user_id": 127966,
    "lab": "\u7ec4\u5408\u51fd\u6570\uff0c\u5b57\u7b26\u4e32\u51fd\u6570\uff0c\u5b57\u7b26\u4e32\u683c\u5f0f\u5316",
    "course": "Go by Example \u4e2d\u6587\u7248"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 11:54:13",
    "user_id": 140305,
    "lab": "Flask\u9879\u76ee\u5b9e\u62181",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:54:24",
    "user_id": 198416,
    "lab": "\u5b66\u4e60\u4f7f\u7528\u5916\u90e8\u6a21\u5757",
    "course": "Node.js\u5305\u6559\u4e0d\u5305\u4f1a"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 11:56:37",
    "user_id": 131712,
    "lab": "\u5f00\u542f\u795e\u5947\u7684Scala\u7f16\u7a0b\u4e4b\u65c5",
    "course": "Scala\u5f00\u53d1\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:57:19",
    "user_id": 199884,
    "lab": "PythonChallenge_1",
    "course": "\u5168\u9762\u89e3\u6790PythonChallenge"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 11:57:42",
    "user_id": 198972,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 11:58:18",
    "user_id": 79972,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 11:59:08",
    "user_id": 148055,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:59:16",
    "user_id": 14919,
    "lab": "Hello World - Struts2",
    "course": "Struts\u6846\u67b6\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 11:59:23",
    "user_id": 146698,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u8fd0\u7b97\u7b26\u548c\u6570\u636e\u8f6c\u6362",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 12:00:41",
    "user_id": 170968,
    "lab": "\u8bfe\u7a0b\u4ecb\u7ecd",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 12:00:53",
    "user_id": 173414,
    "lab": "SciPy - \u79d1\u5b66\u8ba1\u7b97\u5e93\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 12:00:58",
    "user_id": 100580,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 12:01:22",
    "user_id": 171958,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 12:01:47",
    "user_id": 111834,
    "lab": "Java\u548cWebSocket\u5f00\u53d1\u7f51\u9875\u804a\u5929\u5ba4",
    "course": "Java\u548cWebSocket\u5f00\u53d1\u7f51\u9875\u804a\u5929\u5ba4"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 12:05:49",
    "user_id": 104645,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 12:06:12",
    "user_id": 140305,
    "lab": "Flask\u9879\u76ee\u5b9e\u62182",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 12:06:36",
    "user_id": 55107,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e09\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 12:11:03",
    "user_id": 170968,
    "lab": "GCC\u7684\u4f7f\u7528",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 12:11:19",
    "user_id": 131712,
    "lab": "\u8d77\u6b65Scala",
    "course": "Scala\u5f00\u53d1\u6559\u7a0b"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 12:12:37",
    "user_id": 140305,
    "lab": "Flask\u9879\u76ee\u5b9e\u62183",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 12:12:46",
    "user_id": 199739,
    "lab": "\u8ba4\u8bc6wxpython",
    "course": "\u7528Python\u505a2048\u6e38\u620f"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 12:14:05",
    "user_id": 46041,
    "lab": "Python \u7834\u89e3\u9a8c\u8bc1\u7801",
    "course": "Python \u7834\u89e3\u9a8c\u8bc1\u7801"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 12:14:37",
    "user_id": 106447,
    "lab": "Meteor+React\u5b9e\u73b0Todo\u5e94\u7528",
    "course": "Meteor+React\u5b9e\u73b0Todo\u5e94\u7528"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 12:16:09",
    "user_id": 196366,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 12:16:20",
    "user_id": 195663,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 12:18:35",
    "user_id": 186093,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 12:20:18",
    "user_id": 192094,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-03 12:20:32",
    "user_id": 148055,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 12:20:36",
    "user_id": 195298,
    "lab": "\u753b\u51fa\u4e00\u4e9b\u6709\u8da3\u7684\u56fe\u6848",
    "course": "[\u5df2\u4e0b\u7ebf] C++\u4e09\u6bb5\u4ee3\u7801\u673a\u5668\u7ed8\u56fe"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 12:21:09",
    "user_id": 199739,
    "lab": "\u753b\u51e0\u4e2a\u5f62\u72b6",
    "course": "\u7528Python\u505a2048\u6e38\u620f"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 12:22:07",
    "user_id": 199916,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-03 12:22:34",
    "user_id": 121197,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 12:24:00",
    "user_id": 198056,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 12:27:44",
    "user_id": 118312,
    "lab": "\u94fe\u8def\u5c42\u4ecb\u7ecd",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 12:28:46",
    "user_id": 88282,
    "lab": "\u4ecb\u7ecd",
    "course": "[\u5df2\u4e0b\u7ebf] \u4f7f\u7528R\u8bed\u8a00\u8fdb\u884c\u6570\u636e\u6316\u6398"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 12:30:14",
    "user_id": 170968,
    "lab": "gdb\u4f7f\u7528",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 12:30:15",
    "user_id": 199881,
    "lab": "Flask \u7684 Web \u8868\u5355",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-03 12:31:44",
    "user_id": 170713,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 12:31:49",
    "user_id": 198439,
    "lab": "Bash\u4ecb\u7ecd\u4e0e\u5165\u95e8",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 12:33:48",
    "user_id": 171958,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 12:35:06",
    "user_id": 195298,
    "lab": "\u77e5\u8bc6\u50a8\u5907\uff0c\u7b80\u5355\u722c\u866b\u7684\u5fc5\u77e5\u5fc5\u4f1a\uff0c\u6838\u5fc3\u7ae0\u8282",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u57fa\u4e8epython\u7684\u7f51\u7edc\u5c0f\u722c\u866b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 12:36:10",
    "user_id": 113750,
    "lab": "LNMP\u7cfb\u7edf\u5b89\u88c5",
    "course": "Linux Web\u8fd0\u7ef4\uff08Nginx\uff09\u5b9e\u6218 "
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 12:36:18",
    "user_id": 141923,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 12:37:32",
    "user_id": 198336,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 12:39:07",
    "user_id": 170890,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 12:40:09",
    "user_id": 170968,
    "lab": "Makefile\u4f7f\u7528",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 12:42:12",
    "user_id": 199817,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 12:44:27",
    "user_id": 69570,
    "lab": "HTML5\u672c\u5730\u5b58\u50a8\u548c\u672c\u5730\u6570\u636e\u5e93",
    "course": "HTML5\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 12:46:20",
    "user_id": 191690,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0b\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 12:47:28",
    "user_id": 66074,
    "lab": "LNMP\u7cfb\u7edf\u5b89\u88c5",
    "course": "Linux Web\u8fd0\u7ef4\uff08Nginx\uff09\u5b9e\u6218 "
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 12:47:42",
    "user_id": 171961,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 63,
    "created_at": "2016-05-03 12:48:47",
    "user_id": 199925,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 12:49:20",
    "user_id": 170779,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 12:49:39",
    "user_id": 199922,
    "lab": "\u8ba4\u8bc6jQuery",
    "course": "jQuery\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 12:49:47",
    "user_id": 170968,
    "lab": "\u6587\u4ef6IO\uff08\u4e00\uff09",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 12:50:40",
    "user_id": 199926,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 12:52:45",
    "user_id": 15451,
    "lab": "Bash\u4e2d\u7684\u7279\u6b8a\u5b57\u7b26\uff08\u4e0a\uff09",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 12:55:15",
    "user_id": 80243,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 12:58:56",
    "user_id": 72538,
    "lab": "Hadoop2.X 64\u4f4d\u73af\u5883\u642d\u5efa",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:01:27",
    "user_id": 179940,
    "lab": "\u7b2c9\u5468\u8bfe\u5802\u5b9e\u9a8c-\u5b9e\u9a8c1",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 13:02:11",
    "user_id": 118312,
    "lab": "IP\u7f51\u9645\u534f\u8bae",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 13:02:15",
    "user_id": 188212,
    "lab": "Django\uff08\u4e0a\uff09[\u5b9e\u9a8c\u8fc7\u671f\u5df2\u4e0b\u7ebf]",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 13:03:06",
    "user_id": 197912,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 13:03:11",
    "user_id": 146546,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 13:08:19",
    "user_id": 196455,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 13:08:30",
    "user_id": 66074,
    "lab": "nginx\u8fdb\u7a0b\u4e0e\u6a21\u5757",
    "course": "Linux Web\u8fd0\u7ef4\uff08Nginx\uff09\u5b9e\u6218 "
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 13:10:09",
    "user_id": 198889,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:10:59",
    "user_id": 199589,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 13:11:03",
    "user_id": 199703,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:11:34",
    "user_id": 185076,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 13:12:20",
    "user_id": 156356,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-03 13:12:37",
    "user_id": 191690,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0b\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 5,
    "created_at": "2016-05-03 13:13:59",
    "user_id": 199868,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 13:14:32",
    "user_id": 199589,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 13:14:35",
    "user_id": 173414,
    "lab": "SciPy - \u79d1\u5b66\u8ba1\u7b97\u5e93\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 13:15:39",
    "user_id": 199907,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 13:17:06",
    "user_id": 170968,
    "lab": "\u6587\u4ef6IO\uff08\u4e8c\uff09",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 13:17:49",
    "user_id": 172334,
    "lab": "PythonChallenge_3",
    "course": "\u6bcf\u5929\u4e00\u4e2aPythonChallenge\u300a\u4efb\u52a1\u4e09\u300b"
  },
  {
    "minutes": 75,
    "created_at": "2016-05-03 13:19:37",
    "user_id": 27420,
    "lab": "c\u8bed\u8a00\u5229\u7528epoll\u5b9e\u73b0\u804a\u5929\u5ba4",
    "course": "C\u8bed\u8a00\u5229\u7528epoll\u5b9e\u73b0\u9ad8\u5e76\u53d1\u804a\u5929\u5ba4"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:20:26",
    "user_id": 190677,
    "lab": "Python \u7834\u89e3\u9a8c\u8bc1\u7801",
    "course": "Python \u7834\u89e3\u9a8c\u8bc1\u7801"
  },
  {
    "minutes": 57,
    "created_at": "2016-05-03 13:20:47",
    "user_id": 199931,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 13:20:51",
    "user_id": 199868,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 13:20:59",
    "user_id": 2863,
    "lab": "Python\u8865\u5145",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 13:22:48",
    "user_id": 197912,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 13:24:59",
    "user_id": 182621,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 13:25:01",
    "user_id": 196165,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 13:26:13",
    "user_id": 197366,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 13:26:26",
    "user_id": 190674,
    "lab": "makefile",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:26:50",
    "user_id": 199930,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 13:27:18",
    "user_id": 199659,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 13:28:03",
    "user_id": 170713,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 13:28:41",
    "user_id": 72538,
    "lab": "HDFS\u539f\u7406\u53ca\u64cd\u4f5c",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:30:10",
    "user_id": 177781,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 13:30:15",
    "user_id": 146652,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 13:30:27",
    "user_id": 198889,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u7684\u7ea6\u675f",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 13:30:50",
    "user_id": 199868,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:31:23",
    "user_id": 192600,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:32:34",
    "user_id": 196455,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 13:32:58",
    "user_id": 61232,
    "lab": "JavaScript \u5b9e\u73b0\u60c5\u4eba\u8282\u73ab\u7470",
    "course": "\u57fa\u4e8e JavaScript \u5b9e\u73b0\u73ab\u7470\u82b1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 13:33:05",
    "user_id": 191760,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:35:06",
    "user_id": 131199,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:35:09",
    "user_id": 190677,
    "lab": "\u8bfe\u7a0b\u57fa\u7840\u5305\uff08\u4e0a\uff09\uff0d\u5355\u9009\u7c7b\u578b\u8868\u5355\u81ea\u52a8\u63d0\u4ea4",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python\u81ea\u52a8\u586b\u95ee\u5377\u661f"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 13:37:09",
    "user_id": 199589,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:37:24",
    "user_id": 177781,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 13:39:14",
    "user_id": 199670,
    "lab": "Python\u6df1\u5165\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 13:39:18",
    "user_id": 109441,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 13:39:19",
    "user_id": 94767,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e8c\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 13:39:26",
    "user_id": 180533,
    "lab": "Java \u7c7b\u4e0e\u5bf9\u8c61",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 13:40:13",
    "user_id": 195780,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 13:41:51",
    "user_id": 80485,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:42:11",
    "user_id": 199941,
    "lab": "\u4ecb\u7ecd",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 13:42:55",
    "user_id": 189152,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 13:43:06",
    "user_id": 196138,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e09\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 13:43:43",
    "user_id": 154366,
    "lab": "\u6570\u636e\u5e93\u548c\u96c6\u5408\u57fa\u672c\u64cd\u4f5c",
    "course": "MongoDB \u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:44:49",
    "user_id": 131199,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 13:45:04",
    "user_id": 140305,
    "lab": "Flask\u9879\u76ee\u5b9e\u62183",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 13:45:15",
    "user_id": 45702,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:46:06",
    "user_id": 148356,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 13:46:57",
    "user_id": 21991,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:47:12",
    "user_id": 199589,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-03 13:47:13",
    "user_id": 53699,
    "lab": "Python\u6807\u51c6\u5e93\uff08\u4e2d\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:47:23",
    "user_id": 199946,
    "lab": "\u8ba4\u8bc6HTML5",
    "course": "HTML5\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 13:48:07",
    "user_id": 76059,
    "lab": "linux\u7cfb\u7edf\u76d1\u63a7\u5e38\u7528\u547d\u4ee4\uff08\u4e00\uff09",
    "course": "Linux\u7cfb\u7edf\u76d1\u63a7\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:48:12",
    "user_id": 170890,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 13:48:16",
    "user_id": 149056,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 13:48:44",
    "user_id": 46343,
    "lab": "Kubernetes",
    "course": "\u52a8\u624b\u5b9e\u6218\u5b66Docker (15\u4e2a\u5b9e\u9a8c+54\u4e2a\u89c6\u9891)"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 13:50:54",
    "user_id": 182091,
    "lab": "\u8d70\u5411\u5206\u652f",
    "course": "[\u79c1\u6709]\u8fbd\u5b81\u5e08\u8303\u5927\u5b66\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u5b9e\u9a8c\u8bfe\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 13:51:11",
    "user_id": 166516,
    "lab": "Bash\u4e2d\u7684\u7279\u6b8a\u5b57\u7b26\uff08\u4e0a\uff09",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:51:17",
    "user_id": 199589,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:51:33",
    "user_id": 177781,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 13:51:47",
    "user_id": 189427,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:53:01",
    "user_id": 199948,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-03 13:53:03",
    "user_id": 146698,
    "lab": "\u9009\u62e9\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 13:53:18",
    "user_id": 79515,
    "lab": "TensorFlow \u5b9e\u9a8c\u73af\u5883\u642d\u5efa",
    "course": "TensorFlow \u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 13:54:01",
    "user_id": 199949,
    "lab": "\u6570\u636e\u5e93\u548c\u96c6\u5408\u57fa\u672c\u64cd\u4f5c",
    "course": "MongoDB \u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:54:05",
    "user_id": 170890,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 13:54:42",
    "user_id": 16806,
    "lab": "\u5f15\u7528\u548c\u8f6c\u4e49",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 13:54:57",
    "user_id": 84624,
    "lab": "Bash\u4e2d\u7684\u7279\u6b8a\u5b57\u7b26\uff08\u4e0a\uff09",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 13:55:31",
    "user_id": 199589,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:56:20",
    "user_id": 175186,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 13:56:44",
    "user_id": 58677,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 13:57:04",
    "user_id": 193213,
    "lab": "Java\u5b9e\u73b0\u8bb0\u4e8b\u672c",
    "course": "Java\u5b9e\u73b0\u8bb0\u4e8b\u672c"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 13:57:46",
    "user_id": 199011,
    "lab": "Hadoop\u4ecb\u7ecd\u53ca1.X\u4f2a\u5206\u5e03\u5f0f\u5b89\u88c5",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:57:49",
    "user_id": 175385,
    "lab": "MySQL\u7684\u8bed\u8a00\u7ed3\u6784",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 13:58:31",
    "user_id": 199875,
    "lab": "\u8bfe\u7a0b\u57fa\u7840\u5305\uff08\u4e0a\uff09\uff0d\u5355\u9009\u7c7b\u578b\u8868\u5355\u81ea\u52a8\u63d0\u4ea4",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python\u81ea\u52a8\u586b\u95ee\u5377\u661f"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:58:49",
    "user_id": 177781,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:58:54",
    "user_id": 197101,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e00\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 13:58:58",
    "user_id": 199892,
    "lab": "Perl\u7b80\u5355\u4ecb\u7ecd",
    "course": "Perl\u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-03 13:59:08",
    "user_id": 189152,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 13:59:52",
    "user_id": 199943,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 13:59:59",
    "user_id": 76471,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:01:20",
    "user_id": 199949,
    "lab": "\u6570\u636e\u67e5\u8be2",
    "course": "MongoDB \u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 14:01:50",
    "user_id": 171111,
    "lab": "Node.js\u6a21\u5757",
    "course": "Node.js \u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:02:20",
    "user_id": 199953,
    "lab": "\u5b9e\u9a8c\u4e00\uff1a\u5199\u4e00\u4e2ahello world\u5c0f\u7a0b\u5e8f",
    "course": "\u8f6f\u4ef6\u5de5\u7a0b(C\u7f16\u7801\u5b9e\u8df5\u7bc7)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:02:25",
    "user_id": 175186,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:02:26",
    "user_id": 144591,
    "lab": "C\u8bed\u8a00\u5b9e\u73b0ping\u7a0b\u5e8f",
    "course": "C\u8bed\u8a00\u5b9e\u73b0ping\u7a0b\u5e8f"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 14:02:28",
    "user_id": 116727,
    "lab": "Python\u6807\u51c6\u5e93\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 14:03:04",
    "user_id": 79972,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:03:05",
    "user_id": 139870,
    "lab": "\u5f00\u53d1\u73af\u5883\u4ee5\u53ca\u9879\u76ee\u4e0eApp",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:03:38",
    "user_id": 135150,
    "lab": "Java \u7c7b\u4e0e\u5bf9\u8c61",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 14:03:47",
    "user_id": 199930,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 14:03:57",
    "user_id": 198889,
    "lab": "\u57fa\u7840\u7bc7 - SELECT \u8bed\u53e5\u8be6\u89e3",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 14:04:17",
    "user_id": 199956,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:04:26",
    "user_id": 118124,
    "lab": "HTML\u57fa\u7840\u6c47\u603b\u5b9e\u9a8c",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 14:04:28",
    "user_id": 109441,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:04:37",
    "user_id": 199954,
    "lab": "PHP\u7b80\u4ecb",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 11,
    "created_at": "2016-05-03 14:05:50",
    "user_id": 199950,
    "lab": "HBase\u7b80\u4ecb",
    "course": "HBASE\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 14:06:04",
    "user_id": 199960,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 14:06:07",
    "user_id": 198439,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:07:25",
    "user_id": 197101,
    "lab": "LAMP\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "LAMP\u90e8\u7f72\u53ca\u914d\u7f6e"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:08:40",
    "user_id": 199953,
    "lab": "\u5b9e\u9a8c\u4e00\uff1a\u5199\u4e00\u4e2ahello world\u5c0f\u7a0b\u5e8f",
    "course": "\u8f6f\u4ef6\u5de5\u7a0b(C\u7f16\u7801\u5b9e\u8df5\u7bc7)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:09:06",
    "user_id": 146194,
    "lab": "Bash\u4ecb\u7ecd\u4e0e\u5165\u95e8",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 2,
    "created_at": "2016-05-03 14:09:56",
    "user_id": 191690,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 14:10:34",
    "user_id": 196138,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u56db\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:10:44",
    "user_id": 193335,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 14:10:55",
    "user_id": 199868,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 14:10:56",
    "user_id": 171990,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 72,
    "created_at": "2016-05-03 14:11:51",
    "user_id": 91969,
    "lab": "Java \u63a7\u5236\u8bed\u53e5",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 14:12:36",
    "user_id": 197912,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:13:09",
    "user_id": 199962,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:14:04",
    "user_id": 191690,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0b\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 14:14:34",
    "user_id": 22216,
    "lab": "\u6b22\u8fce\u6765\u5230 Flask \u7684\u4e16\u754c",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 14:14:46",
    "user_id": 199892,
    "lab": "Perl\u7b80\u5355\u4ecb\u7ecd",
    "course": "Perl\u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:14:58",
    "user_id": 101033,
    "lab": "Hadoop\u4ecb\u7ecd\u53ca1.X\u4f2a\u5206\u5e03\u5f0f\u5b89\u88c5",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 14:15:22",
    "user_id": 189427,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:16:43",
    "user_id": 197101,
    "lab": "cookie\u57fa\u7840\u548c\u5e94\u7528",
    "course": "PHP\u4f1a\u8bdd\u63a7\u5236"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:17:47",
    "user_id": 180533,
    "lab": "Java \u5c01\u88c5",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:18:13",
    "user_id": 175186,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:18:38",
    "user_id": 149056,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:18:54",
    "user_id": 199959,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:18:55",
    "user_id": 61668,
    "lab": "\u521b\u5efa\u578b\u6a21\u5f0f\uff1a\u5355\u4f8b\u6a21\u5f0f\u548c\u5de5\u5382\u6a21\u5f0f\u5bb6\u65cf",
    "course": "Python\u7248\u8bbe\u8ba1\u6a21\u5f0f\u5b9e\u8df5"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:19:05",
    "user_id": 199011,
    "lab": "\u521d\u8bc6MySQL",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:19:31",
    "user_id": 170890,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:19:50",
    "user_id": 154366,
    "lab": "\u6570\u636e\u67e5\u8be2",
    "course": "MongoDB \u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 14:20:18",
    "user_id": 199394,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:20:33",
    "user_id": 195298,
    "lab": "\u89c2\u5bdf\u8005\u6a21\u5f0f",
    "course": "Java\u8fdb\u9636\u4e4b\u8bbe\u8ba1\u6a21\u5f0f"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:20:50",
    "user_id": 154644,
    "lab": "\u8ba4\u8bc6J2SE",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:21:00",
    "user_id": 146194,
    "lab": "\u6982\u8ff0",
    "course": "\u5b9e\u7528Linux Shell\u7f16\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 14:21:11",
    "user_id": 171111,
    "lab": "Node.js Events\u6a21\u5757",
    "course": "Node.js \u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 14:21:28",
    "user_id": 199965,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:22:02",
    "user_id": 155044,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 14:22:02",
    "user_id": 196766,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:22:08",
    "user_id": 199930,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:22:13",
    "user_id": 177781,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:22:41",
    "user_id": 149789,
    "lab": "\u8fdb\u7a0b\u8fd0\u884c\u8f68\u8ff9\u7684\u8ddf\u8e2a\u4e0e\u7edf\u8ba1",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 14:23:34",
    "user_id": 199516,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:23:46",
    "user_id": 192528,
    "lab": "Flume\u4ecb\u7ecd\u4e0e\u5b89\u88c5",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 14:23:57",
    "user_id": 106447,
    "lab": "\u9879\u76ee\u4e00\uff1a\u7f51\u7ad9\u4fe1\u606f\u722c\u866b",
    "course": "Node.js \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:24:23",
    "user_id": 157173,
    "lab": "\u5728Android Studio\u4e2d\u521b\u5efa\u9879\u76ee\u548c\u865a\u62df\u673a",
    "course": "Android Studio\u9879\u76ee\u521b\u5efa\u548c\u6a21\u62df\u5668\u914d\u7f6e"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 14:24:23",
    "user_id": 199863,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 14:24:31",
    "user_id": 194438,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e00\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-03 14:24:52",
    "user_id": 88282,
    "lab": "\u6570\u636e\u63a2\u7d22",
    "course": "[\u5df2\u4e0b\u7ebf] \u4f7f\u7528R\u8bed\u8a00\u8fdb\u884c\u6570\u636e\u6316\u6398"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:25:04",
    "user_id": 199950,
    "lab": "HBase\u5b89\u88c5\u914d\u7f6e",
    "course": "HBASE\u6559\u7a0b"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-03 14:25:53",
    "user_id": 195661,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 14:25:56",
    "user_id": 122923,
    "lab": "\u5728Android Studio\u4e2d\u521b\u5efa\u9879\u76ee\u548c\u865a\u62df\u673a",
    "course": "Android Studio\u9879\u76ee\u521b\u5efa\u548c\u6a21\u62df\u5668\u914d\u7f6e"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 14:26:01",
    "user_id": 76471,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-03 14:26:18",
    "user_id": 151608,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 14:26:36",
    "user_id": 199011,
    "lab": "MySQL\u57fa\u672c\u64cd\u4f5c",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:27:06",
    "user_id": 197101,
    "lab": "\u8bfe\u540e\u4e60\u9898\u4e00",
    "course": "PHP\u4f1a\u8bdd\u63a7\u5236"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 14:27:07",
    "user_id": 196138,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e94\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 14:27:12",
    "user_id": 199903,
    "lab": "\u4ecb\u7ecd",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 14:27:19",
    "user_id": 16806,
    "lab": "\u5f00\u542f\u795e\u5947\u7684Scala\u7f16\u7a0b\u4e4b\u65c5",
    "course": "Scala\u5f00\u53d1\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:27:35",
    "user_id": 24507,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:27:38",
    "user_id": 199967,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:27:38",
    "user_id": 195287,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 14:28:03",
    "user_id": 155044,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 153,
    "created_at": "2016-05-03 14:28:24",
    "user_id": 187210,
    "lab": "MySQL\u51fd\u6570\u548c\u64cd\u4f5c\u7b26",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:29:04",
    "user_id": 61232,
    "lab": "HTML5\u7684\u65b0\u7684\u7ed3\u6784\u5143\u7d20\u4ecb\u7ecd",
    "course": "HTML5\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:29:15",
    "user_id": 199968,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:29:55",
    "user_id": 47673,
    "lab": "Nginx\u529f\u80fd\u63cf\u8ff0",
    "course": "Linux Web\u8fd0\u7ef4\uff08Nginx\uff09\u5b9e\u6218 "
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:30:18",
    "user_id": 168914,
    "lab": "Collabtive\u7cfb\u7edfSQL\u6ce8\u5165\u5b9e\u9a8c",
    "course": "Collabtive\u7cfb\u7edfSQL\u6ce8\u5165\u5b9e\u9a8c"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 14:30:28",
    "user_id": 118124,
    "lab": "HTML\u57fa\u7840\u6c47\u603b\u5b9e\u9a8c",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 14:30:32",
    "user_id": 199952,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-03 14:30:37",
    "user_id": 171956,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-03 14:31:09",
    "user_id": 175186,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-03 14:31:22",
    "user_id": 53927,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:31:45",
    "user_id": 199892,
    "lab": "\u5217\u8868\u4e0e\u6570\u7ec4",
    "course": "Perl\u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 14:32:05",
    "user_id": 170890,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:32:27",
    "user_id": 199905,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 14:32:58",
    "user_id": 199659,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 14:32:59",
    "user_id": 199969,
    "lab": "Laravel\u5b9e\u73b0\u7528\u6237\u6ce8\u518c\u767b\u5f55",
    "course": "Laravel\u5b9e\u73b0\u7528\u6237\u6ce8\u518c\u767b\u5f55"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:33:05",
    "user_id": 199848,
    "lab": "\u901a\u8fc7\u53cd\u6c47\u7f16\u4e00\u4e2a\u7b80\u5355\u7684C\u7a0b\u5e8f\uff0c\u5206\u6790\u6c47\u7f16\u4ee3\u7801\u7406\u89e3\u8ba1\u7b97\u673a\u662f\u5982\u4f55\u5de5\u4f5c\u7684",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 14:33:16",
    "user_id": 199948,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:33:31",
    "user_id": 199670,
    "lab": "Python\u6807\u51c6\u5e93\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 14:33:37",
    "user_id": 199117,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 66,
    "created_at": "2016-05-03 14:33:40",
    "user_id": 79972,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:34:19",
    "user_id": 84217,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 14:34:21",
    "user_id": 199960,
    "lab": "Python \u6d41\u7a0b\u63a7\u5236",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:34:29",
    "user_id": 198635,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:35:11",
    "user_id": 79515,
    "lab": "\u57fa\u4e8escrapy\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u57fa\u4e8escrapy\u722c\u866b\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6(python)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:35:33",
    "user_id": 47673,
    "lab": "LNMP\u7cfb\u7edf\u5b89\u88c5",
    "course": "Linux Web\u8fd0\u7ef4\uff08Nginx\uff09\u5b9e\u6218 "
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 14:35:35",
    "user_id": 188070,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 14:36:33",
    "user_id": 190681,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:37:20",
    "user_id": 154366,
    "lab": "\u6587\u6863\uff08document\uff09\u57fa\u672c\u64cd\u4f5c",
    "course": "MongoDB \u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 14:37:21",
    "user_id": 167250,
    "lab": "\u96c6\u5408\u7c7b\u6846\u67b6",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:37:33",
    "user_id": 197101,
    "lab": "session\u57fa\u7840\u4e0e\u5b9e\u6218",
    "course": "PHP\u4f1a\u8bdd\u63a7\u5236"
  },
  {
    "minutes": 66,
    "created_at": "2016-05-03 14:37:57",
    "user_id": 170762,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 14:38:30",
    "user_id": 175180,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 14:39:12",
    "user_id": 16806,
    "lab": "\u8d77\u6b65Scala",
    "course": "Scala\u5f00\u53d1\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 14:41:28",
    "user_id": 199540,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 14:41:32",
    "user_id": 146652,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 14:43:08",
    "user_id": 189152,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:43:53",
    "user_id": 199930,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:44:36",
    "user_id": 81951,
    "lab": "\u5b57\u7b26\u4e32\uff08\u4e8c\uff09",
    "course": "\u7ecf\u5178\u7b97\u6cd5\u89e3\u9898\u5b9e\u6218"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 14:44:38",
    "user_id": 191949,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:44:48",
    "user_id": 53175,
    "lab": "Node.js\u8bfe\u7a0b\u4ecb\u7ecd",
    "course": "Node.js \u6559\u7a0b"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-03 14:45:16",
    "user_id": 199394,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 14:45:17",
    "user_id": 170841,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:46:25",
    "user_id": 199976,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:46:42",
    "user_id": 8490,
    "lab": "  HTML5\u4e24\u6b65\u5b9e\u73b0\u62fc\u56fe\u6e38\u620f",
    "course": "\u7f51\u9875\u7248\u62fc\u56fe\u6e38\u620f"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 14:47:12",
    "user_id": 170818,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 14:47:40",
    "user_id": 171990,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 14:47:43",
    "user_id": 146546,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 14:47:44",
    "user_id": 194438,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e8c\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 14:47:54",
    "user_id": 193335,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:48:00",
    "user_id": 199670,
    "lab": "Python\u804a\u5929\u5ba4",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python\u804a\u5929\u5ba4"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:49:07",
    "user_id": 106447,
    "lab": "\u9879\u76ee\u4e00\uff1a\u7f51\u7ad9\u4fe1\u606f\u722c\u866b",
    "course": "Node.js \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:49:40",
    "user_id": 84217,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:49:57",
    "user_id": 197776,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:50:03",
    "user_id": 199965,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:50:12",
    "user_id": 192761,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:50:53",
    "user_id": 80485,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 14:51:29",
    "user_id": 90735,
    "lab": "C \u8bed\u8a00\u6570\u7ec4",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:51:57",
    "user_id": 47673,
    "lab": "nginx\u914d\u7f6e\u5b9e\u6218\uff1a\u6d41\u91cf\u53ca\u5e76\u53d1\u8fde\u63a5\u6570\u9650\u5236",
    "course": "Linux Web\u8fd0\u7ef4\uff08Nginx\uff09\u5b9e\u6218 "
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 14:52:41",
    "user_id": 106447,
    "lab": "\u9879\u76ee\u4e00\uff1a\u7f51\u7ad9\u4fe1\u606f\u722c\u866b",
    "course": "Node.js \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 14:53:52",
    "user_id": 177014,
    "lab": "\u5b9a\u65f6\u5668\uff0c\u6253\u70b9\u5668\uff0c\u5de5\u4f5c\u6c60\uff0c\u901f\u7387\u9650\u5236\uff0c\u539f\u5b50\u8ba1\u6570\u5668",
    "course": "Go by Example \u4e2d\u6587\u7248"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 14:54:01",
    "user_id": 62003,
    "lab": "\u591a\u7ebf\u7a0b\u7f16\u7a0b",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 14:54:15",
    "user_id": 122971,
    "lab": "Bash\u4ecb\u7ecd\u4e0e\u5165\u95e8",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 14:54:34",
    "user_id": 198997,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 57,
    "created_at": "2016-05-03 14:54:41",
    "user_id": 81425,
    "lab": "\u516c\u94a5\u52a0\u5bc6\u4e0ePKI",
    "course": "\u516c\u94a5\u52a0\u5bc6\u4e0ePKI\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:54:51",
    "user_id": 199480,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:55:03",
    "user_id": 199892,
    "lab": "\u6a21\u5f0f\u5339\u914d",
    "course": "Perl\u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 14:55:27",
    "user_id": 65811,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:55:28",
    "user_id": 186325,
    "lab": "\u7f51\u7edc\u5c42\u5176\u5b83\u534f\u8bae",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 14:55:41",
    "user_id": 199985,
    "lab": "\u8bfe\u7a0b\u57fa\u7840\u5305\uff08\u4e0a\uff09\uff0d\u5355\u9009\u7c7b\u578b\u8868\u5355\u81ea\u52a8\u63d0\u4ea4",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python\u81ea\u52a8\u586b\u95ee\u5377\u661f"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 14:57:04",
    "user_id": 197776,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 14:58:17",
    "user_id": 149293,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 14:59:21",
    "user_id": 199986,
    "lab": "Laravel\u5b9e\u73b0\u7528\u6237\u6ce8\u518c\u767b\u5f55",
    "course": "Laravel\u5b9e\u73b0\u7528\u6237\u6ce8\u518c\u767b\u5f55"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 15:00:51",
    "user_id": 199457,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 15:00:58",
    "user_id": 192761,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:00:59",
    "user_id": 196138,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u516d\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:01:14",
    "user_id": 199969,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 15:01:15",
    "user_id": 191868,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 15:01:16",
    "user_id": 23982,
    "lab": "C\u8bed\u8a00\u5b9e\u73b0ping\u7a0b\u5e8f",
    "course": "C\u8bed\u8a00\u5b9e\u73b0ping\u7a0b\u5e8f"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 15:02:30",
    "user_id": 14919,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 15:03:03",
    "user_id": 172029,
    "lab": "Linux\u7cfb\u7edf\u76d1\u63a7\u5de5\u5177\u2014\u2014Nagios",
    "course": "Linux\u7cfb\u7edf\u76d1\u63a7\u5b9e\u6218"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 15:03:22",
    "user_id": 199614,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 15:03:42",
    "user_id": 199984,
    "lab": "Node.js\u8bfe\u7a0b\u4ecb\u7ecd",
    "course": "Node.js \u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 15:05:48",
    "user_id": 108726,
    "lab": "\u6570\u636e\u5e93\u548c\u96c6\u5408\u57fa\u672c\u64cd\u4f5c",
    "course": "MongoDB \u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 15:05:55",
    "user_id": 170890,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 63,
    "created_at": "2016-05-03 15:06:09",
    "user_id": 199990,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 57,
    "created_at": "2016-05-03 15:06:14",
    "user_id": 19009,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 15:06:24",
    "user_id": 193335,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:06:47",
    "user_id": 197569,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 15:07:17",
    "user_id": 79515,
    "lab": "LNMP\u7cfb\u7edf\u5b89\u88c5",
    "course": "Linux Web\u8fd0\u7ef4\uff08Nginx\uff09\u5b9e\u6218 "
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:07:18",
    "user_id": 122971,
    "lab": "Bash\u4e2d\u7684\u7279\u6b8a\u5b57\u7b26\uff08\u4e0a\uff09",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 15:07:28",
    "user_id": 196366,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 15:08:21",
    "user_id": 89820,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 15:08:27",
    "user_id": 148670,
    "lab": "Android\u4e0a\u7684\u624b\u52bf\u76d1\u542c\u5b9e\u73b0",
    "course": "Android\u5c0f\u6848\u4f8b - \u624b\u52bf"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 15:09:20",
    "user_id": 196083,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 15:09:47",
    "user_id": 199991,
    "lab": "Mahout \u5b89\u88c5\u914d\u7f6e",
    "course": "Mahout\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:10:16",
    "user_id": 64162,
    "lab": "Java \u65b9\u6cd5",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 15:10:34",
    "user_id": 190117,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:11:32",
    "user_id": 170841,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 15:11:41",
    "user_id": 199659,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:12:09",
    "user_id": 137931,
    "lab": "\u5bc6\u94a5\u52a0\u89e3\u5bc6\u5b9e\u9a8c\uff08\u4e0a\uff09",
    "course": "\u5bc6\u94a5\u52a0\u89e3\u5bc6\u5b9e\u9a8c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 15:12:11",
    "user_id": 196457,
    "lab": "\u683c\u5f0f\u5316\u5b57\u7b26\u4e32\u6f0f\u6d1e\u5b9e\u9a8c",
    "course": "\u683c\u5f0f\u5316\u5b57\u7b26\u4e32\u6f0f\u6d1e\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:13:49",
    "user_id": 170713,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 15:13:51",
    "user_id": 199457,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:14:11",
    "user_id": 199974,
    "lab": "Go\u8bed\u8a00\u57fa\u7840\u548c\u6570\u503c\u5e03\u5c14\u7c7b\u578b",
    "course": "Go\u8bed\u8a00\u7f16\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 15:14:33",
    "user_id": 146698,
    "lab": "\u5faa\u73af\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:15:28",
    "user_id": 171853,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 15:15:34",
    "user_id": 199614,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 15:15:43",
    "user_id": 27298,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-03 15:15:51",
    "user_id": 188839,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 15:16:00",
    "user_id": 199868,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 15:16:11",
    "user_id": 175186,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 15:16:14",
    "user_id": 52288,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e00\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 15:16:48",
    "user_id": 170760,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 15:16:59",
    "user_id": 118312,
    "lab": "IP\u7f51\u9645\u534f\u8bae",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:17:34",
    "user_id": 196138,
    "lab": "C++\u7b80\u5355\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "\u300aC++\u8bed\u8a00\u7a0b\u5e8f\u8bbe\u8ba1\uff08\u7b2c4\u7248\uff09\u300b\uff08\u90d1\u8389\u8457\uff09\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 66,
    "created_at": "2016-05-03 15:18:02",
    "user_id": 189152,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 15:18:30",
    "user_id": 170768,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 123,
    "created_at": "2016-05-03 15:18:45",
    "user_id": 46343,
    "lab": "Kubernetes",
    "course": "\u52a8\u624b\u5b9e\u6218\u5b66Docker (15\u4e2a\u5b9e\u9a8c+54\u4e2a\u89c6\u9891)"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 15:18:54",
    "user_id": 172029,
    "lab": "\u96c6\u5408\u7c7b\u6846\u67b6",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 15:19:41",
    "user_id": 168914,
    "lab": "Collabtive\u7cfb\u7edfSQL\u6ce8\u5165\u5b9e\u9a8c",
    "course": "Collabtive\u7cfb\u7edfSQL\u6ce8\u5165\u5b9e\u9a8c"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 15:19:55",
    "user_id": 88179,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:21:52",
    "user_id": 197776,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 15:21:58",
    "user_id": 137931,
    "lab": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c",
    "course": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-03 15:22:41",
    "user_id": 171853,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 15:23:18",
    "user_id": 192544,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:23:22",
    "user_id": 199999,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 57,
    "created_at": "2016-05-03 15:23:41",
    "user_id": 170724,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:24:30",
    "user_id": 194951,
    "lab": "PythonChallenge_3",
    "course": "\u6bcf\u5929\u4e00\u4e2aPythonChallenge\u300a\u4efb\u52a1\u4e09\u300b"
  },
  {
    "minutes": 147,
    "created_at": "2016-05-03 15:24:39",
    "user_id": 175180,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 15:24:42",
    "user_id": 193335,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u7684\u7ea6\u675f",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 69,
    "created_at": "2016-05-03 15:24:50",
    "user_id": 118124,
    "lab": "HTML\u57fa\u7840\u6c47\u603b\u5b9e\u9a8c",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:25:24",
    "user_id": 97385,
    "lab": "\u642d\u5efa\u81ea\u5df1\u7684Docker Registry",
    "course": "\u52a8\u624b\u5b9e\u6218\u5b66Docker (15\u4e2a\u5b9e\u9a8c+54\u4e2a\u89c6\u9891)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 15:26:45",
    "user_id": 199997,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 15:26:51",
    "user_id": 186288,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 15:27:13",
    "user_id": 165283,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-03 15:27:52",
    "user_id": 52288,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e8c\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 15:27:54",
    "user_id": 199994,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 15:28:49",
    "user_id": 197101,
    "lab": "\u4f7f\u7528 PHP \u5b9e\u73b0\u6821\u82b1\u6392\u540d",
    "course": "\u6821\u82b1\u8bc4\u6bd4\u6392\u540d\u9879\u76ee-PHP"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 15:28:51",
    "user_id": 199991,
    "lab": "Mahout \u805a\u7c7b\u7b97\u6cd5",
    "course": "Mahout\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 15:28:57",
    "user_id": 170890,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:29:17",
    "user_id": 173414,
    "lab": "SciPy - \u79d1\u5b66\u8ba1\u7b97\u5e93\uff08\u4e0b\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 15:29:26",
    "user_id": 198007,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-03 15:29:58",
    "user_id": 191809,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:30:00",
    "user_id": 84217,
    "lab": "\u8ba4\u8bc6HTML5",
    "course": "HTML5\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:30:10",
    "user_id": 187334,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 15:30:17",
    "user_id": 90735,
    "lab": "C \u8bed\u8a00\u6570\u7ec4",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 15:30:39",
    "user_id": 175265,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:30:48",
    "user_id": 55107,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e94\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:30:53",
    "user_id": 200003,
    "lab": "\u5f00\u53d1\u73af\u5883\u4ee5\u53ca\u9879\u76ee\u4e0eApp",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 15:31:19",
    "user_id": 113542,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 15:31:23",
    "user_id": 109043,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 15:31:46",
    "user_id": 197776,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 15:31:58",
    "user_id": 107086,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:32:15",
    "user_id": 183553,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:32:27",
    "user_id": 200007,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 15:32:37",
    "user_id": 199011,
    "lab": "MySQL\u7684\u8bed\u8a00\u7ed3\u6784",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:32:54",
    "user_id": 199960,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:33:23",
    "user_id": 146652,
    "lab": "Java \u8bed\u8a00\u57fa\u7840",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 15:33:25",
    "user_id": 196766,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:34:42",
    "user_id": 75937,
    "lab": "PHP\u7559\u8a00\u672c",
    "course": "PHP \u5b9e\u73b0\u7559\u8a00\u672c"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-03 15:35:27",
    "user_id": 154439,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 15:37:12",
    "user_id": 200005,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 15:37:16",
    "user_id": 194734,
    "lab": "Elgg\u7cfb\u7edf\u8de8\u7ad9\u811a\u672c\u653b\u51fb\u5b9e\u9a8c",
    "course": "Elgg\u7cfb\u7edf\u8de8\u7ad9\u811a\u672c\u653b\u51fb\u5b9e\u9a8c"
  },
  {
    "minutes": 90,
    "created_at": "2016-05-03 15:37:21",
    "user_id": 171960,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 15:37:44",
    "user_id": 200007,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-03 15:38:16",
    "user_id": 199960,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 15:39:13",
    "user_id": 55107,
    "lab": "\u5728Python\u4e2d\u4f7f\u7528\u6570\u5b57",
    "course": "\u300aPython\u5165\u95e8\u7ecf\u5178\u300b\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 15:39:16",
    "user_id": 88282,
    "lab": "R\u8bed\u8a00\u8bfe\u7a0b\u4ecb\u7ecd",
    "course": "[\u7ef4\u62a4\u4e2d] R\u8bed\u8a00\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 15:41:12",
    "user_id": 199991,
    "lab": "Mahout \u5206\u7c7b\u7b97\u6cd5",
    "course": "Mahout\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 15:41:28",
    "user_id": 199670,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 15:41:37",
    "user_id": 189427,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:42:03",
    "user_id": 199651,
    "lab": "Hadoop2.X 64\u4f4d\u7f16\u8bd1",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 15:44:10",
    "user_id": 146652,
    "lab": "Java  \u8fd0\u7b97\u7b26",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 15:44:27",
    "user_id": 191949,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 15:44:31",
    "user_id": 140305,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 15:44:55",
    "user_id": 165283,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 15:45:38",
    "user_id": 107263,
    "lab": "cookie\u57fa\u7840\u548c\u5e94\u7528",
    "course": "PHP\u4f1a\u8bdd\u63a7\u5236"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 15:46:43",
    "user_id": 195661,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 15:47:51",
    "user_id": 170890,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 15:48:38",
    "user_id": 94253,
    "lab": "LAMP\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "LAMP\u90e8\u7f72\u53ca\u914d\u7f6e"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:49:11",
    "user_id": 109294,
    "lab": "\u4e00\u4e2a\u6700\u7b80\u5355\u7684 express \u5e94\u7528",
    "course": "Node.js\u5305\u6559\u4e0d\u5305\u4f1a"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:49:14",
    "user_id": 199457,
    "lab": "linux\u7cfb\u7edf\u76d1\u63a7\u5e38\u7528\u547d\u4ee4\uff08\u4e00\uff09",
    "course": "Linux\u7cfb\u7edf\u76d1\u63a7\u5b9e\u6218"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-03 15:49:18",
    "user_id": 196366,
    "lab": "\u57fa\u7840\u7bc7 - SELECT \u8bed\u53e5\u8be6\u89e3",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 15:49:37",
    "user_id": 94767,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e09\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 15:50:32",
    "user_id": 199991,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 15:50:52",
    "user_id": 192544,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:50:53",
    "user_id": 194989,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:51:34",
    "user_id": 200016,
    "lab": "\u8ba4\u8bc6HTML5",
    "course": "HTML5\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 15:52:03",
    "user_id": 193335,
    "lab": "\u57fa\u7840\u7bc7 - SELECT \u8bed\u53e5\u8be6\u89e3",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:52:15",
    "user_id": 195298,
    "lab": "Java \u96c6\u5408\u6846\u67b6",
    "course": "JDK \u6838\u5fc3 API"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 15:52:49",
    "user_id": 199011,
    "lab": "MySQL\u51fd\u6570\u548c\u64cd\u4f5c\u7b26",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-03 15:53:27",
    "user_id": 198975,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:53:58",
    "user_id": 180908,
    "lab": "\u57fa\u4e8escrapy\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u57fa\u4e8escrapy\u722c\u866b\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6(python)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 15:54:36",
    "user_id": 194818,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 15:55:05",
    "user_id": 197101,
    "lab": "\u8f6c\u76d8\u62bd\u5956",
    "course": "PHP\u5b9e\u73b0\u8f6c\u76d8\u62bd\u5956"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 15:55:08",
    "user_id": 192178,
    "lab": "\u521d\u8bc6HTML",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 2,
    "created_at": "2016-05-03 15:55:27",
    "user_id": 133586,
    "lab": "Ubuntu14.04 Server\u5b9e\u9a8c\u73af\u5883",
    "course": "Ubuntu Server\u4f53\u9a8c\u8bfe"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 15:55:48",
    "user_id": 200017,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 15:55:59",
    "user_id": 55107,
    "lab": "\u7f16\u7a0b\u4e2d\u7684\u903b\u8f91",
    "course": "\u300aPython\u5165\u95e8\u7ecf\u5178\u300b\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 15:56:09",
    "user_id": 175490,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 15:56:47",
    "user_id": 31320,
    "lab": "\u5f00\u53d1\u73af\u5883\u4ee5\u53ca\u9879\u76ee\u4e0eApp",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:56:53",
    "user_id": 178681,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 15:57:23",
    "user_id": 200023,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:58:09",
    "user_id": 171961,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 57,
    "created_at": "2016-05-03 15:59:08",
    "user_id": 171956,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 15:59:09",
    "user_id": 161790,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 15:59:21",
    "user_id": 106589,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 60,
    "created_at": "2016-05-03 15:59:34",
    "user_id": 196371,
    "lab": "\u5faa\u73af\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 15:59:51",
    "user_id": 165283,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 16:00:50",
    "user_id": 76021,
    "lab": "\u591a\u8fdb\u7a0b\uff08\u4e8c\uff09",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 16:01:15",
    "user_id": 107263,
    "lab": "cookie\u57fa\u7840\u548c\u5e94\u7528",
    "course": "PHP\u4f1a\u8bdd\u63a7\u5236"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 16:01:19",
    "user_id": 146698,
    "lab": "C \u8bed\u8a00\u6570\u7ec4",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 16:02:55",
    "user_id": 171961,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 16:03:15",
    "user_id": 193217,
    "lab": "\u7528CSS\u548cJquery\u6253\u9020\u4e00\u4e2a\u7b80\u5355\u7684\u56fe\u7247\u7f16\u8f91\u5668",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u7528CSS\u548cjQuery\u6253\u9020\u4e00\u4e2a\u7b80\u5355\u7684\u56fe\u7247\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:03:46",
    "user_id": 194818,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 16:03:52",
    "user_id": 200027,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 16:03:52",
    "user_id": 199984,
    "lab": "Node.js\u6a21\u5757",
    "course": "Node.js \u6559\u7a0b"
  },
  {
    "minutes": 87,
    "created_at": "2016-05-03 16:04:06",
    "user_id": 187286,
    "lab": "Python\u6807\u51c6\u5e93\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 16:04:23",
    "user_id": 76471,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 16:04:27",
    "user_id": 120033,
    "lab": "Spark \u7b80\u4ecb\u4e0e\u5b89\u88c5\uff08\u514d\u8d39\uff09",
    "course": "Spark \u5927\u6570\u636e\u52a8\u624b\u5b9e\u9a8c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 16:04:34",
    "user_id": 199480,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 16:05:13",
    "user_id": 153706,
    "lab": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668",
    "course": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:05:22",
    "user_id": 69570,
    "lab": "HTML5\u5b9e\u73b0\u522e\u522e\u4e50\u6548\u679c",
    "course": "\u57fa\u4e8e HTML5 \u5b9e\u73b0\u522e\u522e\u4e50\u6548\u679c"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 16:05:24",
    "user_id": 199952,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0b\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:06:40",
    "user_id": 88767,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 16:07:04",
    "user_id": 171990,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:07:23",
    "user_id": 197631,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 16:07:44",
    "user_id": 57763,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 16:08:46",
    "user_id": 171001,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 16:09:17",
    "user_id": 50282,
    "lab": "grep\u547d\u4ee4\u4e0e\u6b63\u5219\u8868\u8fbe\u5f0f",
    "course": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-03 16:09:50",
    "user_id": 172125,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:09:51",
    "user_id": 160600,
    "lab": "Python\u6587\u672c\u89e3\u91ca\u5668",
    "course": "Python\u6587\u672c\u89e3\u6790\u5668"
  },
  {
    "minutes": 90,
    "created_at": "2016-05-03 16:10:26",
    "user_id": 198336,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 16:10:31",
    "user_id": 193593,
    "lab": "java.lang \u5305",
    "course": "JDK \u6838\u5fc3 API"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 16:10:51",
    "user_id": 76021,
    "lab": "\u591a\u8fdb\u7a0b\uff08\u4e09\uff09",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:11:08",
    "user_id": 199974,
    "lab": "Go\u8bed\u8a00\u5b57\u7b26\u4e32",
    "course": "Go\u8bed\u8a00\u7f16\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:11:37",
    "user_id": 165283,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:11:55",
    "user_id": 200016,
    "lab": "HTML5\u7684\u65b0\u7684\u7ed3\u6784\u5143\u7d20\u4ecb\u7ecd",
    "course": "HTML5\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 16:12:53",
    "user_id": 199991,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0b\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 16:13:24",
    "user_id": 200030,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 16:13:53",
    "user_id": 53927,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:14:06",
    "user_id": 200031,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 78,
    "created_at": "2016-05-03 16:14:07",
    "user_id": 46344,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 16:14:08",
    "user_id": 197776,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 16:14:25",
    "user_id": 173414,
    "lab": "SciPy - \u79d1\u5b66\u8ba1\u7b97\u5e93\uff08\u4e0b\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:14:32",
    "user_id": 107263,
    "lab": "\u8bfe\u540e\u4e60\u9898\u4e00",
    "course": "PHP\u4f1a\u8bdd\u63a7\u5236"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-03 16:14:54",
    "user_id": 175176,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 16:14:57",
    "user_id": 171853,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 16:14:57",
    "user_id": 200034,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 16:15:32",
    "user_id": 80485,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 16:16:37",
    "user_id": 165283,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 16:17:09",
    "user_id": 191690,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0b\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:17:37",
    "user_id": 199457,
    "lab": "\u7528\u65f6\u95f4\u5e8f\u5217\u9884\u6d4b\u80a1\u7968\u6536\u76ca",
    "course": "[\u5df2\u4e0b\u7ebf] R\u8bed\u8a00\u80a1\u7968\u6570\u636e\u5206\u6790"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 16:19:31",
    "user_id": 200007,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 16:19:56",
    "user_id": 170775,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:20:10",
    "user_id": 64162,
    "lab": "Java \u7c7b\u4e0e\u5bf9\u8c61",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 16:20:14",
    "user_id": 200039,
    "lab": "\u57fa\u4e8escrapy\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u57fa\u4e8escrapy\u722c\u866b\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6(python)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:20:37",
    "user_id": 133586,
    "lab": "Ubuntu14.04 Server\u5b9e\u9a8c\u73af\u5883",
    "course": "Ubuntu Server\u4f53\u9a8c\u8bfe"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 16:20:40",
    "user_id": 172029,
    "lab": "\u6570\u5b66\u5de5\u5177",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 16:20:57",
    "user_id": 167250,
    "lab": "\u6570\u5b66\u5de5\u5177",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 93,
    "created_at": "2016-05-03 16:21:09",
    "user_id": 171718,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 16:21:11",
    "user_id": 187226,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u7684\u7ea6\u675f",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:21:11",
    "user_id": 116727,
    "lab": "Python\u6807\u51c6\u5e93\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 16:21:41",
    "user_id": 50282,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u8fd0\u7528\u4e4b sed\u5de5\u5177\u547d\u4ee4 ",
    "course": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 16:21:45",
    "user_id": 52288,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e09\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 16:21:46",
    "user_id": 108726,
    "lab": "\u6570\u636e\u5e93\u548c\u96c6\u5408\u57fa\u672c\u64cd\u4f5c",
    "course": "MongoDB \u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:21:58",
    "user_id": 200036,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:22:10",
    "user_id": 170486,
    "lab": "PHP\u7b80\u4ecb",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 16:22:13",
    "user_id": 200030,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 16:22:51",
    "user_id": 63797,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:24:44",
    "user_id": 199952,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:24:57",
    "user_id": 15536,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e00\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:25:32",
    "user_id": 152484,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 16:26:26",
    "user_id": 170573,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 16:26:39",
    "user_id": 156356,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:27:03",
    "user_id": 2203,
    "lab": "Spark \u7b80\u4ecb\u4e0e\u5b89\u88c5\uff08\u514d\u8d39\uff09",
    "course": "Spark \u5927\u6570\u636e\u52a8\u624b\u5b9e\u9a8c"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 16:27:23",
    "user_id": 165283,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 16:27:47",
    "user_id": 200039,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 16:28:25",
    "user_id": 199984,
    "lab": "Node.js Events\u6a21\u5757",
    "course": "Node.js \u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:28:28",
    "user_id": 200016,
    "lab": "HTML5\u6587\u4ef6\u64cd\u4f5cAPI",
    "course": "HTML5\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 16:29:29",
    "user_id": 200036,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-03 16:30:14",
    "user_id": 199659,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:30:17",
    "user_id": 108097,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 16:30:23",
    "user_id": 200037,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:30:29",
    "user_id": 193248,
    "lab": "\u57fa\u7840\u7ec4\u4ef6\uff082\uff09 - Service",
    "course": "Android\u5e94\u7528\u5f00\u53d1\u57fa\u7840"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 16:30:53",
    "user_id": 199011,
    "lab": "SQL\u8bed\u53e5\u8bed\u6cd5",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 16:30:56",
    "user_id": 189427,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:31:15",
    "user_id": 83316,
    "lab": "\u6587\u4ef6IO\uff08\u4e00\uff09",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 16:32:09",
    "user_id": 116727,
    "lab": "Python\u6807\u51c6\u5e93\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 57,
    "created_at": "2016-05-03 16:32:38",
    "user_id": 79972,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 16:32:58",
    "user_id": 88179,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 16:33:58",
    "user_id": 175265,
    "lab": "\u57fa\u4e8escrapy\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u57fa\u4e8escrapy\u722c\u866b\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6(python)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:34:21",
    "user_id": 126960,
    "lab": "\u9879\u76ee\u56db\uff1a\u7f51\u7ad9\u4fe1\u606f\u722c\u866b",
    "course": "Python \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 16:34:49",
    "user_id": 199999,
    "lab": "\u4ecb\u7ecd",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:35:08",
    "user_id": 200021,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-03 16:35:15",
    "user_id": 188546,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 16:35:34",
    "user_id": 174162,
    "lab": "C\u8bed\u8a00\u5b9e\u73b0WEB\u670d\u52a1\u5668",
    "course": "C\u8bed\u8a00\u5b9e\u73b0\u4e00\u4e2a\u652f\u6301PHP\u7684\u7b80\u6613WEB\u670d\u52a1\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 16:35:38",
    "user_id": 196101,
    "lab": "HTML\u57fa\u7840\u6c47\u603b\u5b9e\u9a8c",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-03 16:36:13",
    "user_id": 170762,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 16:36:28",
    "user_id": 170757,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 16:36:29",
    "user_id": 200045,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:36:45",
    "user_id": 79270,
    "lab": "\u5de5\u5382\u6a21\u5f0f",
    "course": "Java\u8fdb\u9636\u4e4b\u8bbe\u8ba1\u6a21\u5f0f"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:37:21",
    "user_id": 200039,
    "lab": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668",
    "course": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 16:37:27",
    "user_id": 122971,
    "lab": "Bash\u4e2d\u7684\u7279\u6b8a\u5b57\u7b26\uff08\u4e0a\uff09",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 16:37:41",
    "user_id": 170831,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 16:37:43",
    "user_id": 149347,
    "lab": "\u57fa\u7840\u7bc7 - SELECT \u8bed\u53e5\u8be6\u89e3",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 16:38:16",
    "user_id": 113542,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 16:38:58",
    "user_id": 200030,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 16:39:21",
    "user_id": 187226,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:39:50",
    "user_id": 197906,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 16:40:32",
    "user_id": 141083,
    "lab": "Java  \u8fd0\u7b97\u7b26",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 16:40:41",
    "user_id": 131199,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 16:40:58",
    "user_id": 194092,
    "lab": "\u5f00\u53d1\u73af\u5883\u4ee5\u53ca\u9879\u76ee\u4e0eApp",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 16:41:00",
    "user_id": 153459,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 16:41:00",
    "user_id": 193248,
    "lab": "\u57fa\u7840\u7ec4\u4ef6\uff082\uff09 - Service",
    "course": "Android\u5e94\u7528\u5f00\u53d1\u57fa\u7840"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-03 16:41:03",
    "user_id": 167421,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-03 16:41:23",
    "user_id": 200049,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 16:42:02",
    "user_id": 161790,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 16:42:21",
    "user_id": 200036,
    "lab": "matplotlib - 2D \u4e0e 3D \u56fe\u7684\u7ed8\u5236\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:42:25",
    "user_id": 199999,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 16:43:01",
    "user_id": 52288,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u56db\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:44:14",
    "user_id": 194260,
    "lab": "Nginx\u6a21\u5757\u5f00\u53d1\u5b9e\u9a8c",
    "course": "Linux Web\u8fd0\u7ef4\uff08Nginx\uff09\u5b9e\u6218 "
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 16:44:49",
    "user_id": 199991,
    "lab": "Hadoop\u5355\u673a\u6a21\u5f0f\u5b89\u88c5",
    "course": "Hadoop\u90e8\u7f72\u53ca\u7ba1\u7406"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:45:31",
    "user_id": 172286,
    "lab": "\u8f6c\u76d8\u62bd\u5956",
    "course": "PHP\u5b9e\u73b0\u8f6c\u76d8\u62bd\u5956"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 16:45:42",
    "user_id": 55107,
    "lab": "\u5728\u5b57\u7b26\u4e32\u4e2d\u5b58\u50a8\u6587\u672c",
    "course": "\u300aPython\u5165\u95e8\u7ecf\u5178\u300b\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 16:45:57",
    "user_id": 90735,
    "lab": "C \u8bed\u8a00\u6570\u7ec4",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 63,
    "created_at": "2016-05-03 16:46:18",
    "user_id": 170724,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:46:46",
    "user_id": 153706,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 16:46:52",
    "user_id": 170944,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 16:47:05",
    "user_id": 15536,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e8c\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 16:49:10",
    "user_id": 91969,
    "lab": "Java \u63a7\u5236\u8bed\u53e5",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 16:49:47",
    "user_id": 199337,
    "lab": "pandas \u56de\u987e",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python \u6570\u636e\u5206\u6790\uff08\u4e00\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 16:50:12",
    "user_id": 196366,
    "lab": "\u57fa\u7840\u7bc7 - \u6570\u636e\u5e93\u53ca\u8868\u7684\u4fee\u6539\u548c\u5220\u9664",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:50:45",
    "user_id": 200050,
    "lab": "git\u4ecb\u7ecd",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:50:46",
    "user_id": 80277,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 16:51:34",
    "user_id": 172286,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 16:52:14",
    "user_id": 50530,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:52:40",
    "user_id": 156995,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:52:41",
    "user_id": 198975,
    "lab": "PythonChallenge_1",
    "course": "\u5168\u9762\u89e3\u6790PythonChallenge"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 16:54:17",
    "user_id": 187226,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 16:54:51",
    "user_id": 171990,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 16:55:00",
    "user_id": 197906,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:55:25",
    "user_id": 199599,
    "lab": "MySQL\u5e38\u7528\u67e5\u8be2",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:55:28",
    "user_id": 184216,
    "lab": "\u591a\u5f20\u56fe\u7247\u62fc\u63a5\u4e0e\u5c42\u53e0",
    "course": "\u591a\u5f20\u56fe\u7247\u62fc\u63a5\u4e0e\u5c42\u53e0"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 16:56:23",
    "user_id": 170779,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 16:56:38",
    "user_id": 196766,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 16:56:54",
    "user_id": 131199,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 16:58:25",
    "user_id": 154583,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 16:59:12",
    "user_id": 195784,
    "lab": "\u6982\u8ff0",
    "course": "\u5b9e\u7528Linux Shell\u7f16\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 16:59:20",
    "user_id": 194092,
    "lab": "Models\u548cAdmin\u4ee5\u53caViews\u548cURL",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 16:59:36",
    "user_id": 199516,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 16:59:59",
    "user_id": 57763,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:00:45",
    "user_id": 199995,
    "lab": "Python \u7834\u89e3\u9a8c\u8bc1\u7801",
    "course": "Python \u7834\u89e3\u9a8c\u8bc1\u7801"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 17:00:57",
    "user_id": 164040,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:01:13",
    "user_id": 200053,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:02:38",
    "user_id": 172286,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 17:02:55",
    "user_id": 143361,
    "lab": "Redis\u7b80\u4ecb\u4e0e\u5b89\u88c5",
    "course": "Redis\u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:03:16",
    "user_id": 23982,
    "lab": "C\u8bed\u8a00\u5b9e\u73b0ping\u7a0b\u5e8f",
    "course": "C\u8bed\u8a00\u5b9e\u73b0ping\u7a0b\u5e8f"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 17:03:31",
    "user_id": 197906,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:03:38",
    "user_id": 167250,
    "lab": "git\u4ecb\u7ecd",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 17:04:26",
    "user_id": 108726,
    "lab": "\u6570\u636e\u67e5\u8be2",
    "course": "MongoDB \u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:05:23",
    "user_id": 194627,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:07:48",
    "user_id": 200047,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 17:07:52",
    "user_id": 171956,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:08:20",
    "user_id": 172125,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 17:08:42",
    "user_id": 200057,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 17:08:48",
    "user_id": 175280,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 17:09:18",
    "user_id": 178681,
    "lab": "lab0\uff1aCoding!",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u5b9e\u9a8c\uff0d\u57fa\u4e8euCore OS"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 17:09:32",
    "user_id": 165283,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 17:09:42",
    "user_id": 175176,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-03 17:10:19",
    "user_id": 171853,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:11:05",
    "user_id": 200053,
    "lab": "\u5f00\u53d1\u73af\u5883\u4ee5\u53ca\u9879\u76ee\u4e0eApp",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 17:11:34",
    "user_id": 187226,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:11:42",
    "user_id": 198638,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 17:11:59",
    "user_id": 199991,
    "lab": "Hadoop\u4f2a\u5206\u5e03\u6a21\u5f0f\u914d\u7f6e\u90e8\u7f72",
    "course": "Hadoop\u90e8\u7f72\u53ca\u7ba1\u7406"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 17:12:16",
    "user_id": 199232,
    "lab": "pandas \u56de\u987e",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python \u6570\u636e\u5206\u6790\uff08\u4e00\uff09"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-03 17:13:16",
    "user_id": 200056,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 17:14:12",
    "user_id": 164040,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-03 17:14:15",
    "user_id": 170974,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 17:14:22",
    "user_id": 187290,
    "lab": "\u5f00\u53d1\u73af\u5883\u548c\u5256\u6790\u7b2c\u4e00\u4e2a C \u8bed\u8a00",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 17:14:44",
    "user_id": 198533,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 17:14:59",
    "user_id": 193593,
    "lab": "Java \u96c6\u5408\u6846\u67b6",
    "course": "JDK \u6838\u5fc3 API"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 17:16:31",
    "user_id": 131199,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 17:17:14",
    "user_id": 170831,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:17:18",
    "user_id": 200047,
    "lab": "\u57fa\u7840\u6b63\u5219\u8868\u8fbe\u5f0f\u4ecb\u7ecd\u4e0e\u7ec3\u4e60",
    "course": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:19:22",
    "user_id": 172083,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:22:07",
    "user_id": 50530,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:22:14",
    "user_id": 199996,
    "lab": "HTML5\u5b9e\u73b0\u522e\u522e\u4e50\u6548\u679c",
    "course": "\u57fa\u4e8e HTML5 \u5b9e\u73b0\u522e\u522e\u4e50\u6548\u679c"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 17:22:23",
    "user_id": 53927,
    "lab": "\u4ecb\u7ecd",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 17:23:39",
    "user_id": 131199,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 17:24:09",
    "user_id": 200034,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:25:13",
    "user_id": 165283,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 66,
    "created_at": "2016-05-03 17:25:53",
    "user_id": 171970,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 17:27:46",
    "user_id": 90735,
    "lab": "Bash\u4ecb\u7ecd\u4e0e\u5165\u95e8",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 17:28:13",
    "user_id": 197970,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 17:30:02",
    "user_id": 167250,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:30:47",
    "user_id": 62003,
    "lab": "Java\u5b9e\u73b0\u8bb0\u4e8b\u672c",
    "course": "Java\u5b9e\u73b0\u8bb0\u4e8b\u672c"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 17:30:59",
    "user_id": 171956,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:31:23",
    "user_id": 146546,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 17:31:29",
    "user_id": 171001,
    "lab": "Python \u6d41\u7a0b\u63a7\u5236",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 17:31:43",
    "user_id": 199866,
    "lab": "\u4ecb\u7ecd",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 17:32:03",
    "user_id": 198322,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 17:32:23",
    "user_id": 170757,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 17:33:25",
    "user_id": 191350,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 17:34:19",
    "user_id": 187226,
    "lab": "Java \u8bed\u8a00\u57fa\u7840",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:35:43",
    "user_id": 187290,
    "lab": "Java  \u8fd0\u7b97\u7b26",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 17:36:51",
    "user_id": 187210,
    "lab": "MySQL\u51fd\u6570\u548c\u64cd\u4f5c\u7b26",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:36:52",
    "user_id": 200066,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 17:37:08",
    "user_id": 200067,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 17:37:44",
    "user_id": 200007,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 17:37:58",
    "user_id": 196766,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 17:38:34",
    "user_id": 199337,
    "lab": "\u8bfb\u5199\u6587\u672c\u683c\u5f0f\u7684\u6570\u636e",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python \u6570\u636e\u5206\u6790\uff08\u4e00\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 17:39:22",
    "user_id": 172083,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-03 17:39:32",
    "user_id": 199659,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 17:40:19",
    "user_id": 196083,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:41:08",
    "user_id": 197628,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 17:43:36",
    "user_id": 187290,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 17:43:42",
    "user_id": 197970,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 17:43:49",
    "user_id": 193335,
    "lab": "\u57fa\u7840\u7bc7 - \u5176\u4ed6\u57fa\u672c\u64cd\u4f5c",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 17:44:46",
    "user_id": 200071,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:45:25",
    "user_id": 170969,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:46:18",
    "user_id": 113750,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 17:46:28",
    "user_id": 199614,
    "lab": "\u7f51\u9875\u7248\u522b\u8e29\u767d\u5757",
    "course": "\u7f51\u9875\u7248\u522b\u8e29\u767d\u5757\u6e38\u620f"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:46:36",
    "user_id": 163044,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e00\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 17:46:56",
    "user_id": 153706,
    "lab": "\u94fe\u8def\u5c42\u4ecb\u7ecd",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 17:47:08",
    "user_id": 157472,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:47:14",
    "user_id": 79105,
    "lab": "\u6b22\u8fce\u6765\u5230 Flask \u7684\u4e16\u754c",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:47:23",
    "user_id": 194560,
    "lab": "\u4ecb\u7ecd",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:47:34",
    "user_id": 195784,
    "lab": "Linux\u57fa\u7840\u77e5\u8bc6\u4e0e\u5e38\u7528\u547d\u4ee4",
    "course": "\u5b9e\u7528Linux Shell\u7f16\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 17:48:46",
    "user_id": 196606,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 17:49:58",
    "user_id": 200057,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 17:50:37",
    "user_id": 200017,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 17:51:38",
    "user_id": 176440,
    "lab": "\u6570\u636e\u7ed3\u6784-\u4e8c\u53c9\u6811\uff08Binary Tree\uff09",
    "course": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:52:06",
    "user_id": 198322,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 17:52:38",
    "user_id": 200065,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:52:45",
    "user_id": 200072,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 17:55:44",
    "user_id": 200074,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 17:55:57",
    "user_id": 25611,
    "lab": "SET-UID\u7a0b\u5e8f\u6f0f\u6d1e\u5b9e\u9a8c",
    "course": "SET-UID\u7a0b\u5e8f\u6f0f\u6d1e\u5b9e\u9a8c"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-03 17:57:13",
    "user_id": 197628,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 17:57:36",
    "user_id": 131199,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 17:57:40",
    "user_id": 200067,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 18:00:12",
    "user_id": 200069,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 18:01:41",
    "user_id": 165126,
    "lab": "\u683c\u5f0f\u5316\u5b57\u7b26\u4e32\u6f0f\u6d1e\u5b9e\u9a8c",
    "course": "\u683c\u5f0f\u5316\u5b57\u7b26\u4e32\u6f0f\u6d1e\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 18:02:06",
    "user_id": 199546,
    "lab": "Rails \u4ecb\u7ecd\u4e0e\u73af\u5883\u914d\u7f6e",
    "course": "Rails\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 18:03:08",
    "user_id": 200065,
    "lab": "Java \u8bed\u8a00\u57fa\u7840",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 18:03:21",
    "user_id": 175280,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 2,
    "created_at": "2016-05-03 18:03:57",
    "user_id": 133586,
    "lab": "Ubuntu14.04 Server\u5b9e\u9a8c\u73af\u5883",
    "course": "Ubuntu Server\u4f53\u9a8c\u8bfe"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 18:04:06",
    "user_id": 180533,
    "lab": "Java \u5c01\u88c5",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 18:05:06",
    "user_id": 198083,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 18:05:16",
    "user_id": 88282,
    "lab": "R\u8bed\u6cd5\u5b66\u4e60\uff08\u4e00\uff09",
    "course": "[\u7ef4\u62a4\u4e2d] R\u8bed\u8a00\u6559\u7a0b"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 18:08:30",
    "user_id": 198752,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 18:09:11",
    "user_id": 175280,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 18:09:25",
    "user_id": 170573,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 18:10:56",
    "user_id": 2203,
    "lab": "Spark \u7b80\u4ecb\u4e0e\u5b89\u88c5\uff08\u514d\u8d39\uff09",
    "course": "Spark \u5927\u6570\u636e\u52a8\u624b\u5b9e\u9a8c"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-03 18:12:29",
    "user_id": 170730,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-03 18:12:36",
    "user_id": 188229,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-03 18:13:02",
    "user_id": 170762,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 18:13:51",
    "user_id": 175185,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 18:14:17",
    "user_id": 200084,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 18:14:30",
    "user_id": 167480,
    "lab": "Hadoop\u5355\u673a\u6a21\u5f0f\u5b89\u88c5",
    "course": "Hadoop\u90e8\u7f72\u53ca\u7ba1\u7406"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-03 18:16:00",
    "user_id": 173358,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-03 18:16:38",
    "user_id": 197970,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 18:16:48",
    "user_id": 171778,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 18:17:38",
    "user_id": 170779,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 18:18:06",
    "user_id": 198322,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 18:20:47",
    "user_id": 122971,
    "lab": "Bash\u4e2d\u7684\u7279\u6b8a\u5b57\u7b26\uff08\u4e0a\uff09",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 18:20:47",
    "user_id": 200089,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 18:22:21",
    "user_id": 170974,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 18:23:01",
    "user_id": 198083,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 18:24:16",
    "user_id": 175280,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 18:24:33",
    "user_id": 199960,
    "lab": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668",
    "course": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 18:25:23",
    "user_id": 171778,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 18:27:20",
    "user_id": 175185,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 18:31:19",
    "user_id": 200047,
    "lab": "git\u4ecb\u7ecd",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 18:31:36",
    "user_id": 198083,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 18:31:47",
    "user_id": 199772,
    "lab": "lab0\uff1aCoding!",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u5b9e\u9a8c\uff0d\u57fa\u4e8euCore OS"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 18:32:44",
    "user_id": 174820,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 18:34:02",
    "user_id": 188650,
    "lab": "\u57fa\u7840\u6b63\u5219\u8868\u8fbe\u5f0f\u4ecb\u7ecd\u4e0e\u7ec3\u4e60",
    "course": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-03 18:35:51",
    "user_id": 170724,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e94",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 18:37:28",
    "user_id": 94644,
    "lab": "\u6570\u636e\u7ed3\u6784-\u94fe\u8868\uff08Linked List\uff09",
    "course": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 18:38:10",
    "user_id": 199984,
    "lab": "Node.js fs\u6a21\u5757",
    "course": "Node.js \u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 18:38:41",
    "user_id": 175265,
    "lab": "python\u751f\u6210\u6c49\u5b57\u56fe\u7247\u5b57\u5e93",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011python\u751f\u6210\u6c49\u5b57\u56fe\u7247\u5b57\u5e93"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 18:39:39",
    "user_id": 171778,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 18:40:29",
    "user_id": 200096,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 18:40:41",
    "user_id": 175819,
    "lab": "\u6c47\u7f16\u8bed\u8a00\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u90d1\u6653\u8587\u7f16\u8457\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 18:41:20",
    "user_id": 131199,
    "lab": "\u57fa\u672c\u6982\u5ff5",
    "course": "\u6570\u636e\u7ed3\u6784(\u65b0\u7248)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 18:41:22",
    "user_id": 200065,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 18:41:35",
    "user_id": 200097,
    "lab": "ShellShock \u653b\u51fb\u5b9e\u9a8c",
    "course": "ShellShock \u653b\u51fb\u5b9e\u9a8c"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 18:41:53",
    "user_id": 118312,
    "lab": "\u4f20\u8f93\u5c42\uff1aUDP\u534f\u8bae",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 18:44:01",
    "user_id": 171960,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 18:44:04",
    "user_id": 157318,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 18:44:42",
    "user_id": 113750,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 18:45:37",
    "user_id": 191350,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 57,
    "created_at": "2016-05-03 18:46:56",
    "user_id": 175185,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 18:47:03",
    "user_id": 198322,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 18:48:34",
    "user_id": 200065,
    "lab": "Java \u8bed\u8a00\u57fa\u7840",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 18:49:44",
    "user_id": 171778,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 18:51:31",
    "user_id": 199659,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 18:52:00",
    "user_id": 175172,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 18:52:31",
    "user_id": 199866,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 18:53:09",
    "user_id": 146207,
    "lab": "\u6570\u636e\u7ed3\u6784",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 18:53:43",
    "user_id": 197865,
    "lab": "\u5f00\u53d1\u73af\u5883\u4ee5\u53ca\u9879\u76ee\u4e0eApp",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 18:53:47",
    "user_id": 175182,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 18:53:59",
    "user_id": 171778,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 18:54:06",
    "user_id": 192069,
    "lab": "\u9879\u76ee\u4e94\uff1a\u6587\u5b57\u804a\u5929\u5ba4",
    "course": "Python \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-03 18:54:27",
    "user_id": 200007,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 18:54:39",
    "user_id": 200101,
    "lab": "Bash\u4ecb\u7ecd\u4e0e\u5165\u95e8",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 18:54:52",
    "user_id": 200036,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 18:55:02",
    "user_id": 199817,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 18:55:38",
    "user_id": 198322,
    "lab": "\u57fa\u672c\u6982\u5ff5",
    "course": "\u6570\u636e\u7ed3\u6784(\u65b0\u7248)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 18:57:57",
    "user_id": 170775,
    "lab": "Java \u63a7\u5236\u8bed\u53e5",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-03 18:58:11",
    "user_id": 25611,
    "lab": "\u683c\u5f0f\u5316\u5b57\u7b26\u4e32\u6f0f\u6d1e\u5b9e\u9a8c",
    "course": "\u683c\u5f0f\u5316\u5b57\u7b26\u4e32\u6f0f\u6d1e\u5b9e\u9a8c"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 18:58:32",
    "user_id": 191640,
    "lab": "HTML5 \u672c\u5730\u88c1\u526a\u56fe\u7247",
    "course": "\u57fa\u4e8e HTML5 \u5b9e\u73b0\u672c\u5730\u56fe\u7247\u88c1\u526a"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 18:58:36",
    "user_id": 200069,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 18:58:37",
    "user_id": 104807,
    "lab": "PythonChallenge_1",
    "course": "\u5168\u9762\u89e3\u6790PythonChallenge"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 18:59:56",
    "user_id": 171853,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 18:59:59",
    "user_id": 74797,
    "lab": "\u64cd\u4f5c\u7cfb\u7edf\u7684\u5f15\u5bfc",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 19:00:01",
    "user_id": 196366,
    "lab": "\u57fa\u7840\u7bc7 - \u5176\u4ed6\u57fa\u672c\u64cd\u4f5c",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:00:21",
    "user_id": 188229,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 19:00:36",
    "user_id": 199991,
    "lab": "Hadoop\u5355\u673a\u6a21\u5f0f\u5b89\u88c5",
    "course": "Hadoop\u90e8\u7f72\u53ca\u7ba1\u7406"
  },
  {
    "minutes": 96,
    "created_at": "2016-05-03 19:00:58",
    "user_id": 187210,
    "lab": "MySQL\u51fd\u6570\u548c\u64cd\u4f5c\u7b26",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:01:29",
    "user_id": 114104,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 19:03:11",
    "user_id": 171970,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 19:03:51",
    "user_id": 171778,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 19:04:55",
    "user_id": 175182,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 19:05:22",
    "user_id": 157318,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 19:05:46",
    "user_id": 198752,
    "lab": "\u8ba4\u8bc6wxpython",
    "course": "\u7528Python\u505a2048\u6e38\u620f"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:07:44",
    "user_id": 196366,
    "lab": "\u4e2d\u7ea7\u6280\u80fd\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:07:45",
    "user_id": 135816,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:08:12",
    "user_id": 200104,
    "lab": "\u521d\u8bc6HTML",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:08:29",
    "user_id": 199906,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 19:08:34",
    "user_id": 170775,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:09:14",
    "user_id": 65441,
    "lab": "Hibernate \u7b80\u5355\u589e\u5220\u6539\u67e5",
    "course": "Hibernate\u6846\u67b6\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 19:10:11",
    "user_id": 199868,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:10:47",
    "user_id": 200105,
    "lab": "\u8ba4\u8bc6wxpython",
    "course": "\u7528Python\u505a2048\u6e38\u620f"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 19:10:50",
    "user_id": 175172,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-03 19:10:59",
    "user_id": 170974,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 19:11:04",
    "user_id": 180937,
    "lab": "pygame\u5f00\u53d1\u6253\u98de\u673a\u6e38\u620f",
    "course": "pygame\u5f00\u53d1\u6253\u98de\u673a\u6e38\u620f"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 19:11:41",
    "user_id": 200101,
    "lab": "Bash\u4e2d\u7684\u7279\u6b8a\u5b57\u7b26\uff08\u4e0a\uff09",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 19:12:30",
    "user_id": 170963,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:13:39",
    "user_id": 170779,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 19:14:52",
    "user_id": 199994,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 19:14:56",
    "user_id": 170947,
    "lab": "\u7cfb\u7edf\u8c03\u7528",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 19:15:34",
    "user_id": 200036,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0b\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:15:37",
    "user_id": 170957,
    "lab": "\u57fa\u4e8e\u5185\u6838\u6808\u5207\u6362\u7684\u8fdb\u7a0b\u5207\u6362",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 19:15:40",
    "user_id": 170942,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 19:16:16",
    "user_id": 192596,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 19:16:29",
    "user_id": 170961,
    "lab": "\u6982\u8ff0",
    "course": "\u5b9e\u7528Linux Shell\u7f16\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 19:16:34",
    "user_id": 170979,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-03 19:19:48",
    "user_id": 170779,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 19:19:51",
    "user_id": 198234,
    "lab": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668",
    "course": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 19:20:19",
    "user_id": 24574,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:21:44",
    "user_id": 66652,
    "lab": "\u901a\u8fc7\u53cd\u6c47\u7f16\u4e00\u4e2a\u7b80\u5355\u7684C\u7a0b\u5e8f\uff0c\u5206\u6790\u6c47\u7f16\u4ee3\u7801\u7406\u89e3\u8ba1\u7b97\u673a\u662f\u5982\u4f55\u5de5\u4f5c\u7684",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 19:23:42",
    "user_id": 173346,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e00\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-03 19:25:12",
    "user_id": 53699,
    "lab": "Python\u6807\u51c6\u5e93\uff08\u4e2d\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 19:25:53",
    "user_id": 199599,
    "lab": "\u7ebf\u6027\u7ed3\u6784-\u7ebf\u6027\u8868",
    "course": "\u6570\u636e\u7ed3\u6784(\u65b0\u7248)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:25:57",
    "user_id": 170947,
    "lab": "\u8fdb\u7a0b\u8fd0\u884c\u8f68\u8ff9\u7684\u8ddf\u8e2a\u4e0e\u7edf\u8ba1",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:26:11",
    "user_id": 200065,
    "lab": "Java \u63a7\u5236\u8bed\u53e5",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:26:38",
    "user_id": 200027,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 19:26:49",
    "user_id": 74797,
    "lab": "\u7cfb\u7edf\u8c03\u7528",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 19:26:56",
    "user_id": 199991,
    "lab": "Hadoop\u4f2a\u5206\u5e03\u6a21\u5f0f\u914d\u7f6e\u90e8\u7f72",
    "course": "Hadoop\u90e8\u7f72\u53ca\u7ba1\u7406"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 19:27:07",
    "user_id": 59652,
    "lab": "\u6587\u4ef6IO\uff08\u4e8c\uff09",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:27:08",
    "user_id": 200110,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 19:28:58",
    "user_id": 171853,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:30:13",
    "user_id": 175182,
    "lab": "Java \u8bed\u8a00\u57fa\u7840",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:30:31",
    "user_id": 123828,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-03 19:30:38",
    "user_id": 200037,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:30:39",
    "user_id": 186139,
    "lab": "PythonChallenge_1",
    "course": "\u5168\u9762\u89e3\u6790PythonChallenge"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 19:30:42",
    "user_id": 170947,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 19:30:55",
    "user_id": 200110,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 19:31:10",
    "user_id": 190912,
    "lab": "Collabtive\u7cfb\u7edfSQL\u6ce8\u5165\u5b9e\u9a8c",
    "course": "Collabtive\u7cfb\u7edfSQL\u6ce8\u5165\u5b9e\u9a8c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 19:31:16",
    "user_id": 170963,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 19:31:42",
    "user_id": 197798,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:33:00",
    "user_id": 163952,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 19:33:32",
    "user_id": 199705,
    "lab": "PythonChallenge_1",
    "course": "\u5168\u9762\u89e3\u6790PythonChallenge"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 19:34:02",
    "user_id": 79972,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:35:19",
    "user_id": 200036,
    "lab": "\u4e2d\u7ea7\u6280\u80fd\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 19:35:38",
    "user_id": 170724,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 19:35:40",
    "user_id": 171718,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 19:37:45",
    "user_id": 193335,
    "lab": "\u521d\u8bc6MySQL",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:38:58",
    "user_id": 186082,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 19:40:32",
    "user_id": 199994,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 19:40:45",
    "user_id": 128189,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-03 19:41:21",
    "user_id": 141939,
    "lab": "\u8f93\u5165\u548c\u8f93\u51fa",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 19:42:02",
    "user_id": 200117,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 19:42:21",
    "user_id": 200118,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 19:42:23",
    "user_id": 189427,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:43:11",
    "user_id": 163952,
    "lab": "IP\u7f51\u9645\u534f\u8bae",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:44:03",
    "user_id": 175182,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:44:08",
    "user_id": 170947,
    "lab": "\u8bfe\u7a0b\u4ecb\u7ecd",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 19:44:25",
    "user_id": 198759,
    "lab": "\u521d\u8bc6HTML",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 19:46:15",
    "user_id": 170963,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 19:47:10",
    "user_id": 200119,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e00\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 19:47:39",
    "user_id": 175185,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 19:47:59",
    "user_id": 170947,
    "lab": "GCC\u7684\u4f7f\u7528",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 19:48:09",
    "user_id": 157318,
    "lab": "Linux\u57fa\u7840\u77e5\u8bc6\u4e0e\u5e38\u7528\u547d\u4ee4",
    "course": "\u5b9e\u7528Linux Shell\u7f16\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 19:48:14",
    "user_id": 170961,
    "lab": "Linux\u57fa\u7840\u77e5\u8bc6\u4e0e\u5e38\u7528\u547d\u4ee4",
    "course": "\u5b9e\u7528Linux Shell\u7f16\u7a0b"
  },
  {
    "minutes": 96,
    "created_at": "2016-05-03 19:48:38",
    "user_id": 50252,
    "lab": "MySQL\u57fa\u672c\u64cd\u4f5c",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 19:48:55",
    "user_id": 170979,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:49:07",
    "user_id": 170768,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 19:49:45",
    "user_id": 200089,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 19:50:16",
    "user_id": 170968,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 19:50:35",
    "user_id": 191868,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 19:50:53",
    "user_id": 170831,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 19:51:14",
    "user_id": 190912,
    "lab": "Elgg\u7cfb\u7edf\u8de8\u7ad9\u811a\u672c\u653b\u51fb\u5b9e\u9a8c",
    "course": "Elgg\u7cfb\u7edf\u8de8\u7ad9\u811a\u672c\u653b\u51fb\u5b9e\u9a8c"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-03 19:51:58",
    "user_id": 182902,
    "lab": "\u6587\u4ef6IO\uff08\u4e00\uff09",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 19:52:33",
    "user_id": 22216,
    "lab": "\u57fa\u4e8escrapy\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u57fa\u4e8escrapy\u722c\u866b\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6(python)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 19:52:42",
    "user_id": 173346,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e8c\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:53:09",
    "user_id": 170946,
    "lab": "\u8fdb\u7a0b\u8fd0\u884c\u8f68\u8ff9\u7684\u8ddf\u8e2a\u4e0e\u7edf\u8ba1",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 19:54:05",
    "user_id": 171960,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 19:54:11",
    "user_id": 107571,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 19:54:40",
    "user_id": 175172,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 19:55:09",
    "user_id": 170979,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 19:55:11",
    "user_id": 131507,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:55:14",
    "user_id": 192600,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 19:55:39",
    "user_id": 200118,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:55:41",
    "user_id": 186082,
    "lab": "\u94fe\u8def\u5c42\u4ecb\u7ecd",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 19:55:49",
    "user_id": 199954,
    "lab": "\u57fa\u672c\u8bed\u6cd5",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 19:56:28",
    "user_id": 198126,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 19:57:50",
    "user_id": 171720,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 19:58:42",
    "user_id": 175182,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 19:59:07",
    "user_id": 199991,
    "lab": "\u5173\u4e8eMapReduce",
    "course": "\u300aHadoop\u6743\u5a01\u6307\u5357\u300b\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:01:58",
    "user_id": 163952,
    "lab": "\u7f51\u7edc\u5c42\u5176\u5b83\u534f\u8bae",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:02:18",
    "user_id": 199337,
    "lab": "\u8bfb\u5199\u6587\u672c\u683c\u5f0f\u7684\u6570\u636e",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python \u6570\u636e\u5206\u6790\uff08\u4e00\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:02:55",
    "user_id": 199954,
    "lab": "PHP\u7b80\u4ecb",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 20:03:10",
    "user_id": 170841,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 38,
    "created_at": "2016-05-03 20:03:25",
    "user_id": 175181,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:04:10",
    "user_id": 173346,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e09\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:04:15",
    "user_id": 200009,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:04:22",
    "user_id": 59652,
    "lab": "\u591a\u8fdb\u7a0b\uff08\u4e00\uff09",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:05:13",
    "user_id": 199991,
    "lab": "Hadoop\u5206\u5e03\u5f0f\u6587\u4ef6\u7cfb\u7edf",
    "course": "\u300aHadoop\u6743\u5a01\u6307\u5357\u300b\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 20:05:17",
    "user_id": 46238,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:05:56",
    "user_id": 65441,
    "lab": "Hibernate - HQL \u67e5\u8be2",
    "course": "Hibernate\u6846\u67b6\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:06:00",
    "user_id": 81951,
    "lab": "\u5b57\u7b26\u4e32\uff08\u4e8c\uff09",
    "course": "\u7ecf\u5178\u7b97\u6cd5\u89e3\u9898\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:06:16",
    "user_id": 200127,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-03 20:06:29",
    "user_id": 198759,
    "lab": "HTML\u6587\u672c",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 20:07:27",
    "user_id": 174172,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:07:27",
    "user_id": 200101,
    "lab": "Bash\u4e2d\u7684\u7279\u6b8a\u5b57\u7b26\uff08\u4e0b\uff09",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:07:28",
    "user_id": 170975,
    "lab": "\u57fa\u4e8e\u5185\u6838\u6808\u5207\u6362\u7684\u8fdb\u7a0b\u5207\u6362",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:07:29",
    "user_id": 182235,
    "lab": "ShellShock \u653b\u51fb\u5b9e\u9a8c",
    "course": "ShellShock \u653b\u51fb\u5b9e\u9a8c"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 20:08:34",
    "user_id": 200128,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:09:21",
    "user_id": 170831,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:09:47",
    "user_id": 181476,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:09:54",
    "user_id": 200096,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 20:10:49",
    "user_id": 200131,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:10:54",
    "user_id": 199337,
    "lab": "\u4f7f\u7528 HTML \u548c Web API",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python \u6570\u636e\u5206\u6790\uff08\u4e00\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 20:11:10",
    "user_id": 197798,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 20:11:22",
    "user_id": 170947,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 20:11:38",
    "user_id": 190677,
    "lab": "Python \u7834\u89e3\u9a8c\u8bc1\u7801",
    "course": "Python \u7834\u89e3\u9a8c\u8bc1\u7801"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 20:11:41",
    "user_id": 176915,
    "lab": "\u6570\u636e\u7c7b\u578b\uff08\u4e00\uff09",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:11:47",
    "user_id": 192596,
    "lab": "\u5f00\u53d1\u73af\u5883\u548c\u5256\u6790\u7b2c\u4e00\u4e2a C \u8bed\u8a00",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 20:12:24",
    "user_id": 163952,
    "lab": "\u4f20\u8f93\u5c42\uff1aUDP\u534f\u8bae",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-03 20:12:44",
    "user_id": 197404,
    "lab": "HTML\u8d85\u6587\u672c\uff08\u4e00\uff09",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:13:01",
    "user_id": 173346,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u56db\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 20:13:31",
    "user_id": 175172,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 20:14:18",
    "user_id": 199991,
    "lab": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668",
    "course": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 20:14:55",
    "user_id": 200096,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 20:14:58",
    "user_id": 170942,
    "lab": "\u64cd\u4f5c\u7cfb\u7edf\u7684\u5f15\u5bfc",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:15:19",
    "user_id": 199337,
    "lab": "\u4f7f\u7528\u6570\u636e\u5e93",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python \u6570\u636e\u5206\u6790\uff08\u4e00\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 20:15:36",
    "user_id": 181476,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 114,
    "created_at": "2016-05-03 20:15:57",
    "user_id": 175171,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:17:50",
    "user_id": 171853,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:18:50",
    "user_id": 173346,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e94\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:19:00",
    "user_id": 200127,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:19:04",
    "user_id": 198126,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:19:18",
    "user_id": 199954,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:19:20",
    "user_id": 170975,
    "lab": "\u57fa\u4e8e\u5185\u6838\u6808\u5207\u6362\u7684\u8fdb\u7a0b\u5207\u6362",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 120,
    "created_at": "2016-05-03 20:20:36",
    "user_id": 175280,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 20:21:50",
    "user_id": 171853,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 20:22:17",
    "user_id": 168628,
    "lab": "\u57fa\u7840\u7bc7 - \u5176\u4ed6\u57fa\u672c\u64cd\u4f5c",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:22:20",
    "user_id": 174172,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:22:22",
    "user_id": 168759,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 20:22:31",
    "user_id": 175180,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e94",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 20:22:31",
    "user_id": 188357,
    "lab": "\u6a21\u5757\u5316\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:23:18",
    "user_id": 173161,
    "lab": "\u57fa\u672c\u6982\u5ff5",
    "course": "\u6570\u636e\u7ed3\u6784(\u65b0\u7248)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:23:32",
    "user_id": 197089,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 20:24:06",
    "user_id": 170947,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 20:25:46",
    "user_id": 197948,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 20:25:51",
    "user_id": 163952,
    "lab": "\u4f20\u8f93\u5c42\uff1aTCP\u534f\u8bae",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:26:22",
    "user_id": 173346,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u516d\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 20:26:22",
    "user_id": 199868,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 20:26:57",
    "user_id": 199337,
    "lab": "\u591a\u5f20\u56fe\u7247\u62fc\u63a5\u4e0e\u5c42\u53e0",
    "course": "\u591a\u5f20\u56fe\u7247\u62fc\u63a5\u4e0e\u5c42\u53e0"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 20:27:09",
    "user_id": 196366,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:27:39",
    "user_id": 192310,
    "lab": "JDBC \u63a5\u53e3",
    "course": "JDBC \u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 75,
    "created_at": "2016-05-03 20:27:40",
    "user_id": 171963,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:28:30",
    "user_id": 174172,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 20:28:31",
    "user_id": 59303,
    "lab": "\u535a\u5ba2\u7684\u9996\u9875\u4e0e\u6295\u7a3f\u8bbe\u8ba1",
    "course": "\u57fa\u4e8eGO\u8bed\u8a00Revel\u6846\u67b6\u548cmgo\u7684\u535a\u5ba2"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 20:28:39",
    "user_id": 192596,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 20:29:02",
    "user_id": 199954,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 63,
    "created_at": "2016-05-03 20:29:33",
    "user_id": 199856,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:30:35",
    "user_id": 114954,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 20:30:37",
    "user_id": 13963,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:30:51",
    "user_id": 199703,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 20:31:34",
    "user_id": 199991,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 20:31:40",
    "user_id": 173414,
    "lab": "SciPy - \u79d1\u5b66\u8ba1\u7b97\u5e93\uff08\u4e0b\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 20:31:59",
    "user_id": 200037,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0b\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 20:32:02",
    "user_id": 170757,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:32:28",
    "user_id": 194718,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 20:33:05",
    "user_id": 199570,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e00\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 20:33:38",
    "user_id": 107571,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:33:49",
    "user_id": 200096,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 20:34:12",
    "user_id": 29851,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 20:34:12",
    "user_id": 200137,
    "lab": "git\u4ecb\u7ecd",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:34:29",
    "user_id": 200128,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 20:34:56",
    "user_id": 200117,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e00\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:35:22",
    "user_id": 170775,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:35:25",
    "user_id": 173346,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u516b\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 20:36:26",
    "user_id": 171960,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 20:37:04",
    "user_id": 200089,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:37:11",
    "user_id": 119998,
    "lab": "java.io \u5305\u2014\u2014\u5b57\u8282\u6d41",
    "course": "JDK \u6838\u5fc3 API"
  },
  {
    "minutes": 66,
    "created_at": "2016-05-03 20:37:23",
    "user_id": 175180,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 20:38:26",
    "user_id": 175137,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 20:38:34",
    "user_id": 198335,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 20:38:41",
    "user_id": 174172,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:38:52",
    "user_id": 199994,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 81,
    "created_at": "2016-05-03 20:39:04",
    "user_id": 172083,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 20:39:38",
    "user_id": 96265,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:40:21",
    "user_id": 194989,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 20:40:52",
    "user_id": 175490,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 20:41:24",
    "user_id": 199868,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 20:41:31",
    "user_id": 200096,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:41:39",
    "user_id": 173346,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e5d\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:42:19",
    "user_id": 175176,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 20:43:37",
    "user_id": 27420,
    "lab": "c\u8bed\u8a00\u5229\u7528epoll\u5b9e\u73b0\u804a\u5929\u5ba4",
    "course": "C\u8bed\u8a00\u5229\u7528epoll\u5b9e\u73b0\u9ad8\u5e76\u53d1\u804a\u5929\u5ba4"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 20:44:29",
    "user_id": 199994,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:44:45",
    "user_id": 198180,
    "lab": "Java \u7c7b\u4e0e\u5bf9\u8c61",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 20:45:15",
    "user_id": 79972,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-03 20:45:53",
    "user_id": 200056,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 20:45:56",
    "user_id": 186082,
    "lab": "IP\u7f51\u9645\u534f\u8bae",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 20:46:10",
    "user_id": 33268,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 20:46:14",
    "user_id": 107571,
    "lab": "\u5b57\u7b26\u4e32\u4e0e\u5305\u88c5\u7c7b",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:46:43",
    "user_id": 168628,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:47:24",
    "user_id": 178992,
    "lab": "ShellShock \u653b\u51fb\u5b9e\u9a8c",
    "course": "ShellShock \u653b\u51fb\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:47:42",
    "user_id": 178455,
    "lab": "\u7b2c\u4e00\u7ae0  \u5b66\u4f1aC++\u683c\u5f0f\u7684\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:47:43",
    "user_id": 199589,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:49:15",
    "user_id": 192596,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e00\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:49:47",
    "user_id": 173346,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u5341\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 20:49:47",
    "user_id": 176880,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 20:50:01",
    "user_id": 174172,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-03 20:50:22",
    "user_id": 199991,
    "lab": "Hive \u5b89\u88c5\u914d\u7f6e",
    "course": "HIVE\u6559\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 20:50:27",
    "user_id": 128189,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 20:50:31",
    "user_id": 13963,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 20:50:58",
    "user_id": 194384,
    "lab": "Bash\u4e2d\u7684\u7279\u6b8a\u5b57\u7b26\uff08\u4e0a\uff09",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 20:51:06",
    "user_id": 175181,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:52:47",
    "user_id": 200037,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:53:54",
    "user_id": 199817,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:54:37",
    "user_id": 196366,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:54:52",
    "user_id": 200027,
    "lab": "Python \u7834\u89e3\u9a8c\u8bc1\u7801",
    "course": "Python \u7834\u89e3\u9a8c\u8bc1\u7801"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 20:55:11",
    "user_id": 198759,
    "lab": "HTML\u8d85\u6587\u672c\uff08\u4e00\uff09",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:55:33",
    "user_id": 171970,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 20:55:35",
    "user_id": 167421,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:56:35",
    "user_id": 198126,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:56:47",
    "user_id": 199994,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 20:56:52",
    "user_id": 175137,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 57,
    "created_at": "2016-05-03 20:58:33",
    "user_id": 185934,
    "lab": "LAMP\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "LAMP\u90e8\u7f72\u53ca\u914d\u7f6e"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-03 20:58:35",
    "user_id": 199394,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 20:58:41",
    "user_id": 199817,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 20:59:08",
    "user_id": 163952,
    "lab": "\u5e94\u7528\u5c42\u534f\u8bae\u4e00",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 20:59:16",
    "user_id": 171685,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 20:59:47",
    "user_id": 199589,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 21:00:03",
    "user_id": 170757,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 21:01:13",
    "user_id": 200101,
    "lab": "\u5f15\u7528\u548c\u8f6c\u4e49",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 11,
    "created_at": "2016-05-03 21:01:13",
    "user_id": 197330,
    "lab": "\u7cfb\u7edf\u8c03\u7528",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 21:01:30",
    "user_id": 160950,
    "lab": "c\u8bed\u8a00\u5236\u4f5c2048",
    "course": "C\u8bed\u8a00\u5236\u4f5c2048"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 21:02:26",
    "user_id": 197799,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:03:08",
    "user_id": 200147,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:03:13",
    "user_id": 199610,
    "lab": "python\u751f\u6210\u6c49\u5b57\u56fe\u7247\u5b57\u5e93",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011python\u751f\u6210\u6c49\u5b57\u56fe\u7247\u5b57\u5e93"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 21:03:50",
    "user_id": 175181,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-03 21:04:20",
    "user_id": 31183,
    "lab": "\u5faa\u73af\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 21:05:26",
    "user_id": 170775,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:06:05",
    "user_id": 138684,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:06:13",
    "user_id": 171720,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 21:07:01",
    "user_id": 187235,
    "lab": "\u53d8\u91cf\u91cd\u6e38",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 21:07:02",
    "user_id": 200103,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:07:18",
    "user_id": 200128,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 21:08:18",
    "user_id": 199570,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e00\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 21:08:22",
    "user_id": 199994,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:08:30",
    "user_id": 126960,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:08:38",
    "user_id": 200096,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:08:59",
    "user_id": 155319,
    "lab": "Fragment\u7b80\u4ecb\u53ca\u57fa\u672c\u4f7f\u7528",
    "course": "Android\u5c0f\u6848\u4f8b - Fragment\uff08\u7247\u6bb5\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 21:10:01",
    "user_id": 171720,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 21:10:49",
    "user_id": 186082,
    "lab": "\u7f51\u7edc\u5c42\u5176\u5b83\u534f\u8bae",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 21:11:08",
    "user_id": 199817,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:11:09",
    "user_id": 198056,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:11:59",
    "user_id": 200153,
    "lab": "\u8bfe\u7a0b\u57fa\u7840\u5305\uff08\u4e0a\uff09\uff0d\u5355\u9009\u7c7b\u578b\u8868\u5355\u81ea\u52a8\u63d0\u4ea4",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python\u81ea\u52a8\u586b\u95ee\u5377\u661f"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 21:12:31",
    "user_id": 176445,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:12:36",
    "user_id": 198180,
    "lab": "Java \u7ee7\u627f",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:12:57",
    "user_id": 200155,
    "lab": "\u8bfe\u7a0b\u57fa\u7840\u5305\uff08\u4e0a\uff09\uff0d\u5355\u9009\u7c7b\u578b\u8868\u5355\u81ea\u52a8\u63d0\u4ea4",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python\u81ea\u52a8\u586b\u95ee\u5377\u661f"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:13:03",
    "user_id": 196636,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:13:38",
    "user_id": 113542,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u7684\u7ea6\u675f",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:13:47",
    "user_id": 119998,
    "lab": "\u6cdb\u578b",
    "course": "JDK \u6838\u5fc3 API"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:14:27",
    "user_id": 166724,
    "lab": "HTML5 \u672c\u5730\u88c1\u526a\u56fe\u7247",
    "course": "\u57fa\u4e8e HTML5 \u5b9e\u73b0\u672c\u5730\u56fe\u7247\u88c1\u526a"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:14:31",
    "user_id": 197799,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 21:17:15",
    "user_id": 163952,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:17:28",
    "user_id": 146207,
    "lab": "\u9762\u5411\u5bf9\u8c61\u7f16\u7a0b",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 63,
    "created_at": "2016-05-03 21:17:44",
    "user_id": 154439,
    "lab": "LAMP\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "LAMP\u90e8\u7f72\u53ca\u914d\u7f6e"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 21:18:03",
    "user_id": 174172,
    "lab": "Java \u8bed\u8a00\u57fa\u7840",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 21:18:04",
    "user_id": 16806,
    "lab": "\u7c7b\u548c\u5bf9\u8c61\uff08\u4e00\uff09",
    "course": "Scala\u5f00\u53d1\u6559\u7a0b"
  },
  {
    "minutes": 66,
    "created_at": "2016-05-03 21:18:39",
    "user_id": 171962,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:18:45",
    "user_id": 107571,
    "lab": "\u96c6\u5408\u7c7b\u6846\u67b6",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 21:18:53",
    "user_id": 199010,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:20:21",
    "user_id": 171584,
    "lab": "\u7b2c10-11\u5468\u8bfe\u5802\u5b9e\u9a8c-\u5b9e\u9a8c\u4e8c \u7ee7\u627f\u6027\u7684\u5b9e\u73b0\uff081-2\uff09",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:20:51",
    "user_id": 79270,
    "lab": "\u96c6\u5408\u7c7b\u6846\u67b6",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:21:30",
    "user_id": 172072,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 21:21:45",
    "user_id": 195375,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:22:14",
    "user_id": 191690,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0b\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 21:22:30",
    "user_id": 200089,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 21:22:42",
    "user_id": 200153,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:22:55",
    "user_id": 114954,
    "lab": "\u9002\u914d\u5668\u6a21\u5f0f",
    "course": "Java\u8fdb\u9636\u4e4b\u8bbe\u8ba1\u6a21\u5f0f"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:23:02",
    "user_id": 66456,
    "lab": "\u4e00\u4e2a\u6700\u7b80\u5355\u7684 express \u5e94\u7528",
    "course": "Node.js\u5305\u6559\u4e0d\u5305\u4f1a"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 21:23:19",
    "user_id": 197798,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 21:23:24",
    "user_id": 197404,
    "lab": "HTML\u8d85\u6587\u672c\uff08\u4e00\uff09",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 21:23:48",
    "user_id": 194384,
    "lab": "Bash\u4e2d\u7684\u7279\u6b8a\u5b57\u7b26\uff08\u4e0b\uff09",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:23:54",
    "user_id": 79901,
    "lab": "\u521d\u8bc6HTML",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-03 21:24:11",
    "user_id": 199570,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e8c\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 21:25:52",
    "user_id": 169883,
    "lab": "\u901a\u8fc7\u53cd\u6c47\u7f16\u4e00\u4e2a\u7b80\u5355\u7684C\u7a0b\u5e8f\uff0c\u5206\u6790\u6c47\u7f16\u4ee3\u7801\u7406\u89e3\u8ba1\u7b97\u673a\u662f\u5982\u4f55\u5de5\u4f5c\u7684",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 21:26:27",
    "user_id": 171720,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:26:36",
    "user_id": 178526,
    "lab": "\u7b2c\u4e8c\u7ae0 \u7c7b\u548c\u5bf9\u8c61",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:26:54",
    "user_id": 186290,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 21:27:15",
    "user_id": 170573,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:27:29",
    "user_id": 138684,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:27:32",
    "user_id": 168010,
    "lab": "c\u8bed\u8a00\u5229\u7528epoll\u5b9e\u73b0\u804a\u5929\u5ba4",
    "course": "C\u8bed\u8a00\u5229\u7528epoll\u5b9e\u73b0\u9ad8\u5e76\u53d1\u804a\u5929\u5ba4"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 21:28:26",
    "user_id": 95911,
    "lab": "\u6570\u636e\u5e93\u548c\u96c6\u5408\u57fa\u672c\u64cd\u4f5c",
    "course": "MongoDB \u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:28:53",
    "user_id": 174172,
    "lab": "Java  \u8fd0\u7b97\u7b26",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:29:03",
    "user_id": 171685,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 21:29:30",
    "user_id": 170775,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 21:30:02",
    "user_id": 200128,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:30:08",
    "user_id": 66456,
    "lab": "\u5b66\u4e60\u4f7f\u7528\u5916\u90e8\u6a21\u5757",
    "course": "Node.js\u5305\u6559\u4e0d\u5305\u4f1a"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 21:30:12",
    "user_id": 16806,
    "lab": "\u7c7b\u548c\u5bf9\u8c61\uff08\u4e00\uff09",
    "course": "Scala\u5f00\u53d1\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:30:18",
    "user_id": 87845,
    "lab": "pandas \u56de\u987e",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python \u6570\u636e\u5206\u6790\uff08\u4e00\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:30:24",
    "user_id": 2203,
    "lab": "Spark RDD\u4e0e\u7f16\u7a0b\u6a21\u578b",
    "course": "Spark \u5927\u6570\u636e\u52a8\u624b\u5b9e\u9a8c"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 21:30:34",
    "user_id": 149901,
    "lab": "\u521b\u5efa\u4e91\u8bb0\u8d26\u9879\u76ee",
    "course": "\u57fa\u4e8edjango\u7684\u4e91\u8bb0\u8d26\u9879\u76ee\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:30:49",
    "user_id": 200157,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 21:31:08",
    "user_id": 188357,
    "lab": "\u6a21\u5757\u5316\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 21:31:28",
    "user_id": 175490,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:31:53",
    "user_id": 200159,
    "lab": "Rails \u4ecb\u7ecd\u4e0e\u73af\u5883\u914d\u7f6e",
    "course": "Rails\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 21:33:09",
    "user_id": 175181,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:33:13",
    "user_id": 200162,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 63,
    "created_at": "2016-05-03 21:33:38",
    "user_id": 199010,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 21:34:05",
    "user_id": 198633,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 21:34:19",
    "user_id": 193900,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:34:23",
    "user_id": 173414,
    "lab": "SciPy - \u79d1\u5b66\u8ba1\u7b97\u5e93\uff08\u4e0b\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 21:35:36",
    "user_id": 200165,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 21:35:40",
    "user_id": 199991,
    "lab": "HBase\u5b89\u88c5\u914d\u7f6e",
    "course": "HBASE\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:35:41",
    "user_id": 187499,
    "lab": "HTML5 \u672c\u5730\u88c1\u526a\u56fe\u7247",
    "course": "\u57fa\u4e8e HTML5 \u5b9e\u73b0\u672c\u5730\u56fe\u7247\u88c1\u526a"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:36:46",
    "user_id": 186290,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:36:47",
    "user_id": 42272,
    "lab": "c\u8bed\u8a00\u5229\u7528epoll\u5b9e\u73b0\u804a\u5929\u5ba4",
    "course": "C\u8bed\u8a00\u5229\u7528epoll\u5b9e\u73b0\u9ad8\u5e76\u53d1\u804a\u5929\u5ba4"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:37:25",
    "user_id": 174172,
    "lab": "Java \u63a7\u5236\u8bed\u53e5",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 21:37:25",
    "user_id": 171841,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 21:37:56",
    "user_id": 200056,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:38:01",
    "user_id": 107571,
    "lab": "\u8bbe\u8ba1\u6a21\u5f0f\u7b80\u4ecb",
    "course": "Java\u8fdb\u9636\u4e4b\u8bbe\u8ba1\u6a21\u5f0f"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 21:38:10",
    "user_id": 176880,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 21:38:22",
    "user_id": 199394,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:38:23",
    "user_id": 193472,
    "lab": "Flask\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:38:47",
    "user_id": 200170,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:38:48",
    "user_id": 199307,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 21:39:41",
    "user_id": 200162,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:40:19",
    "user_id": 200157,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:41:10",
    "user_id": 200128,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:41:26",
    "user_id": 187499,
    "lab": "JavaScript \u5b9e\u73b0\u60c5\u4eba\u8282\u73ab\u7470",
    "course": "\u57fa\u4e8e JavaScript \u5b9e\u73b0\u73ab\u7470\u82b1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:41:48",
    "user_id": 200101,
    "lab": "\u9000\u51fa\u548c\u9000\u51fa\u72b6\u6001\u7801",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:42:29",
    "user_id": 89043,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 21:43:23",
    "user_id": 173161,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-03 21:43:25",
    "user_id": 199817,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:43:52",
    "user_id": 192968,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 21:44:13",
    "user_id": 173414,
    "lab": "SciPy - \u79d1\u5b66\u8ba1\u7b97\u5e93\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 21:44:34",
    "user_id": 170757,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:44:46",
    "user_id": 163952,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 21:45:43",
    "user_id": 48851,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 21:46:48",
    "user_id": 199480,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:46:50",
    "user_id": 175181,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e94",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:47:06",
    "user_id": 138684,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:47:10",
    "user_id": 53699,
    "lab": "Python\u6807\u51c6\u5e93\uff08\u4e2d\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 21:47:20",
    "user_id": 95911,
    "lab": "\u6570\u636e\u67e5\u8be2",
    "course": "MongoDB \u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:49:28",
    "user_id": 149901,
    "lab": "\u521b\u5efaaccounts\u6a21\u5757\u7684\u6846\u67b6",
    "course": "\u57fa\u4e8edjango\u7684\u4e91\u8bb0\u8d26\u9879\u76ee\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:50:59",
    "user_id": 107571,
    "lab": "\u5de5\u5382\u6a21\u5f0f",
    "course": "Java\u8fdb\u9636\u4e4b\u8bbe\u8ba1\u6a21\u5f0f"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 21:51:12",
    "user_id": 199866,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-03 21:51:19",
    "user_id": 200117,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e8c\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:51:23",
    "user_id": 200128,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:51:48",
    "user_id": 175181,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 21:51:53",
    "user_id": 171685,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 21:52:09",
    "user_id": 170775,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 21:52:36",
    "user_id": 6102,
    "lab": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c",
    "course": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:52:41",
    "user_id": 193472,
    "lab": "Flask\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:52:42",
    "user_id": 200162,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 21:52:50",
    "user_id": 187208,
    "lab": "\u6c47\u7f16\u8bed\u8a00\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u90d1\u6653\u8587\u7f16\u8457\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 21:53:12",
    "user_id": 198915,
    "lab": "Java  \u8fd0\u7b97\u7b26",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 21:53:22",
    "user_id": 196306,
    "lab": "DOS\u53caDEBUG\u4ecb\u7ecd",
    "course": "\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u90d1\u6653\u8587\u7f16\u8457\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:53:25",
    "user_id": 199307,
    "lab": "\u5f00\u53d1\u73af\u5883\u548c\u5256\u6790\u7b2c\u4e00\u4e2a C \u8bed\u8a00",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 21:53:27",
    "user_id": 200177,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 21:54:37",
    "user_id": 187121,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:54:58",
    "user_id": 149901,
    "lab": "\u521b\u5efa\u4e91\u8bb0\u8d26\u9879\u76ee",
    "course": "\u57fa\u4e8edjango\u7684\u4e91\u8bb0\u8d26\u9879\u76ee\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 21:55:15",
    "user_id": 200128,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 21:55:51",
    "user_id": 49702,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:55:52",
    "user_id": 171720,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:55:52",
    "user_id": 198200,
    "lab": "\u6253\u9020\u7f51\u9875\u7248\u300c\u5927\u767d\u300d- Baymax",
    "course": "\u7eaf CSS \u6253\u9020\u7f51\u9875\u7248\u300c\u5927\u767d\u300d"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 21:56:03",
    "user_id": 199232,
    "lab": "pandas \u56de\u987e",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python \u6570\u636e\u5206\u6790\uff08\u4e00\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 21:57:08",
    "user_id": 106481,
    "lab": "\u8bfe\u7a0b\u7ba1\u7406\u7cfb\u7edf",
    "course": "C++ \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-03 21:57:17",
    "user_id": 171963,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 21:57:48",
    "user_id": 197928,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:58:05",
    "user_id": 114954,
    "lab": "java.lang \u5305",
    "course": "JDK \u6838\u5fc3 API"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 21:58:07",
    "user_id": 200157,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 21:59:13",
    "user_id": 199800,
    "lab": "C\u8bed\u8a00\u5b9e\u73b0ping\u7a0b\u5e8f",
    "course": "C\u8bed\u8a00\u5b9e\u73b0ping\u7a0b\u5e8f"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 21:59:44",
    "user_id": 127224,
    "lab": "\u8def\u7531",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:00:09",
    "user_id": 194989,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 22:00:50",
    "user_id": 195375,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e8c\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:00:54",
    "user_id": 199813,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:01:33",
    "user_id": 178526,
    "lab": "\u7b2c\u4e8c\u7ae0 \u7c7b\u548c\u5bf9\u8c61",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-03 22:02:00",
    "user_id": 23521,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 22:02:08",
    "user_id": 200162,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:02:22",
    "user_id": 149901,
    "lab": "\u521b\u5efa\u4e91\u8bb0\u8d26\u9879\u76ee",
    "course": "\u57fa\u4e8edjango\u7684\u4e91\u8bb0\u8d26\u9879\u76ee\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:02:32",
    "user_id": 171720,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:02:44",
    "user_id": 114954,
    "lab": "java.util \u5305",
    "course": "JDK \u6838\u5fc3 API"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 22:03:47",
    "user_id": 195227,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:04:35",
    "user_id": 197928,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:05:43",
    "user_id": 183988,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:06:37",
    "user_id": 193472,
    "lab": "Flask\u8fd0\u884c\u53ca\u8c03\u8bd5\u6a21\u5f0f",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:07:24",
    "user_id": 167421,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-03 22:07:26",
    "user_id": 199856,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:08:01",
    "user_id": 178526,
    "lab": "\u7b2c\u4e8c\u7ae0  \u7c7b\u548c\u5bf9\u8c61\uff082\uff09",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 22:08:37",
    "user_id": 200165,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:09:01",
    "user_id": 186082,
    "lab": "\u4f20\u8f93\u5c42\uff1aUDP\u534f\u8bae",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 22:09:24",
    "user_id": 200185,
    "lab": "\u8ba4\u8bc6J2SE",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 22:09:57",
    "user_id": 194260,
    "lab": "Nginx\u6a21\u5757\u5f00\u53d1\u5b9e\u9a8c",
    "course": "Linux Web\u8fd0\u7ef4\uff08Nginx\uff09\u5b9e\u6218 "
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 22:10:26",
    "user_id": 200184,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 22:10:30",
    "user_id": 199480,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 22:12:00",
    "user_id": 170890,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:12:14",
    "user_id": 198056,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 22:12:37",
    "user_id": 195978,
    "lab": "lab0\uff1aCoding!",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u5b9e\u9a8c\uff0d\u57fa\u4e8euCore OS"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:13:25",
    "user_id": 200128,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 78,
    "created_at": "2016-05-03 22:13:32",
    "user_id": 170757,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:14:06",
    "user_id": 195921,
    "lab": "Java \u7ee7\u627f",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:16:05",
    "user_id": 198729,
    "lab": "\u5bc6\u94a5\u52a0\u89e3\u5bc6\u5b9e\u9a8c\uff08\u4e0a\uff09",
    "course": "\u5bc6\u94a5\u52a0\u89e3\u5bc6\u5b9e\u9a8c"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 22:16:55",
    "user_id": 171685,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:16:56",
    "user_id": 172083,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:17:30",
    "user_id": 193769,
    "lab": "Linux\u57fa\u7840\u77e5\u8bc6\u4e0e\u5e38\u7528\u547d\u4ee4",
    "course": "\u5b9e\u7528Linux Shell\u7f16\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:17:33",
    "user_id": 95911,
    "lab": "\u5b57\u7b26\u4e32\uff08\u4e00\uff09",
    "course": "\u7ecf\u5178\u7b97\u6cd5\u89e3\u9898\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:17:42",
    "user_id": 141550,
    "lab": "C\u8bed\u8a00\u7248flappy_bird",
    "course": "C\u8bed\u8a00\u7248flappy_bird"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:18:01",
    "user_id": 122252,
    "lab": "\u521d\u8bc6GraphX",
    "course": "Spark\u57fa\u7840\u4e4bGraphX\u56fe\u8ba1\u7b97\u6846\u67b6\u5b66\u4e60"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 22:18:41",
    "user_id": 119886,
    "lab": "Swing\u5165\u95e8",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:18:50",
    "user_id": 170775,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 22:19:01",
    "user_id": 199863,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 22:19:13",
    "user_id": 48851,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:19:33",
    "user_id": 200192,
    "lab": "PHP\u7b80\u4ecb",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 22:19:46",
    "user_id": 200128,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 22:20:34",
    "user_id": 197912,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:20:35",
    "user_id": 197928,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:20:58",
    "user_id": 61590,
    "lab": "MySQL\u6570\u636e\u5e93\u5bf9\u8c61\u7ba1\u7406",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011MySQL\u6570\u636e\u5e93\u5bf9\u8c61\u7ba1\u7406"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:21:14",
    "user_id": 199232,
    "lab": "\u8bfb\u5199\u6587\u672c\u683c\u5f0f\u7684\u6570\u636e",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python \u6570\u636e\u5206\u6790\uff08\u4e00\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:21:50",
    "user_id": 63559,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 22:21:57",
    "user_id": 133579,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:22:10",
    "user_id": 121074,
    "lab": "\u591a\u8bf4,markdown\u548c\u4ee3\u7801\u9ad8\u4eae",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 22:22:28",
    "user_id": 195227,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:23:36",
    "user_id": 190677,
    "lab": "\u4ecb\u7ecd",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:23:46",
    "user_id": 176445,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 22:24:04",
    "user_id": 173414,
    "lab": "SciPy - \u79d1\u5b66\u8ba1\u7b97\u5e93\uff08\u4e0b\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:25:06",
    "user_id": 196306,
    "lab": "DOS\u53caDEBUG\u4ecb\u7ecd",
    "course": "\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u90d1\u6653\u8587\u7f16\u8457\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:25:17",
    "user_id": 200184,
    "lab": "\u5f00\u53d1\u73af\u5883\u548c\u5256\u6790\u7b2c\u4e00\u4e2a C \u8bed\u8a00",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 22:25:43",
    "user_id": 175080,
    "lab": "python\u751f\u6210\u6c49\u5b57\u56fe\u7247\u5b57\u5e93",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011python\u751f\u6210\u6c49\u5b57\u56fe\u7247\u5b57\u5e93"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 22:26:07",
    "user_id": 170758,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:26:17",
    "user_id": 52227,
    "lab": "MySQL\u6570\u636e\u5e93\u5bf9\u8c61\u7ba1\u7406",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011MySQL\u6570\u636e\u5e93\u5bf9\u8c61\u7ba1\u7406"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 22:26:44",
    "user_id": 144538,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:27:20",
    "user_id": 200047,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 22:27:28",
    "user_id": 197920,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 22:28:06",
    "user_id": 194384,
    "lab": "\u53d8\u91cf\u548c\u53c2\u6570",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 22:28:48",
    "user_id": 200165,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 22:29:10",
    "user_id": 171962,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:29:43",
    "user_id": 149901,
    "lab": "\u521b\u5efaaccounts\u6a21\u5757\u7684\u6846\u67b6",
    "course": "\u57fa\u4e8edjango\u7684\u4e91\u8bb0\u8d26\u9879\u76ee\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:29:53",
    "user_id": 191690,
    "lab": "SciPy - \u79d1\u5b66\u8ba1\u7b97\u5e93\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:30:57",
    "user_id": 170890,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 22:31:36",
    "user_id": 187121,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:33:21",
    "user_id": 171685,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 78,
    "created_at": "2016-05-03 22:35:28",
    "user_id": 172083,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:35:40",
    "user_id": 200199,
    "lab": "\u5f00\u53d1\u73af\u5883\u4ee5\u53ca\u9879\u76ee\u4e0eApp",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 22:35:52",
    "user_id": 199570,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e8c\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:35:55",
    "user_id": 174908,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 22:36:15",
    "user_id": 24574,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:37:52",
    "user_id": 136055,
    "lab": "Flask\u4ecb\u7ecd\u53ca\u5b89\u88c5",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:38:58",
    "user_id": 185934,
    "lab": "Apache \u914d\u7f6e",
    "course": "LAMP\u90e8\u7f72\u53ca\u914d\u7f6e"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 22:39:19",
    "user_id": 186093,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 22:39:25",
    "user_id": 175280,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:40:04",
    "user_id": 48851,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:40:08",
    "user_id": 175186,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 22:40:39",
    "user_id": 76108,
    "lab": "Makefile\u4f7f\u7528",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 22:40:56",
    "user_id": 166935,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-03 22:41:22",
    "user_id": 172003,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 22:41:36",
    "user_id": 79972,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 22:42:09",
    "user_id": 175182,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 22:42:24",
    "user_id": 200128,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:42:45",
    "user_id": 175176,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:43:06",
    "user_id": 174908,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:43:27",
    "user_id": 6432,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:43:58",
    "user_id": 200197,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 22:44:18",
    "user_id": 198423,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 22:44:21",
    "user_id": 2203,
    "lab": "Spark RDD\u4e0e\u7f16\u7a0b\u6a21\u578b",
    "course": "Spark \u5927\u6570\u636e\u52a8\u624b\u5b9e\u9a8c"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 22:44:22",
    "user_id": 149129,
    "lab": "Hadoop\u5355\u673a\u6a21\u5f0f\u5b89\u88c5",
    "course": "Hadoop\u90e8\u7f72\u53ca\u7ba1\u7406"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:45:02",
    "user_id": 199010,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 22:45:38",
    "user_id": 187121,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 22:45:53",
    "user_id": 133579,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 22:46:25",
    "user_id": 196306,
    "lab": "\u6307\u4ee4\u7cfb\u7edf\u4e0e\u5bfb\u5740\u65b9\u5f0f",
    "course": "\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u90d1\u6653\u8587\u7f16\u8457\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 22:46:44",
    "user_id": 113542,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u7684\u7ea6\u675f",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:46:59",
    "user_id": 200206,
    "lab": "\u521d\u8bc6Hadoop",
    "course": "\u300aHadoop\u6743\u5a01\u6307\u5357\u300b\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:47:17",
    "user_id": 200065,
    "lab": "Java \u63a7\u5236\u8bed\u53e5",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:47:26",
    "user_id": 183976,
    "lab": "Models\u548cAdmin\u4ee5\u53caViews\u548cURL",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 22:48:20",
    "user_id": 171963,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 22:49:00",
    "user_id": 195227,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:49:21",
    "user_id": 185934,
    "lab": "\u5982\u4f55\u5728 CentOS 7 \u4e0a\u5b89\u88c5 Docker",
    "course": "CentOS 7\u4f53\u9a8c\u8bfe"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 22:49:33",
    "user_id": 49702,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:51:44",
    "user_id": 166935,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-03 22:52:14",
    "user_id": 199570,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e8c\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 22:53:51",
    "user_id": 159405,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-03 22:54:14",
    "user_id": 175171,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-03 22:55:22",
    "user_id": 171415,
    "lab": "\u7b2c\u4e8c\u7ae0 \u7c7b\u548c\u5bf9\u8c61",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 22:56:36",
    "user_id": 196996,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:56:46",
    "user_id": 199599,
    "lab": "\u7ebf\u6027\u7ed3\u6784-\u7ebf\u6027\u8868",
    "course": "\u6570\u636e\u7ed3\u6784(\u65b0\u7248)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:56:48",
    "user_id": 185934,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:57:13",
    "user_id": 170758,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 22:57:19",
    "user_id": 200208,
    "lab": "Welcome to Django!",
    "course": "[\u5df2\u4e0b\u7ebf] Python Django Web\u6846\u67b6"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 22:59:21",
    "user_id": 24574,
    "lab": "Python \u6d41\u7a0b\u63a7\u5236",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 22:59:25",
    "user_id": 172804,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 35,
    "created_at": "2016-05-03 23:00:09",
    "user_id": 200212,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 23:00:29",
    "user_id": 200205,
    "lab": "C\u8bed\u8a00\u7248flappy_bird",
    "course": "C\u8bed\u8a00\u7248flappy_bird"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 23:01:48",
    "user_id": 175182,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 23:01:53",
    "user_id": 191690,
    "lab": "SciPy - \u79d1\u5b66\u8ba1\u7b97\u5e93\uff08\u4e0b\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 23:02:46",
    "user_id": 200128,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 23:03:08",
    "user_id": 195503,
    "lab": "\u7b2c\u4e8c\u7ae0 \u7c7b\u548c\u5bf9\u8c61",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 23:03:44",
    "user_id": 198423,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 23:04:01",
    "user_id": 200208,
    "lab": "Django\u5165\u95e8",
    "course": "[\u5df2\u4e0b\u7ebf] Python Django Web\u6846\u67b6"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 23:04:50",
    "user_id": 171902,
    "lab": "Hadoop\u4ecb\u7ecd\u53ca1.X\u4f2a\u5206\u5e03\u5f0f\u5b89\u88c5",
    "course": "BTBU-\u7814\u7a76\u751f2015\u7ea7-Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 23:04:54",
    "user_id": 149129,
    "lab": "Hadoop\u4f2a\u5206\u5e03\u6a21\u5f0f\u914d\u7f6e\u90e8\u7f72",
    "course": "Hadoop\u90e8\u7f72\u53ca\u7ba1\u7406"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 23:05:36",
    "user_id": 175176,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 23:06:24",
    "user_id": 116421,
    "lab": "\u4ecb\u7ecd",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 23:06:35",
    "user_id": 171962,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 23:07:21",
    "user_id": 174612,
    "lab": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c",
    "course": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 23:07:35",
    "user_id": 80242,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-03 23:07:45",
    "user_id": 76108,
    "lab": "\u6587\u4ef6IO\uff08\u4e00\uff09",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 23:08:37",
    "user_id": 200139,
    "lab": "HTML\u6587\u672c",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 23:09:39",
    "user_id": 133579,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 23:09:45",
    "user_id": 199938,
    "lab": "\u521d\u8bc6HTML",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-03 23:09:49",
    "user_id": 199856,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 23:11:20",
    "user_id": 194989,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 23:11:29",
    "user_id": 160138,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 23:11:59",
    "user_id": 164460,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 23:12:20",
    "user_id": 10668,
    "lab": "DOS\u53caDEBUG\u4ecb\u7ecd",
    "course": "\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u90d1\u6653\u8587\u7f16\u8457\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 23:12:26",
    "user_id": 24574,
    "lab": "\u6570\u636e\u7ed3\u6784",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 23:14:16",
    "user_id": 84362,
    "lab": "C \u8bed\u8a00\u6570\u7ec4",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 23:14:18",
    "user_id": 79105,
    "lab": "Flask \u6a21\u677f",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 23:14:54",
    "user_id": 200208,
    "lab": "\u521b\u5efa\u4e91\u8bb0\u8d26\u9879\u76ee",
    "course": "\u57fa\u4e8edjango\u7684\u4e91\u8bb0\u8d26\u9879\u76ee\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 23:15:14",
    "user_id": 92381,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-03 23:15:19",
    "user_id": 175182,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 23:16:20",
    "user_id": 195094,
    "lab": "\u7b2c\u4e00\u7ae0  \u5b66\u4f1aC++\u683c\u5f0f\u7684\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 23:16:55",
    "user_id": 198423,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-03 23:17:36",
    "user_id": 175280,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 23:20:08",
    "user_id": 174739,
    "lab": "\u7b2c9\u5468\u8bfe\u5802\u5b9e\u9a8c-\u5b9e\u9a8c1",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 23:20:09",
    "user_id": 200218,
    "lab": "git\u4ecb\u7ecd",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 57,
    "created_at": "2016-05-03 23:20:35",
    "user_id": 159405,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 23:20:49",
    "user_id": 80242,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 23:21:51",
    "user_id": 172003,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 23:22:25",
    "user_id": 146207,
    "lab": "\u5f00\u53d1\u73af\u5883\u4ee5\u53ca\u9879\u76ee\u4e0eApp",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-03 23:23:39",
    "user_id": 120292,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 23:27:41",
    "user_id": 200165,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 23:29:07",
    "user_id": 175176,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 23:30:35",
    "user_id": 133579,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 23:30:46",
    "user_id": 174739,
    "lab": "\u7b2c10-11\u5468\u8bfe\u5802\u5b9e\u9a8c-\u5b9e\u9a8c\u4e8c \u7ee7\u627f\u6027\u7684\u5b9e\u73b0\uff081-2\uff09",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 23:31:17",
    "user_id": 200217,
    "lab": "k-\u8fd1\u90bb\u7b97\u6cd5\u6539\u8fdb\u7ea6\u4f1a\u7f51\u7ad9\u914d\u5bf9\u6548\u679c",
    "course": "\u6df1\u5165\u5b66\u4e60\u300a\u673a\u5668\u5b66\u4e60\u5b9e\u6218\u300b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 23:33:52",
    "user_id": 195123,
    "lab": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c",
    "course": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 23:34:05",
    "user_id": 90310,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 23:34:25",
    "user_id": 198423,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 23:35:29",
    "user_id": 200220,
    "lab": "  HTML5\u4e24\u6b65\u5b9e\u73b0\u62fc\u56fe\u6e38\u620f",
    "course": "\u7f51\u9875\u7248\u62fc\u56fe\u6e38\u620f"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 23:35:31",
    "user_id": 192193,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 23:35:53",
    "user_id": 175176,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 23:35:58",
    "user_id": 195227,
    "lab": "\u521d\u8bc6HTML",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 23:36:35",
    "user_id": 68079,
    "lab": "Hive \u5b89\u88c5\u914d\u7f6e",
    "course": "HIVE\u6559\u7a0b"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-03 23:37:12",
    "user_id": 199863,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 23:38:53",
    "user_id": 198614,
    "lab": "\u57fa\u7840\u8bed\u6cd5",
    "course": "Ruby\u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 23:40:43",
    "user_id": 200116,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 23:40:56",
    "user_id": 119886,
    "lab": "\u591a\u7ebf\u7a0b\u7f16\u7a0b",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-03 23:41:24",
    "user_id": 198423,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 23:41:39",
    "user_id": 133579,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 23:43:15",
    "user_id": 2060,
    "lab": "Rails \u4ecb\u7ecd\u4e0e\u73af\u5883\u914d\u7f6e",
    "course": "Rails\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 23:43:27",
    "user_id": 74549,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 23:43:38",
    "user_id": 175170,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-03 23:43:53",
    "user_id": 172003,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 23:44:44",
    "user_id": 195227,
    "lab": "HTML\u6587\u672c",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 23:45:13",
    "user_id": 7216,
    "lab": "Spark \u7b80\u4ecb\u4e0e\u5b89\u88c5\uff08\u514d\u8d39\uff09",
    "course": "Spark \u5927\u6570\u636e\u52a8\u624b\u5b9e\u9a8c"
  },
  {
    "minutes": 102,
    "created_at": "2016-05-03 23:45:31",
    "user_id": 170757,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 23:47:40",
    "user_id": 175176,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-03 23:49:42",
    "user_id": 195123,
    "lab": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c",
    "course": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 23:50:37",
    "user_id": 194934,
    "lab": "Python \u7834\u89e3\u9a8c\u8bc1\u7801",
    "course": "Python \u7834\u89e3\u9a8c\u8bc1\u7801"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 23:52:52",
    "user_id": 200165,
    "lab": "Python\u6df1\u5165\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 23:53:45",
    "user_id": 133579,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-03 23:53:46",
    "user_id": 68079,
    "lab": "Mahout \u5b89\u88c5\u914d\u7f6e",
    "course": "Mahout\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 23:53:53",
    "user_id": 147386,
    "lab": "\u6570\u636e\u7c7b\u578b\uff08\u4e8c\uff09",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-03 23:54:05",
    "user_id": 200212,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-03 23:55:12",
    "user_id": 195978,
    "lab": "lab0\uff1aCoding!",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u5b9e\u9a8c\uff0d\u57fa\u4e8euCore OS"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-03 23:56:09",
    "user_id": 172083,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-03 23:57:52",
    "user_id": 200218,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-03 23:59:13",
    "user_id": 197798,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 00:00:37",
    "user_id": 187286,
    "lab": "\u4ecb\u7ecd",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 00:00:53",
    "user_id": 172003,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 00:01:46",
    "user_id": 74797,
    "lab": "gdb\u4f7f\u7528",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 00:03:50",
    "user_id": 175170,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-04 00:04:14",
    "user_id": 197912,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 00:07:11",
    "user_id": 172003,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 00:09:43",
    "user_id": 170724,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 66,
    "created_at": "2016-05-04 00:11:31",
    "user_id": 175171,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 00:11:54",
    "user_id": 175176,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-04 00:13:42",
    "user_id": 199863,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 00:13:45",
    "user_id": 57011,
    "lab": "\u7b97\u6cd5-\u6570\u5b66\u76f8\u5173\uff08Math\uff09",
    "course": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 00:16:45",
    "user_id": 175182,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-04 00:17:06",
    "user_id": 187286,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-04 00:21:08",
    "user_id": 175176,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 00:24:57",
    "user_id": 190677,
    "lab": "Python \u7834\u89e3\u9a8c\u8bc1\u7801",
    "course": "Python \u7834\u89e3\u9a8c\u8bc1\u7801"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 00:26:44",
    "user_id": 131595,
    "lab": "\u57fa\u7840\u6b63\u5219\u8868\u8fbe\u5f0f\u4ecb\u7ecd\u4e0e\u7ec3\u4e60",
    "course": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 00:29:42",
    "user_id": 171863,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 00:30:50",
    "user_id": 147386,
    "lab": "git\u4ecb\u7ecd",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 00:36:32",
    "user_id": 147386,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 00:38:56",
    "user_id": 200165,
    "lab": "\u57fa\u4e8escrapy\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u57fa\u4e8escrapy\u722c\u866b\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6(python)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 00:39:11",
    "user_id": 33425,
    "lab": "\u975e\u7ebf\u6027\u7ed3\u6784-\u6811",
    "course": "\u6570\u636e\u7ed3\u6784(\u65b0\u7248)"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 00:40:05",
    "user_id": 131595,
    "lab": "grep\u547d\u4ee4\u4e0e\u6b63\u5219\u8868\u8fbe\u5f0f",
    "course": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840"
  },
  {
    "minutes": 66,
    "created_at": "2016-05-04 00:45:15",
    "user_id": 172083,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 00:50:46",
    "user_id": 171863,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 00:56:29",
    "user_id": 185399,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 01:00:50",
    "user_id": 175176,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 01:04:15",
    "user_id": 199599,
    "lab": "\u7ebf\u6027\u7ed3\u6784-\u7ebf\u6027\u8868",
    "course": "\u6570\u636e\u7ed3\u6784(\u65b0\u7248)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 01:06:16",
    "user_id": 185399,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 01:10:43",
    "user_id": 175176,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-04 01:12:59",
    "user_id": 171863,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 01:16:08",
    "user_id": 175176,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 01:18:29",
    "user_id": 200229,
    "lab": "\u591a\u5f20\u56fe\u7247\u62fc\u63a5\u4e0e\u5c42\u53e0",
    "course": "\u591a\u5f20\u56fe\u7247\u62fc\u63a5\u4e0e\u5c42\u53e0"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 01:30:35",
    "user_id": 170757,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 01:42:17",
    "user_id": 171863,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-04 01:51:55",
    "user_id": 170757,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 01:56:20",
    "user_id": 170715,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 01:58:47",
    "user_id": 172083,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 02:04:00",
    "user_id": 172083,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e94",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 02:13:51",
    "user_id": 172083,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 02:17:39",
    "user_id": 170715,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 02:28:36",
    "user_id": 150597,
    "lab": "\u4efb\u52a1\uff1a\u7cfb\u7edf\u76d1\u63a7\u4fe1\u606f\u6536\u96c6",
    "course": "\u5b9e\u9a8c\u697c\u8fd0\u7ef4\u5de5\u7a0b\u5e08"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 02:55:23",
    "user_id": 200232,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 03:32:45",
    "user_id": 200232,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 04:12:04",
    "user_id": 199765,
    "lab": "\u9879\u76ee\u4e00\uff1a\u7b80\u5355\u8ba1\u7b97\u5668",
    "course": "Python \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-04 04:42:56",
    "user_id": 176435,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 04:59:18",
    "user_id": 198635,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-04 05:00:20",
    "user_id": 200233,
    "lab": "HTML\u8d85\u6587\u672c\uff08\u4e00\uff09",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 05:42:30",
    "user_id": 198635,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 05:50:08",
    "user_id": 60135,
    "lab": "\u57fa\u7840\u7ec4\u4ef6\uff081\uff09 - Activity",
    "course": "Android\u5e94\u7528\u5f00\u53d1\u57fa\u7840"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 06:11:54",
    "user_id": 60135,
    "lab": "Android UI\u7f16\u7a0b",
    "course": "Android\u5e94\u7528\u5f00\u53d1\u57fa\u7840"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 06:16:48",
    "user_id": 200233,
    "lab": "HTML\u8d85\u6587\u672c\uff08\u4e8c\uff09",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 06:18:15",
    "user_id": 200236,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 06:33:53",
    "user_id": 199817,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 07:02:46",
    "user_id": 80242,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 07:16:30",
    "user_id": 195921,
    "lab": "\u8bbe\u8ba1\u6a21\u5f0f\u7b80\u4ecb",
    "course": "Java\u8fdb\u9636\u4e4b\u8bbe\u8ba1\u6a21\u5f0f"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 07:27:07",
    "user_id": 80242,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-04 07:27:49",
    "user_id": 198889,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-04 07:55:46",
    "user_id": 198889,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 07:56:51",
    "user_id": 147664,
    "lab": "Pig\u4ecb\u7ecd\u3001\u5b89\u88c5\u4e0e\u5e94\u7528\u6848\u4f8b",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-04 07:59:33",
    "user_id": 180238,
    "lab": "\u7b2c9\u5468\u8bfe\u5802\u5b9e\u9a8c-\u5b9e\u9a8c1",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 08:01:33",
    "user_id": 199670,
    "lab": "Python\u804a\u5929\u5ba4",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python\u804a\u5929\u5ba4"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:01:48",
    "user_id": 200153,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 08:03:21",
    "user_id": 188162,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 08:03:55",
    "user_id": 188152,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-04 08:04:34",
    "user_id": 188153,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 08:05:20",
    "user_id": 167439,
    "lab": "java.lang \u5305",
    "course": "JDK \u6838\u5fc3 API"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 08:06:11",
    "user_id": 199991,
    "lab": "Hive \u5b89\u88c5\u914d\u7f6e",
    "course": "HIVE\u6559\u7a0b"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-04 08:08:55",
    "user_id": 179597,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:10:48",
    "user_id": 195075,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-04 08:11:07",
    "user_id": 195081,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 51,
    "created_at": "2016-05-04 08:12:00",
    "user_id": 188199,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-04 08:12:08",
    "user_id": 188183,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 08:12:31",
    "user_id": 188159,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:13:12",
    "user_id": 156245,
    "lab": "\u6570\u636e\u7ed3\u6784-\u4e8c\u53c9\u6811\uff08Binary Tree\uff09",
    "course": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 08:13:34",
    "user_id": 181899,
    "lab": "\u7b2c9\u5468\u8bfe\u5802\u5b9e\u9a8c-\u5b9e\u9a8c1",
    "course": "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\uff08C++\uff09\u5b9e\u9a8c\u8bfe"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:14:25",
    "user_id": 188156,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:14:34",
    "user_id": 24084,
    "lab": "\u62bd\u8c61\u6210\u5458",
    "course": "Scala \u4e13\u9898\u6559\u7a0b - \u62bd\u8c61\u6210\u5458"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 08:15:09",
    "user_id": 188173,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:16:27",
    "user_id": 198759,
    "lab": "HTML\u8d85\u6587\u672c\uff08\u4e00\uff09",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-04 08:16:30",
    "user_id": 186284,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:17:23",
    "user_id": 195092,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-04 08:17:43",
    "user_id": 80485,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 08:18:38",
    "user_id": 195082,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:18:47",
    "user_id": 188149,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 08:19:05",
    "user_id": 188167,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u516d\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 08:19:06",
    "user_id": 188150,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-04 08:19:08",
    "user_id": 188163,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-04 08:19:10",
    "user_id": 195075,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-04 08:19:53",
    "user_id": 188156,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-04 08:20:02",
    "user_id": 188168,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 08:20:11",
    "user_id": 188204,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 08:21:26",
    "user_id": 199670,
    "lab": "Python\u804a\u5929\u5ba4",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python\u804a\u5929\u5ba4"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-04 08:22:30",
    "user_id": 188161,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 08:22:36",
    "user_id": 188158,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 08:22:50",
    "user_id": 188154,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:22:51",
    "user_id": 195080,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-04 08:23:07",
    "user_id": 200247,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 08:23:44",
    "user_id": 188178,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-04 08:23:57",
    "user_id": 188171,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 08:24:03",
    "user_id": 121877,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 08:24:16",
    "user_id": 200245,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-04 08:24:18",
    "user_id": 188175,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 22,
    "created_at": "2016-05-04 08:24:31",
    "user_id": 182548,
    "lab": "\u8d70\u5411\u5206\u652f",
    "course": "[\u79c1\u6709]\u8fbd\u5b81\u5e08\u8303\u5927\u5b66\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u5b9e\u9a8c\u8bfe\u7a0b"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-04 08:24:42",
    "user_id": 195085,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 08:25:33",
    "user_id": 188177,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:25:38",
    "user_id": 181662,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 08:25:39",
    "user_id": 188187,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 08:25:39",
    "user_id": 188209,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 08:27:14",
    "user_id": 113542,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u7684\u7ea6\u675f",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:28:33",
    "user_id": 200249,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 08:28:52",
    "user_id": 188191,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 08:29:23",
    "user_id": 195092,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:30:13",
    "user_id": 200251,
    "lab": "Go\u8bed\u8a00\u4ecb\u7ecd",
    "course": "Go\u8bed\u8a00\u7f16\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 08:30:17",
    "user_id": 200252,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 08:31:50",
    "user_id": 197925,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-04 08:32:10",
    "user_id": 188173,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 08:32:37",
    "user_id": 188149,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-04 08:33:56",
    "user_id": 200249,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 08:34:17",
    "user_id": 197920,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:34:57",
    "user_id": 200250,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:34:59",
    "user_id": 181662,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 08:35:26",
    "user_id": 188174,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u516d\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:35:31",
    "user_id": 200255,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-04 08:35:42",
    "user_id": 197912,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-04 08:36:00",
    "user_id": 200245,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 08:36:28",
    "user_id": 142906,
    "lab": "\u8d2a\u5403\u86c7\u4ecb\u7ecd",
    "course": "\u7ec8\u7aef\u8d2a\u5403\u86c7"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-04 08:36:48",
    "user_id": 50313,
    "lab": "Docker \u6570\u636e\u5377\u7ba1\u7406",
    "course": "\u52a8\u624b\u5b9e\u6218\u5b66Docker (15\u4e2a\u5b9e\u9a8c+54\u4e2a\u89c6\u9891)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 08:39:05",
    "user_id": 199991,
    "lab": "Bash\u4ecb\u7ecd\u4e0e\u5165\u95e8",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:39:52",
    "user_id": 195079,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 08:41:36",
    "user_id": 188162,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 08:43:08",
    "user_id": 188204,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:43:16",
    "user_id": 188164,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 08:43:31",
    "user_id": 188159,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-04 08:45:03",
    "user_id": 197906,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 08:45:20",
    "user_id": 188156,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 08:45:38",
    "user_id": 59262,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 08:46:03",
    "user_id": 47745,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-04 08:46:05",
    "user_id": 198056,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-04 08:46:47",
    "user_id": 79972,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-04 08:47:27",
    "user_id": 195092,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:47:27",
    "user_id": 200252,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:47:37",
    "user_id": 197923,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 08:47:47",
    "user_id": 194469,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 08:48:23",
    "user_id": 200258,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 08:49:06",
    "user_id": 199991,
    "lab": "Bash\u4e2d\u7684\u7279\u6b8a\u5b57\u7b26\uff08\u4e0a\uff09",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 08:49:15",
    "user_id": 199990,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 08:49:39",
    "user_id": 188183,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-04 08:50:11",
    "user_id": 109441,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:50:19",
    "user_id": 196557,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:50:31",
    "user_id": 188154,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 08:51:32",
    "user_id": 197938,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 08:52:03",
    "user_id": 195081,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:52:35",
    "user_id": 197928,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 08:52:37",
    "user_id": 197923,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-04 08:53:13",
    "user_id": 188168,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 08:55:42",
    "user_id": 197916,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:56:33",
    "user_id": 188154,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-04 08:57:06",
    "user_id": 200252,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 08:58:15",
    "user_id": 179597,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 08:58:49",
    "user_id": 186284,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 08:59:37",
    "user_id": 197909,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 09:00:06",
    "user_id": 94253,
    "lab": "linux\u7cfb\u7edf\u76d1\u63a7\u5e38\u7528\u547d\u4ee4\uff08\u4e00\uff09",
    "course": "Linux\u7cfb\u7edf\u76d1\u63a7\u5b9e\u6218"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:00:21",
    "user_id": 181662,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 09:01:33",
    "user_id": 194901,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:02:12",
    "user_id": 188177,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 09:02:32",
    "user_id": 189427,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 09:03:30",
    "user_id": 188191,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 09:03:59",
    "user_id": 144230,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-04 09:04:02",
    "user_id": 195123,
    "lab": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c",
    "course": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 09:04:28",
    "user_id": 188162,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 09:04:44",
    "user_id": 59262,
    "lab": "\u8bfe\u7a0b\u4ecb\u7ecd",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 09:04:49",
    "user_id": 188159,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 09:05:22",
    "user_id": 83807,
    "lab": "Bash\u5185\u7f6e\u547d\u4ee4\u4e0e\u73af\u5883\u7b80\u4ecb",
    "course": "\u5b9e\u7528Linux Shell\u7f16\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:05:25",
    "user_id": 200259,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 09:06:47",
    "user_id": 193104,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-04 09:07:48",
    "user_id": 153038,
    "lab": "MapReduce\u539f\u7406\u53ca\u64cd\u4f5c",
    "course": "BTBU-\u7814\u7a76\u751f2015\u7ea7-Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 09:09:05",
    "user_id": 197912,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 09:09:12",
    "user_id": 195081,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 09:09:28",
    "user_id": 188183,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 09:09:31",
    "user_id": 53927,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 09:09:49",
    "user_id": 200258,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 09:09:58",
    "user_id": 200245,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 09:10:24",
    "user_id": 200247,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:10:27",
    "user_id": 188177,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:10:29",
    "user_id": 181662,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:10:36",
    "user_id": 188161,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:10:48",
    "user_id": 188156,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:10:50",
    "user_id": 188153,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:11:10",
    "user_id": 188154,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:11:14",
    "user_id": 188167,
    "lab": "Linux\u64cd\u4f5c\u547d\u4ee4\uff08\u4e03\uff09",
    "course": "Linux\u547d\u4ee4\u5b9e\u4f8b\u7ec3\u4e60"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:11:47",
    "user_id": 192069,
    "lab": "\u9879\u76ee\u4e94\uff1a\u6587\u5b57\u804a\u5929\u5ba4",
    "course": "Python \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 09:12:17",
    "user_id": 113542,
    "lab": "\u57fa\u7840\u7bc7 - SELECT \u8bed\u53e5\u8be6\u89e3",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 09:12:45",
    "user_id": 16320,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:14:21",
    "user_id": 195298,
    "lab": "\u6cdb\u578b",
    "course": "JDK \u6838\u5fc3 API"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:15:43",
    "user_id": 200269,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-04 09:15:44",
    "user_id": 128580,
    "lab": "Makefile\u4f7f\u7528",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:17:16",
    "user_id": 94253,
    "lab": "linux\u7cfb\u7edf\u76d1\u63a7\u5e38\u7528\u547d\u4ee4\uff08\u4e8c\uff09",
    "course": "Linux\u7cfb\u7edf\u76d1\u63a7\u5b9e\u6218"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 09:17:57",
    "user_id": 195075,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:18:35",
    "user_id": 200250,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 09:18:52",
    "user_id": 188156,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 09:19:23",
    "user_id": 186284,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:19:38",
    "user_id": 191567,
    "lab": "DOS\u53caDEBUG\u4ecb\u7ecd",
    "course": "\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u90d1\u6653\u8587\u7f16\u8457\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 09:20:13",
    "user_id": 197916,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:20:19",
    "user_id": 188177,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:20:20",
    "user_id": 188153,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:20:37",
    "user_id": 181662,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:20:55",
    "user_id": 200245,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 09:22:40",
    "user_id": 200269,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:22:47",
    "user_id": 188154,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 09:22:53",
    "user_id": 134430,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-04 09:23:48",
    "user_id": 185981,
    "lab": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668",
    "course": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:24:10",
    "user_id": 62626,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:24:13",
    "user_id": 199868,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:24:14",
    "user_id": 200245,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 09:24:22",
    "user_id": 179597,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:25:21",
    "user_id": 195092,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-04 09:25:55",
    "user_id": 190538,
    "lab": "Python\u6807\u51c6\u5e93\uff08\u4e2d\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-04 09:26:20",
    "user_id": 146698,
    "lab": "C \u8bed\u8a00\u6570\u7ec4",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:26:42",
    "user_id": 84557,
    "lab": "\u8d2a\u5403\u86c7\u4ecb\u7ecd",
    "course": "\u7ec8\u7aef\u8d2a\u5403\u86c7"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:27:10",
    "user_id": 188161,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:27:12",
    "user_id": 121245,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 09:28:03",
    "user_id": 197908,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 09:28:04",
    "user_id": 158009,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:28:22",
    "user_id": 188154,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 09:28:39",
    "user_id": 126585,
    "lab": "Yii 2\u7684\u5b89\u88c5",
    "course": "Yii 2\u7cfb\u5217\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:29:56",
    "user_id": 16320,
    "lab": "\u94fe\u8def\u5c42\u4ecb\u7ecd",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 09:31:50",
    "user_id": 175490,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:32:10",
    "user_id": 199868,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 09:32:33",
    "user_id": 84557,
    "lab": "\u7ec8\u7aef\u56fe\u5f62\u5e93\u7f16\u7a0b",
    "course": "\u7ec8\u7aef\u8d2a\u5403\u86c7"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 09:32:34",
    "user_id": 121245,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:33:17",
    "user_id": 14562,
    "lab": "\u8bbe\u8ba1\u6a21\u5f0f\u7b80\u4ecb",
    "course": "Java\u8fdb\u9636\u4e4b\u8bbe\u8ba1\u6a21\u5f0f"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:33:28",
    "user_id": 190412,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-04 09:33:49",
    "user_id": 191690,
    "lab": "matplotlib - 2D \u4e0e 3D \u56fe\u7684\u7ed8\u5236\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:33:55",
    "user_id": 188177,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:36:56",
    "user_id": 195298,
    "lab": "\u6587\u4ef6\u64cd\u4f5c/\u968f\u673a\u8bbf\u95ee\u6587\u4ef6",
    "course": "JDK \u6838\u5fc3 API"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:37:39",
    "user_id": 14562,
    "lab": "\u5de5\u5382\u6a21\u5f0f",
    "course": "Java\u8fdb\u9636\u4e4b\u8bbe\u8ba1\u6a21\u5f0f"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:37:47",
    "user_id": 129164,
    "lab": "HTML\u6587\u672c",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 09:38:40",
    "user_id": 136927,
    "lab": "ShellShock \u653b\u51fb\u5b9e\u9a8c",
    "course": "ShellShock \u653b\u51fb\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:38:45",
    "user_id": 176435,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 09:38:48",
    "user_id": 113542,
    "lab": "\u57fa\u7840\u7bc7 - \u6570\u636e\u5e93\u53ca\u8868\u7684\u4fee\u6539\u548c\u5220\u9664",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:41:09",
    "user_id": 197970,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-04 09:41:29",
    "user_id": 78074,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:41:33",
    "user_id": 173956,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:41:38",
    "user_id": 103254,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:42:04",
    "user_id": 58719,
    "lab": "Hive \u7b80\u4ecb",
    "course": "HIVE\u6559\u7a0b"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-04 09:42:08",
    "user_id": 199337,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:42:29",
    "user_id": 190648,
    "lab": "makefile",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:42:59",
    "user_id": 200252,
    "lab": "\u64cd\u4f5c\u7cfb\u7edf\u7684\u5f15\u5bfc",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 09:44:26",
    "user_id": 126585,
    "lab": "Yii2 \u7684MVC Forms Layouts",
    "course": "Yii 2\u7cfb\u5217\u6559\u7a0b"
  },
  {
    "minutes": 57,
    "created_at": "2016-05-04 09:45:01",
    "user_id": 198566,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:45:07",
    "user_id": 195298,
    "lab": "\u8ba4\u8bc6 JDBC",
    "course": "JDBC \u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:45:31",
    "user_id": 84557,
    "lab": "\u8d2a\u5403\u86c7\u6838\u5fc3\u7f16\u7a0b",
    "course": "\u7ec8\u7aef\u8d2a\u5403\u86c7"
  },
  {
    "minutes": 99,
    "created_at": "2016-05-04 09:46:08",
    "user_id": 53927,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:46:44",
    "user_id": 199868,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:48:12",
    "user_id": 198635,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 87,
    "created_at": "2016-05-04 09:49:14",
    "user_id": 197970,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 09:50:04",
    "user_id": 200274,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 09:50:11",
    "user_id": 199589,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:50:11",
    "user_id": 195298,
    "lab": "\u8ba4\u8bc6 JDBC",
    "course": "JDBC \u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:50:15",
    "user_id": 194901,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 09:50:17",
    "user_id": 134270,
    "lab": "nginx\u4f18\u5316",
    "course": "Linux Web\u8fd0\u7ef4\uff08Nginx\uff09\u5b9e\u6218 "
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:50:26",
    "user_id": 200269,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:51:17",
    "user_id": 184742,
    "lab": "\u8ba4\u8bc6wxpython",
    "course": "\u7528Python\u505a2048\u6e38\u620f"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 09:52:20",
    "user_id": 110583,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 09:52:34",
    "user_id": 144230,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:52:48",
    "user_id": 126198,
    "lab": "\u7406\u89e3\u8fdb\u7a0b\u8c03\u5ea6\u65f6\u673a\u8ddf\u8e2a\u5206\u6790\u8fdb\u7a0b\u8c03\u5ea6\u4e0e\u8fdb\u7a0b\u5207\u6362\u7684\u8fc7\u7a0b",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 09:53:51",
    "user_id": 107767,
    "lab": "ShellShock \u653b\u51fb\u5b9e\u9a8c",
    "course": "ShellShock \u653b\u51fb\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:54:43",
    "user_id": 102705,
    "lab": "css\u5165\u95e8\u57fa\u7840",
    "course": "CSS\u901f\u6210\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 09:55:29",
    "user_id": 107982,
    "lab": "k-\u8fd1\u90bb\u7b97\u6cd5\u6539\u8fdb\u7ea6\u4f1a\u7f51\u7ad9\u914d\u5bf9\u6548\u679c",
    "course": "\u6df1\u5165\u5b66\u4e60\u300a\u673a\u5668\u5b66\u4e60\u5b9e\u6218\u300b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:55:37",
    "user_id": 113542,
    "lab": "\u57fa\u7840\u7bc7 - \u5176\u4ed6\u57fa\u672c\u64cd\u4f5c",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-04 09:55:49",
    "user_id": 198106,
    "lab": "\u5907\u4efd\u7a0b\u5e8f-\u57fa\u7840",
    "course": "\u57fa\u4e8e Python \u7684\u6587\u4ef6\u5907\u4efd"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-04 09:56:29",
    "user_id": 197366,
    "lab": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c",
    "course": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c"
  },
  {
    "minutes": 117,
    "created_at": "2016-05-04 09:56:32",
    "user_id": 46343,
    "lab": "Docker API",
    "course": "\u52a8\u624b\u5b9e\u6218\u5b66Docker (15\u4e2a\u5b9e\u9a8c+54\u4e2a\u89c6\u9891)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:57:10",
    "user_id": 184742,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 09:57:16",
    "user_id": 108726,
    "lab": "\u6570\u636e\u67e5\u8be2",
    "course": "MongoDB \u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 09:57:37",
    "user_id": 176435,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-04 09:57:45",
    "user_id": 74797,
    "lab": "\u6587\u4ef6IO\uff08\u4e00\uff09",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 09:58:11",
    "user_id": 182106,
    "lab": "\u6307\u9488\uff08\u4e00\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:58:34",
    "user_id": 200277,
    "lab": "JavaScript \u7b80\u4ecb",
    "course": "Javascript\u57fa\u7840\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 09:59:22",
    "user_id": 199589,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 09:59:23",
    "user_id": 122971,
    "lab": "Bash\u4e2d\u7684\u7279\u6b8a\u5b57\u7b26\uff08\u4e0a\uff09",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 09:59:37",
    "user_id": 189152,
    "lab": "\u6587\u4ef6\u7cfb\u7edf\u64cd\u4f5c\u4e0e\u78c1\u76d8\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 10:00:45",
    "user_id": 200278,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-04 10:01:19",
    "user_id": 2863,
    "lab": "Python\u6807\u51c6\u5e93\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:01:31",
    "user_id": 181744,
    "lab": "\u64cd\u4f5c\u7cfb\u7edf\u7684\u5f15\u5bfc",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:02:00",
    "user_id": 128580,
    "lab": "\u591a\u8fdb\u7a0b\uff08\u4e8c\uff09",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 10:02:08",
    "user_id": 196144,
    "lab": "\u6570\u636e\u7ed3\u6784-\u94fe\u8868\uff08Linked List\uff09",
    "course": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 10:02:09",
    "user_id": 134270,
    "lab": "nginx\u914d\u7f6e\u5b9e\u6218\uff1a\u6d41\u91cf\u53ca\u5e76\u53d1\u8fde\u63a5\u6570\u9650\u5236",
    "course": "Linux Web\u8fd0\u7ef4\uff08Nginx\uff09\u5b9e\u6218 "
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 10:02:53",
    "user_id": 79972,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 10:03:03",
    "user_id": 191760,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:04:08",
    "user_id": 199589,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:04:21",
    "user_id": 196108,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:05:17",
    "user_id": 103254,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 72,
    "created_at": "2016-05-04 10:06:36",
    "user_id": 200030,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-04 10:06:43",
    "user_id": 80485,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 10:07:13",
    "user_id": 160919,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:07:30",
    "user_id": 199874,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 10:08:16",
    "user_id": 200283,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 10:08:42",
    "user_id": 200255,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 10:08:58",
    "user_id": 200284,
    "lab": "TensorFlow \u5b9e\u9a8c\u73af\u5883\u642d\u5efa",
    "course": "TensorFlow \u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 10:09:29",
    "user_id": 111886,
    "lab": "\u8ba4\u8bc6HTML5",
    "course": "HTML5\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:09:59",
    "user_id": 103254,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 10:14:58",
    "user_id": 187210,
    "lab": "SQL\u8bed\u53e5\u8bed\u6cd5",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 10:16:02",
    "user_id": 199866,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0b\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 10:16:08",
    "user_id": 200286,
    "lab": "Python \u7834\u89e3\u9a8c\u8bc1\u7801",
    "course": "Python \u7834\u89e3\u9a8c\u8bc1\u7801"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 10:16:52",
    "user_id": 195632,
    "lab": "\u6587\u4ef6\u548c\u6587\u4ef6\u7684\u8f93\u5165\u4e0e\u8f93\u51fa",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-04 10:17:23",
    "user_id": 78448,
    "lab": "\u8bbe\u8ba1\u6a21\u5f0f\u7b80\u4ecb",
    "course": "Java\u8fdb\u9636\u4e4b\u8bbe\u8ba1\u6a21\u5f0f"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 10:17:26",
    "user_id": 134270,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 10:17:34",
    "user_id": 164635,
    "lab": "\u521d\u8bc6HTML",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:18:09",
    "user_id": 63797,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 10:18:11",
    "user_id": 126585,
    "lab": "Yii 2\u7684\u5b89\u88c5",
    "course": "Yii 2\u7cfb\u5217\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:18:34",
    "user_id": 200288,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-04 10:20:02",
    "user_id": 195375,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u8fd0\u7b97\u7b26\u548c\u6570\u636e\u8f6c\u6362",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:20:29",
    "user_id": 191027,
    "lab": "vi\u7f16\u8bd1\u5668\u7684\u4f7f\u7528",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:20:33",
    "user_id": 29832,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 10:21:37",
    "user_id": 189427,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:22:38",
    "user_id": 171919,
    "lab": "HDFS\u539f\u7406\u53ca\u64cd\u4f5c",
    "course": "Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-04 10:22:44",
    "user_id": 146698,
    "lab": "\u6a21\u5757\u5316\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-04 10:22:48",
    "user_id": 88179,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 10:22:55",
    "user_id": 57763,
    "lab": "ThinkPHP\u5b89\u88c5\u4e0e\u914d\u7f6e",
    "course": "ThinkPHP\u6846\u67b6\u5b9e\u8df5"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:23:00",
    "user_id": 63797,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-04 10:23:17",
    "user_id": 153162,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 10:23:44",
    "user_id": 167164,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-04 10:24:33",
    "user_id": 195784,
    "lab": "Linux\u57fa\u7840\u77e5\u8bc6\u4e0e\u5e38\u7528\u547d\u4ee4",
    "course": "\u5b9e\u7528Linux Shell\u7f16\u7a0b"
  },
  {
    "minutes": 72,
    "created_at": "2016-05-04 10:25:07",
    "user_id": 191760,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 10:25:23",
    "user_id": 191027,
    "lab": "gcc\u7f16\u8bd1\u5668\u7684\u4f7f\u7528",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:25:56",
    "user_id": 6574,
    "lab": "\u5f00\u542f\u795e\u5947\u7684Scala\u7f16\u7a0b\u4e4b\u65c5",
    "course": "Scala\u5f00\u53d1\u6559\u7a0b"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-04 10:26:02",
    "user_id": 187121,
    "lab": "Python\u8fdb\u9636\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 10:26:11",
    "user_id": 200293,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-04 10:27:00",
    "user_id": 153038,
    "lab": "Hive\u4ecb\u7ecd\u548c\u5b89\u88c5\u90e8\u7f72",
    "course": "BTBU-\u7814\u7a76\u751f2015\u7ea7-Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 10:27:32",
    "user_id": 62621,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-04 10:28:15",
    "user_id": 199866,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 10:28:37",
    "user_id": 189152,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 10:28:48",
    "user_id": 126585,
    "lab": "Yii2 \u7684MVC Forms Layouts",
    "course": "Yii 2\u7cfb\u5217\u6559\u7a0b"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-04 10:29:56",
    "user_id": 196083,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 10:31:01",
    "user_id": 189141,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:31:19",
    "user_id": 192076,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:31:27",
    "user_id": 199337,
    "lab": "HTML5 \u672c\u5730\u88c1\u526a\u56fe\u7247",
    "course": "\u57fa\u4e8e HTML5 \u5b9e\u73b0\u672c\u5730\u56fe\u7247\u88c1\u526a"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 10:31:47",
    "user_id": 88237,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 10:32:46",
    "user_id": 78074,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 60,
    "created_at": "2016-05-04 10:32:48",
    "user_id": 27298,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 10:32:56",
    "user_id": 195737,
    "lab": "\u57fa\u4e8escrapy\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011\u57fa\u4e8escrapy\u722c\u866b\u7684\u5929\u6c14\u6570\u636e\u91c7\u96c6(python)"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:32:59",
    "user_id": 184955,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:33:04",
    "user_id": 200014,
    "lab": "cookie\u57fa\u7840\u548c\u5e94\u7528",
    "course": "PHP\u4f1a\u8bdd\u63a7\u5236"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 10:33:16",
    "user_id": 107767,
    "lab": "\u6982\u8ff0",
    "course": "\u5b9e\u7528Linux Shell\u7f16\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 10:34:20",
    "user_id": 79972,
    "lab": "\u547d\u4ee4\u6267\u884c\u987a\u5e8f\u63a7\u5236\u4e0e\u7ba1\u9053",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:34:39",
    "user_id": 200065,
    "lab": "Java \u65b9\u6cd5",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 10:34:44",
    "user_id": 149392,
    "lab": "Redis\u7b80\u4ecb\u4e0e\u5b89\u88c5",
    "course": "Redis\u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-04 10:35:39",
    "user_id": 181744,
    "lab": "\u64cd\u4f5c\u7cfb\u7edf\u7684\u5f15\u5bfc",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 10:36:18",
    "user_id": 184955,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:36:23",
    "user_id": 189646,
    "lab": "\u8868\u8fbe\u5f0f\u7684\u8ba1\u7b97",
    "course": "Scala \u5f00\u53d1\u4e8c\u5341\u56db\u70b9\u6e38\u620f"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 10:36:30",
    "user_id": 185981,
    "lab": "Python\u8865\u5145",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-04 10:36:42",
    "user_id": 195152,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 10:37:14",
    "user_id": 199337,
    "lab": "Hadoop\u5355\u673a\u6a21\u5f0f\u5b89\u88c5",
    "course": "Hadoop\u90e8\u7f72\u53ca\u7ba1\u7406"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-04 10:37:46",
    "user_id": 167164,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 10:38:21",
    "user_id": 175009,
    "lab": "Hadoop\u4ecb\u7ecd\u53ca1.X\u4f2a\u5206\u5e03\u5f0f\u5b89\u88c5",
    "course": "BTBU-\u7814\u7a76\u751f2015\u7ea7-Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 10:38:41",
    "user_id": 131866,
    "lab": "Hadoop\u5355\u673a\u6a21\u5f0f\u5b89\u88c5",
    "course": "Hadoop\u90e8\u7f72\u53ca\u7ba1\u7406"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:38:51",
    "user_id": 111886,
    "lab": "HTML5\u7684\u65b0\u7684\u7ed3\u6784\u5143\u7d20\u4ecb\u7ecd",
    "course": "HTML5\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 10:39:19",
    "user_id": 65245,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 10:40:50",
    "user_id": 174938,
    "lab": "Hadoop\u4ecb\u7ecd\u53ca1.X\u4f2a\u5206\u5e03\u5f0f\u5b89\u88c5",
    "course": "BTBU-\u7814\u7a76\u751f2015\u7ea7-Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:40:52",
    "user_id": 134270,
    "lab": "Go\u8bed\u8a00\u4ecb\u7ecd",
    "course": "Go\u8bed\u8a00\u7f16\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:41:06",
    "user_id": 197166,
    "lab": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048",
    "course": "200\u884cPython\u4ee3\u7801\u5b9e\u73b02048"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 10:41:48",
    "user_id": 198635,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u7684\u7ea6\u675f",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-04 10:42:41",
    "user_id": 189146,
    "lab": "makefile",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:43:04",
    "user_id": 197227,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:43:13",
    "user_id": 187809,
    "lab": "\u4ecb\u7ecd",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 10:43:33",
    "user_id": 117567,
    "lab": "Python\u8865\u5145",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 10:45:51",
    "user_id": 195792,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 10:46:00",
    "user_id": 198060,
    "lab": "PythonChallenge_2",
    "course": "\u6bcf\u5929\u4e00\u4e2aPythonChallenge\u300a\u4efb\u52a1\u4e8c\u300b"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-04 10:47:36",
    "user_id": 176612,
    "lab": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c",
    "course": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 10:47:41",
    "user_id": 197673,
    "lab": "\u9009\u62e9\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:48:29",
    "user_id": 200014,
    "lab": "amo.js\u6307\u5357",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011amo.js\u2014\u7528\u4e8e\u521b\u5efa CSS3 \u52a8\u753b\u7684JS\u5e93"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 10:48:32",
    "user_id": 188394,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-04 10:49:38",
    "user_id": 200069,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 10:50:03",
    "user_id": 111886,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-04 10:50:38",
    "user_id": 161790,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-04 10:52:08",
    "user_id": 186288,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 10:52:29",
    "user_id": 134270,
    "lab": "MySQL\u6570\u636e\u5e93\u5bf9\u8c61\u7ba1\u7406",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011MySQL\u6570\u636e\u5e93\u5bf9\u8c61\u7ba1\u7406"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 10:52:32",
    "user_id": 82553,
    "lab": "\u9879\u76ee\u56db\uff1a\u5728\u7ebf\u804a\u5929\u5ba4",
    "course": "Node.js \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 10:52:50",
    "user_id": 198060,
    "lab": "PythonChallenge_3",
    "course": "\u6bcf\u5929\u4e00\u4e2aPythonChallenge\u300a\u4efb\u52a1\u4e09\u300b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:53:51",
    "user_id": 79972,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 10:53:57",
    "user_id": 197948,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 10:54:03",
    "user_id": 199984,
    "lab": "Node.js fs\u6a21\u5757",
    "course": "Node.js \u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 10:54:23",
    "user_id": 199540,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-04 10:55:08",
    "user_id": 107767,
    "lab": "Linux\u57fa\u7840\u77e5\u8bc6\u4e0e\u5e38\u7528\u547d\u4ee4",
    "course": "\u5b9e\u7528Linux Shell\u7f16\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 10:55:28",
    "user_id": 106447,
    "lab": "\u9879\u76ee\u4e00\uff1a\u7f51\u7ad9\u4fe1\u606f\u722c\u866b",
    "course": "Node.js \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:56:14",
    "user_id": 126585,
    "lab": "Yii2 \u6570\u636e\u5e93\u548cGii",
    "course": "Yii 2\u7cfb\u5217\u6559\u7a0b"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-04 10:57:05",
    "user_id": 149392,
    "lab": "Redis\u6570\u636e\u7c7b\u578b ",
    "course": "Redis\u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 10:57:24",
    "user_id": 189141,
    "lab": "Bash\u4ecb\u7ecd\u4e0e\u5165\u95e8",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:57:57",
    "user_id": 200283,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-04 10:57:59",
    "user_id": 65965,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:58:24",
    "user_id": 196585,
    "lab": "HTML5\u6587\u4ef6\u64cd\u4f5cAPI",
    "course": "HTML5\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 10:58:51",
    "user_id": 29229,
    "lab": "\u4e00\u4e2a\u6700\u7b80\u5355\u7684 express \u5e94\u7528",
    "course": "Node.js\u5305\u6559\u4e0d\u5305\u4f1a"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 10:59:04",
    "user_id": 182339,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e8c\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 10:59:28",
    "user_id": 200303,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 10:59:58",
    "user_id": 189152,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-04 11:00:28",
    "user_id": 199516,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 11:01:24",
    "user_id": 200255,
    "lab": "\u7f16\u5199\u4e00\u4e2als\u547d\u4ee4",
    "course": "C\u8bed\u8a00\u5b9e\u73b0Linux ls\u547d\u4ee4"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 11:03:21",
    "user_id": 175490,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 11:04:10",
    "user_id": 194210,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 11:04:35",
    "user_id": 198638,
    "lab": "Hello\uff0cShiYanLou!",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 11:04:45",
    "user_id": 181325,
    "lab": "Flask\u8fd0\u884c\u53ca\u8c03\u8bd5\u6a21\u5f0f",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 11:05:02",
    "user_id": 191545,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 11:05:03",
    "user_id": 151992,
    "lab": "\u4f7f\u7528 PHP \u5b9e\u73b0\u6821\u82b1\u6392\u540d",
    "course": "\u6821\u82b1\u8bc4\u6bd4\u6392\u540d\u9879\u76ee-PHP"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 11:05:19",
    "user_id": 197763,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 11:05:30",
    "user_id": 195784,
    "lab": "Bash\u5185\u7f6e\u547d\u4ee4\u4e0e\u73af\u5883\u7b80\u4ecb",
    "course": "\u5b9e\u7528Linux Shell\u7f16\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 11:05:53",
    "user_id": 96218,
    "lab": "\u57fa\u7840\u8bed\u6cd5",
    "course": "Ruby\u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 11:06:07",
    "user_id": 25174,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-04 11:06:49",
    "user_id": 194260,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 11:07:54",
    "user_id": 197166,
    "lab": "\u5b8c\u6210\u4e00\u4e2a\u7b80\u5355\u7684\u65f6\u95f4\u7247\u8f6e\u8f6c\u591a\u9053\u7a0b\u5e8f\u5185\u6838\u4ee3\u7801",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 11:08:20",
    "user_id": 199394,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-04 11:09:11",
    "user_id": 200218,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 11:10:41",
    "user_id": 197763,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 11:10:56",
    "user_id": 27353,
    "lab": "\u6b22\u8fce\u6765\u5230 Flask \u7684\u4e16\u754c",
    "course": "[\u5df2\u4e0b\u7ebf\u3011Flask \u5f00\u53d1\u8f7b\u535a\u5ba2"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 11:11:02",
    "user_id": 181325,
    "lab": "\u8def\u7531",
    "course": "Python Flask Web\u6846\u67b6"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 11:11:52",
    "user_id": 197166,
    "lab": "\u8ddf\u8e2a\u5206\u6790Linux\u5185\u6838\u7684\u542f\u52a8\u8fc7\u7a0b",
    "course": "Linux\u5185\u6838\u5206\u6790"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 11:11:53",
    "user_id": 198638,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 11:12:03",
    "user_id": 200303,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 11:13:03",
    "user_id": 107366,
    "lab": "\u94fe\u8def\u5c42\u4ecb\u7ecd",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 11:14:21",
    "user_id": 79972,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 11:15:15",
    "user_id": 198106,
    "lab": "\u9700\u6c42\u4ecb\u7ecd+\u57fa\u7840\u77e5\u8bc6",
    "course": "\u57fa\u4e8e Python \u7684\u6587\u4ef6\u5907\u4efd"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 11:15:20",
    "user_id": 200283,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 11:16:26",
    "user_id": 197322,
    "lab": "java.util \u5305",
    "course": "JDK \u6838\u5fc3 API"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 11:16:33",
    "user_id": 197763,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 11:16:48",
    "user_id": 146207,
    "lab": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668",
    "course": "Python \u5b9e\u73b0\u7aef\u53e3\u626b\u63cf\u5668"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-04 11:18:29",
    "user_id": 200309,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 11:18:32",
    "user_id": 78448,
    "lab": "\u5355\u4f8b\u6a21\u5f0f",
    "course": "Java\u8fdb\u9636\u4e4b\u8bbe\u8ba1\u6a21\u5f0f"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 11:18:50",
    "user_id": 25174,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 36,
    "created_at": "2016-05-04 11:19:34",
    "user_id": 189152,
    "lab": "\u6570\u636e\u6d41\u91cd\u5b9a\u5411",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 11:21:32",
    "user_id": 199984,
    "lab": "Node.js fs\u6a21\u5757",
    "course": "Node.js \u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 11:21:41",
    "user_id": 200314,
    "lab": "\u5f00\u53d1\u73af\u5883\u4ee5\u53ca\u9879\u76ee\u4e0eApp",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 11:22:37",
    "user_id": 191029,
    "lab": "TCP/IP\u7b80\u4ecb",
    "course": "TCP/IP\u7f51\u7edc\u534f\u8bae\u57fa\u7840"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 11:22:45",
    "user_id": 198878,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-04 11:22:56",
    "user_id": 167250,
    "lab": "\u6570\u5b66\u5de5\u5177",
    "course": "J2SE\u6838\u5fc3\u5f00\u53d1\u5b9e\u6218"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 11:23:25",
    "user_id": 200283,
    "lab": "Java \u8bed\u8a00\u57fa\u7840",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 11:23:32",
    "user_id": 200313,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 11:23:34",
    "user_id": 197231,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 11:23:35",
    "user_id": 103254,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 11,
    "created_at": "2016-05-04 11:24:16",
    "user_id": 199201,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 11:25:11",
    "user_id": 316,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 11:25:16",
    "user_id": 189146,
    "lab": "makefile",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 11:25:28",
    "user_id": 25174,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 11:26:18",
    "user_id": 196033,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-04 11:27:37",
    "user_id": 198592,
    "lab": "pandas \u56de\u987e",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python \u6570\u636e\u5206\u6790\uff08\u4e00\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 11:28:28",
    "user_id": 197763,
    "lab": "\u67e5\u627e\u66ff\u6362",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 11:29:38",
    "user_id": 198960,
    "lab": "\u521d\u8bc6HTML",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-04 11:30:59",
    "user_id": 181995,
    "lab": "DOS\u53caDEBUG\u4ecb\u7ecd",
    "course": "\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u90d1\u6653\u8587\u7f16\u8457\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 11:31:27",
    "user_id": 192069,
    "lab": "\u9879\u76ee\u4e94\uff1a\u6587\u5b57\u804a\u5929\u5ba4",
    "course": "Python \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 11:31:49",
    "user_id": 199866,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0b\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 11:32:20",
    "user_id": 198889,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-04 11:32:59",
    "user_id": 196033,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 11:33:17",
    "user_id": 200030,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 11:37:08",
    "user_id": 199540,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 11:37:40",
    "user_id": 25174,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 11:39:28",
    "user_id": 167164,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 11:40:30",
    "user_id": 187210,
    "lab": "MySQL\u89e6\u53d1\u5668",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 2,
    "created_at": "2016-05-04 11:40:38",
    "user_id": 133586,
    "lab": "Ubuntu14.04 Server\u5b9e\u9a8c\u73af\u5883",
    "course": "Ubuntu Server\u4f53\u9a8c\u8bfe"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-04 11:41:19",
    "user_id": 200069,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 11:41:31",
    "user_id": 200030,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 11:41:58",
    "user_id": 316,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 11:43:39",
    "user_id": 72538,
    "lab": "\u57fa\u7840\u6b63\u5219\u8868\u8fbe\u5f0f\u4ecb\u7ecd\u4e0e\u7ec3\u4e60",
    "course": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 11:44:08",
    "user_id": 200283,
    "lab": "Java \u8bed\u8a00\u57fa\u7840",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 57,
    "created_at": "2016-05-04 11:44:14",
    "user_id": 200324,
    "lab": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c",
    "course": "\u7f13\u51b2\u533a\u6ea2\u51fa\u6f0f\u6d1e\u5b9e\u9a8c"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 11:46:56",
    "user_id": 107767,
    "lab": "Bash\u5185\u7f6e\u547d\u4ee4\u4e0e\u73af\u5883\u7b80\u4ecb",
    "course": "\u5b9e\u7528Linux Shell\u7f16\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 11:47:26",
    "user_id": 174938,
    "lab": "Hadoop\u4ecb\u7ecd\u53ca1.X\u4f2a\u5206\u5e03\u5f0f\u5b89\u88c5",
    "course": "BTBU-\u7814\u7a76\u751f2015\u7ea7-Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 11:48:22",
    "user_id": 153162,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 11:49:14",
    "user_id": 200219,
    "lab": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668",
    "course": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668"
  },
  {
    "minutes": 72,
    "created_at": "2016-05-04 11:49:40",
    "user_id": 198423,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 11:51:38",
    "user_id": 200309,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 11:51:49",
    "user_id": 200327,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 11:52:10",
    "user_id": 175844,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 11:52:55",
    "user_id": 72538,
    "lab": "grep\u547d\u4ee4\u4e0e\u6b63\u5219\u8868\u8fbe\u5f0f",
    "course": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 11:57:33",
    "user_id": 171956,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-04 12:01:55",
    "user_id": 196435,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 12:02:27",
    "user_id": 120033,
    "lab": "Spark \u7b80\u4ecb\u4e0e\u5b89\u88c5\uff08\u514d\u8d39\uff09",
    "course": "Spark \u5927\u6570\u636e\u52a8\u624b\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 12:02:29",
    "user_id": 200331,
    "lab": "PythonChallenge_1",
    "course": "\u5168\u9762\u89e3\u6790PythonChallenge"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 12:03:17",
    "user_id": 72538,
    "lab": "\u6b63\u5219\u8868\u8fbe\u5f0f\u8fd0\u7528\u4e4b sed\u5de5\u5177\u547d\u4ee4 ",
    "course": "\u6b63\u5219\u8868\u8fbe\u5f0f\u57fa\u7840"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 12:06:36",
    "user_id": 200218,
    "lab": "\u57fa\u672c\u7528\u6cd5\uff08\u4e0a\uff09",
    "course": "Git \u5b9e\u6218\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 12:07:04",
    "user_id": 170013,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 12:08:12",
    "user_id": 200309,
    "lab": "\u521d\u8bc6HTML",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 12:09:25",
    "user_id": 146207,
    "lab": "Python\u57fa\u7840\uff08\u4e0a\uff09\u00a0\u00a0 ",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 12:09:35",
    "user_id": 175009,
    "lab": "Hadoop\u4ecb\u7ecd\u53ca1.X\u4f2a\u5206\u5e03\u5f0f\u5b89\u88c5",
    "course": "BTBU-\u7814\u7a76\u751f2015\u7ea7-Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 12:10:20",
    "user_id": 200331,
    "lab": "PythonChallenge_1",
    "course": "\u5168\u9762\u89e3\u6790PythonChallenge"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 12:11:18",
    "user_id": 182339,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e8c\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 12:12:07",
    "user_id": 197798,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 93,
    "created_at": "2016-05-04 12:13:28",
    "user_id": 200069,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 12:16:03",
    "user_id": 186465,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 12:18:24",
    "user_id": 182339,
    "lab": "\u987a\u5e8f\u7a0b\u5e8f\u8bbe\u8ba1 - \u6570\u636e\u7c7b\u578b\uff08\u4e8c\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 12:20:24",
    "user_id": 30526,
    "lab": "\u5f00\u542f\u795e\u5947\u7684Scala\u7f16\u7a0b\u4e4b\u65c5",
    "course": "Scala\u5f00\u53d1\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 12:21:06",
    "user_id": 200335,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 12:22:59",
    "user_id": 186465,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 12:23:15",
    "user_id": 146207,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 72,
    "created_at": "2016-05-04 12:31:14",
    "user_id": 76363,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 78,
    "created_at": "2016-05-04 12:31:29",
    "user_id": 199258,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 12:31:33",
    "user_id": 199540,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 12:31:41",
    "user_id": 25538,
    "lab": "\u8ba4\u8bc6 Java",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 12:32:27",
    "user_id": 171964,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 12:33:22",
    "user_id": 200335,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 12:33:41",
    "user_id": 200337,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-04 12:34:41",
    "user_id": 174938,
    "lab": "Hadoop\u4ecb\u7ecd\u53ca1.X\u4f2a\u5206\u5e03\u5f0f\u5b89\u88c5",
    "course": "BTBU-\u7814\u7a76\u751f2015\u7ea7-Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-04 12:36:57",
    "user_id": 200157,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 12:37:50",
    "user_id": 190727,
    "lab": "makefile",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 48,
    "created_at": "2016-05-04 12:38:42",
    "user_id": 200327,
    "lab": "Redis\u7b80\u4ecb\u4e0e\u5b89\u88c5",
    "course": "Redis\u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 12:38:47",
    "user_id": 172125,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 54,
    "created_at": "2016-05-04 12:39:32",
    "user_id": 121197,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 66,
    "created_at": "2016-05-04 12:40:06",
    "user_id": 195792,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 87,
    "created_at": "2016-05-04 12:41:19",
    "user_id": 173266,
    "lab": "MapReduce\u5e94\u7528\u6848\u4f8b",
    "course": "BTBU-\u7814\u7a76\u751f2015\u7ea7-Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 12:42:52",
    "user_id": 175174,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 12:44:32",
    "user_id": 15451,
    "lab": "Bash\u4e2d\u7684\u7279\u6b8a\u5b57\u7b26\uff08\u4e0a\uff09",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 12:44:45",
    "user_id": 66074,
    "lab": "nginx\u8fdb\u7a0b\u4e0e\u6a21\u5757",
    "course": "Linux Web\u8fd0\u7ef4\uff08Nginx\uff09\u5b9e\u6218 "
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 12:47:37",
    "user_id": 171956,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 12:48:52",
    "user_id": 180741,
    "lab": "\u5728\u5b57\u7b26\u4e32\u4e2d\u5b58\u50a8\u6587\u672c",
    "course": "\u300aPython\u5165\u95e8\u7ecf\u5178\u300b\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 12:50:11",
    "user_id": 171965,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 60,
    "created_at": "2016-05-04 12:51:48",
    "user_id": 191516,
    "lab": "\u6587\u4ef6IO\u57fa\u7840",
    "course": "\u5d4c\u5165\u5f0fLinux\u57fa\u7840\u5b9e\u9a8c"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 12:52:37",
    "user_id": 200255,
    "lab": "\u719f\u6089\u5b9e\u9a8c\u73af\u5883 ",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 12:52:44",
    "user_id": 199817,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 13:00:06",
    "user_id": 198592,
    "lab": "pandas \u56de\u987e",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python \u6570\u636e\u5206\u6790\uff08\u4e00\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:00:09",
    "user_id": 200324,
    "lab": "\u7ade\u6001\u6761\u4ef6\u6f0f\u6d1e\u5b9e\u9a8c",
    "course": "\u7ade\u6001\u6761\u4ef6\u6f0f\u6d1e\u5b9e\u9a8c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:00:12",
    "user_id": 164635,
    "lab": "HTML\u6587\u672c",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 13:00:40",
    "user_id": 66074,
    "lab": "Nginx\u6a21\u5757\u5f00\u53d1\u5b9e\u9a8c",
    "course": "Linux Web\u8fd0\u7ef4\uff08Nginx\uff09\u5b9e\u6218 "
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:02:40",
    "user_id": 187195,
    "lab": "Python\u5feb\u901f\u5165\u95e8",
    "course": "Python\u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 13:03:26",
    "user_id": 200337,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:04:10",
    "user_id": 198056,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 13:05:18",
    "user_id": 187210,
    "lab": "MySQL\u89e6\u53d1\u5668",
    "course": "MySQL \u53c2\u8003\u624b\u518c\u4e2d\u6587\u7248"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-04 13:05:54",
    "user_id": 171902,
    "lab": "HDFS\u539f\u7406\u53ca\u64cd\u4f5c",
    "course": "BTBU-\u7814\u7a76\u751f2015\u7ea7-Hadoop\u5165\u95e8\u8fdb\u9636\u8bfe\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-04 13:06:38",
    "user_id": 200335,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-04 13:08:06",
    "user_id": 186243,
    "lab": "Linux\u4e0b\u8f6f\u4ef6\u5b89\u88c5",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 13:08:24",
    "user_id": 148055,
    "lab": "Vim\u6587\u6863\u7f16\u8f91",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:09:21",
    "user_id": 164624,
    "lab": "ThinkPHP\u5b89\u88c5\u4e0e\u914d\u7f6e",
    "course": "ThinkPHP\u6846\u67b6\u5b9e\u8df5"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 13:09:48",
    "user_id": 146698,
    "lab": "\u6a21\u5757\u5316\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 13:11:30",
    "user_id": 170987,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 13:11:35",
    "user_id": 197153,
    "lab": "HTML5 Canvas\u5c0f\u6e38\u620f",
    "course": "\u57fa\u4e8eHTML5 Canvas\u5b9e\u73b0\u5c0f\u6e38\u620f"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 13:12:32",
    "user_id": 175174,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e00",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:12:45",
    "user_id": 198933,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 13:12:56",
    "user_id": 198056,
    "lab": "\u4e3a\u4ec0\u4e48\u662f C \u2014\u2014\u56e0\u4e3a\u4f60\u65e0\u53ef\u66ff\u4ee3",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 13:13:06",
    "user_id": 2863,
    "lab": "Python\u6807\u51c6\u5e93\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 13:15:56",
    "user_id": 180741,
    "lab": "\u7f16\u7a0b\u4e2d\u7684\u903b\u8f91",
    "course": "\u300aPython\u5165\u95e8\u7ecf\u5178\u300b\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 13:16:14",
    "user_id": 195632,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 13:16:24",
    "user_id": 185627,
    "lab": "\u7b80\u5355\u7684\u6587\u672c\u5904\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:17:06",
    "user_id": 200349,
    "lab": "pandas \u56de\u987e",
    "course": "\u3010\u5df2\u4e0b\u7ebf\u3011Python \u6570\u636e\u5206\u6790\uff08\u4e00\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:17:29",
    "user_id": 71106,
    "lab": "\u5728Android Studio\u4e2d\u521b\u5efa\u9879\u76ee\u548c\u865a\u62df\u673a",
    "course": "Android Studio\u9879\u76ee\u521b\u5efa\u548c\u6a21\u62df\u5668\u914d\u7f6e"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 13:19:04",
    "user_id": 116092,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 13:19:05",
    "user_id": 191690,
    "lab": "matplotlib - 2D \u4e0e 3D \u56fe\u7684\u7ed8\u5236\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 39,
    "created_at": "2016-05-04 13:19:07",
    "user_id": 198889,
    "lab": "Python\u57fa\u7840\uff08\u4e0b\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 72,
    "created_at": "2016-05-04 13:19:23",
    "user_id": 90735,
    "lab": "\u6a21\u5757\u5316\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 13:20:45",
    "user_id": 198056,
    "lab": "\u5f00\u53d1\u73af\u5883\u548c\u5256\u6790\u7b2c\u4e00\u4e2a C \u8bed\u8a00",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 13:21:00",
    "user_id": 164635,
    "lab": "HTML\u8d85\u6587\u672c\uff08\u4e00\uff09",
    "course": "HTML\u57fa\u7840\u5165\u95e8"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 13:21:10",
    "user_id": 171965,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e09",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:21:55",
    "user_id": 199984,
    "lab": "Node.js fs\u6a21\u5757",
    "course": "Node.js \u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 13:22:57",
    "user_id": 120304,
    "lab": "\u6307\u9488\uff08\u4e00\uff09",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 13:26:05",
    "user_id": 153162,
    "lab": "\u6587\u4ef6\u6253\u5305\u4e0e\u89e3\u538b\u7f29",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:26:50",
    "user_id": 200283,
    "lab": "Java \u6570\u7ec4",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 13:27:26",
    "user_id": 199703,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 42,
    "created_at": "2016-05-04 13:27:49",
    "user_id": 122971,
    "lab": "Bash\u4e2d\u7684\u7279\u6b8a\u5b57\u7b26\uff08\u4e0b\uff09",
    "course": "\u9ad8\u7ea7Bash\u811a\u672c\u7f16\u7a0b\u6307\u5357"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:28:22",
    "user_id": 197673,
    "lab": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668",
    "course": "C\u8bed\u8a00\u5236\u4f5c\u7b80\u5355\u8ba1\u7b97\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:28:36",
    "user_id": 191567,
    "lab": "DOS\u53caDEBUG\u4ecb\u7ecd",
    "course": "\u300a\u6c47\u7f16\u8bed\u8a00\uff08\u7b2c2\u7248\uff09\u300b\u90d1\u6653\u8587\u7f16\u8457\u914d\u5957\u5b9e\u9a8c"
  },
  {
    "minutes": 57,
    "created_at": "2016-05-04 13:30:29",
    "user_id": 175174,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u4e8c",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:32:37",
    "user_id": 171965,
    "lab": "\u5b9e\u9a8c\u62a5\u544a\u56db",
    "course": "JAVA\u7a0b\u5e8f\u8bbe\u8ba1"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 13:32:53",
    "user_id": 107767,
    "lab": "Bash\u5185\u7f6e\u547d\u4ee4\u4e0e\u73af\u5883\u7b80\u4ecb",
    "course": "\u5b9e\u7528Linux Shell\u7f16\u7a0b"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-04 13:32:57",
    "user_id": 195661,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 33,
    "created_at": "2016-05-04 13:32:57",
    "user_id": 200335,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 69,
    "created_at": "2016-05-04 13:33:01",
    "user_id": 27420,
    "lab": "c\u8bed\u8a00\u5229\u7528epoll\u5b9e\u73b0\u804a\u5929\u5ba4",
    "course": "C\u8bed\u8a00\u5229\u7528epoll\u5b9e\u73b0\u9ad8\u5e76\u53d1\u804a\u5929\u5ba4"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 13:33:29",
    "user_id": 135234,
    "lab": "\u89c6\u56fe\u548cURL\u914d\u7f6e",
    "course": "[\u5df2\u4e0b\u7ebf] Python Django Web\u6846\u67b6"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 13:33:39",
    "user_id": 64633,
    "lab": "Linux \u7cfb\u7edf\u7b80\u4ecb",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-04 13:34:58",
    "user_id": 188717,
    "lab": "C \u8bed\u8a00\u6570\u7ec4",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:35:18",
    "user_id": 57253,
    "lab": "\u9009\u62e9\u5668",
    "course": "jQuery\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:35:49",
    "user_id": 2863,
    "lab": "Python\u6807\u51c6\u5e93\uff08\u4e2d\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-04 13:37:06",
    "user_id": 198638,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 13:37:06",
    "user_id": 198635,
    "lab": "Python\u6587\u672c\u89e3\u91ca\u5668",
    "course": "Python\u6587\u672c\u89e3\u6790\u5668"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 13:38:04",
    "user_id": 15711,
    "lab": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b",
    "course": "Python \u56fe\u7247\u8f6c\u5b57\u7b26\u753b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:39:40",
    "user_id": 199984,
    "lab": "Node.js\u7684http\u6a21\u5757",
    "course": "Node.js \u6559\u7a0b"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 13:40:00",
    "user_id": 195632,
    "lab": "C\u8bed\u8a00\u7248flappy_bird",
    "course": "C\u8bed\u8a00\u7248flappy_bird"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:40:18",
    "user_id": 182636,
    "lab": "Django\u5165\u95e8",
    "course": "[\u5df2\u4e0b\u7ebf] Python Django Web\u6846\u67b6"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 13:40:42",
    "user_id": 194901,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:40:42",
    "user_id": 94253,
    "lab": "\u5f00\u53d1\u73af\u5883\u4ee5\u53ca\u9879\u76ee\u4e0eApp",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 13:43:14",
    "user_id": 46343,
    "lab": "Docker API",
    "course": "\u52a8\u624b\u5b9e\u6218\u5b66Docker (15\u4e2a\u5b9e\u9a8c+54\u4e2a\u89c6\u9891)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 13:43:53",
    "user_id": 181676,
    "lab": "\u6253\u9020\u7f51\u9875\u7248\u300c\u5927\u767d\u300d- Baymax",
    "course": "\u7eaf CSS \u6253\u9020\u7f51\u9875\u7248\u300c\u5927\u767d\u300d"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-04 13:44:39",
    "user_id": 146698,
    "lab": "\u6a21\u5757\u5316\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 30,
    "created_at": "2016-05-04 13:46:40",
    "user_id": 91969,
    "lab": "Java \u6570\u7ec4",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 13:47:43",
    "user_id": 199195,
    "lab": "Hello World\uff01",
    "course": "\u65b0\u624b\u6307\u5357\u4e4b\u73a9\u8f6c\u5b9e\u9a8c\u697c"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:47:45",
    "user_id": 199873,
    "lab": "\u64cd\u4f5c\u7cfb\u7edf\u7684\u5f15\u5bfc",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 13:47:49",
    "user_id": 190767,
    "lab": "\u57fa\u7840\u7bc7 - SQL \u4ecb\u7ecd\u53ca MySQL \u5b89\u88c5",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:49:01",
    "user_id": 82553,
    "lab": "\u9879\u76ee\u56db\uff1a\u5728\u7ebf\u804a\u5929\u5ba4",
    "course": "Node.js \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:49:31",
    "user_id": 107767,
    "lab": "GCC\u7684\u4f7f\u7528",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:50:04",
    "user_id": 25538,
    "lab": "Java \u8bed\u8a00\u57fa\u7840",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 24,
    "created_at": "2016-05-04 13:50:08",
    "user_id": 154334,
    "lab": "\u67e5\u8be2\u3001\u7d22\u5f15\u4e0e\u805a\u5408",
    "course": "MongoDB \u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 45,
    "created_at": "2016-05-04 13:50:37",
    "user_id": 94253,
    "lab": "LNMP\u7cfb\u7edf\u5b89\u88c5",
    "course": "Linux Web\u8fd0\u7ef4\uff08Nginx\uff09\u5b9e\u6218 "
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 13:50:39",
    "user_id": 198398,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:51:35",
    "user_id": 200356,
    "lab": "Linux\u57fa\u7840\u77e5\u8bc6\u4e0e\u5e38\u7528\u547d\u4ee4",
    "course": "\u5b9e\u7528Linux Shell\u7f16\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:51:55",
    "user_id": 19036,
    "lab": "Redis\u7684\u9ad8\u7ea7\u5e94\u7528",
    "course": "Redis\u57fa\u7840\u6559\u7a0b"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:52:10",
    "user_id": 190677,
    "lab": "Python \u7834\u89e3\u9a8c\u8bc1\u7801",
    "course": "Python \u7834\u89e3\u9a8c\u8bc1\u7801"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:52:39",
    "user_id": 179248,
    "lab": "JavaScript \u7b80\u4ecb",
    "course": "Javascript\u57fa\u7840\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 21,
    "created_at": "2016-05-04 13:53:00",
    "user_id": 198635,
    "lab": "\u9ad8\u7ea7\u529f\u80fd\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:53:12",
    "user_id": 25538,
    "lab": "Java  \u8fd0\u7b97\u7b26",
    "course": "Java\u7f16\u7a0b\u8bed\u8a00\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-04 13:53:28",
    "user_id": 47754,
    "lab": "Numpy - \u591a\u7ef4\u6570\u7ec4\uff08\u4e0a\uff09",
    "course": "Python\u79d1\u5b66\u8ba1\u7b97(\u4e00)"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 13:53:53",
    "user_id": 107767,
    "lab": "gdb\u4f7f\u7528",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 13:54:01",
    "user_id": 200357,
    "lab": "TensorFlow \u5b9e\u9a8c\u73af\u5883\u642d\u5efa",
    "course": "TensorFlow \u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 13:54:34",
    "user_id": 120304,
    "lab": "\u6a21\u5757\u5316\u7a0b\u5e8f\u8bbe\u8ba1",
    "course": "C \u8bed\u8a00\u5165\u95e8\u6559\u7a0b"
  },
  {
    "minutes": 18,
    "created_at": "2016-05-04 13:54:42",
    "user_id": 82553,
    "lab": "\u9879\u76ee\u56db\uff1a\u5728\u7ebf\u804a\u5929\u5ba4",
    "course": "Node.js \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:54:57",
    "user_id": 199991,
    "lab": "\u57fa\u4e8eNode.js+Express\u5b9e\u73b0\u7b80\u6613\u535a\u5ba2\u7cfb\u7edf",
    "course": "[\u5df2\u4e0b\u7ebf] \u57fa\u4e8eNode.js+Express\u5b9e\u73b0\u7b80\u6613\u535a\u5ba2\u7cfb\u7edf"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 13:55:14",
    "user_id": 200314,
    "lab": "\u5f00\u53d1\u73af\u5883\u4ee5\u53ca\u9879\u76ee\u4e0eApp",
    "course": "Django \u642d\u5efa\u7b80\u6613\u535a\u5ba2"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 13:55:27",
    "user_id": 143366,
    "lab": "\u5165\u95e8",
    "course": "Bootstrap3.0\u5165\u95e8\u5b66\u4e60"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 13:55:51",
    "user_id": 50310,
    "lab": "PHP\u7b80\u4ecb",
    "course": "PHP \u7f16\u7a0b\u8bed\u8a00"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 13:56:43",
    "user_id": 199195,
    "lab": "Vim\u5feb\u901f\u5165\u95e8",
    "course": "Vim\u7f16\u8f91\u5668"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 13:56:52",
    "user_id": 190767,
    "lab": "\u57fa\u7840\u7bc7 - \u521b\u5efa\u6570\u636e\u5e93\u5e76\u63d2\u5165\u6570\u636e",
    "course": "MySQL \u57fa\u7840\u8bfe\u7a0b"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 13:59:08",
    "user_id": 192069,
    "lab": "\u9879\u76ee\u4e94\uff1a\u6587\u5b57\u804a\u5929\u5ba4",
    "course": "Python \u7ecf\u5178\u9879\u76ee\u5b9e\u6218"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-04 13:59:20",
    "user_id": 199873,
    "lab": "\u7cfb\u7edf\u8c03\u7528",
    "course": "\u64cd\u4f5c\u7cfb\u7edf\u539f\u7406\u4e0e\u5b9e\u8df5"
  },
  {
    "minutes": 6,
    "created_at": "2016-05-04 13:59:33",
    "user_id": 170440,
    "lab": "\u73af\u5883\u53d8\u91cf\u4e0e\u6587\u4ef6\u67e5\u627e",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 9,
    "created_at": "2016-05-04 14:00:16",
    "user_id": 107767,
    "lab": "Makefile\u4f7f\u7528",
    "course": "Linux\u7cfb\u7edf\u7f16\u7a0b"
  },
  {
    "minutes": 84,
    "created_at": "2016-05-04 14:00:37",
    "user_id": 46343,
    "lab": "\u57fa\u4e8eDocker API\u5f00\u53d1\u5e94\u7528",
    "course": "\u52a8\u624b\u5b9e\u6218\u5b66Docker (15\u4e2a\u5b9e\u9a8c+54\u4e2a\u89c6\u9891)"
  },
  {
    "minutes": 27,
    "created_at": "2016-05-04 14:01:06",
    "user_id": 200069,
    "lab": "Linux \u76ee\u5f55\u7ed3\u6784\u53ca\u6587\u4ef6\u57fa\u672c\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 3,
    "created_at": "2016-05-04 14:02:26",
    "user_id": 198398,
    "lab": "\u57fa\u672c\u6982\u5ff5\u53ca\u64cd\u4f5c",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  },
  {
    "minutes": 15,
    "created_at": "2016-05-04 14:02:33",
    "user_id": 198889,
    "lab": "Python\u8fdb\u9636\uff08\u4e0a\uff09",
    "course": "Python\u5feb\u901f\u6559\u7a0b"
  },
  {
    "minutes": 12,
    "created_at": "2016-05-04 14:04:13",
    "user_id": 200356,
    "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406",
    "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"
  }
]

