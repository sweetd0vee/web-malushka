queries = {
    "home_page": {
        "get_click_users_info": """
                    select u.name,g.database 
                    FROM system.users u 
                    left join (
                        select user_name,groupArray(distinct database) as database
                        from system.grants 
                        group by user_name
                    )g on u.name = g.user_name
                    where name <> 'admin' and startsWith(name, '_') = 0 
                """
    }
}
