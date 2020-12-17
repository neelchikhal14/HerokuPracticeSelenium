i=3

base_string_start="return document.getElementsByTagName('img')["
base_string_end="].naturalHeight"



for current in range(0,i):
    final_js_query=base_string_start + str(current) + base_string_end
    print(final_js_query)
