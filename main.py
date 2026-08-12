from flask import Flask, render_template, request

app = Flask(__name__)

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

result = ""
times = ""
typed_nums=[]

def first_digit():
    result = nums.get(typed_nums[0])
    return result

def teen():
    if typed_nums[0] == 0:
        result = nums.get(typed_nums[1])
    elif typed_nums[1] == 0:
        result = nums.get(typed_nums[0])
    else:
        result = (
            f"{nums.get(typed_nums[1])} d "
            f"{nums.get(typed_nums[0])} "
        )
    return result

def hundred():
    if typed_nums[2] == 0:
        result = teen()
    elif typed_nums[0] == 0 and typed_nums[1] == 0:
        times = typed_nums[2] // 100
        if times == 1:
            result = nums.get(100)
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

    return result

def _hundred():
    if typed_nums[2] == 0:
        result = f" d {teen()}"
    elif typed_nums[0] == 0 and typed_nums[1] == 0:
        times = typed_nums[2] // 100
        if times == 1:
            result = f"d {nums.get(100)}"
        else:
            result = (
                f"d {nums.get(times)} " 
                f"{nums.get('+100')} "
            )
    elif typed_nums[0] == 0 and typed_nums[1] != 0:
        times = typed_nums[2] // 100
        if times == 1:
            result = ( 
                f"d {nums.get(100)} d "
                f"{nums.get(typed_nums[1])} "
            )
        else:
            result = (
                f"d {nums.get(times)} " 
                f"{nums.get('+100')} d " 
                f"{nums.get(typed_nums[1])} "
            )
    elif typed_nums[0] != 0 and typed_nums[1] == 0:
        times = typed_nums[2] // 100
        if times == 1:
            result = (
                f"d {nums.get(100)} d " 
                f"{nums.get(typed_nums[0])} "
            )
        else:
            result = (
                f"d {nums.get(times)} " 
                f"{nums.get('+100')} d " 
                f"{nums.get(typed_nums[0])} "
            )
    else:
        times = typed_nums[2] // 100
        if times == 1:
            result = (
                f"d {nums.get(100)} d " 
                f"{nums.get(typed_nums[1])} d " 
                f"{nums.get(typed_nums[0])} "
            )
        else:
            result = (
                f"d {nums.get(times)} " 
                f"{nums.get('+100')} d " 
                f"{nums.get(typed_nums[1])} d " 
                f"{nums.get(typed_nums[0])} "
            )

    return result

def thounsand():
    if times != 0:
        if typed_nums[0] == 0 and typed_nums[1] == 0 and typed_nums[2] == 0:
            result = ""
        else:
            result = _hundred()
    else:
        if typed_nums[0] == 0 and typed_nums[1] == 0 and typed_nums[2] == 0:
            result = ""
        else:
            result = hundred()
    return result

def hundred_thousands():
    times = typed_nums[5] // 100000
    ten_times = typed_nums[4] // 1000
    unit_times = typed_nums[3] // 1000
    if times == 0:
        if unit_times == 0:
            if ten_times != 0:
                result = (
                    f"{nums.get(ten_times)} n " 
                    f"{nums.get('+1000')} "
                )
        elif ten_times == 0:
            if unit_times == 1:
                result = nums.get(1000)
            else:
                result = (
                    f"{nums.get(unit_times)} n " 
                    f"{nums.get('+1000')}"
                )
        else:
            result = (
                f"{nums.get(ten_times)} d " 
                f"{nums.get(unit_times)} n " 
                f"{nums.get('+1000')} "
            )
    elif unit_times == 0 and ten_times == 0:
        if times == 1:
            result = (
                f"{nums.get(100)} n "
                f"{nums.get('+1000')} "
            )
        else:
            result = (
                f"{nums.get(times)} " 
                f"{nums.get('+100')} n " 
                f"{nums.get('+1000')} "
            )
    elif unit_times == 0 and ten_times != 0:
        if times == 1:
            result = (
                f"{nums.get(100)} d "
                f"{nums.get(ten_times)} n "
                f"{nums.get('+1000')} "
            )
        else:
            result = (
                f"{nums.get(times)} "
                f"{nums.get('+100')} d "
                f"{nums.get(ten_times)} n "
                f"{nums.get('+1000')} "
            )
    elif unit_times != 0 and ten_times == 0:
        if times == 1:
            result = (
                f"{nums.get(100)} d "
                f"{nums.get(unit_times)} n "
                f"{nums.get('+1000')} "
            )
        else:
            result = (
                f"{nums.get(times)} "
                f"{nums.get('+100')} d "
                f"{nums.get(unit_times)} n " 
                f"{nums.get('+1000')} "
            )
    else:
        if times == 1:
            result = (
                f"{nums.get(100)} d " 
                f"{nums.get(ten_times)} d "
                f"{nums.get(unit_times)} n "
                f"{nums.get('+1000')} "
            )
        else:
            result = (
                f"{nums.get(times)} "
                f"{nums.get('+100')} d "
                f"{nums.get(ten_times)} d "
                f"{nums.get(unit_times)} n "
                f"{nums.get('+1000')} "
            )
    if times != 0 or ten_times !=0 or unit_times != 0:
        result = hundred()
    else:
        result = _hundred()

    return result

def translate(word):
    global typed_nums
    typed_nums = []
    length = len(str(word))
    num = 0

    for i in range(length):
        unit = pow(10,i+1)
        previous_num = num
        num = word % unit
        final_num = num - previous_num
        typed_nums.append(final_num)

    if len(typed_nums) == 1: #unit
        result = first_digit()
    elif len(typed_nums) == 2: #ten
        result = teen()
    elif len(typed_nums) == 3: #hundred
        result = hundred()


    elif len(typed_nums) == 4: #thousand
        times = typed_nums[3] // 1000
        if times != 0:
            if times == 1:
                result = f"{nums.get(1000)} "
            else:
                result = (
                    f"{nums.get(times)} n " 
                    f"{nums.get('+1000')} "
            )
        else:
            result = ""
        
        result += thounsand()


    elif len(typed_nums) == 5: #ten thousands
        times = typed_nums[4] // 1000
        unit_times = typed_nums[3] // 1000
        if times != 0 and unit_times == 0:
            result = (
                f"{nums.get(times)} n "
                f"{nums.get('+1000')} "
            )
        elif times == 0 and unit_times != 0:
            result = (
                f"{nums.get(unit_times)} n "
                f"{nums.get('+1000')} "
            )
        elif times != 0 and unit_times != 0:
            result = (
                f"{nums.get(times)} d "
                f"{nums.get(unit_times)} n "
                f"{nums.get('+1000')} "
            )
        else:
            result = ""
        
        result += thounsand()

    elif len(typed_nums) == 6: #hundred thousands
        result = hundred_thousands()
    elif len(typed_nums) == 7:
        if typed_nums[6] == 1000000:  # million
            result = nums.get(typed_nums[6])
        elif typed_nums[6] == 0:
            result = hundred_thousands()

    return result.strip()

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        user_input = request.form["number"]

        if user_input == "":
            result = "Please Enter A Number."
        else:
            try:
                word = int(user_input)

                if word < 0 or word > 1000000 :
                    result = "Number must be between 0 and 1,000,000."
                else:
                    result = translate(word)
            except:
                result = "Invalid input. Please enter a whole number."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
