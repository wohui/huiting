/**
 * Created by Administrator on 2017/9/17.
 */
var singer_list = new Vue({
    el:'#singer_list_ul',
    data:{
        //歌手列表
        singer_list:[],

    },
    /*页面加载完成后请求*/
    mounted:function () {
        var that = this;
        fetch("./get_singer_list")
            .then(
                function (response) {
                    if (response.status !== 200) {

                        console.log("存在一个问题，状态码为：" + response.status);
                        return;
                    }
                    //检查响应文本
                    response.json().then(function (data) {
                        /*给data中的singer_list赋值*/
                        data_json = JSON.stringify(data);
                        that.singer_list = data['result']
                    });
                }
            )
            .catch(function (err) {
                console.log("Fetch错误:" + err);
            });
    },
    methods:{
        onSearch:function (item) {
            location.href = 'singer_info/'+ item.singer_id;
        }
    }
});