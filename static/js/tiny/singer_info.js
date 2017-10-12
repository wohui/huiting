/**
 * Created by Administrator on 2017/9/17.
 */
var singer = new Vue({
    el:'#singer_info',
    data:{
        singer_data:[]
    },
    mounted:function () {
         var url_array = location.href.split('/');
         singer_id = url_array[url_array.length-2] ;//获取url倒数第二个即id
         var that = this;
        fetch("../../get_singer_data/?id="+singer_id)
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
                        that.singer_data = data['data']
                    });
                }
            )
            .catch(function (err) {
                console.log("Fetch错误:" + err);
            });

    },
    methods:{
        onSearch:function (item) {

        }
    }
});