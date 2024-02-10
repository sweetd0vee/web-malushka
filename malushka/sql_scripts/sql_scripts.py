queries = {
    "home_page": {
        "sql_get_last_updates": """
                select t1.`Category 1` as Category1, time_load_1 as Estim,time_load_2 as KPI,time_load_3 as Fact, User_load_1,User_load_2,User_load_3
                from(
                    SELECT *
                        FROM (    
                                select dictGet('DP_Analytics_dictionaries.Calc3_ItemType_Categories_dict_cat1', 'Category 1', tuple(assumeNotNull(`Category 1`))) as `Category 1`,
                                        MAX(Time_load) as time_load_1,
                                        argMax(User_load,Time_load) as User_load_1 
                                from calc_mp.main_datamart_d 
                                where Version = 1 and empty(`Category 1`) = 0
                                group by `Category 1` ,Version


                        ) t1 
                        left JOIN ( 
                            select dictGet('DP_Analytics_dictionaries.Calc3_ItemType_Categories_dict_cat1', 'Category 1', tuple(assumeNotNull(`Category 1`))) as `Category 1`,
                                    MAX(Time_load) as time_load_2,
                                        argMax(User_load,Time_load) as User_load_2
                            from calc_mp.main_datamart_d t2
                            where Version = 2
                            group by `Category 1` ,Version 
                        ) t2 on t1.`Category 1` = t2.`Category 1`
                )t1
                left JOIN ( 
                            select dictGet('DP_Analytics_dictionaries.Calc3_ItemType_Categories_dict_cat1', 'Category 1', tuple(assumeNotNull(`Category 1`))) as `Category 1`,
                                    MAX(Time_load) as time_load_3,
                                    argMax(User_load,Time_load) as User_load_3
                            from calc_mp.main_datamart_d t2
                            where Version = 3
                            group by `Category 1` ,Version 
                        ) t3 on t1.`Category 1` = t3.`Category 1`
            """,
        "get_log_data": """
                    SELECT t2.Project, t2.status, t2.time_load, t2.`result`
                    from bot_dev.Webma_external_script_info t1
                    left join(
                        select Project ,argMax(Status,Time_load) as status ,MAX(Time_load) as time_load ,argMax(`Result` ,Time_load) as `result`
                        from bot_dev.Webma_external_script_logs lfw
                        group by Project
                    )t2 on t1.script_name = t2.Project
                    where visible_on_web = '1'
                """,
        "get_last_timeload_mp": """
                    SELECT  DISTINCT dictGet('DP_Analytics_dictionaries.Calc3_ItemType_Categories_dict_cat1', 'Category 1',tuple(assumeNotNull(`Category 1`))) as `Category 1`,max(Time_load)
                    from calc_mp.main_datamart_d cmind 
                    where Version_to_analitic = 2 and Version = 1 
                    group by `Category 1` 
                    order by `Category 1`
                """,
    }
}
