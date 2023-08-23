import json

def create_sql(user_name):
    with open('.\\fileput\id_system.json',"r",encoding="utf-8") as openfile:
        last_id = int(json.load(openfile)['id']) + 1

    main_hold_create_id = {
        "id" : last_id
    }

    main_data_list = {
        "id" : str(last_id).zfill(9),
        "user" : user_name
    }

    with open('.\\fileput\\'+str(last_id).zfill(9)+'.json',"a+",encoding="utf-8") as outfile:
        json.dump(main_data_list ,outfile ,indent=4 ,ensure_ascii=False)

    with open('.\\fileput\id_system.json',"w",encoding="utf-8") as outfile:
        json.dump(main_hold_create_id ,outfile ,ensure_ascii=False)

#若需引用請註記出處