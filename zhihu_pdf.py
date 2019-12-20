import requests
import pdfkit
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def get_data(url):
    try:
        headers = {
            'cookie': '_zap=fc49d92e-f244-4643-b38a-abae1a61d2e6; d_c0="APDqCX_qkw-PTsfKES3gDJUuZRAC5i0buzU=|1560404512"; __utma=51854390.291149964.1562223544.1562223544.1562223544.1; __utmz=51854390.1562223544.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.000--|3=entry_date=20190704=1; z_c0="2|1:0|10:1574163854|4:z_c0|92:Mi4xMHJpWUR3QUFBQUFBOE9vSmYtcVREeVlBQUFCZ0FsVk5qaVBCWGdCUnpyNG1wLTQ1eUpHaGRKRmJVdUJ6MjFhVEJn|867598c121c674df00282eb03e4c81a60c52aef2a143f18400b952e63d3f7fb8"; tst=r; _xsrf=cda689f5-68f8-43bc-b472-99284e7b87bd; q_c1=add64800e7534dc69f381a17e6402522|1576809306000|1562223537000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1576820386,1576821396,1576821432,1576821535; tgw_l7_route=ace26f527cbd74fe33dbcdf5e5402f84; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1576826407',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'x-ab-param': 'zr_answer_rec_cp=open;se_pek_test2=0;se_subtext=1;zr_des_detail=0;se_aa_base=0;se_cate=1;soc_update=1;ug_newtag=1;zr_esmm_model_mix=model_17;se_entity_model_14=0;se_backsearch=0;tp_club_pk=1;tp_topic_head=0;li_qa_cover=old;se_preset_label=0;se_multianswer=1;tp_topic_tab=0;li_se_heat=1;li_video_section=1;li_de=no;zr_recall_heatscore=4_6;se_pek_test=0;se_cardrank_4=1;soc_leave_recommend=2;li_se_media_icon=1;zr_km_feed_rerank=0;tp_score_1=a;tp_sft_v2=d;li_ebook_audio=0;zw_sameq_sorce=999;se_webrs=1;se_hotsearch=1;se_movietab=1;soc_zcfw_broadcast2=1;se_amovietab=1;se_club_post=5;zr_prerank_heatscore=true;zr_slotpaidexp=7;se_entity_model=1;se_site_onebox=0;tsp_redirecthotlist=8;li_paid_answer_exp=0;li_qa_ad_card=0;soc_bignew=1;pf_newguide_vertical=0;ug_goodcomment_0=1;ug_fw_answ_aut_1=0;tp_qa_metacard_top=top;tsp_hotlist_ui=2;li_vip_no_ad_mon=0;zr_rewrite_query=1;zr_km_feed_prerank=new;soc_authormore=0;zr_video_recall=current_recall;tp_topic_entry=0;ls_videoad=2;qap_thanks=1;zr_km_recall=default;tp_club_header=1;li_album_liutongab=0;soc_special=0;ls_zvideo_like=2;qap_question_author=0;zr_infinity_member=close;se_topiclabel=1;se_time_threshold=0;se_adxtest=1;se_use_zitem=0;soc_zcfw_badcase=0;se_zu_onebox=0;se_featured=1;soc_yxzl_zcfw=0;zr_ans_rec=gbrank;se_sug=1;se_college_cm=1;se_lottery=0;qap_question_visitor= 0;zr_se_new_xgb=0;se_webmajorob=0;tp_sticky_android=2;top_native_answer=6;li_qc_pt=0;se_billboardsearch=0;li_vip_lr=1;li_se_section=1;zr_km_answer=open_cvr;zr_video_rank=new_rank;zr_paid_answer_mix=mixed_13;tp_sft=a;top_hotcommerce=1;li_salt_hot=1;zr_rec_answer_cp=close;se_ad_index=10;li_pay_banner_type=6;zr_esmm_model=old;se_mobileweb=1;se_cardrank_3=0;top_v_album=1;li_answer_card=0;zr_slot_cold_start=aver;se_topicfeed=0;se_p_slideshow=1;tp_m_intro_re_topic=1;ug_follow_answerer=0;se_likebutton=0;se_ctx=0;se_wannasearch=a;se_timebox_up=0;tp_header_style=1;soc_brdcst3=0;tsp_vote=2;zr_km_item_prerank=old;se_member_rescore=0;soc_zuichangfangwen=0;tp_topic_rec=0;top_ebook=0;soc_cardheight=0;pf_fuceng=1;se_webtimebox=1;se_new_merger=1;ug_zero_follow=0;ug_zero_follow_0=0;li_tjys_ec_ab=0;se_search_feed=N;tp_topic_style=0;se_ltr_cp_new=0;se_hot_timebox=1;li_android_vip=0;qap_payc_invite=0;se_whitelist=1;ug_follow_answerer_0=0;ls_zvideo_rec=2;li_cln_vl=no;zr_km_sku_mix=sku_50;se_preset_tech=0;se_payconsult=5;top_root=0;top_test_4_liguangyi=1;zr_km_recall_num=open;top_quality=0;se_multi_task_new=0;zr_article_new=open;zr_km_style=base;se_waterfall=0;tp_club_qa_pic=1;li_sku_bottom_bar_re=0;zr_expslotpaid=1;zr_video_rank_nn=new_rank;zr_km_topic_zann=new;se_pek_test3=1;zw_payc_qaedit=0;zr_new_commodity=1;se_dnn_unbias=1;se_cardrank_2=1;zr_test_aa1=0;se_colorfultab=1;tp_qa_toast=1;soc_zcfw_broadcast=0;li_qa_btn_text=0;zr_intervene=1;se_ltr_dnn_cp=0;se_college=default;zr_art_rec=base;zr_paid_answer_exp=0;se_col_boost=1;se_auto_syn=0;se_rel_search=1;li_hot_score_ab=0;zr_km_prerank=new;se_hotmore=2;se_spb309=0;se_ctr=0;zr_rel_search=base;se_new_topic=0;se_cardrank_1=0;ls_bullet_guide=0;qap_ques_invite=0;zr_km_special=open;zr_book_chap=1;se_zu_recommend=0;ls_zvideo_license=1;se_famous=1;ug_follow_topic_1=2;se_perf=0;tp_qa_metacard=1;pf_noti_entry_num=0;pf_foltopic_usernum=0;zr_km_slot_style=event_card;top_new_feed=5;soc_notification=1;sem_up_growth=in_app;li_se_across=1;zr_item_nn_recall=close;se_websearch=3;tp_club_qa=1;li_query_match=0;zr_km_item_cf=open;zr_km_category=open;se_agency= 0;top_ydyq=X;se_expired_ob=0;se_senet=0;tp_meta_card=0;zr_km_feed_nlp=old;se_ab=0;soc_bigone=1;soc_stickypush=0;soc_zcfw_shipinshiti=1;soc_ri_merge=0;ls_zvideo_trans=0;zr_paid_answer_merge=50;se_ios_spb309=1;soc_wonderuser_recom=0;pf_creator_card=1;ls_fmp4=0;li_purchase_test=0;li_qa_new_cover=1;top_universalebook=1',
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        response = r.json()
        print(response)
        return dict(response)
    except:
        return 'error'

def get_content(url):

    comments = []
    content = get_data(url)
    data_list = content['data']

    for data in data_list:
        comment = {}
        print(data)
        try:
            comment['title'] = data['title']
            comment['url'] = data['url']
            comment['image_url'] = data['image_url']

            comments.append(comment)
        except:
            print('error')

    return comments


def save_pdf(html, filename):
    """
    把所有html文件保存到pdf文件
    :param html:  html内容
    :param file_name: pdf文件名
    :return:
    """
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        'outline-depth': 10,
    }
    pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
    pdfkit.from_string(html, filename, options=options)

