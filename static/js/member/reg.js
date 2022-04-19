;
var member_reg_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        $(".reg_wrap .do-login").click(function () {

                        var btn_target = $(this);
                        if (btn_target.hasClass("disabled")) {
                            layer.alert("稍等，正处理呢～");
                           return;
                        }
            var login_name = $(".reg_wrap input[name = login_name]").val();
            var userpwd = $(".reg_wrap input[name = userpwd]").val();
            var userpwd1 = $(".reg_wrap input[name = userpwd1]").val();
            /*手机号验证方法
            if (!(/^1[34578]\d{9}$/.test(login_name))) {
                alert("施主，整点阳间的手机号再试试吧！");

            return;
            }
        */

           if (login_name == undefined || login_name.length<1){
                layer.alert("用户名不能为空")
                return;
            };
            btn_target.addClass("disabled");

            if (userpwd == "undefined" || userpwd.length<6) {
                layer.alert("密码不能小于6位");
                return;
            };
            if (userpwd1 == "undefined" || userpwd1.length<6) {
                layer.alert("密码不能小于6位");
                return;
            };
            if (userpwd != userpwd1){
                layer.alert("两次密码不也一样，再试试");
                return;

            }


            $.ajax({
                url: common_ops.buildUrl("/member/reg"),
                type:"POST",
                data:{
                    login_name:login_name,
                    userpwd:userpwd,
                    userpwd1:userpwd1,

                },
                dataType:'json',
                success:function (res) {
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if(res.code = 200){
                        callback = function(){
                            window.location = common_ops.buildUrl("/member/login");
                        };

                    }
                    common_ops.alert(res.msg,callback)
                }
            })


        });
    }
}
$(document).ready(function () {
    member_reg_ops.init();
})