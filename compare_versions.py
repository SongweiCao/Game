def compared_version(version1, version2):
    """
    传入参数示例："11.13.3.6.7">"11.13.3.3.8"
    :param version1: 版本号1
    :param version2: 版本号2
    :return:  version1 < = > version2 返回 -1/0/1
    """
    list1 = str(version1).split(".")
    list2 = str(version2).split(".")

    print(list1)
    print(list2)

    for i in range(len(list1)) if len(list1) < len(list2) else range(len(list2)):
        if int(list1[i]) == int(list2[i]):
            pass
        elif int(list1[i]) < int(list2[i]):
            return -1
        else:
            return 1

    if len(list1) == len(list2):
        return 0
    elif len(list1) < len(list2):
        return -1
    else:
        return 1

result = compared_version("0.1","1.1")
print(result)