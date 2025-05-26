from tabulate import tabulate
import pandas as pd

class Employee:
    def __init__(self, name, id, courses):
        self.name = name
        self.id = id
        self.courses = courses

all_employees = [
    Employee("John", 1, [ "IT 101", "DB 202"]),
    Employee("Smith", 2, [ "IT 202"]),
    ]

arr = [ [x.name, x.id, "\n".join(x.courses)] for x in all_employees ]
df = pd.DataFrame(arr, columns=["Name", "ID", "Courses"])
print(tabulate(df, headers=df.columns, tablefmt="grid", floatfmt=".2f", showindex=False))

# group by department count
arr = [ [x.name, x.id, "\n".join(x.courses), len(x.courses)] for x in all_employees ]
df = pd.DataFrame(arr, columns=["Name", "ID", "Courses", "dept_count"])
for group_val, group_df in df.groupby("dept_count"):
    print(group_val)
    print(tabulate(group_df, headers=group_df.columns, tablefmt="grid", floatfmt=".2f", showindex=False))


