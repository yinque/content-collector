def camel_to_snake(camel_case):
    snake_case = ""
    for char in camel_case:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    if snake_case.startswith("_"):
        snake_case = snake_case[1:]
    return snake_case


# 指定文件路径和表名
template_name = "curd.pyi"
# table_name_list = ['User', 'News', 'NewsCategory', 'Comment', 'Message']
table_name_list = ['Note']

encoding = 'utf-8'

for table_name in table_name_list:
    snake_name = camel_to_snake(table_name)
    new_file_name = 'gen/' + snake_name+'_dao.py'

    with open(template_name, "r", encoding=encoding) as file:
        content = file.read()
        updated_content = content.replace("TableNameOrigin", table_name).replace("tablename_snackcase", snake_name)

    with open(new_file_name, "w",  encoding=encoding) as new_file:
        new_file.write(updated_content)

    # 执行替换操作
    print(f"替换后的文件已保存为: {new_file_name}")
