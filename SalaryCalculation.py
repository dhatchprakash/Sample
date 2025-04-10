# SalaryCalculation.py

employee = {}

def calculate_salary(name, basic_pay, hra, acs, etc):
    total_salary = basic_pay + hra + acs + etc
    employee[name] = {
        "basic_pay": basic_pay,
        "hra": hra,
        "acs": acs,
        "etc": etc,
        "total_salary": total_salary
    }
    return total_salary

def salary_after_hike(name, hike_percent):
    if name in employee:
        original_salary = employee[name]["total_salary"]
        hike_amount = original_salary * (hike_percent / 100)
        new_salary = original_salary + hike_amount
        employee[name]["hike_percent"] = hike_percent
        employee[name]["salary_after_hike"] = new_salary
        return new_salary
    else:
        return something_not_ok(f"Employee {name} not found.")

def something_not_ok(message="Something went wrong"):
    print("❌", message)
    return None

def notice_period(name, is_serving):
    if is_serving:
        print(f"⚠️ {name} is currently serving the notice period.")
    else:
        print(f"✅ {name} is an active employee.")

def itr(name):
    if name in employee:
        salary = employee[name].get("salary_after_hike", employee[name]["total_salary"])
        if salary > 500000:
            print(f"💰 {name} must file ITR. Salary: ₹{salary}")
        else:
            print(f"🟢 {name} is exempt from ITR. Salary: ₹{salary}")
    else:
        something_not_ok(f"Employee {name} not found.")


       
