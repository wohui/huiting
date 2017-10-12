/**
 * Created by Administrator on 2017/9/16.
 */



var song_action = new Vue({
  el: '#song_action',
  data: {
    message: 'test'
  },
    methods:{
      onSearch:function (e) {
        fetch("./getSongs",{
            method:'get'
        }).then(function (response) {
                return response.text();
            }).then(function (data) {
              console.log(data);
            }).catch(function (e) {
            console.log("error");
        });
      }
    }
});