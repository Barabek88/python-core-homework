def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    categories_list = []

    for categoriesId in mapping.get('categoryIdsSorted'):
        category = mapping.get('categories').get(categoriesId)
        roles_list = []

        for roleId in category.get('roleIds'):
            role = mapping.get("roles").get(roleId)
            roles_list.append({"id": role.get("id"), "text": role.get("name")})

        categories_list.append(
            {"id": "category-" + category.get('id'), "text": category.get('name'), "items": roles_list}
        )

    return {"categories": categories_list}
