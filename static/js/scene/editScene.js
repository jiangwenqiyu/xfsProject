// 页面自动加载
$(document).on('click', '.relateCase', function () {
    nowPage = $(".modal-body").children("input").val();
    $(".queryCase").children("tbody").html("");
    $(".modal-body").children("span").remove();
    $(".modal-body").children("input").remove();
    $(".modal-body").children("a").remove();

    data = {
        "nowPage":nowPage,
        "caseName":"",
        "caseSys":"",
        "caseFunc":"",
        "isupdate":false
    }

    $.ajax({
        url: '/case/relateQueryCase',
        type: 'post',
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify(data),
        success: function (res) {
            for (var i in res.data) {
                t = "<tr><td>" + res.data[i][0] + "</td><td>" + res.data[i][1] + "</td><td>" + res.data[i][2] + "</td><td>" + res.data[i][3] + "</td><td><a href='#' class='choose-case'>选择</a></td></tr>>"
                $(".queryCase").children("tbody").append(t);
            }
            $(".modal-body").append("<span style='margin-left: 40%;margin-bottom: 20px'>" + res.nowPage+"/"+res.totalPage + "</span>" +
                "<input style='width: 30px;margin-left: 5px;margin-right: 5px' type='text' id='jumpNum' ><a href='#' id='jump' class='relateCase'>跳转</a>");

        }
    });
});

// $('.relateCase').click(function () {
//     nowPage = $(".modal-body").children("input").val();
//     $(".queryCase").children("tbody").html("");
//     $(".modal-body").children("span").remove();
//     $(".modal-body").children("input").remove();
//     $(".modal-body").children("a").remove();
//
//     data = {
//         "nowPage":nowPage,
//         "caseName":"",
//         "caseSys":"",
//         "caseFunc":"",
//         "isupdate":false
//     }
//
//     $.ajax({
//         url: '/case/relateQueryCase',
//         type: 'post',
//         contentType: 'application/json',
//         dataType: 'json',
//         data: JSON.stringify(data),
//         success: function (res) {
//             for (var i in res.data) {
//                 t = "<tr><td>" + res.data[i][0] + "</td><td>" + res.data[i][1] + "</td><td>" + res.data[i][2] + "</td><td>" + res.data[i][3] + "</td><td><a href='#' class='choose-case'>选择</a></td></tr>>"
//                 $(".queryCase").children("tbody").append(t);
//             }
//             $(".modal-body").append("<span style='margin-left: 40%;margin-bottom: 20px'>" + res.nowPage+"/"+res.totalNum + "</span>" +
//                 "<input style='width: 30px;margin-left: 5px;margin-right: 5px' type='text' id='jumpNum' ><a href='#' id='jump' class='relateCase'>跳转</a>");
//
//         }
//     });
// });



// 点击查询
$('.query-case').click(function () {
    $(".queryCase").children("tbody").html("");
    $(".modal-body").children("span").remove();
    $(".modal-body").children("input").remove();
    $(".modal-body").children("a").remove();

    data = {
        "nowPage":"1",
        "caseName":$(".caseName").val().trim(),
        "caseSys":$(".caseSys").val().trim(),
        "caseFunc":$(".caseFunc").val().trim(),
        "isupdate":true
    }

    $.ajax({
        url: '/case/relateQueryCase',
        type: 'post',
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify(data),
        success: function (res) {
            for (var i in res.data) {
                t = "<tr><td>" + res.data[i][0] + "</td><td>" + res.data[i][1] + "</td><td>" + res.data[i][2] + "</td><td>" + res.data[i][3] + "</td><td><a href='#' class='choose-case'>选择</a></td></tr>"
                $(".queryCase").children("tbody").append(t);

            }
            $(".modal-body").append("<span style='margin-left: 40%;margin-bottom: 20px'>" + res.nowPage+"/"+res.totalPage + "</span>" +
                "<input style='width: 30px;margin-left: 5px;margin-right: 5px' type='text' id='jumpNum'><a href='#' id='jump' class='relateCase'>跳转</a>");


        }
    });
});



$(document).on('click', '.choose-case', function () {

    currentCase = $(this).parent().parent();
    caseid = currentCase.children('td').eq(0).html();
    casename = currentCase.children('td').eq(1).html();
    sysname = currentCase.children('td').eq(2).html();
    funcname = currentCase.children('td').eq(3).html();

    var t = '';
    t += '<tr>'
    t+= '<td>' + caseid + '</td>'
    t+= '<td><a href="/case/editcase?case_id=' + caseid + '" target="_blank">' + casename + '</a></td>'
    t+= '<td>' + sysname + '</td>'
    t+= '<td>' + funcname + '</td>'
    t+= '<td><a href="#" class="deleteCase">删除</a></td>'
    t += '</tr>'
    $("#editCaseIndex").children("tbody").append(t)
});


$(document).on('click', '.deleteCase', function () {
    $(this).parent().parent().remove();
});


$(document).on('click', '#saveSence', function () {
    sceneName = $("#sceneName").val();
    sceneid = $("#sceneid").attr('sceneid');
    var caseids = '';

    trs = $("#editCaseIndex").children('tbody').children('tr').each(function (i) {
        var name = $(this).children('td:eq(0)').html();
        caseids += name + ','
    });
    caseids = caseids.substr(0, caseids.length-1)



    data = {
        "sceneid":sceneid,
        "sceneName":sceneName,
        "caseids":caseids
    }

    $.ajax({
        url: '/case/saveEditScene',
        type: 'post',
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify(data),
        success: function (res) {
                alert(res.msg);
            }


    });




});




$(document).on("click", "#editCaseIndex", function () {
    $("#editCaseIndex").children('tbody').sortable({
        stop: function () {

        }
    });
});

