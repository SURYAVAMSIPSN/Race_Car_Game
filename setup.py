# To make an executable. 

import cx_Freeze 

executables = [cx_Freeze.Executable("A_bit_Racey.py")]

cx_Freeze.setup(
        name="A bit Racey",
        options={"build_exe":{"packages":["pygame"], 
                              "include_files":["my_car.png"]}},
        executables = executables
        )