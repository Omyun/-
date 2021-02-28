def video_g_d(id):
    g_d = {
        "tt_from":"load_more",
        "sub_category":"video",
        "category":"all",
        "count":"20",
        "concern_id":str(id),
        "max_behot_time":"1612339703",
        "impression_info":"{\"page_id\":\"page_car_series\",\"sub_tab\":\"all\",\"product_name\":\"web\",\"car_series_id\":\""+id+"\"}",
        "aid":"1839",
        "refer":"1",
        "channel":"web",
        "device_platform":"web",
        "web_id":"532961586760236",
        "motor_feed_extra_params":"{\"new_feed\"\":\"true, \"feed_type\"\":\"1}",
        "source":"pc"
    }
    return g_d

def text_g_d(id):
    t_g_d = {
    "tt_from":"load_more",
    "sub_category":"",
    "category":"all",
    "count":"20",
    "concern_id":str(id),
    "max_behot_time":"1612351774",
    "aid":"1839",
    "refer":"1",
    "channel":"web",
    "device_platform":"web",
    "web_id":"532961586760236",
    "source":"pc",
    "impression_info":"{\"page_id\":\"page_car_series\",\"sub_tab\":\"all\",\"product_name\":\"web\",\"car_series_id\":\""+id+"\"}",
    "motor_feed_extra_params":"{\"new_feed\": true, \"feed_type\": 1}"
    }
    return t_g_d

