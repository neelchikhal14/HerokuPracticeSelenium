i=3


base_string_start="return check_box_elements_list["
base_string_end="].checked"



for current in range(0,i):
    final_js_query=base_string_start + str(current) + base_string_end
    print(final_js_query)