def merge_pdf(infnList, outfn):
    """
    合并pdf
    :param infnList: 要合并的PDF文件路径列表
    :param outfn: 保存的PDF文件名
    :return: None
    """
    pagenum = 0
    pdf_output = PdfFileWriter()

    for pdf in infnList:
        # 先合并一级目录的内容
        title = pdf['title']
        pdf_path = '{}_zhihu.pdf'.format(title)

        pdf_input = PdfFileReader(open(pdf_path, 'rb'))
        # 获取 pdf 共用多少页
        page_count = pdf_input.getNumPages()
        for i in range(page_count):
            pdf_output.addPage(pdf_input.getPage(i))

        # 添加书签
        pdf_output.addBookmark(title, pagenum=pagenum)

        # 页数增加
        pagenum += page_count

        os.remove(pdf_path)

    # 合并
    pdf_output.write(open(outfn, 'wb'))
    # 删除所有章节文件
    # shutil.rmtree(os.path.join(os.path.dirname(__file__), 'gen'))

def get_html(url):
    try:
        headers = {
            'cookie': '_zap=fc49d92e-f244-4643-b38a-abae1a61d2e6; d_c0="APDqCX_qkw-PTsfKES3gDJUuZRAC5i0buzU=|1560404512"; __utma=51854390.291149964.1562223544.1562223544.1562223544.1; __utmz=51854390.1562223544.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.000--|3=entry_date=20190704=1; z_c0="2|1:0|10:1574163854|4:z_c0|92:Mi4xMHJpWUR3QUFBQUFBOE9vSmYtcVREeVlBQUFCZ0FsVk5qaVBCWGdCUnpyNG1wLTQ1eUpHaGRKRmJVdUJ6MjFhVEJn|867598c121c674df00282eb03e4c81a60c52aef2a143f18400b952e63d3f7fb8"; tst=r; _xsrf=cda689f5-68f8-43bc-b472-99284e7b87bd; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1576552680,1576644333,1576660116,1576756462; q_c1=add64800e7534dc69f381a17e6402522|1576809306000|1562223537000; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1576809912',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        content = r.text
        content = content.replace('lazy', '')
        content = content.replace('src', 'data-src')
        content = content.replace('data-lazy-status="ok"', '')
        content = content.replace('data-original', 'src')

        return content
    except:
        return 'error'

def main():
    urls = []
    for idx in range(0, 29):
        urls.append('https://zhuanlan.zhihu.com/api/columns/pinjinrong/articles?include=data%5B%2A%5D.admin_closed_comment%2Ccomment_count%2Csuggest_edit%2Cis_title_image_full_screen%2Ccan_comment%2Cupvoted_followees%2Ccan_open_tipjar%2Ccan_tip%2Cvoteup_count%2Cvoting%2Ctopics%2Creview_info%2Cauthor.is_following%2Cis_labeled%2Clabel_info&limit=10&offset={}'.format((idx + 1) * 20))

    contents = []
    for url in urls:
        data_content = get_content(url)
        contents = contents + data_content


    print(contents)

    for content in contents:
        print('content')
        print(content)
        html = get_html(content['url'])
        save_pdf(html, '{}_zhihu.pdf'.format(content['title']))

    merge_pdf(contents, '笨虎聊金融.pdf')


if __name__ == '__main__':
    main()
