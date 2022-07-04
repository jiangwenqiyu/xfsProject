;
var member_login_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        $(".login_wrap .do-login").click(function () {

            var btn_target = $(this);
            // if (btn_target.hasClass("disabled")) {
            //     alert("稍等户，正处理呢～");
            //     return;
            // }


            var login_name = $(".login_wrap input[name = login_name]").val();
            var userpwd = $(".login_wrap input[name = userpwd]").val();
/*
            if (!(/^1[34578]\d{9}$/.test(login_name))) {
                alert("验证手机号");
                return;
            }
            ;
            */
            // alert(login_name)
            // btn_target.addClass("disabled");
            if (login_name == "undefined" || login_name.length<1) {
                common_ops.alert("请输入正确用户名或密码")
                return;
            }
            ;
            if (userpwd == "undefined" || userpwd.length<6) {
                common_ops.alert("请输入正确用户名或密码")
                return;
            }
            ;

            $.ajax({
                url: common_ops.buildUrl("/member/login"),
                type:"POST",
                data:{
                    login_name:login_name,
                    userpwd:userpwd,
                },
                dataType:'json',
                success:function (res) {
                    // btn_target.removeClass("disabled");
                    var callback = null;
                    if (res.code == 200) {
                        callback = function () {
                            window.location = common_ops.buildUrl("/");
                        };
                        common_ops.alert(res.msg, callback);


                    } else {
                        common_ops.alert(res.msg);
                    }


                }
            })

        });
    }
}
$(document).ready(function () {
    member_login_ops.init();
})