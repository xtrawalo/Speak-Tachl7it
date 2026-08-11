from pyscript import document
from pyscript import when

print("------- Speak Tachl7it -------")
print("Welcome to Speak Tachl7it!")

#numbers
nums =        {0:"amya",
               1:"yan",
               2:"sin",
               3:"krad",
               4:"koz",
               5:"smos",
               6:"sdis",
               7:"sa",
               8:"tam",
               9:"tza",
               10:"mraw",
               20:"si mraw",
               30:"kra mraw",
               40:"ko mraw",
               50:"smo mraw",
               60:"sdi mraw",
               70:"sa mraw",
               80:"ta mraw",
               90:"tza mraw",
               100:"timidi",
               "+100":"timad",
               1000:"ifd",
               "+1000":"afdan",
               1000000:"akndid",}

def translate():
    user_input = document.getElementById("number").value
    if user_input == "":
        document.getElementById("result").InnerText = "Please Enter A Number."
        return
    word = int(user_input)
    if 0 > word < 1000000 :
        document.getElementById("result").InnerText = "Number must be between 1 and 1,000,000."
        return

    typed_nums=[]
    length = len(str(word))
    num = 0
    for i in range(length):
        unit = pow(10,i+1)
        previous_num = num
        num = word % unit
        final_num = num - previous_num
        typed_nums.append(final_num)

        if len(typed_nums) == 1: #unit
            result = nums.get(typed_nums[0])

        elif len(typed_nums) == 2: #ten
            if typed_nums[0] == 0:
                result = nums.get(typed_nums[1])
            elif typed_nums[1] == 0:
                result = nums.get(typed_nums[0])
            else:
                result = (
                    f"{nums.get(typed_nums[1])} d"
                    f"{nums.get(typed_nums[0])}"
                )

        elif len(typed_nums) == 3: #hundred
            if typed_nums[2] == 0:
                if typed_nums[0] == 0:
                    result = f"{nums.get(typed_nums[1])} "
                elif typed_nums[1] == 0:
                    result = f"{nums.get(typed_nums[0])} "
                else:
                    result = (
                        f"{nums.get(typed_nums[1])} d "
                        f"{nums.get(typed_nums[0])} "
                    )
            elif typed_nums[0] == 0 and typed_nums[1] == 0:
                times = typed_nums[2] // 100
                if times == 1:
                    result = f"{nums.get(100)} "
                else:
                    result = (
                        f"{nums.get(times)} " 
                        f"{nums.get('+100')} "
                    )
            elif typed_nums[0] == 0 and typed_nums[1] != 0:
                times = typed_nums[2] // 100
                if times == 1:
                    result = ( 
                        f"{nums.get(100)} d "
                        f"{nums.get(typed_nums[1])} "
                    )
                else:
                    result = (
                        f"{nums.get(times)} " 
                        f"{nums.get('+100')} d " 
                        f"{nums.get(typed_nums[1])} "
                    )
            elif typed_nums[0] != 0 and typed_nums[1] == 0:
                times = typed_nums[2] // 100
                if times == 1:
                    result = (
                        f"{nums.get(100)} d " 
                        f"{nums.get(typed_nums[0])} "
                    )
                else:
                    result = (
                        f"{nums.get(times)} " 
                        f"{nums.get('+100')} d " 
                        f"{nums.get(typed_nums[0])} "
                    )
            else:
                times = typed_nums[2] // 100
                if times == 1:
                    result = (
                        f"{nums.get(100)} d " 
                        f"{nums.get(typed_nums[1])} d " 
                        f"{nums.get(typed_nums[0])} "
                    )
                else:
                    result = (
                        f"{nums.get(times)} " 
                        f"{nums.get('+100')} d " 
                        f"{nums.get(typed_nums[1])} d " 
                        f"{nums.get(typed_nums[0])} "
                    )

        elif len(typed_nums) == 4: #thousand
            times = typed_nums[3] // 1000
            if times != 0 :
                if times == 1:
                    result = f" {nums.get(1000)} "
                else:
                    result = (
                        f"{nums.get(times)} n " 
                        f"{nums.get('+1000')} "
                    )
            if times != 0:
                if typed_nums[2] != 0:
                    if typed_nums[0] == 0 and typed_nums[1] == 0:
                        times = typed_nums[2] // 100
                        if times == 1:
                            result += f"d {nums.get(100)} "
                        else:
                            result += (
                                f"d {nums.get(times)} "
                                f"{nums.get('+100')} "
                            )
                    elif typed_nums[0] == 0 and typed_nums[1] != 0:
                        times = typed_nums[2] // 100
                        if times == 1:
                            result += (
                                f"d {nums.get(100)} d "
                                f"{nums.get(typed_nums[1])} "
                            )
                        else:
                            result += (
                                f"d {nums.get(times)} " 
                                f"{nums.get('+100')} d " 
                                f"{nums.get(typed_nums[1])} "
                            )
                    elif typed_nums[0] != 0 and typed_nums[1] == 0:
                        times = typed_nums[2] // 100
                        if times == 1:
                            result += (
                                f"d {nums.get(100)} d " 
                                f"{nums.get(typed_nums[0])} "
                            )
                        else:
                            result += (
                                f"d {nums.get(times)} " 
                                f"{nums.get('+100')} d " 
                                f"{nums.get(typed_nums[0])} "
                            )
                    else:
                        times = typed_nums[2] // 100
                        if times == 1:
                            result += (
                                f"d {nums.get(100)} d " 
                                f"{nums.get(typed_nums[1])} d " 
                                f"{nums.get(typed_nums[0])} "
                            )
                        else:
                            result += (
                                f"d {nums.get(times)} " 
                                f"{nums.get('+100')} d " 
                                f"{nums.get(typed_nums[1])} d " 
                                f"{nums.get(typed_nums[0])} "
                            )
                else:
                        if typed_nums[0] == 0 and typed_nums[1] == 0:
                            print()
                        elif typed_nums[0] == 0 and typed_nums[1] != 0:
                            result += f"d {nums.get(typed_nums[1])} "
                        elif typed_nums[0] != 0 and typed_nums[1] == 0:
                            result += f"d {nums.get(typed_nums[0])} "
                        elif typed_nums[0] != 0 and typed_nums[1] != 0:
                            result += (
                                f"d {nums.get(typed_nums[1])} d " 
                                f"{nums.get(typed_nums[0])} "
                            )
            else:
                if typed_nums[2] != 0:
                    if typed_nums[0] == 0 and typed_nums[1] == 0:
                        times = typed_nums[2] // 100
                        if times == 1:
                            result = f"{nums.get(100)} "
                        else:
                            result = (
                                f"{nums.get(times)} " 
                                f"{nums.get('+100')} "
                            )
                    elif typed_nums[0] == 0 and typed_nums[1] != 0:
                        times = typed_nums[2] // 100
                        if times == 1:
                            result = (
                                f"{nums.get(100)} d " 
                                f"{nums.get(typed_nums[1])} "
                            )
                        else:
                            result = (
                                f"{nums.get(times)} " 
                                f"{nums.get('+100')} d " 
                                f"{nums.get(typed_nums[1])} "
                            )
                    elif typed_nums[0] != 0 and typed_nums[1] == 0:
                        times = typed_nums[2] // 100
                        if times == 1:
                            result = (
                                f"{nums.get(100)} d " 
                                f"{nums.get(typed_nums[0])} "
                            )
                        else:
                            result = (
                                f"{nums.get(times)} " 
                                f"{nums.get('+100')} d " 
                                f"{nums.get(typed_nums[0])} "
                            )
                    else:
                        times = typed_nums[2] // 100
                        if times == 1:
                            result = (
                                f"{nums.get(100)} d " 
                                f"{nums.get(typed_nums[1])} d "
                                f"{nums.get(typed_nums[0])} "
                            )
                        else:
                            result = (
                                f"{nums.get(times)} "
                                f"{nums.get('+100')} d " 
                                f"{nums.get(typed_nums[1])} d " 
                                f"{nums.get(typed_nums[0])} "
                            )
                else:
                        if typed_nums[0] == 0 and typed_nums[1] == 0:
                            result = f"{nums.get(0)} "
                        elif typed_nums[0] == 0 and typed_nums[1] != 0:
                            result = f"{nums.get(typed_nums[1])} "
                        elif typed_nums[0] != 0 and typed_nums[1] == 0:
                            result = f"{nums.get(typed_nums[0])} "
                        elif typed_nums[0] != 0 and typed_nums[1] != 0:
                            result = (
                                f"{nums.get(typed_nums[1])} d " 
                                f"{nums.get(typed_nums[0])} "
                            )

        elif len(typed_nums) == 5: #ten thousands
            times = typed_nums[4] // 1000
            unit_times = typed_nums[3] // 1000
            if times != 0 and unit_times == 0:
                print(f"{nums.get(times)} n {nums.get('+1000')}", end=" ")
            elif times == 0 and unit_times != 0:
                print(f"{nums.get(unit_times)} n {nums.get('+1000')}", end=" ")
            elif times != 0 and unit_times != 0:
                print(f"{nums.get(times)} d {nums.get(unit_times)} n {nums.get('+1000')}", end=" ")
            if times != 0:
                if typed_nums[2] != 0:
                    if typed_nums[0] == 0 and typed_nums[1] == 0:
                        times = typed_nums[2] // 100
                        if times == 1:
                            print(f"d {nums.get(100)}")
                        else:
                            print(f"d {nums.get(times)} {nums.get('+100')}")
                    elif typed_nums[0] == 0 and typed_nums[1] != 0:
                        times = typed_nums[2] // 100
                        if times == 1:
                            print(f"d {nums.get(100)} d {nums.get(typed_nums[1])}")
                        else:
                            print(f"d {nums.get(times)} {nums.get('+100')} d {nums.get(typed_nums[1])}")
                    elif typed_nums[0] != 0 and typed_nums[1] == 0:
                        times = typed_nums[2] // 100
                        if times == 1:
                            print(f"d {nums.get(100)} d {nums.get(typed_nums[0])}")
                        else:
                            print(f"d {nums.get(times)} {nums.get('+100')} d {nums.get(typed_nums[0])}")
                    else:
                        times = typed_nums[2] // 100
                        if times == 1:
                            print(f"d {nums.get(100)} d {nums.get(typed_nums[1])} d {nums.get(typed_nums[0])}")
                        else:
                            print(f"d {nums.get(times)} {nums.get('+100')} d {nums.get(typed_nums[1])} d {nums.get(typed_nums[0])}")
                else:
                        if typed_nums[0] == 0 and typed_nums[1] == 0:
                            print()
                        elif typed_nums[0] == 0 and typed_nums[1] != 0:
                            print(f"d {nums.get(typed_nums[1])}")
                        elif typed_nums[0] != 0 and typed_nums[1] == 0:
                            print(f"d {nums.get(typed_nums[0])}")
                        elif typed_nums[0] != 0 and typed_nums[1] != 0:
                            print(f"d {nums.get(typed_nums[1])} d {nums.get(typed_nums[0])}")
            else:
                if typed_nums[2] != 0:
                    if typed_nums[0] == 0 and typed_nums[1] == 0:
                        times = typed_nums[2] // 100
                        if times == 1:
                            print(f"{nums.get(100)}")
                        else:
                            print(f"{nums.get(times)} {nums.get('+100')}")
                    elif typed_nums[0] == 0 and typed_nums[1] != 0:
                        times = typed_nums[2] // 100
                        if times == 1:
                            print(f"{nums.get(100)} d {nums.get(typed_nums[1])}")
                        else:
                            print(f"{nums.get(times)} {nums.get('+100')} d {nums.get(typed_nums[1])}")
                    elif typed_nums[0] != 0 and typed_nums[1] == 0:
                        times = typed_nums[2] // 100
                        if times == 1:
                            print(f"{nums.get(100)} d {nums.get(typed_nums[0])}")
                        else:
                            print(f"{nums.get(times)} {nums.get('+100')} d {nums.get(typed_nums[0])}")
                    else:
                        times = typed_nums[2] // 100
                        if times == 1:
                            print(f"{nums.get(100)} d {nums.get(typed_nums[1])} d {nums.get(typed_nums[0])}")
                        else:
                            print(f"{nums.get(times)} {nums.get('+100')} d {nums.get(typed_nums[1])} d {nums.get(typed_nums[0])}")
                else:
                        if typed_nums[0] == 0 and typed_nums[1] == 0:
                            print(f"{nums.get(0)}")
                        elif typed_nums[0] == 0 and typed_nums[1] != 0:
                            print(f"{nums.get(typed_nums[1])}")
                        elif typed_nums[0] != 0 and typed_nums[1] == 0:
                            print(f"{nums.get(typed_nums[0])}")
                        elif typed_nums[0] != 0 and typed_nums[1] != 0:
                            print(f"{nums.get(typed_nums[1])} d {nums.get(typed_nums[0])}")

        elif len(typed_nums) == 6: #hundred thousands
            times = typed_nums[5] // 100000
            ten_times = typed_nums[4] // 1000
            unit_times = typed_nums[3] // 1000
            if times == 0:
                if unit_times == 0:
                    if ten_times == 0:
                        pass
                    else:
                        print(f"{nums.get(ten_times)} n {nums.get('+1000')}", end=" ")
                elif ten_times == 0:
                    if unit_times == 1:
                        print(f"{nums.get(1000)}", end=" ")
                    else:
                        print(f"{nums.get(unit_times)} n {nums.get('+1000')}", end=" ")
                else:
                    print(f"{nums.get(ten_times)} d {nums.get(unit_times)} n {nums.get('+1000')}", end=" ")
            elif unit_times == 0 and ten_times == 0:
                if times == 1:
                    print(f"{nums.get(100)} n {nums.get('+1000')}", end=" ")
                else:
                    print(f"{nums.get(times)} {nums.get('+100')} n {nums.get('+1000')}", end=" ")
            elif unit_times == 0 and ten_times != 0:
                if times == 1:
                    print(f"{nums.get(100)} d {nums.get(ten_times)} n {nums.get('+1000')}", end=" ")
                else:
                    print(f"{nums.get(times)} {nums.get('+100')} d {nums.get(ten_times)} n {nums.get('+1000')}", end=" ")
            elif unit_times != 0 and ten_times == 0:
                if times == 1:
                    print(f"{nums.get(100)} d {nums.get(unit_times)} n {nums.get('+1000')}", end=" ")
                else:
                    print(f"{nums.get(times)} {nums.get('+100')} d {nums.get(unit_times)} n {nums.get('+1000')}", end=" ")
            else:
                if times == 1:
                    print(f"{nums.get(100)} d {nums.get(ten_times)} d {nums.get(unit_times)} n {nums.get('+1000')}", end=" ")
                else:
                    print(f"{nums.get(times)} {nums.get('+100')} d {nums.get(ten_times)} d {nums.get(unit_times)} n {nums.get('+1000')}", end=" ")
            if times != 0 or ten_times !=0 or unit_times != 0:
                if typed_nums[2] != 0:
                    if typed_nums[0] == 0 and typed_nums[1] == 0:
                        times = typed_nums[2] // 100
                        if times == 1:
                            print(f"d {nums.get(100)}")
                        else:
                            print(f"d {nums.get(times)} {nums.get('+100')}")
                    elif typed_nums[0] == 0 and typed_nums[1] != 0:
                        times = typed_nums[2] // 100
                        if times == 1:
                            print(f"d {nums.get(100)} d {nums.get(typed_nums[1])}")
                        else:
                            print(f"d {nums.get(times)} {nums.get('+100')} d {nums.get(typed_nums[1])}")
                    elif typed_nums[0] != 0 and typed_nums[1] == 0:
                        times = typed_nums[2] // 100
                        if times == 1:
                            print(f"d {nums.get(100)} d {nums.get(typed_nums[0])}")
                        else:
                            print(f"d {nums.get(times)} {nums.get('+100')} d {nums.get(typed_nums[0])}")
                    else:
                        times = typed_nums[2] // 100
                        if times == 1:
                            print(f"d {nums.get(100)} d {nums.get(typed_nums[1])} d {nums.get(typed_nums[0])}")
                        else:
                            print(f"d {nums.get(times)} {nums.get('+100')} d {nums.get(typed_nums[1])} d {nums.get(typed_nums[0])}")
                else:
                        if typed_nums[0] == 0 and typed_nums[1] == 0:
                            print()
                        elif typed_nums[0] == 0 and typed_nums[1] != 0:
                            print(f"d {nums.get(typed_nums[1])}")
                        elif typed_nums[0] != 0 and typed_nums[1] == 0:
                            print(f"d {nums.get(typed_nums[0])}")
                        elif typed_nums[0] != 0 and typed_nums[1] != 0:
                            print(f"d {nums.get(typed_nums[1])} d {nums.get(typed_nums[0])}")
            else:
                if typed_nums[2] != 0:
                    if typed_nums[0] == 0 and typed_nums[1] == 0:
                        times = typed_nums[2] // 100
                        if times == 1:
                            print(f"{nums.get(100)}")
                        else:
                            print(f"{nums.get(times)} {nums.get('+100')}")
                    elif typed_nums[0] == 0 and typed_nums[1] != 0:
                        times = typed_nums[2] // 100
                        if times == 1:
                            print(f"{nums.get(100)} d {nums.get(typed_nums[1])}")
                        else:
                            print(f"{nums.get(times)} {nums.get('+100')} d {nums.get(typed_nums[1])}")
                    elif typed_nums[0] != 0 and typed_nums[1] == 0:
                        times = typed_nums[2] // 100
                        if times == 1:
                            print(f"{nums.get(100)} d {nums.get(typed_nums[0])}")
                        else:
                            print(f"{nums.get(times)} {nums.get('+100')} d {nums.get(typed_nums[0])}")
                    else:
                        times = typed_nums[2] // 100
                        if times == 1:
                            print(f"{nums.get(100)} d {nums.get(typed_nums[1])} d {nums.get(typed_nums[0])}")
                        else:
                            print(f"{nums.get(times)} {nums.get('+100')} d {nums.get(typed_nums[1])} d {nums.get(typed_nums[0])}")
                else:
                        if typed_nums[0] == 0 and typed_nums[1] == 0:
                            print(f"{nums.get(0)}")
                        elif typed_nums[0] == 0 and typed_nums[1] != 0:
                            print(f"{nums.get(typed_nums[1])}")
                        elif typed_nums[0] != 0 and typed_nums[1] == 0:
                            print(f"{nums.get(typed_nums[0])}")
                        elif typed_nums[0] != 0 and typed_nums[1] != 0:
                            print(f"{nums.get(typed_nums[1])} d {nums.get(typed_nums[0])}")

        elif len(typed_nums) == 7:
            if typed_nums[6] == 1000000:  # million
                print(nums.get(typed_nums[6]))
            elif typed_nums[6] == 0:
                times = typed_nums[5] // 100000
                ten_times = typed_nums[4] // 1000
                unit_times = typed_nums[3] // 1000
                if times == 0:
                    if unit_times == 0:
                        if ten_times == 0:
                            pass
                        else:
                            print(f"{nums.get(ten_times)} n {nums.get('+1000')}", end=" ")
                    elif ten_times == 0:
                        if unit_times == 1:
                            print(f"{nums.get(1000)}", end=" ")
                        else:
                            print(f"{nums.get(unit_times)} n {nums.get('+1000')}", end=" ")
                    else:
                        print(f"{nums.get(ten_times)} d {nums.get(unit_times)} n {nums.get('+1000')}", end=" ")
                elif unit_times == 0 and ten_times == 0:
                    if times == 1:
                        print(f"{nums.get(100)} n {nums.get('+1000')}", end=" ")
                    else:
                        print(f"{nums.get(times)} {nums.get('+100')} n {nums.get('+1000')}", end=" ")
                elif unit_times == 0 and ten_times != 0:
                    if times == 1:
                        print(f"{nums.get(100)} d {nums.get(ten_times)} n {nums.get('+1000')}", end=" ")
                    else:
                        print(f"{nums.get(times)} {nums.get('+100')} d {nums.get(ten_times)} n {nums.get('+1000')}",
                                end=" ")
                elif unit_times != 0 and ten_times == 0:
                    if times == 1:
                        print(f"{nums.get(100)} d {nums.get(unit_times)} n {nums.get('+1000')}", end=" ")
                    else:
                        print(f"{nums.get(times)} {nums.get('+100')} d {nums.get(unit_times)} n {nums.get('+1000')}",
                                end=" ")
                else:
                    if times == 1:
                        print(f"{nums.get(100)} d {nums.get(ten_times)} d {nums.get(unit_times)} n {nums.get('+1000')}",
                                end=" ")
                    else:
                        print(
                            f"{nums.get(times)} {nums.get('+100')} d {nums.get(ten_times)} d {nums.get(unit_times)} n {nums.get('+1000')}",
                            end=" ")
                if times != 0 or ten_times != 0 or unit_times != 0:
                    if typed_nums[2] != 0:
                        if typed_nums[0] == 0 and typed_nums[1] == 0:
                            times = typed_nums[2] // 100
                            if times == 1:
                                print(f"d {nums.get(100)}")
                            else:
                                print(f"d {nums.get(times)} {nums.get('+100')}")
                        elif typed_nums[0] == 0 and typed_nums[1] != 0:
                            times = typed_nums[2] // 100
                            if times == 1:
                                print(f"d {nums.get(100)} d {nums.get(typed_nums[1])}")
                            else:
                                print(f"d {nums.get(times)} {nums.get('+100')} d {nums.get(typed_nums[1])}")
                        elif typed_nums[0] != 0 and typed_nums[1] == 0:
                            times = typed_nums[2] // 100
                            if times == 1:
                                print(f"d {nums.get(100)} d {nums.get(typed_nums[0])}")
                            else:
                                print(f"d {nums.get(times)} {nums.get('+100')} d {nums.get(typed_nums[0])}")
                        else:
                            times = typed_nums[2] // 100
                            if times == 1:
                                print(f"d {nums.get(100)} d {nums.get(typed_nums[1])} d {nums.get(typed_nums[0])}")
                            else:
                                print(
                                    f"d {nums.get(times)} {nums.get('+100')} d {nums.get(typed_nums[1])} d {nums.get(typed_nums[0])}")
                    else:
                        if typed_nums[0] == 0 and typed_nums[1] == 0:
                            print()
                        elif typed_nums[0] == 0 and typed_nums[1] != 0:
                            print(f"d {nums.get(typed_nums[1])}")
                        elif typed_nums[0] != 0 and typed_nums[1] == 0:
                            print(f"d {nums.get(typed_nums[0])}")
                        elif typed_nums[0] != 0 and typed_nums[1] != 0:
                            print(f"d {nums.get(typed_nums[1])} d {nums.get(typed_nums[0])}")
                else:
                    if typed_nums[2] != 0:
                        if typed_nums[0] == 0 and typed_nums[1] == 0:
                            times = typed_nums[2] // 100
                            if times == 1:
                                print(f"{nums.get(100)}")
                            else:
                                print(f"{nums.get(times)} {nums.get('+100')}")
                        elif typed_nums[0] == 0 and typed_nums[1] != 0:
                            times = typed_nums[2] // 100
                            if times == 1:
                                print(f"{nums.get(100)} d {nums.get(typed_nums[1])}")
                            else:
                                print(f"{nums.get(times)} {nums.get('+100')} d {nums.get(typed_nums[1])}")
                        elif typed_nums[0] != 0 and typed_nums[1] == 0:
                            times = typed_nums[2] // 100
                            if times == 1:
                                print(f"{nums.get(100)} d {nums.get(typed_nums[0])}")
                            else:
                                print(f"{nums.get(times)} {nums.get('+100')} d {nums.get(typed_nums[0])}")
                        else:
                            times = typed_nums[2] // 100
                            if times == 1:
                                print(f"{nums.get(100)} d {nums.get(typed_nums[1])} d {nums.get(typed_nums[0])}")
                            else:
                                print(
                                    f"{nums.get(times)} {nums.get('+100')} d {nums.get(typed_nums[1])} d {nums.get(typed_nums[0])}")
                    else:
                        if typed_nums[0] == 0 and typed_nums[1] == 0:
                            print(f"{nums.get(0)}")
                        elif typed_nums[0] == 0 and typed_nums[1] != 0:
                            print(f"{nums.get(typed_nums[1])}")
                        elif typed_nums[0] != 0 and typed_nums[1] == 0:
                            print(f"{nums.get(typed_nums[0])}")
                        elif typed_nums[0] != 0 and typed_nums[1] != 0:
                            print(f"{nums.get(typed_nums[1])} d {nums.get(typed_nums[0])}")

    document.getElementId(result).innerText = result

@when("click","#translate")
def button_click(event):
    translate
