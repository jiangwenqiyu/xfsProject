;
var common_ops = {
    buildUrl: function (path, params) {
        var url = "" + path;
        var _path_url = "";
        if (params) {
            _path_url = Object.keys(params).map(function (k) {
                return [encodeURIComponent(k), encodeURIComponent(params(k))].join("=")
            }).join("&");
            _path_url = "?" + _path_url;

        }
        return url + _path_url
    },
    send_requests: function (url, method, data) {
        alert(data)
        var httpRequest = new XMLHttpRequest();//第一步：创建需要的对象
        httpRequest.open("post", url, true); //第二步：打开连接/***发送json格式文件必须设置请求头 ；如下 - */
        httpRequest.setRequestHeader("Content-type", "application/json");//设置请求头 注：post方式必须设置请求头（在建立连接后设置请求头）var obj = { name: 'zhansgan', age: 18 };
        httpRequest.send(data);//发送请求 将json写入send中
        /**
         * 获取数据后的处理程序
         */
        httpRequest.onreadystatechange = function () {//请求后的回调接口，可将请求成功后要执行的程序写在其中
            if (httpRequest.readyState == 4 && httpRequest.status == 200) {//验证请求是否发送成功
                var json = httpRequest.responseText;//获取到服务端返回的数据
           //     return json ;
                console.log(json);
            }
        };

    },


    alert: function (msg, cb) {
        layer.alert(msg, {
            yes: function (index) {
                if (typeof cb == "function") {
                    cb();
                }
                layer.close(index);
            }
        });
    }
};